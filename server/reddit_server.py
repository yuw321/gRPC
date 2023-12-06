import argparse
import grpc
from concurrent import futures
from datetime import datetime
from collections import defaultdict
import reddit_pb2
import reddit_pb2_grpc


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
        )
        self.comments["comment0"] = reddit_pb2.Comment(
            author_id="user0",
            text="Some text to comment",
            score=0,
            status=reddit_pb2.CommentStatus.COMMENT_NORMAL,
            publication_date=datetime.today().strftime("%Y-%m-%d"),
            parent_id="post0",
            comment_id=f"comment{len(self.comments)}",
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
        )

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
        # TODO: Implement logic to retrieve top N comments
        pass

    def ExpandComment(self, request, context):
        # TODO: Implement logic to expand a comment branch
        pass

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
