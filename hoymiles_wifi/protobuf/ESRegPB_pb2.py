# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ESRegPB.proto
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
    'ESRegPB.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rESRegPB.proto\x12\"com.hoymiles_wifi.protobuf.ESRegPB\"@\n\x07\x43hgCPMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x0e\n\x06sw_ver\x18\x02 \x01(\x05\x12\x0e\n\x06hw_ver\x18\x03 \x01(\x05\"\x8d\x02\n\x0b\x45SRegReqDTO\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12=\n\x05meter\x18\x02 \x01(\x0b\x32..com.hoymiles_wifi.protobuf.ESRegPB.RegMeterMO\x12\x39\n\x03inv\x18\x03 \x03(\x0b\x32,.com.hoymiles_wifi.protobuf.ESRegPB.RegInvMO\x12\x10\n\x08gen_mode\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x05\x12\x0e\n\x06offset\x18\x06 \x01(\x05\x12\x39\n\x03mid\x18\x07 \x03(\x0b\x32,.com.hoymiles_wifi.protobuf.ESRegPB.RegMidMO\x12\x0b\n\x03\x64\x66s\x18\x08 \x01(\x03\"M\n\x0b\x45SRegResDTO\x12\x0c\n\x04time\x18\x01 \x01(\x05\x12\x14\n\x0ctime_ymd_hms\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\n\n\x02\x63p\x18\x04 \x01(\x05\"\xd0\x02\n\x08RegInvMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0e\n\x06hw_ver\x18\x03 \x01(\t\x12\x10\n\x08sw_m_ver\x18\x04 \x01(\t\x12\x10\n\x08sw_s_ver\x18\x05 \x01(\t\x12\x12\n\nsw_sys_ver\x18\x06 \x01(\t\x12\x0e\n\x06\x62ms_sn\x18\x07 \x01(\t\x12\x12\n\nbms_hw_ver\x18\x08 \x01(\t\x12\x12\n\nbms_sw_ver\x18\t \x01(\t\x12\x0f\n\x07\x62ms_cap\x18\n \x01(\x05\x12\x0e\n\x06pv_num\x18\x0b \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x0c \x01(\x05\x12\x12\n\nmodel_name\x18\r \x01(\t\x12\x10\n\x08\x62ms_prot\x18\x0e \x01(\x05\x12\x10\n\x08\x62ms_type\x18\x0f \x01(\x05\x12\x38\n\x03\x63ps\x18\x10 \x03(\x0b\x32+.com.hoymiles_wifi.protobuf.ESRegPB.ChgCPMO\"\'\n\nRegMeterMO\x12\n\n\x02sn\x18\x01 \x01(\t\x12\r\n\x05sn_pv\x18\x02 \x01(\t\"A\n\x08RegMidMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x0e\n\x06sw_ver\x18\x02 \x01(\t\x12\x0e\n\x06hw_ver\x18\x03 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ESRegPB_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHGCPMO']._serialized_start=53
  _globals['_CHGCPMO']._serialized_end=117
  _globals['_ESREGREQDTO']._serialized_start=120
  _globals['_ESREGREQDTO']._serialized_end=389
  _globals['_ESREGRESDTO']._serialized_start=391
  _globals['_ESREGRESDTO']._serialized_end=468
  _globals['_REGINVMO']._serialized_start=471
  _globals['_REGINVMO']._serialized_end=807
  _globals['_REGMETERMO']._serialized_start=809
  _globals['_REGMETERMO']._serialized_end=848
  _globals['_REGMIDMO']._serialized_start=850
  _globals['_REGMIDMO']._serialized_end=915
# @@protoc_insertion_point(module_scope)
