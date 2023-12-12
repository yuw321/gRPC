import os
import sys
import unittest
from unittest.mock import Mock

directory_path = os.path.join(os.getcwd(), "server")
sys.path.append(directory_path)
from client.reddit_client import get_most_upvoted_reply


class MockPostResponse:
    def __init__(
        self,
        title="Test Title",
        text="Test text",
        author_id="user0",
        post_id="post0",
        image_url="",
        video_url="",
        score=0,
        publication_date="2023-12-09",
        subreddit="Testing",
        tags=None,
    ):
        if tags is None:
            tags = ["tech", "gRPC", "google"]
        self.post = Mock()
        self.post.title = title
        self.post.text = text
        self.post.author_id = author_id
        self.post.post_id = post_id
        self.post.image_url = image_url
        self.post.video_url = video_url
        self.post.score = score
        self.post.publication_date = publication_date
        self.post.subreddit = subreddit
        self.post.tags.extend(tags)


class MockTopCommentsResponse:
    def __init__(self, comments=None):
        if comments is None:
            comments = [
                MockComment(
                    author_id="user0",
                    text="Sample Comment",
                    score=10,
                    comment_id="comment0",
                )
            ]
        self.comments = comments


class MockExpandCommentResponse:
    def __init__(self, parent_comments=None):
        if parent_comments is None:
            parent_comments = [
                MockCommentWithReplies(
                    comment=MockComment(
                        author_id="user0",
                        text="Parent comment",
                        score=10,
                        comment_id="comment0",
                    ),
                    replies=[
                        MockComment(
                            author_id="user0",
                            text="Reply comment",
                            score=5,
                            comment_id="comment1",
                        )
                    ],
                )
            ]
        self.parent_comments = parent_comments


class MockComment:
    def __init__(
        self, author_id, text, score, comment_id, parent_id="post0", reply_count=0
    ):
        self.author_id = author_id
        self.text = text
        self.score = score
        self.comment_id = comment_id
        self.parent_id = parent_id
        self.reply_count = reply_count


class MockCommentWithReplies:
    def __init__(self, comment, replies=None):
        if replies is None:
            replies = []
        self.comment = comment
        self.replies = replies


class TestRedditClient(unittest.TestCase):
    def test_get_most_upvoted_reply(self):
        # Mock the RedditClient
        mock_client = Mock()
        mock_client.get_post.return_value = (
            MockPostResponse()
        ) 
        mock_client.get_top_comments.return_value = (
            MockTopCommentsResponse()
        )  
        mock_client.expand_comment.return_value = (
            MockExpandCommentResponse()
        )  

        # Call the function
        result = get_most_upvoted_reply(mock_client, "post0")

        # Assertions
        self.assertIsNotNone(
            result
        ) 


if __name__ == "__main__":
    unittest.main()
