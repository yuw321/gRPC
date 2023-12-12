import sys
import os
import grpc
import argparse
directory_path = os.path.join(os.getcwd(), "gRPC/server")
sys.path.append(directory_path)

from server import reddit_pb2, reddit_pb2_grpc
class RedditClient:
    def __init__(self, host, port):
        # Establish a connection to the server
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(
        self,
        title,
        text,
        author_id=None,
        subreddit=None,
        image_url=None,
        video_url=None,
    ):
        if image_url is not None:
            create_post_request = reddit_pb2.CreatePostRequest(
                title=title,
                text=text,
                author_id=author_id if author_id else "",
                image_url=image_url,
                subreddit=subreddit if subreddit else "",
            )
        else:
            create_post_request = reddit_pb2.CreatePostRequest(
                title=title,
                text=text,
                author_id=author_id if author_id else "",
                video_url=video_url,
                subreddit=subreddit if subreddit else "",
            )
        return self.stub.CreatePost(create_post_request)

    def vote_post(self, post_id, vote):
        vote_post_request = reddit_pb2.VotePostRequest(post_id=post_id, vote=vote)
        return self.stub.VotePost(vote_post_request)

    def get_post(self, post_id):
        get_post_request = reddit_pb2.GetPostRequest(post_id=post_id)
        return self.stub.GetPost(get_post_request)

    def create_comment(self, author_id, text, parent_id):
        create_comment_request = reddit_pb2.CreateCommentRequest(
            author_id=author_id, text=text, parent_id=parent_id
        )
        return self.stub.CreateComment(create_comment_request)

    def vote_comment(self, comment_id, vote):
        vote_comment_request = reddit_pb2.VoteCommentRequest(
            comment_id=comment_id, vote=vote
        )
        return self.stub.VoteComment(vote_comment_request)

    def get_top_comments(self, post_id, number_of_comments=1):
        get_top_comments_request = reddit_pb2.GetTopCommentsRequest(
            post_id=post_id, number_of_comments=number_of_comments
        )
        return self.stub.GetTopComments(get_top_comments_request)

    def expand_comment(self, comment_id, number_of_comments=1):
        expand_comment_request = reddit_pb2.ExpandCommentRequest(
            comment_id=comment_id, number_of_comments=number_of_comments
        )
        return self.stub.ExpandComment(expand_comment_request)

    def close(self):
        self.channel.close()


def get_most_upvoted_reply(client, post_id):
    # Retrieve the post
    get_post_response = client.get_post(post_id=post_id)
    desired_post_id = get_post_response.post.post_id
    
    # Retrieve the most upvoted comments under the post
    top_comments_response = client.get_top_comments(desired_post_id, number_of_comments=1)
    top_comments = top_comments_response.comments
    if not top_comments:
        return None

    # Expand the most upvoted comment
    most_upvoted_comment = top_comments[0]
    most_upvoted_comment_id = most_upvoted_comment.comment_id
    expanded_comments_response = client.expand_comment(most_upvoted_comment_id, number_of_comments=10)

    # Process the expanded comments
    most_upvoted_reply_under_most_upvoted_comment = None
    for comment_with_replies in expanded_comments_response.parent_comments:
        potential_most_upvoted_reply = comment_with_replies.comment
        if not most_upvoted_reply_under_most_upvoted_comment or potential_most_upvoted_reply.score> most_upvoted_reply_under_most_upvoted_comment.score:
            most_upvoted_reply_under_most_upvoted_comment = potential_most_upvoted_reply

    return most_upvoted_reply_under_most_upvoted_comment
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gRPC Reddit-like Client")
    parser.add_argument("--host", type=str, default="localhost", help="Server host")
    parser.add_argument("--port", type=int, default=50051, help="Server port")

    args = parser.parse_args()

    client = RedditClient(args.host, args.port)

    creat_post_response = client.create_post(
        "Test Title", "Test text", "user0", "Testing"
    )
    print(creat_post_response)

    vote_post_response = client.vote_post(post_id="post0", vote=-1)
    print(vote_post_response)

    get_post_response = client.get_post(post_id="post0")
    print(get_post_response)

    create_comment_response = client.create_comment(
        text="This is a comment.", author_id="user0", parent_id="post0"
    )
    print(create_comment_response)

    vote_comment_response = client.vote_comment(comment_id="comment123", vote=1)
    print(vote_comment_response)

    get_top_comments_response = client.get_top_comments(
        post_id="post0", number_of_comments=3
    )
    print(get_top_comments_response)

    expand_comment_response = client.expand_comment(
        comment_id="comment0", number_of_comments=3
    )
    print(expand_comment_response)

    get_most_upvoted_reply(client=client, post_id="post0")

    # Close the client
    client.close()
