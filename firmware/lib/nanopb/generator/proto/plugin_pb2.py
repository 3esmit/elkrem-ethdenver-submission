# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='plugin.proto',
  package='google.protobuf.compiler',
  syntax='proto2',
  serialized_pb=_b('\n\x0cplugin.proto\x12\x18google.protobuf.compiler\x1a google/protobuf/descriptor.proto\"}\n\x14\x43odeGeneratorRequest\x12\x18\n\x10\x66ile_to_generate\x18\x01 \x03(\t\x12\x11\n\tparameter\x18\x02 \x01(\t\x12\x38\n\nproto_file\x18\x0f \x03(\x0b\x32$.google.protobuf.FileDescriptorProto\"\xaa\x01\n\x15\x43odeGeneratorResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\x42\n\x04\x66ile\x18\x0f \x03(\x0b\x32\x34.google.protobuf.compiler.CodeGeneratorResponse.File\x1a>\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0finsertion_point\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x0f \x01(\tB,\n\x1c\x63om.google.protobuf.compilerB\x0cPluginProtos')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])




_CODEGENERATORREQUEST = _descriptor.Descriptor(
  name='CodeGeneratorRequest',
  full_name='google.protobuf.compiler.CodeGeneratorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_to_generate', full_name='google.protobuf.compiler.CodeGeneratorRequest.file_to_generate', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='google.protobuf.compiler.CodeGeneratorRequest.parameter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_file', full_name='google.protobuf.compiler.CodeGeneratorRequest.proto_file', index=2,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=201,
)


_CODEGENERATORRESPONSE_FILE = _descriptor.Descriptor(
  name='File',
  full_name='google.protobuf.compiler.CodeGeneratorResponse.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insertion_point', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.insertion_point', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='google.protobuf.compiler.CodeGeneratorResponse.File.content', index=2,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=374,
)

_CODEGENERATORRESPONSE = _descriptor.Descriptor(
  name='CodeGeneratorResponse',
  full_name='google.protobuf.compiler.CodeGeneratorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='google.protobuf.compiler.CodeGeneratorResponse.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='google.protobuf.compiler.CodeGeneratorResponse.file', index=1,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CODEGENERATORRESPONSE_FILE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=374,
)

_CODEGENERATORREQUEST.fields_by_name['proto_file'].message_type = google_dot_protobuf_dot_descriptor__pb2._FILEDESCRIPTORPROTO
_CODEGENERATORRESPONSE_FILE.containing_type = _CODEGENERATORRESPONSE
_CODEGENERATORRESPONSE.fields_by_name['file'].message_type = _CODEGENERATORRESPONSE_FILE
DESCRIPTOR.message_types_by_name['CodeGeneratorRequest'] = _CODEGENERATORREQUEST
DESCRIPTOR.message_types_by_name['CodeGeneratorResponse'] = _CODEGENERATORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CodeGeneratorRequest = _reflection.GeneratedProtocolMessageType('CodeGeneratorRequest', (_message.Message,), dict(
  DESCRIPTOR = _CODEGENERATORREQUEST,
  __module__ = 'plugin_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorRequest)
  ))
_sym_db.RegisterMessage(CodeGeneratorRequest)

CodeGeneratorResponse = _reflection.GeneratedProtocolMessageType('CodeGeneratorResponse', (_message.Message,), dict(

  File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
    DESCRIPTOR = _CODEGENERATORRESPONSE_FILE,
    __module__ = 'plugin_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorResponse.File)
    ))
  ,
  DESCRIPTOR = _CODEGENERATORRESPONSE,
  __module__ = 'plugin_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.compiler.CodeGeneratorResponse)
  ))
_sym_db.RegisterMessage(CodeGeneratorResponse)
_sym_db.RegisterMessage(CodeGeneratorResponse.File)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.google.protobuf.compilerB\014PluginProtos'))
# @@protoc_insertion_point(module_scope)
