# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from transport import config_pb2 as transport_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\x12\nv2ray.core\x1a\x19google/protobuf/any.proto\x1a\x16transport/config.proto\"\xf7\x01\n\x06\x43onfig\x12\x31\n\x07inbound\x18\x01 \x03(\x0b\x32 .v2ray.core.InboundHandlerConfig\x12\x33\n\x08outbound\x18\x02 \x03(\x0b\x32!.v2ray.core.OutboundHandlerConfig\x12!\n\x03\x61pp\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x33\n\ttransport\x18\x05 \x01(\x0b\x32\x1c.v2ray.core.transport.ConfigB\x02\x18\x01\x12\'\n\textension\x18\x06 \x03(\x0b\x32\x14.google.protobuf.AnyJ\x04\x08\x03\x10\x04\"\x82\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12/\n\x11receiver_settings\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12,\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\xa2\x01\n\x15OutboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12-\n\x0fsender_settings\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12,\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x05 \x01(\tBD\n\x0e\x63om.v2ray.coreP\x01Z#github.com/v2fly/v2ray-core/v5;core\xaa\x02\nV2Ray.Coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.v2ray.coreP\001Z#github.com/v2fly/v2ray-core/v5;core\252\002\nV2Ray.Core'
  _globals['_CONFIG'].fields_by_name['transport']._options = None
  _globals['_CONFIG'].fields_by_name['transport']._serialized_options = b'\030\001'
  _globals['_CONFIG']._serialized_start=80
  _globals['_CONFIG']._serialized_end=327
  _globals['_INBOUNDHANDLERCONFIG']._serialized_start=330
  _globals['_INBOUNDHANDLERCONFIG']._serialized_end=460
  _globals['_OUTBOUNDHANDLERCONFIG']._serialized_start=463
  _globals['_OUTBOUNDHANDLERCONFIG']._serialized_end=625
# @@protoc_insertion_point(module_scope)
