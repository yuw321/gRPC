import argparse
import grpc
from concurrent import futures
from datetime import datetime
from collections import defaultdict
import random
import reddit_pb2, reddit_pb2_grpc


# Service implementation
class RedditServiceServicer(reddit_pb2_grpc.RedditServiceServicer):
    def __init__(self):
        self.users = {}
        self.sub_reddit = {}
        self.posts = {}
        self.comments = {}
        self.parent_comments = defaultdict(list)

        # Load dummy data
        self.users["user0"] = reddit_pb2.User(user_id="user0")
        self.sub_reddit["Testing"] = ["tech", "gRPC", "google"]

        self.posts["post0"] = reddit_pb2.Post(
            title="Example Title",
            text="Example Text",
            author_id=self.users.get("user0").user_id,
            # Handle 'oneof' field for media
            video_url="www.video.com/123",
            # Default values for score, status, and publication date
            score=0,
            status=reddit_pb2.PostStatus.POST_NORMAL,
            publication_date=datetime.today().strftime("%Y-%m-%d"),
            subreddit="",
            post_id=f"post{len(self.posts)}",
            tags=[],
            reply_count=0,
        )

        # Create 10 top level comments
        for _ in range(10):
            top_level_comment_id = f"comment{len(self.comments)}"
            reply_count = random.randint(3, 12)
            self.comments[top_level_comment_id] = reddit_pb2.Comment(
                author_id="user0",
                text=f"{top_level_comment_id}, THis is the top of the comment tree",
                score=random.randint(0, 10),
                status=reddit_pb2.CommentStatus.COMMENT_NORMAL,
                publication_date=datetime.today().strftime("%Y-%m-%d"),
                parent_id="post0",
                comment_id=top_level_comment_id,
                reply_count=reply_count,
            )
            self.parent_comments["post0"].append(self.comments[top_level_comment_id])
            for _ in range(reply_count):
                first_level_comment_id = f"comment{len(self.comments)}"
                self.comments[first_level_comment_id] = reddit_pb2.Comment(
                    author_id="user0",
                    text=f"{first_level_comment_id}, THis is the first level of the comment tree",
                    score=random.randint(0, 10),
                    status=reddit_pb2.CommentStatus.COMMENT_NORMAL,
                    publication_date=datetime.today().strftime("%Y-%m-%d"),
                    parent_id=top_level_comment_id,
                    comment_id=first_level_comment_id,
                    reply_count=reply_count,
                )
                self.parent_comments[top_level_comment_id].append(
                    self.comments[first_level_comment_id]
                )
                for _ in range(reply_count):
                    second_level_commnt_id = f"comment{len(self.comments)}"

                    self.comments[second_level_commnt_id] = reddit_pb2.Comment(
                        author_id="user0",
                        text=f"{second_level_commnt_id}, THis is the second level of the comment tree",
                        score=random.randint(0, 10),
                        status=reddit_pb2.CommentStatus.COMMENT_NORMAL,
                        publication_date=datetime.today().strftime("%Y-%m-%d"),
                        parent_id=first_level_comment_id,
                        comment_id=second_level_commnt_id,
                        reply_count=reply_count,
                    )
                    self.parent_comments[first_level_comment_id].append(
                        self.comments[second_level_commnt_id]
                    )

    def CreatePost(self, request, context):
        # Retrieve input
        title = request.title
        text = request.text
        author_id = request.author_id
        author = self.users.get(author_id, None)
        subreddit = request.subreddit
        subreddit_tags = self.sub_reddit.get(subreddit, [])

        # Validate input
        if author_id and not author:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Author ID not found among list of users")
            return reddit_pb2.PostResponse(post=None)
        elif subreddit and not subreddit_tags:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Subreddit tags not found among list of tags")
            return reddit_pb2.PostResponse(post=None)
        elif not title:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Post title not provideded")
            return reddit_pb2.PostResponse(post=None)
        elif not text:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Post text not provideded")
            return reddit_pb2.PostResponse(post=None)

        # Create a new Post object
        new_post = reddit_pb2.Post(
            title=request.title,
            text=request.text,
            author_id=request.author_id,
            # Handle 'oneof' field for media
            video_url=request.video_url if request.HasField("video_url") else "",
            image_url=request.image_url if request.HasField("image_url") else "",
            # Default values for score, status, and publication date
            score=0,
            status=reddit_pb2.PostStatus.POST_NORMAL,
            publication_date=datetime.today().strftime("%Y-%m-%d"),
            subreddit=request.subreddit,
            post_id=f"post{len(self.posts)}",
            tags=subreddit_tags,
            reply_count=0,
        )
        # Save new post
        self.posts[new_post.post_id] = new_post
        response = reddit_pb2.PostResponse(post=new_post)
        return response

    def VotePost(self, request, context):
        post_id = request.post_id
        vote = request.vote
        post = self.posts.get(post_id, None)

        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post not found")
            return reddit_pb2.VoteResponse(new_score=0)

        post.score += vote
        self.posts[post_id] = post
        return reddit_pb2.VoteResponse(new_score=post.score)

    def GetPost(self, request, context):
        post_id = request.post_id
        post = self.posts.get(post_id, None)
        # Post NOT Found
        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post not found")
            return reddit_pb2.PostResponse(post=None)
        # Return found post
        return reddit_pb2.PostResponse(post=post)

    def CreateComment(self, request, context):
        # Retreive input
        author_id = request.author_id
        author = self.users.get(author_id, None)
        comment_text = request.text
        parent_id = request.parent_id
        parent_type_is_post = parent_id.startswith("post")
        parent_content = (
            self.posts.get(parent_id, None)
            if parent_type_is_post
            else self.comments.get(parent_id, None)
        )

        # Validate Input
        if not author:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Author ID not Found")
            return reddit_pb2.CommentResponse(comment=None)
        elif not comment_text:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("No comment text provided")
            return reddit_pb2.CommentResponse(comment=None)
        elif not parent_content:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Parent resource not found")
            return reddit_pb2.CommentResponse(comment=None)

        # Create New comment
        new_comment = reddit_pb2.Comment(
            author_id=author_id,
            text=comment_text,
            score=0,
            status=reddit_pb2.CommentStatus.COMMENT_NORMAL,
            publication_date=datetime.today().strftime("%Y-%m-%d"),
            parent_id=parent_id,
            comment_id=f"comment{len(self.comments)}",
            reply_count=0,
        )

        # Increment reply count for parent
        parent_content.reply_count += 1

        # Save new comment
        self.comments[new_comment.comment_id] = new_comment
        self.parent_comments[parent_id].append(new_comment)
        print(self.parent_comments)
        return reddit_pb2.CommentResponse(comment=new_comment)

    def VoteComment(self, request, context):
        comment_id = request.comment_id
        vote = request.vote
        comment = self.comments.get(comment_id, None)

        if not comment:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Comment not found")
            return reddit_pb2.VoteResponse(new_score=0)

        comment.score += vote
        self.comments[comment_id] = comment
        return reddit_pb2.VoteResponse(new_score=comment.score)

    def GetTopComments(self, request, context):
        post_id = request.post_id
        number_of_comments = request.number_of_comments
        post = self.posts.get(post_id, None)

        # Validate Input
        if number_of_comments < 1:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Number of comments can not be less than 1")
            return reddit_pb2.TopCommentsResponse(comments=None)
        elif not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post requested not found")
            return reddit_pb2.TopCommentsResponse(comments=None)

        # Find the comments under requested post
        sorted_post_comments = sorted(
            self.parent_comments[post_id], key=lambda x: x.score, reverse=True
        )

        return reddit_pb2.TopCommentsResponse(
            comments=sorted_post_comments[:number_of_comments]
        )

    def ExpandComment(self, request, context):
        comment_id = request.comment_id
        number_of_comments = request.number_of_comments

        comment = self.comments.get(comment_id, None)

        if not comment:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Comment requested not found")
            return reddit_pb2.ExpandCommentRequest(parent_comments=None)
        elif number_of_comments < 1:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Number of Comment expanded must be greater than 0")
            return reddit_pb2.ExpandCommentRequest(parent_comments=None)

        first_level_comments = self.parent_comments.get(comment_id, None)
        if not first_level_comments:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No Comments under comment requested")
            return reddit_pb2.ExpandCommentRequest(parent_comments=None)

        first_level_comments = sorted(
            first_level_comments, key=lambda x: x.score, reverse=True
        )[:number_of_comments]

        expanded_comment_response = []
        for flc in first_level_comments:
            flc_id = flc.comment_id
            second_level_comments = self.parent_comments.get(flc_id, None)
            new_comment_with_replies = (
                reddit_pb2.CommentWithReplies(
                    comment=flc,
                    replies=sorted(
                        second_level_comments,
                        key=lambda x: x.score,
                        reverse=True,
                    )[:number_of_comments],
                )
                if second_level_comments
                else reddit_pb2.CommentWithReplies(comment=flc, replies=[])
            )
            expanded_comment_response.append(new_comment_with_replies)

        return reddit_pb2.ExpandedCommentsResponse(
            parent_comments=expanded_comment_response
        )

    # Extra Credit: Implement MonitorUpdates if required
    def MonitorUpdates(self, request, context):
        # TODO: Implement logic for monitoring updates
        pass


# Function to start the gRPC server
def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServiceServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="gRPC Reddit-like Server")
    parser.add_argument(
        "--port", type=int, default=50051, help="Port to run the server on"
    )

    # Parse command line arguments
    args = parser.parse_args()

    # Start server with specified port
    serve(args.port)
