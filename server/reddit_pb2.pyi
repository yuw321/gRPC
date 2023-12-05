from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POST_NORMAL: _ClassVar[PostStatus]
    POST_LOCKED: _ClassVar[PostStatus]
    POST_HIDDEN: _ClassVar[PostStatus]

class CommentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMMENT_NORMAL: _ClassVar[CommentStatus]
    COMMENT_HIDDEN: _ClassVar[CommentStatus]

class SubredditVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SUBREDDIT_PUBLIC: _ClassVar[SubredditVisibility]
    SUBREDDIT_PRIVATE: _ClassVar[SubredditVisibility]
    SUBREDDIT_HIDDEN: _ClassVar[SubredditVisibility]
POST_NORMAL: PostStatus
POST_LOCKED: PostStatus
POST_HIDDEN: PostStatus
COMMENT_NORMAL: CommentStatus
COMMENT_HIDDEN: CommentStatus
SUBREDDIT_PUBLIC: SubredditVisibility
SUBREDDIT_PRIVATE: SubredditVisibility
SUBREDDIT_HIDDEN: SubredditVisibility

class User(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ["title", "text", "video_url", "image_url", "author_id", "score", "status", "publication_date", "subreddit", "post_id", "tags"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author_id: str
    score: int
    status: PostStatus
    publication_date: str
    subreddit: str
    post_id: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author_id: _Optional[str] = ..., score: _Optional[int] = ..., status: _Optional[_Union[PostStatus, str]] = ..., publication_date: _Optional[str] = ..., subreddit: _Optional[str] = ..., post_id: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["author_id", "text", "score", "status", "publication_date", "parent_id", "comment_id"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    text: str
    score: int
    status: CommentStatus
    publication_date: str
    parent_id: str
    comment_id: int
    def __init__(self, author_id: _Optional[str] = ..., text: _Optional[str] = ..., score: _Optional[int] = ..., status: _Optional[_Union[CommentStatus, str]] = ..., publication_date: _Optional[str] = ..., parent_id: _Optional[str] = ..., comment_id: _Optional[int] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ["name", "visibility", "tags"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    visibility: SubredditVisibility
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., visibility: _Optional[_Union[SubredditVisibility, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ["title", "text", "video_url", "image_url", "author_id", "subreddit"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    SUBREDDIT_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author_id: str
    subreddit: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author_id: _Optional[str] = ..., subreddit: _Optional[str] = ...) -> None: ...

class PostResponse(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ["post_id", "vote"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    vote: int
    def __init__(self, post_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteResponse(_message.Message):
    __slots__ = ["new_score"]
    NEW_SCORE_FIELD_NUMBER: _ClassVar[int]
    new_score: int
    def __init__(self, new_score: _Optional[int] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ["author_id", "text", "parent_id"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    text: str
    parent_id: str
    def __init__(self, author_id: _Optional[str] = ..., text: _Optional[str] = ..., parent_id: _Optional[str] = ...) -> None: ...

class CommentResponse(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ["comment_id", "vote"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    vote: int
    def __init__(self, comment_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class GetTopCommentsRequest(_message.Message):
    __slots__ = ["post_id", "number_of_comments"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    number_of_comments: int
    def __init__(self, post_id: _Optional[str] = ..., number_of_comments: _Optional[int] = ...) -> None: ...

class TopCommentsResponse(_message.Message):
    __slots__ = ["comments"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentRequest(_message.Message):
    __slots__ = ["comment_id", "depth"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    depth: int
    def __init__(self, comment_id: _Optional[str] = ..., depth: _Optional[int] = ...) -> None: ...

class ExpandedCommentsResponse(_message.Message):
    __slots__ = ["parent_comments"]
    PARENT_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    parent_comments: _containers.RepeatedCompositeFieldContainer[CommentWithReplies]
    def __init__(self, parent_comments: _Optional[_Iterable[_Union[CommentWithReplies, _Mapping]]] = ...) -> None: ...

class CommentWithReplies(_message.Message):
    __slots__ = ["comment", "replies"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    replies: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ..., replies: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class MonitorUpdatesRequest(_message.Message):
    __slots__ = ["post_id", "comment_ids"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    comment_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, post_id: _Optional[str] = ..., comment_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["id", "new_score"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NEW_SCORE_FIELD_NUMBER: _ClassVar[int]
    id: str
    new_score: int
    def __init__(self, id: _Optional[str] = ..., new_score: _Optional[int] = ...) -> None: ...
