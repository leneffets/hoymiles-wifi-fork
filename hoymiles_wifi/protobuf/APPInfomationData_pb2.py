# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: APPInfomationData.proto
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
    'APPInfomationData.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x41PPInfomationData.proto\"\xa6\x04\n\x0c\x41PPDtuInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x16\n\x0e\x64tu_sw_version\x18\x02 \x01(\x05\x12\x16\n\x0e\x64tu_hw_version\x18\x03 \x01(\x05\x12\x15\n\rdtu_step_time\x18\x04 \x01(\x05\x12\x19\n\x11\x64tu_rf_hw_version\x18\x05 \x01(\x05\x12\x19\n\x11\x64tu_rf_sw_version\x18\x06 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_model\x18\x07 \x01(\x05\x12\x1a\n\x12\x63ommunication_time\x18\x08 \x01(\x05\x12\x17\n\x0fsignal_strength\x18\t \x01(\x05\x12\x14\n\x0cgprs_version\x18\n \x01(\t\x12\x14\n\x0cwifi_version\x18\x0b \x01(\t\x12\x11\n\tka_number\x18\x0c \x01(\t\x12\x13\n\x0b\x64tu_rule_id\x18\r \x01(\x05\x12\x16\n\x0e\x64tu_error_code\x18\x0e \x01(\x05\x12\x13\n\x0b\x64tu485_mode\x18\x0f \x01(\x05\x12\x16\n\x0e\x64tu485_address\x18\x10 \x01(\x05\x12\x1c\n\x14sub1g_frequency_band\x18\x11 \x01(\x05\x12\"\n\x1asub1g_channel_total_number\x18\x12 \x01(\x05\x12\x1c\n\x14sub1g_channel_number\x18\x13 \x01(\x05\x12\x10\n\x08sub1g_rp\x18\x14 \x01(\x05\x12\x1b\n\x13sub1g_channel_total\x18\x15 \x01(\x05\x12\x11\n\tgprs_imei\x18\x16 \x01(\t\"\xc2\x01\n\x0e\x41PPMeterInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x1b\n\x13meter_serial_number\x18\x02 \x01(\x03\x12\x13\n\x0bmeter_model\x18\x03 \x01(\x05\x12\x10\n\x08meter_ct\x18\x04 \x01(\x05\x12\x19\n\x11\x63ommunication_way\x18\x05 \x01(\x05\x12\x13\n\x0b\x61\x63\x63\x65ss_mode\x18\x06 \x01(\x05\x12\x12\n\nsw_version\x18\x07 \x01(\x05\x12\x13\n\x0bmeter_value\x18\x08 \x01(\t\"~\n\x0b\x41PPRpInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x18\n\x10rp_serial_number\x18\x02 \x01(\x03\x12\x15\n\rrp_sw_version\x18\x03 \x01(\x05\x12\x15\n\rrp_hw_version\x18\x04 \x01(\x05\x12\x12\n\nrp_rule_id\x18\x05 \x01(\x05\"\x95\x02\n\x0b\x41PPPvInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x18\n\x10pv_serial_number\x18\x02 \x01(\x03\x12\x0f\n\x07pv_usfw\x18\x03 \x01(\x05\x12\x15\n\rpv_sw_version\x18\x04 \x01(\x05\x12\x19\n\x11pv_hw_part_number\x18\x05 \x01(\x05\x12\x15\n\rpv_hw_version\x18\x06 \x01(\x05\x12\x1c\n\x14pv_grid_profile_code\x18\x07 \x01(\x05\x12\x17\n\x0fpv_grid_profile\x18\x08 \x01(\x05\x12\x18\n\x10pv_rf_hw_version\x18\t \x01(\x05\x12\x18\n\x10pv_rf_sw_version\x18\n \x01(\x05\x12\x12\n\nmi_rule_id\x18\x0b \x01(\x05\"*\n\x0c\x41PPFeatureMO\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"\xed\x02\n\x11\x41PPInfoDataReqDTO\x12\x19\n\x11\x64tu_serial_number\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x15\n\rdevice_number\x18\x03 \x01(\x05\x12\x11\n\tpv_number\x18\x04 \x01(\x05\x12\x16\n\x0epackage_number\x18\x05 \x01(\x05\x12\x17\n\x0f\x63urrent_package\x18\x06 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\x05\x12\x1f\n\x08\x64tu_info\x18\x08 \x01(\x0b\x32\r.APPDtuInfoMO\x12#\n\nmeter_info\x18\t \x03(\x0b\x32\x0f.APPMeterInfoMO\x12\x1d\n\x07rp_info\x18\n \x03(\x0b\x32\x0c.APPRpInfoMO\x12\x1d\n\x07pv_info\x18\x0b \x03(\x0b\x32\x0c.APPPvInfoMO\x12\x15\n\runknown_field\x18\x0c \x01(\r\x12#\n\x0c\x61pp_features\x18\r \x03(\x0b\x32\r.APPFeatureMO\"t\n\x11\x41PPInfoDataResDTO\x12\x14\n\x0ctime_ymd_hms\x18\x01 \x01(\x0c\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x17\n\x0f\x63urrent_package\x18\x03 \x01(\x05\x12\x12\n\nerror_code\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'APPInfomationData_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APPDTUINFOMO']._serialized_start=28
  _globals['_APPDTUINFOMO']._serialized_end=578
  _globals['_APPMETERINFOMO']._serialized_start=581
  _globals['_APPMETERINFOMO']._serialized_end=775
  _globals['_APPRPINFOMO']._serialized_start=777
  _globals['_APPRPINFOMO']._serialized_end=903
  _globals['_APPPVINFOMO']._serialized_start=906
  _globals['_APPPVINFOMO']._serialized_end=1183
  _globals['_APPFEATUREMO']._serialized_start=1185
  _globals['_APPFEATUREMO']._serialized_end=1227
  _globals['_APPINFODATAREQDTO']._serialized_start=1230
  _globals['_APPINFODATAREQDTO']._serialized_end=1595
  _globals['_APPINFODATARESDTO']._serialized_start=1597
  _globals['_APPINFODATARESDTO']._serialized_end=1713
# @@protoc_insertion_point(module_scope)
