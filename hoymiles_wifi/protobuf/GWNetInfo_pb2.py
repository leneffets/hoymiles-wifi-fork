# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GWNetInfo.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'GWNetInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fGWNetInfo.proto\"\xcd\x01\n\x0cGWNetInfoReq\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x13\n\x0bnet_set_mod\x18\x03 \x01(\x05\x12\x14\n\x0cnet_set_time\x18\x04 \x01(\x05\x12\x15\n\rnet_set_state\x18\x05 \x01(\x05\x12\x0f\n\x07net_mod\x18\x06 \x01(\x05\x12\x10\n\x08net_time\x18\x07 \x01(\x05\x12\x0b\n\x03\x63sq\x18\x08 \x01(\x05\x12\x11\n\tnet_state\x18\t \x01(\x05\x12\x13\n\x0b\x61p_set_tate\x18\n \x01(\x05\",\n\x0cGWNetInfoRes\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GWNetInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GWNETINFOREQ']._serialized_start=20
  _globals['_GWNETINFOREQ']._serialized_end=225
  _globals['_GWNETINFORES']._serialized_start=227
  _globals['_GWNETINFORES']._serialized_end=271
# @@protoc_insertion_point(module_scope)
