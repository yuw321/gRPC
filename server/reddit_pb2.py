# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creddit.proto\x12\x06reddit\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xe8\x01\n\x04Post\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\tvideo_url\x18\x03 \x01(\tH\x00\x12\x13\n\timage_url\x18\x04 \x01(\tH\x00\x12\x11\n\tauthor_id\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x05\x12\"\n\x06status\x18\x07 \x01(\x0e\x32\x12.reddit.PostStatus\x12\x18\n\x10publication_date\x18\x08 \x01(\t\x12\x11\n\tsubreddit\x18\t \x01(\t\x12\x0f\n\x07post_id\x18\n \x01(\x05\x12\x0c\n\x04tags\x18\x0b \x03(\tB\x07\n\x05media\"\xa1\x01\n\x07\x43omment\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x12%\n\x06status\x18\x04 \x01(\x0e\x32\x15.reddit.CommentStatus\x12\x18\n\x10publication_date\x18\x05 \x01(\t\x12\x11\n\tparent_id\x18\x06 \x01(\t\x12\x12\n\ncomment_id\x18\x07 \x01(\x05\"X\n\tSubreddit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\nvisibility\x18\x02 \x01(\x0e\x32\x1b.reddit.SubredditVisibility\x12\x0c\n\x04tags\x18\x03 \x03(\t\"\x89\x01\n\x11\x43reatePostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\tvideo_url\x18\x03 \x01(\tH\x00\x12\x13\n\timage_url\x18\x04 \x01(\tH\x00\x12\x11\n\tauthor_id\x18\x05 \x01(\t\x12\x11\n\tsubreddit\x18\x06 \x01(\tB\x07\n\x05media\"*\n\x0cPostResponse\x12\x1a\n\x04post\x18\x01 \x01(\x0b\x32\x0c.reddit.Post\"0\n\x0fVotePostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x0c\n\x04vote\x18\x02 \x01(\x05\"!\n\x0cVoteResponse\x12\x11\n\tnew_score\x18\x01 \x01(\x05\"!\n\x0eGetPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\"J\n\x14\x43reateCommentRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tparent_id\x18\x03 \x01(\t\"3\n\x0f\x43ommentResponse\x12 \n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\"6\n\x12VoteCommentRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\x0c\n\x04vote\x18\x02 \x01(\x05\"D\n\x15GetTopCommentsRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x1a\n\x12number_of_comments\x18\x02 \x01(\x05\"8\n\x13TopCommentsResponse\x12!\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x0f.reddit.Comment\"9\n\x14\x45xpandCommentRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"O\n\x18\x45xpandedCommentsResponse\x12\x33\n\x0fparent_comments\x18\x01 \x03(\x0b\x32\x1a.reddit.CommentWithReplies\"X\n\x12\x43ommentWithReplies\x12 \n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\x12 \n\x07replies\x18\x02 \x03(\x0b\x32\x0f.reddit.Comment\"=\n\x15MonitorUpdatesRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63omment_ids\x18\x02 \x03(\t\"/\n\x0eUpdateResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tnew_score\x18\x02 \x01(\x05*?\n\nPostStatus\x12\x0f\n\x0bPOST_NORMAL\x10\x00\x12\x0f\n\x0bPOST_LOCKED\x10\x01\x12\x0f\n\x0bPOST_HIDDEN\x10\x02*7\n\rCommentStatus\x12\x12\n\x0e\x43OMMENT_NORMAL\x10\x00\x12\x12\n\x0e\x43OMMENT_HIDDEN\x10\x01*X\n\x13SubredditVisibility\x12\x14\n\x10SUBREDDIT_PUBLIC\x10\x00\x12\x15\n\x11SUBREDDIT_PRIVATE\x10\x01\x12\x14\n\x10SUBREDDIT_HIDDEN\x10\x02\x32\xb5\x04\n\rRedditService\x12=\n\nCreatePost\x12\x19.reddit.CreatePostRequest\x1a\x14.reddit.PostResponse\x12\x39\n\x08VotePost\x12\x17.reddit.VotePostRequest\x1a\x14.reddit.VoteResponse\x12\x37\n\x07GetPost\x12\x16.reddit.GetPostRequest\x1a\x14.reddit.PostResponse\x12\x46\n\rCreateComment\x12\x1c.reddit.CreateCommentRequest\x1a\x17.reddit.CommentResponse\x12?\n\x0bVoteComment\x12\x1a.reddit.VoteCommentRequest\x1a\x14.reddit.VoteResponse\x12L\n\x0eGetTopComments\x12\x1d.reddit.GetTopCommentsRequest\x1a\x1b.reddit.TopCommentsResponse\x12O\n\rExpandComment\x12\x1c.reddit.ExpandCommentRequest\x1a .reddit.ExpandedCommentsResponse\x12I\n\x0eMonitorUpdates\x12\x1d.reddit.MonitorUpdatesRequest\x1a\x16.reddit.UpdateResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POSTSTATUS']._serialized_start=1497
  _globals['_POSTSTATUS']._serialized_end=1560
  _globals['_COMMENTSTATUS']._serialized_start=1562
  _globals['_COMMENTSTATUS']._serialized_end=1617
  _globals['_SUBREDDITVISIBILITY']._serialized_start=1619
  _globals['_SUBREDDITVISIBILITY']._serialized_end=1707
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=47
  _globals['_POST']._serialized_start=50
  _globals['_POST']._serialized_end=282
  _globals['_COMMENT']._serialized_start=285
  _globals['_COMMENT']._serialized_end=446
  _globals['_SUBREDDIT']._serialized_start=448
  _globals['_SUBREDDIT']._serialized_end=536
  _globals['_CREATEPOSTREQUEST']._serialized_start=539
  _globals['_CREATEPOSTREQUEST']._serialized_end=676
  _globals['_POSTRESPONSE']._serialized_start=678
  _globals['_POSTRESPONSE']._serialized_end=720
  _globals['_VOTEPOSTREQUEST']._serialized_start=722
  _globals['_VOTEPOSTREQUEST']._serialized_end=770
  _globals['_VOTERESPONSE']._serialized_start=772
  _globals['_VOTERESPONSE']._serialized_end=805
  _globals['_GETPOSTREQUEST']._serialized_start=807
  _globals['_GETPOSTREQUEST']._serialized_end=840
  _globals['_CREATECOMMENTREQUEST']._serialized_start=842
  _globals['_CREATECOMMENTREQUEST']._serialized_end=916
  _globals['_COMMENTRESPONSE']._serialized_start=918
  _globals['_COMMENTRESPONSE']._serialized_end=969
  _globals['_VOTECOMMENTREQUEST']._serialized_start=971
  _globals['_VOTECOMMENTREQUEST']._serialized_end=1025
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_start=1027
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_end=1095
  _globals['_TOPCOMMENTSRESPONSE']._serialized_start=1097
  _globals['_TOPCOMMENTSRESPONSE']._serialized_end=1153
  _globals['_EXPANDCOMMENTREQUEST']._serialized_start=1155
  _globals['_EXPANDCOMMENTREQUEST']._serialized_end=1212
  _globals['_EXPANDEDCOMMENTSRESPONSE']._serialized_start=1214
  _globals['_EXPANDEDCOMMENTSRESPONSE']._serialized_end=1293
  _globals['_COMMENTWITHREPLIES']._serialized_start=1295
  _globals['_COMMENTWITHREPLIES']._serialized_end=1383
  _globals['_MONITORUPDATESREQUEST']._serialized_start=1385
  _globals['_MONITORUPDATESREQUEST']._serialized_end=1446
  _globals['_UPDATERESPONSE']._serialized_start=1448
  _globals['_UPDATERESPONSE']._serialized_end=1495
  _globals['_REDDITSERVICE']._serialized_start=1710
  _globals['_REDDITSERVICE']._serialized_end=2275
# @@protoc_insertion_point(module_scope)
