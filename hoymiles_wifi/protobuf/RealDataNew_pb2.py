# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: RealDataNew.proto
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
    'RealDataNew.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11RealDataNew.proto\"\x9b\x05\n\x07MeterMO\x12\x13\n\x0b\x64\x65vice_type\x18\x01 \x01(\x05\x12\x15\n\rserial_number\x18\x02 \x01(\x03\x12\x19\n\x11phase_total_power\x18\x03 \x01(\x05\x12\x15\n\rphase_A_power\x18\x04 \x01(\x05\x12\x15\n\rphase_B_power\x18\x05 \x01(\x05\x12\x15\n\rphase_C_power\x18\x06 \x01(\x05\x12\x1a\n\x12power_factor_total\x18\x07 \x01(\x05\x12\x1a\n\x12\x65nergy_total_power\x18\x08 \x01(\x05\x12\x16\n\x0e\x65nergy_phase_A\x18\t \x01(\x05\x12\x16\n\x0e\x65nergy_phase_B\x18\n \x01(\x05\x12\x16\n\x0e\x65nergy_phase_C\x18\x0b \x01(\x05\x12\x1d\n\x15\x65nergy_total_consumed\x18\x0c \x01(\x05\x12\x1f\n\x17\x65nergy_phase_A_consumed\x18\r \x01(\x05\x12\x1f\n\x17\x65nergy_phase_B_consumed\x18\x0e \x01(\x05\x12\x1f\n\x17\x65nergy_phase_C_consumed\x18\x0f \x01(\x05\x12\x12\n\nfault_code\x18\x10 \x01(\x05\x12\x17\n\x0fvoltage_phase_A\x18\x11 \x01(\x05\x12\x17\n\x0fvoltage_phase_B\x18\x12 \x01(\x05\x12\x17\n\x0fvoltage_phase_C\x18\x13 \x01(\x05\x12\x17\n\x0f\x63urrent_phase_A\x18\x14 \x01(\x05\x12\x17\n\x0f\x63urrent_phase_B\x18\x15 \x01(\x05\x12\x17\n\x0f\x63urrent_phase_C\x18\x16 \x01(\x05\x12\x1c\n\x14power_factor_phase_A\x18\x17 \x01(\x05\x12\x1c\n\x14power_factor_phase_B\x18\x18 \x01(\x05\x12\x1c\n\x14power_factor_phase_C\x18\x19 \x01(\x05\"i\n\x04RpMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x11\n\tsignature\x18\x02 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\x05\x12\x11\n\tpv_number\x18\x04 \x01(\x05\x12\x13\n\x0blink_status\x18\x05 \x01(\x05\"\xb0\x01\n\x05RSDMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x18\n\x10\x66irmware_version\x18\x02 \x01(\x05\x12\x0f\n\x07voltage\x18\x03 \x01(\x05\x12\r\n\x05power\x18\x04 \x01(\x05\x12\x13\n\x0btemperature\x18\x05 \x01(\x05\x12\x16\n\x0ewarning_number\x18\x06 \x01(\x05\x12\x14\n\x0c\x63rc_checksum\x18\x07 \x01(\x05\x12\x13\n\x0blink_status\x18\x08 \x01(\x05\"\xbf\x02\n\x05SGSMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x18\n\x10\x66irmware_version\x18\x02 \x01(\x05\x12\x0f\n\x07voltage\x18\x03 \x01(\x05\x12\x11\n\tfrequency\x18\x04 \x01(\x05\x12\x14\n\x0c\x61\x63tive_power\x18\x05 \x01(\x05\x12\x16\n\x0ereactive_power\x18\x06 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x07 \x01(\x05\x12\x14\n\x0cpower_factor\x18\x08 \x01(\x05\x12\x13\n\x0btemperature\x18\t \x01(\x05\x12\x16\n\x0ewarning_number\x18\n \x01(\x05\x12\x14\n\x0c\x63rc_checksum\x18\x0b \x01(\x05\x12\x13\n\x0blink_status\x18\x0c \x01(\x05\x12\x13\n\x0bpower_limit\x18\r \x01(\x05\x12\x1f\n\x17modulation_index_signal\x18\x14 \x01(\x05\"\xe9\x03\n\x05TGSMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x18\n\x10\x66irmware_version\x18\x02 \x01(\x05\x12\x17\n\x0fvoltage_phase_A\x18\x03 \x01(\x05\x12\x17\n\x0fvoltage_phase_B\x18\x04 \x01(\x05\x12\x17\n\x0fvoltage_phase_C\x18\x05 \x01(\x05\x12\x17\n\x0fvoltage_line_AB\x18\x06 \x01(\x05\x12\x17\n\x0fvoltage_line_BC\x18\x07 \x01(\x05\x12\x17\n\x0fvoltage_line_CA\x18\x08 \x01(\x05\x12\x11\n\tfrequency\x18\t \x01(\x05\x12\x14\n\x0c\x61\x63tive_power\x18\n \x01(\x05\x12\x16\n\x0ereactive_power\x18\x0b \x01(\x05\x12\x17\n\x0f\x63urrent_phase_A\x18\x0c \x01(\x05\x12\x17\n\x0f\x63urrent_phase_B\x18\r \x01(\x05\x12\x17\n\x0f\x63urrent_phase_C\x18\x0e \x01(\x05\x12\x14\n\x0cpower_factor\x18\x0f \x01(\x05\x12\x13\n\x0btemperature\x18\x10 \x01(\x05\x12\x16\n\x0ewarning_number\x18\x11 \x01(\x05\x12\x14\n\x0c\x63rc_checksum\x18\x12 \x01(\x05\x12\x13\n\x0blink_status\x18\x13 \x01(\x05\x12\x1f\n\x17modulation_index_signal\x18\x14 \x01(\x05\"\xa3\x01\n\x04PvMO\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x13\n\x0bport_number\x18\x02 \x01(\x05\x12\x0f\n\x07voltage\x18\x03 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x04 \x01(\x05\x12\r\n\x05power\x18\x05 \x01(\x05\x12\x14\n\x0c\x65nergy_total\x18\x06 \x01(\x05\x12\x14\n\x0c\x65nergy_daily\x18\x07 \x01(\x05\x12\x12\n\nerror_code\x18\x08 \x01(\x05\"\xbf\x02\n\x11RealDataNewReqDTO\x12\x1c\n\x14\x64\x65vice_serial_number\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x05\x12\n\n\x02\x61p\x18\x03 \x01(\x05\x12\n\n\x02\x63p\x18\x04 \x01(\x05\x12\x18\n\x10\x66irmware_version\x18\x05 \x01(\x05\x12\x1c\n\nmeter_data\x18\x06 \x03(\x0b\x32\x08.MeterMO\x12\x16\n\x07rp_data\x18\x07 \x03(\x0b\x32\x05.RpMO\x12\x18\n\x08rsd_data\x18\x08 \x03(\x0b\x32\x06.RSDMO\x12\x18\n\x08sgs_data\x18\t \x03(\x0b\x32\x06.SGSMO\x12\x18\n\x08tgs_data\x18\n \x03(\x0b\x32\x06.TGSMO\x12\x16\n\x07pv_data\x18\x0b \x03(\x0b\x32\x05.PvMO\x12\x11\n\tdtu_power\x18\x0c \x01(\x04\x12\x18\n\x10\x64tu_daily_energy\x18\r \x01(\x04\"g\n\x11RealDataNewResDTO\x12\x14\n\x0ctime_ymd_hms\x18\x01 \x01(\x0c\x12\n\n\x02\x63p\x18\x02 \x01(\x05\x12\x12\n\nerror_code\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RealDataNew_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_METERMO']._serialized_start=22
  _globals['_METERMO']._serialized_end=689
  _globals['_RPMO']._serialized_start=691
  _globals['_RPMO']._serialized_end=796
  _globals['_RSDMO']._serialized_start=799
  _globals['_RSDMO']._serialized_end=975
  _globals['_SGSMO']._serialized_start=978
  _globals['_SGSMO']._serialized_end=1297
  _globals['_TGSMO']._serialized_start=1300
  _globals['_TGSMO']._serialized_end=1789
  _globals['_PVMO']._serialized_start=1792
  _globals['_PVMO']._serialized_end=1955
  _globals['_REALDATANEWREQDTO']._serialized_start=1958
  _globals['_REALDATANEWREQDTO']._serialized_end=2277
  _globals['_REALDATANEWRESDTO']._serialized_start=2279
  _globals['_REALDATANEWRESDTO']._serialized_end=2382
# @@protoc_insertion_point(module_scope)
