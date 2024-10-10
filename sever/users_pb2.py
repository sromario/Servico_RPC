# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: users.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'users.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"A\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"\x11\n\x0fGetUsersRequest\".\n\x10GetUsersResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.users.User\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"0\n\x13GetUserByIdResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11\x43reateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x43reateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11UpdateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12UpdateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11\x44\x65leteUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x44\x65leteUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User2\xd3\x02\n\x05Users\x12;\n\x08GetUsers\x12\x16.users.GetUsersRequest\x1a\x17.users.GetUsersResponse\x12\x44\n\x0bGetUserById\x12\x19.users.GetUserByIdRequest\x1a\x1a.users.GetUserByIdResponse\x12\x41\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponse\x12\x41\n\nUpdateUser\x12\x18.users.UpdateUserRequest\x1a\x19.users.UpdateUserResponse\x12\x41\n\nDeleteUser\x12\x18.users.DeleteUserRequest\x1a\x19.users.DeleteUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=22
  _globals['_USER']._serialized_end=87
  _globals['_GETUSERSREQUEST']._serialized_start=89
  _globals['_GETUSERSREQUEST']._serialized_end=106
  _globals['_GETUSERSRESPONSE']._serialized_start=108
  _globals['_GETUSERSRESPONSE']._serialized_end=154
  _globals['_GETUSERBYIDREQUEST']._serialized_start=156
  _globals['_GETUSERBYIDREQUEST']._serialized_end=188
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=190
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=238
  _globals['_CREATEUSERREQUEST']._serialized_start=240
  _globals['_CREATEUSERREQUEST']._serialized_end=286
  _globals['_CREATEUSERRESPONSE']._serialized_start=288
  _globals['_CREATEUSERRESPONSE']._serialized_end=335
  _globals['_UPDATEUSERREQUEST']._serialized_start=337
  _globals['_UPDATEUSERREQUEST']._serialized_end=383
  _globals['_UPDATEUSERRESPONSE']._serialized_start=385
  _globals['_UPDATEUSERRESPONSE']._serialized_end=432
  _globals['_DELETEUSERREQUEST']._serialized_start=434
  _globals['_DELETEUSERREQUEST']._serialized_end=480
  _globals['_DELETEUSERRESPONSE']._serialized_start=482
  _globals['_DELETEUSERRESPONSE']._serialized_end=529
  _globals['_USERS']._serialized_start=532
  _globals['_USERS']._serialized_end=871
# @@protoc_insertion_point(module_scope)
