import argparse
import sys
import grpc
from concurrent import futures
from datetime import datetime
import reddit_pb2
import reddit_pb2_grpc


# Service implementation
class RedditServiceServicer(reddit_pb2_grpc.RedditServiceServicer):
    def __init__(self):
        self.posts = {}
        self.sub_reddit = {
            "Testing": ["tech", "gRPC", "google"],
        }

    def CreatePost(self, request, context):
        # Check if subreddit is provided and exists
        subreddit_tags = (
            self.sub_reddit.get(request.subreddit, []) if request.subreddit else []
        )
        print(subreddit_tags)
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
            post_id=len(self.posts),
            tags=subreddit_tags,
        )
        self.posts[new_post.post_id] = new_post
        print("post tags",new_post.tags)
        response = reddit_pb2.PostResponse(post=new_post)
        return response

    def VotePost(self, request, context):
        # TODO: Implement logic to upvote/downvote a post
        pass

    def GetPost(self, request, context):
        # TODO: Implement logic to retrieve a post
        pass

    def CreateComment(self, request, context):
        # TODO: Implement logic to create a comment
        pass

    def VoteComment(self, request, context):
        # TODO: Implement logic to upvote/downvote a comment
        pass

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
