# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\x12\x07\x65xample\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\x1e\n\rSimpleMessage\x12\r\n\x05\x66ield\x18\x01 \x01(\x05\"-\n\x0fKeyValueMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"\xae\x01\n\nMapMessage\x12\x39\n\x17repeated_keyvalue_field\x18\x01 \x03(\x0b\x32\x18.example.KeyValueMessage\x12\x34\n\tmap_field\x18\x02 \x03(\x0b\x32!.example.MapMessage.MapFieldEntry\x1a/\n\rMapFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x8e\x01\n\x0bTimeMessage\x12)\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xfa\x08\n\x0e\x43omplexMessage\x12\x14\n\x0c\x64ouble_field\x18\x01 \x01(\x01\x12\x13\n\x0b\x66loat_field\x18\x02 \x01(\x02\x12\x13\n\x0bint32_field\x18\x03 \x01(\x05\x12\x13\n\x0bint64_field\x18\x04 \x01(\x03\x12\x14\n\x0cuint32_field\x18\x05 \x01(\r\x12\x14\n\x0cuint64_field\x18\x06 \x01(\x04\x12\x14\n\x0csint32_field\x18\x07 \x01(\x11\x12\x14\n\x0csint64_field\x18\x08 \x01(\x12\x12\x15\n\rfixed32_field\x18\t \x01(\x07\x12\x15\n\rfixed64_field\x18\n \x01(\x06\x12\x16\n\x0esfixed32_field\x18\x0b \x01(\x0f\x12\x16\n\x0esfixed64_field\x18\x0c \x01(\x10\x12\x12\n\nbool_field\x18\r \x01(\x08\x12\x14\n\x0cstring_field\x18\x0e \x01(\t\x12\x13\n\x0b\x62ytes_field\x18\x0f \x01(\x0c\x12\x30\n\nenum_field\x18\x10 \x01(\x0e\x32\x1c.example.ComplexMessage.Enum\x12\x16\n\x0erepeated_field\x18\x11 \x03(\x05\x12,\n\x0cnested_field\x18\x12 \x01(\x0b\x32\x16.example.SimpleMessage\x12\x35\n\x15repeated_nested_field\x18\x13 \x03(\x0b\x32\x16.example.SimpleMessage\x12\x39\n\x17repeated_keyvalue_field\x18\x14 \x03(\x0b\x32\x18.example.KeyValueMessage\x12\x45\n\x10simple_map_field\x18\x15 \x03(\x0b\x32+.example.ComplexMessage.SimpleMapFieldEntry\x12G\n\x11\x63omplex_map_field\x18\x16 \x03(\x0b\x32,.example.ComplexMessage.ComplexMapFieldEntry\x12/\n\x12repeated_map_field\x18\x17 \x03(\x0b\x32\x13.example.MapMessage\x12\x43\n\x0fmap_times_field\x18\x18 \x03(\x0b\x32*.example.ComplexMessage.MapTimesFieldEntry\x12\x32\n\x14repeated_times_field\x18\x19 \x03(\x0b\x32\x14.example.TimeMessage\x1a\x35\n\x13SimpleMapFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1aK\n\x14\x43omplexMapFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.example.MapMessage:\x02\x38\x01\x1aJ\n\x12MapTimesFieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.example.TimeMessage:\x02\x38\x01\"*\n\x04\x45num\x12\n\n\x06ITEM_0\x10\x00\x12\n\n\x06ITEM_1\x10\x01\x12\n\n\x06ITEM_2\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_COMPLEXMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='example.ComplexMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ITEM_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ITEM_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1597,
  serialized_end=1639,
)
_sym_db.RegisterEnumDescriptor(_COMPLEXMESSAGE_ENUM)


_SIMPLEMESSAGE = _descriptor.Descriptor(
  name='SimpleMessage',
  full_name='example.SimpleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='example.SimpleMessage.field', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=121,
)


_KEYVALUEMESSAGE = _descriptor.Descriptor(
  name='KeyValueMessage',
  full_name='example.KeyValueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.KeyValueMessage.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.KeyValueMessage.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=168,
)


_MAPMESSAGE_MAPFIELDENTRY = _descriptor.Descriptor(
  name='MapFieldEntry',
  full_name='example.MapMessage.MapFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.MapMessage.MapFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.MapMessage.MapFieldEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=345,
)

_MAPMESSAGE = _descriptor.Descriptor(
  name='MapMessage',
  full_name='example.MapMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeated_keyvalue_field', full_name='example.MapMessage.repeated_keyvalue_field', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map_field', full_name='example.MapMessage.map_field', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MAPMESSAGE_MAPFIELDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=345,
)


_TIMEMESSAGE = _descriptor.Descriptor(
  name='TimeMessage',
  full_name='example.TimeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='example.TimeMessage.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='example.TimeMessage.end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='example.TimeMessage.duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=490,
)


_COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY = _descriptor.Descriptor(
  name='SimpleMapFieldEntry',
  full_name='example.ComplexMessage.SimpleMapFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.ComplexMessage.SimpleMapFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.ComplexMessage.SimpleMapFieldEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1389,
  serialized_end=1442,
)

_COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY = _descriptor.Descriptor(
  name='ComplexMapFieldEntry',
  full_name='example.ComplexMessage.ComplexMapFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.ComplexMessage.ComplexMapFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.ComplexMessage.ComplexMapFieldEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1444,
  serialized_end=1519,
)

_COMPLEXMESSAGE_MAPTIMESFIELDENTRY = _descriptor.Descriptor(
  name='MapTimesFieldEntry',
  full_name='example.ComplexMessage.MapTimesFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.ComplexMessage.MapTimesFieldEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.ComplexMessage.MapTimesFieldEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1521,
  serialized_end=1595,
)

_COMPLEXMESSAGE = _descriptor.Descriptor(
  name='ComplexMessage',
  full_name='example.ComplexMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_field', full_name='example.ComplexMessage.double_field', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_field', full_name='example.ComplexMessage.float_field', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_field', full_name='example.ComplexMessage.int32_field', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_field', full_name='example.ComplexMessage.int64_field', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint32_field', full_name='example.ComplexMessage.uint32_field', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint64_field', full_name='example.ComplexMessage.uint64_field', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint32_field', full_name='example.ComplexMessage.sint32_field', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sint64_field', full_name='example.ComplexMessage.sint64_field', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed32_field', full_name='example.ComplexMessage.fixed32_field', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed64_field', full_name='example.ComplexMessage.fixed64_field', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed32_field', full_name='example.ComplexMessage.sfixed32_field', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sfixed64_field', full_name='example.ComplexMessage.sfixed64_field', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_field', full_name='example.ComplexMessage.bool_field', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_field', full_name='example.ComplexMessage.string_field', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_field', full_name='example.ComplexMessage.bytes_field', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enum_field', full_name='example.ComplexMessage.enum_field', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_field', full_name='example.ComplexMessage.repeated_field', index=16,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_field', full_name='example.ComplexMessage.nested_field', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_nested_field', full_name='example.ComplexMessage.repeated_nested_field', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_keyvalue_field', full_name='example.ComplexMessage.repeated_keyvalue_field', index=19,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simple_map_field', full_name='example.ComplexMessage.simple_map_field', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='complex_map_field', full_name='example.ComplexMessage.complex_map_field', index=21,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_map_field', full_name='example.ComplexMessage.repeated_map_field', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map_times_field', full_name='example.ComplexMessage.map_times_field', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_times_field', full_name='example.ComplexMessage.repeated_times_field', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY, _COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY, _COMPLEXMESSAGE_MAPTIMESFIELDENTRY, ],
  enum_types=[
    _COMPLEXMESSAGE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=1639,
)

_MAPMESSAGE_MAPFIELDENTRY.containing_type = _MAPMESSAGE
_MAPMESSAGE.fields_by_name['repeated_keyvalue_field'].message_type = _KEYVALUEMESSAGE
_MAPMESSAGE.fields_by_name['map_field'].message_type = _MAPMESSAGE_MAPFIELDENTRY
_TIMEMESSAGE.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEMESSAGE.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEMESSAGE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY.containing_type = _COMPLEXMESSAGE
_COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY.fields_by_name['value'].message_type = _MAPMESSAGE
_COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY.containing_type = _COMPLEXMESSAGE
_COMPLEXMESSAGE_MAPTIMESFIELDENTRY.fields_by_name['value'].message_type = _TIMEMESSAGE
_COMPLEXMESSAGE_MAPTIMESFIELDENTRY.containing_type = _COMPLEXMESSAGE
_COMPLEXMESSAGE.fields_by_name['enum_field'].enum_type = _COMPLEXMESSAGE_ENUM
_COMPLEXMESSAGE.fields_by_name['nested_field'].message_type = _SIMPLEMESSAGE
_COMPLEXMESSAGE.fields_by_name['repeated_nested_field'].message_type = _SIMPLEMESSAGE
_COMPLEXMESSAGE.fields_by_name['repeated_keyvalue_field'].message_type = _KEYVALUEMESSAGE
_COMPLEXMESSAGE.fields_by_name['simple_map_field'].message_type = _COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY
_COMPLEXMESSAGE.fields_by_name['complex_map_field'].message_type = _COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY
_COMPLEXMESSAGE.fields_by_name['repeated_map_field'].message_type = _MAPMESSAGE
_COMPLEXMESSAGE.fields_by_name['map_times_field'].message_type = _COMPLEXMESSAGE_MAPTIMESFIELDENTRY
_COMPLEXMESSAGE.fields_by_name['repeated_times_field'].message_type = _TIMEMESSAGE
_COMPLEXMESSAGE_ENUM.containing_type = _COMPLEXMESSAGE
DESCRIPTOR.message_types_by_name['SimpleMessage'] = _SIMPLEMESSAGE
DESCRIPTOR.message_types_by_name['KeyValueMessage'] = _KEYVALUEMESSAGE
DESCRIPTOR.message_types_by_name['MapMessage'] = _MAPMESSAGE
DESCRIPTOR.message_types_by_name['TimeMessage'] = _TIMEMESSAGE
DESCRIPTOR.message_types_by_name['ComplexMessage'] = _COMPLEXMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleMessage = _reflection.GeneratedProtocolMessageType('SimpleMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.SimpleMessage)
  })
_sym_db.RegisterMessage(SimpleMessage)

KeyValueMessage = _reflection.GeneratedProtocolMessageType('KeyValueMessage', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUEMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.KeyValueMessage)
  })
_sym_db.RegisterMessage(KeyValueMessage)

MapMessage = _reflection.GeneratedProtocolMessageType('MapMessage', (_message.Message,), {

  'MapFieldEntry' : _reflection.GeneratedProtocolMessageType('MapFieldEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPMESSAGE_MAPFIELDENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:example.MapMessage.MapFieldEntry)
    })
  ,
  'DESCRIPTOR' : _MAPMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.MapMessage)
  })
_sym_db.RegisterMessage(MapMessage)
_sym_db.RegisterMessage(MapMessage.MapFieldEntry)

TimeMessage = _reflection.GeneratedProtocolMessageType('TimeMessage', (_message.Message,), {
  'DESCRIPTOR' : _TIMEMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.TimeMessage)
  })
_sym_db.RegisterMessage(TimeMessage)

ComplexMessage = _reflection.GeneratedProtocolMessageType('ComplexMessage', (_message.Message,), {

  'SimpleMapFieldEntry' : _reflection.GeneratedProtocolMessageType('SimpleMapFieldEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:example.ComplexMessage.SimpleMapFieldEntry)
    })
  ,

  'ComplexMapFieldEntry' : _reflection.GeneratedProtocolMessageType('ComplexMapFieldEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:example.ComplexMessage.ComplexMapFieldEntry)
    })
  ,

  'MapTimesFieldEntry' : _reflection.GeneratedProtocolMessageType('MapTimesFieldEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPLEXMESSAGE_MAPTIMESFIELDENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:example.ComplexMessage.MapTimesFieldEntry)
    })
  ,
  'DESCRIPTOR' : _COMPLEXMESSAGE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.ComplexMessage)
  })
_sym_db.RegisterMessage(ComplexMessage)
_sym_db.RegisterMessage(ComplexMessage.SimpleMapFieldEntry)
_sym_db.RegisterMessage(ComplexMessage.ComplexMapFieldEntry)
_sym_db.RegisterMessage(ComplexMessage.MapTimesFieldEntry)


_MAPMESSAGE_MAPFIELDENTRY._options = None
_COMPLEXMESSAGE_SIMPLEMAPFIELDENTRY._options = None
_COMPLEXMESSAGE_COMPLEXMAPFIELDENTRY._options = None
_COMPLEXMESSAGE_MAPTIMESFIELDENTRY._options = None
# @@protoc_insertion_point(module_scope)
