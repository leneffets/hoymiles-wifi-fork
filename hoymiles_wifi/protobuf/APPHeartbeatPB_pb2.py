# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: APPHeartbeatPB.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'APPHeartbeatPB.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x41PPHeartbeatPB.proto\x12)com.hoymiles_wifi.protobuf.AppHeartbeatPB\"n\n\x08HBReqDTO\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x0b\n\x03\x63sq\x18\x03 \x01(\x05\x12\x19\n\x11\x64tu_serial_number\x18\x04 \x01(\t\x12\x1c\n\x14\x64\x65vice_serial_number\x18\x05 \x01(\t\">\n\x08HBResDTO\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x14\n\x0ctime_ymd_hms\x18\x03 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'APPHeartbeatPB_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HBREQDTO']._serialized_start=67
  _globals['_HBREQDTO']._serialized_end=177
  _globals['_HBRESDTO']._serialized_start=179
  _globals['_HBRESDTO']._serialized_end=241
# @@protoc_insertion_point(module_scope)
