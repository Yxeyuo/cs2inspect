# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: econ.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'econ.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\necon.proto\"\x99\x08\n\x19\x43\x45\x63onItemPreviewDataBlock\x12\x16\n\taccountid\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x13\n\x06itemid\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x15\n\x08\x64\x65\x66index\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x17\n\npaintindex\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x13\n\x06rarity\x18\x05 \x01(\rH\x04\x88\x01\x01\x12\x14\n\x07quality\x18\x06 \x01(\rH\x05\x88\x01\x01\x12\x16\n\tpaintwear\x18\x07 \x01(\rH\x06\x88\x01\x01\x12\x16\n\tpaintseed\x18\x08 \x01(\rH\x07\x88\x01\x01\x12\x1f\n\x12killeaterscoretype\x18\t \x01(\rH\x08\x88\x01\x01\x12\x1b\n\x0ekilleatervalue\x18\n \x01(\rH\t\x88\x01\x01\x12\x17\n\ncustomname\x18\x0b \x01(\tH\n\x88\x01\x01\x12\x34\n\x08stickers\x18\x0c \x03(\x0b\x32\".CEconItemPreviewDataBlock.Sticker\x12\x16\n\tinventory\x18\r \x01(\rH\x0b\x88\x01\x01\x12\x13\n\x06origin\x18\x0e \x01(\rH\x0c\x88\x01\x01\x12\x14\n\x07questid\x18\x0f \x01(\rH\r\x88\x01\x01\x12\x17\n\ndropreason\x18\x10 \x01(\rH\x0e\x88\x01\x01\x12\x17\n\nmusicindex\x18\x11 \x01(\rH\x0f\x88\x01\x01\x12\x15\n\x08\x65ntindex\x18\x12 \x01(\x05H\x10\x88\x01\x01\x12\x15\n\x08petindex\x18\x13 \x01(\rH\x11\x88\x01\x01\x1a\x95\x02\n\x07Sticker\x12\x11\n\x04slot\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x17\n\nsticker_id\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x11\n\x04wear\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x12\n\x05scale\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x15\n\x08rotation\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12\x14\n\x07tint_id\x18\x06 \x01(\rH\x05\x88\x01\x01\x12\x15\n\x08offset_x\x18\x07 \x01(\x02H\x06\x88\x01\x01\x12\x15\n\x08offset_y\x18\x08 \x01(\x02H\x07\x88\x01\x01\x42\x07\n\x05_slotB\r\n\x0b_sticker_idB\x07\n\x05_wearB\x08\n\x06_scaleB\x0b\n\t_rotationB\n\n\x08_tint_idB\x0b\n\t_offset_xB\x0b\n\t_offset_yB\x0c\n\n_accountidB\t\n\x07_itemidB\x0b\n\t_defindexB\r\n\x0b_paintindexB\t\n\x07_rarityB\n\n\x08_qualityB\x0c\n\n_paintwearB\x0c\n\n_paintseedB\x15\n\x13_killeaterscoretypeB\x11\n\x0f_killeatervalueB\r\n\x0b_customnameB\x0c\n\n_inventoryB\t\n\x07_originB\n\n\x08_questidB\r\n\x0b_dropreasonB\r\n\x0b_musicindexB\x0b\n\t_entindexB\x0b\n\t_petindexb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'econ_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CECONITEMPREVIEWDATABLOCK']._serialized_start=15
  _globals['_CECONITEMPREVIEWDATABLOCK']._serialized_end=1064
  _globals['_CECONITEMPREVIEWDATABLOCK_STICKER']._serialized_start=533
  _globals['_CECONITEMPREVIEWDATABLOCK_STICKER']._serialized_end=810
# @@protoc_insertion_point(module_scope)
