# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: InfomationData.proto
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
    'InfomationData.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14InfomationData.proto\"\xcb\x03\n\tDtuInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x0e\n\x06\x64tu_sw\x18\x02 \x01(\x05\x12\x0e\n\x06\x64tu_hw\x18\x03 \x01(\x05\x12\x15\n\rdtu_step_time\x18\x04 \x01(\x05\x12\x11\n\tdtu_rf_hw\x18\x05 \x01(\x05\x12\x11\n\tdtu_rf_sw\x18\x06 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_model\x18\x07 \x01(\x05\x12\x10\n\x08gprs_vsn\x18\x08 \x01(\t\x12\x10\n\x08wifi_vsn\x18\t \x01(\t\x12\x0e\n\x06ka_nub\x18\n \x01(\t\x12\x13\n\x0b\x64tu_rule_id\x18\x0b \x01(\x05\x12\x16\n\x0e\x64tu_error_code\x18\x0c \x01(\x05\x12\x11\n\tgrid_type\x18\r \x01(\x05\x12\x1a\n\x12zero_export_switch\x18\x0e \x01(\x05\x12\x17\n\x0fsurplus_power_a\x18\x0f \x01(\x05\x12\x17\n\x0fsurplus_power_b\x18\x10 \x01(\x05\x12\x17\n\x0fsurplus_power_c\x18\x11 \x01(\x05\x12\x1b\n\x13zero_export_control\x18\x12 \x01(\x05\x12\x1c\n\x14phase_balance_switch\x18\x13 \x01(\x05\x12 \n\x18tolerance_between_phases\x18\x14 \x01(\x05\"\x81\x01\n\x0bMeterInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\x10\n\x08meter_sn\x18\x02 \x01(\x03\x12\x13\n\x0bmeter_model\x18\x03 \x01(\x05\x12\x10\n\x08meter_ct\x18\x04 \x01(\x05\x12\x0f\n\x07\x63om_way\x18\x05 \x01(\x05\x12\x13\n\x0b\x61\x63\x63\x65ss_mode\x18\x06 \x01(\x05\"`\n\x08RpInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\r\n\x05rp_sn\x18\x02 \x01(\x03\x12\r\n\x05rp_sw\x18\x03 \x01(\x05\x12\r\n\x05rp_hw\x18\x04 \x01(\x05\x12\x12\n\nrp_rule_id\x18\x05 \x01(\x05\"\xcc\x01\n\x08PvInfoMO\x12\x13\n\x0b\x64\x65vice_kind\x18\x01 \x01(\x05\x12\r\n\x05pv_sn\x18\x02 \x01(\x03\x12\x0f\n\x07pv_usfw\x18\x03 \x01(\x05\x12\r\n\x05pv_sw\x18\x04 \x01(\x05\x12\x10\n\x08pv_hw_pn\x18\x05 \x01(\x05\x12\r\n\x05pv_hw\x18\x06 \x01(\x05\x12\x13\n\x0bpv_gpf_code\x18\x07 \x01(\x05\x12\x0e\n\x06pv_gpf\x18\x08 \x01(\x05\x12\x10\n\x08pv_rf_hw\x18\t \x01(\x05\x12\x10\n\x08pv_rf_sw\x18\n \x01(\x05\x12\x12\n\nmi_rule_id\x18\x0b \x01(\x05\"\'\n\tFeatureMO\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"\xa4\x02\n\x0eInfoDataReqDTO\x12\x0e\n\x06\x64tu_sn\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x12\n\ndevice_nub\x18\x03 \x01(\x05\x12\x0e\n\x06pv_nub\x18\x04 \x01(\x05\x12\x13\n\x0bpackage_nub\x18\x05 \x01(\x05\x12\x13\n\x0bpackage_now\x18\x06 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\x05\x12\x1c\n\x08mDtuInfo\x18\x08 \x01(\x0b\x32\n.DtuInfoMO\x12 \n\nmMeterInfo\x18\t \x03(\x0b\x32\x0c.MeterInfoMO\x12\x1a\n\x07mRpInfo\x18\n \x03(\x0b\x32\t.RpInfoMO\x12\x1a\n\x07mpvInfo\x18\x0b \x03(\x0b\x32\t.PvInfoMO\x12\x1d\n\tm_feature\x18\x0c \x03(\x0b\x32\n.FeatureMO\"m\n\x0eInfoDataResDTO\x12\x14\n\x0ctime_ymd_hms\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x13\n\x0bpackage_now\x18\x03 \x01(\x05\x12\x12\n\nerror_code\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InfomationData_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DTUINFOMO']._serialized_start=25
  _globals['_DTUINFOMO']._serialized_end=484
  _globals['_METERINFOMO']._serialized_start=487
  _globals['_METERINFOMO']._serialized_end=616
  _globals['_RPINFOMO']._serialized_start=618
  _globals['_RPINFOMO']._serialized_end=714
  _globals['_PVINFOMO']._serialized_start=717
  _globals['_PVINFOMO']._serialized_end=921
  _globals['_FEATUREMO']._serialized_start=923
  _globals['_FEATUREMO']._serialized_end=962
  _globals['_INFODATAREQDTO']._serialized_start=965
  _globals['_INFODATAREQDTO']._serialized_end=1257
  _globals['_INFODATARESDTO']._serialized_start=1259
  _globals['_INFODATARESDTO']._serialized_end=1368
# @@protoc_insertion_point(module_scope)
