# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/protocol/server_spec.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.net import address_pb2 as common_dot_net_dot_address__pb2
from common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!common/protocol/server_spec.proto\x12\x1av2ray.core.common.protocol\x1a\x18\x63ommon/net/address.proto\x1a\x1a\x63ommon/protocol/user.proto\"\x82\x01\n\x0eServerEndpoint\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12.\n\x04user\x18\x03 \x03(\x0b\x32 .v2ray.core.common.protocol.UserBo\n\x1e\x63om.v2ray.core.common.protocolP\x01Z.github.com/v2fly/v2ray-core/v5/common/protocol\xaa\x02\x1aV2Ray.Core.Common.Protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.protocol.server_spec_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.v2ray.core.common.protocolP\001Z.github.com/v2fly/v2ray-core/v5/common/protocol\252\002\032V2Ray.Core.Common.Protocol'
  _globals['_SERVERENDPOINT']._serialized_start=120
  _globals['_SERVERENDPOINT']._serialized_end=250
# @@protoc_insertion_point(module_scope)
