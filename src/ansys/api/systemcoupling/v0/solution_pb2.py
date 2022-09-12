# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: solution.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="solution.proto",
    package="ansys.api.systemcoupling.v0",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0esolution.proto\x12\x1b\x61nsys.api.systemcoupling.v0"\x0e\n\x0cSolveRequest"\x0f\n\rSolveResponse""\n\x10InterruptRequest\x12\x0e\n\x06reason\x18\x01 \x01(\t"\x13\n\x11InterruptResponse"\x1e\n\x0c\x41\x62ortRequest\x12\x0e\n\x06reason\x18\x01 \x01(\t"\x0f\n\rAbortResponse2\xbc\x02\n\x08Solution\x12`\n\x05Solve\x12).ansys.api.systemcoupling.v0.SolveRequest\x1a*.ansys.api.systemcoupling.v0.SolveResponse"\x00\x12l\n\tInterrupt\x12-.ansys.api.systemcoupling.v0.InterruptRequest\x1a..ansys.api.systemcoupling.v0.InterruptResponse"\x00\x12`\n\x05\x41\x62ort\x12).ansys.api.systemcoupling.v0.AbortRequest\x1a*.ansys.api.systemcoupling.v0.AbortResponse"\x00\x62\x06proto3',
)


_SOLVEREQUEST = _descriptor.Descriptor(
    name="SolveRequest",
    full_name="ansys.api.systemcoupling.v0.SolveRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=47,
    serialized_end=61,
)


_SOLVERESPONSE = _descriptor.Descriptor(
    name="SolveResponse",
    full_name="ansys.api.systemcoupling.v0.SolveResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=63,
    serialized_end=78,
)


_INTERRUPTREQUEST = _descriptor.Descriptor(
    name="InterruptRequest",
    full_name="ansys.api.systemcoupling.v0.InterruptRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="reason",
            full_name="ansys.api.systemcoupling.v0.InterruptRequest.reason",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=80,
    serialized_end=114,
)


_INTERRUPTRESPONSE = _descriptor.Descriptor(
    name="InterruptResponse",
    full_name="ansys.api.systemcoupling.v0.InterruptResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=116,
    serialized_end=135,
)


_ABORTREQUEST = _descriptor.Descriptor(
    name="AbortRequest",
    full_name="ansys.api.systemcoupling.v0.AbortRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="reason",
            full_name="ansys.api.systemcoupling.v0.AbortRequest.reason",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=137,
    serialized_end=167,
)


_ABORTRESPONSE = _descriptor.Descriptor(
    name="AbortResponse",
    full_name="ansys.api.systemcoupling.v0.AbortResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=169,
    serialized_end=184,
)

DESCRIPTOR.message_types_by_name["SolveRequest"] = _SOLVEREQUEST
DESCRIPTOR.message_types_by_name["SolveResponse"] = _SOLVERESPONSE
DESCRIPTOR.message_types_by_name["InterruptRequest"] = _INTERRUPTREQUEST
DESCRIPTOR.message_types_by_name["InterruptResponse"] = _INTERRUPTRESPONSE
DESCRIPTOR.message_types_by_name["AbortRequest"] = _ABORTREQUEST
DESCRIPTOR.message_types_by_name["AbortResponse"] = _ABORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SolveRequest = _reflection.GeneratedProtocolMessageType(
    "SolveRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SOLVEREQUEST,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.SolveRequest)
    },
)
_sym_db.RegisterMessage(SolveRequest)

SolveResponse = _reflection.GeneratedProtocolMessageType(
    "SolveResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SOLVERESPONSE,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.SolveResponse)
    },
)
_sym_db.RegisterMessage(SolveResponse)

InterruptRequest = _reflection.GeneratedProtocolMessageType(
    "InterruptRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTERRUPTREQUEST,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.InterruptRequest)
    },
)
_sym_db.RegisterMessage(InterruptRequest)

InterruptResponse = _reflection.GeneratedProtocolMessageType(
    "InterruptResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTERRUPTRESPONSE,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.InterruptResponse)
    },
)
_sym_db.RegisterMessage(InterruptResponse)

AbortRequest = _reflection.GeneratedProtocolMessageType(
    "AbortRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ABORTREQUEST,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.AbortRequest)
    },
)
_sym_db.RegisterMessage(AbortRequest)

AbortResponse = _reflection.GeneratedProtocolMessageType(
    "AbortResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ABORTRESPONSE,
        "__module__": "solution_pb2"
        # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.AbortResponse)
    },
)
_sym_db.RegisterMessage(AbortResponse)


_SOLUTION = _descriptor.ServiceDescriptor(
    name="Solution",
    full_name="ansys.api.systemcoupling.v0.Solution",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=187,
    serialized_end=503,
    methods=[
        _descriptor.MethodDescriptor(
            name="Solve",
            full_name="ansys.api.systemcoupling.v0.Solution.Solve",
            index=0,
            containing_service=None,
            input_type=_SOLVEREQUEST,
            output_type=_SOLVERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Interrupt",
            full_name="ansys.api.systemcoupling.v0.Solution.Interrupt",
            index=1,
            containing_service=None,
            input_type=_INTERRUPTREQUEST,
            output_type=_INTERRUPTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Abort",
            full_name="ansys.api.systemcoupling.v0.Solution.Abort",
            index=2,
            containing_service=None,
            input_type=_ABORTREQUEST,
            output_type=_ABORTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SOLUTION)

DESCRIPTOR.services_by_name["Solution"] = _SOLUTION

# @@protoc_insertion_point(module_scope)
