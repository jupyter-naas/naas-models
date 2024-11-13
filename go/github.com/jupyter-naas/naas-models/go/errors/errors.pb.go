// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.1
// 	protoc        v5.26.1
// source: errors.proto

package errors

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Error int32

const (
	Error_NO_ERROR                                       Error = 0
	Error_INTERNAL_SERVER_ERROR                          Error = 199
	Error_IAM_USER_NOT_FOUND                             Error = 200
	Error_IAM_USER_NOT_AUTHORIZED                        Error = 201
	Error_WORKSPACE_NOT_FOUND                            Error = 300
	Error_WORKSPACE_USER_ALREADY_EXISTS                  Error = 302
	Error_WORKSPACE_USER_NOT_FOUND                       Error = 303
	Error_WORKSPACE_USER_ALREADY_ACTIVE                  Error = 304
	Error_WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE Error = 305
	Error_WORKSPACE_PLUGIN_NOT_FOUND                     Error = 306
	Error_WORKSPACE_INVITE_INVALID                       Error = 307
	Error_WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE  Error = 308
	Error_CREDITS_USER_HAS_NO_PARENT                     Error = 400
	Error_CREDITS_OUT_OF_CREDITS                         Error = 401
	// Ontology errors 500 - 599
	Error_ONTOLOGY_NOT_FOUND Error = 500
	// Chat errors - 600 - 699
	Error_CHAT_NOT_FOUND                         Error = 600
	Error_CHAT_NOT_AUTHORIZED                    Error = 601
	Error_CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXIST Error = 602
	Error_CHAT_CONTEXT_LENGTH_EXCEEDED           Error = 603
	Error_CHAT_MESSAGE_ALREADY_EXISTS            Error = 604
	Error_CHAT_MESSAGE_NOT_FOUND                 Error = 605
	Error_CHAT_INTERNAL_SERVER_ERROR             Error = 699
	// AIModel errors - 700 - 799
	Error_AIMODEL_NOT_FOUND Error = 700
)

// Enum value maps for Error.
var (
	Error_name = map[int32]string{
		0:   "NO_ERROR",
		199: "INTERNAL_SERVER_ERROR",
		200: "IAM_USER_NOT_FOUND",
		201: "IAM_USER_NOT_AUTHORIZED",
		300: "WORKSPACE_NOT_FOUND",
		302: "WORKSPACE_USER_ALREADY_EXISTS",
		303: "WORKSPACE_USER_NOT_FOUND",
		304: "WORKSPACE_USER_ALREADY_ACTIVE",
		305: "WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE",
		306: "WORKSPACE_PLUGIN_NOT_FOUND",
		307: "WORKSPACE_INVITE_INVALID",
		308: "WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE",
		400: "CREDITS_USER_HAS_NO_PARENT",
		401: "CREDITS_OUT_OF_CREDITS",
		500: "ONTOLOGY_NOT_FOUND",
		600: "CHAT_NOT_FOUND",
		601: "CHAT_NOT_AUTHORIZED",
		602: "CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXIST",
		603: "CHAT_CONTEXT_LENGTH_EXCEEDED",
		604: "CHAT_MESSAGE_ALREADY_EXISTS",
		605: "CHAT_MESSAGE_NOT_FOUND",
		699: "CHAT_INTERNAL_SERVER_ERROR",
		700: "AIMODEL_NOT_FOUND",
	}
	Error_value = map[string]int32{
		"NO_ERROR":                                       0,
		"INTERNAL_SERVER_ERROR":                          199,
		"IAM_USER_NOT_FOUND":                             200,
		"IAM_USER_NOT_AUTHORIZED":                        201,
		"WORKSPACE_NOT_FOUND":                            300,
		"WORKSPACE_USER_ALREADY_EXISTS":                  302,
		"WORKSPACE_USER_NOT_FOUND":                       303,
		"WORKSPACE_USER_ALREADY_ACTIVE":                  304,
		"WORKSPACE_USER_ALREADY_HAVE_PERSONAL_WORKSPACE": 305,
		"WORKSPACE_PLUGIN_NOT_FOUND":                     306,
		"WORKSPACE_INVITE_INVALID":                       307,
		"WORKSPACE_CANNOT_INVITE_TO_PERSONAL_WORKSPACE":  308,
		"CREDITS_USER_HAS_NO_PARENT":                     400,
		"CREDITS_OUT_OF_CREDITS":                         401,
		"ONTOLOGY_NOT_FOUND":                             500,
		"CHAT_NOT_FOUND":                                 600,
		"CHAT_NOT_AUTHORIZED":                            601,
		"CHAT_COMPLETION_ADAPTOR_DOES_NOT_EXIST":         602,
		"CHAT_CONTEXT_LENGTH_EXCEEDED":                   603,
		"CHAT_MESSAGE_ALREADY_EXISTS":                    604,
		"CHAT_MESSAGE_NOT_FOUND":                         605,
		"CHAT_INTERNAL_SERVER_ERROR":                     699,
		"AIMODEL_NOT_FOUND":                              700,
	}
)

func (x Error) Enum() *Error {
	p := new(Error)
	*p = x
	return p
}

func (x Error) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Error) Descriptor() protoreflect.EnumDescriptor {
	return file_errors_proto_enumTypes[0].Descriptor()
}

func (Error) Type() protoreflect.EnumType {
	return &file_errors_proto_enumTypes[0]
}

func (x Error) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Error.Descriptor instead.
func (Error) EnumDescriptor() ([]byte, []int) {
	return file_errors_proto_rawDescGZIP(), []int{0}
}

type ErrorResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Code    *Error  `protobuf:"varint,1,opt,name=code,proto3,enum=errors.Error,oneof" json:"code,omitempty"`
	Message *string `protobuf:"bytes,2,opt,name=message,proto3,oneof" json:"message,omitempty"`
}

func (x *ErrorResponse) Reset() {
	*x = ErrorResponse{}
	mi := &file_errors_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ErrorResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ErrorResponse) ProtoMessage() {}

func (x *ErrorResponse) ProtoReflect() protoreflect.Message {
	mi := &file_errors_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ErrorResponse.ProtoReflect.Descriptor instead.
func (*ErrorResponse) Descriptor() ([]byte, []int) {
	return file_errors_proto_rawDescGZIP(), []int{0}
}

func (x *ErrorResponse) GetCode() Error {
	if x != nil && x.Code != nil {
		return *x.Code
	}
	return Error_NO_ERROR
}

func (x *ErrorResponse) GetMessage() string {
	if x != nil && x.Message != nil {
		return *x.Message
	}
	return ""
}

var File_errors_proto protoreflect.FileDescriptor

var file_errors_proto_rawDesc = []byte{
	0x0a, 0x0c, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x06,
	0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x1a, 0x0e, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x6b, 0x0a, 0x0d, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x26, 0x0a, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0d, 0x2e, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x2e, 0x45,
	0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x88, 0x01, 0x01, 0x12,
	0x1d, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x48, 0x01, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07,
	0x0a, 0x05, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x6d, 0x65, 0x73, 0x73,
	0x61, 0x67, 0x65, 0x2a, 0xe0, 0x05, 0x0a, 0x05, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x0c, 0x0a,
	0x08, 0x4e, 0x4f, 0x5f, 0x45, 0x52, 0x52, 0x4f, 0x52, 0x10, 0x00, 0x12, 0x1a, 0x0a, 0x15, 0x49,
	0x4e, 0x54, 0x45, 0x52, 0x4e, 0x41, 0x4c, 0x5f, 0x53, 0x45, 0x52, 0x56, 0x45, 0x52, 0x5f, 0x45,
	0x52, 0x52, 0x4f, 0x52, 0x10, 0xc7, 0x01, 0x12, 0x17, 0x0a, 0x12, 0x49, 0x41, 0x4d, 0x5f, 0x55,
	0x53, 0x45, 0x52, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10, 0xc8, 0x01,
	0x12, 0x1c, 0x0a, 0x17, 0x49, 0x41, 0x4d, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x4e, 0x4f, 0x54,
	0x5f, 0x41, 0x55, 0x54, 0x48, 0x4f, 0x52, 0x49, 0x5a, 0x45, 0x44, 0x10, 0xc9, 0x01, 0x12, 0x18,
	0x0a, 0x13, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43, 0x45, 0x5f, 0x4e, 0x4f, 0x54, 0x5f,
	0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10, 0xac, 0x02, 0x12, 0x22, 0x0a, 0x1d, 0x57, 0x4f, 0x52, 0x4b,
	0x53, 0x50, 0x41, 0x43, 0x45, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x41, 0x4c, 0x52, 0x45, 0x41,
	0x44, 0x59, 0x5f, 0x45, 0x58, 0x49, 0x53, 0x54, 0x53, 0x10, 0xae, 0x02, 0x12, 0x1d, 0x0a, 0x18,
	0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43, 0x45, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x4e,
	0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10, 0xaf, 0x02, 0x12, 0x22, 0x0a, 0x1d, 0x57,
	0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43, 0x45, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x41, 0x4c,
	0x52, 0x45, 0x41, 0x44, 0x59, 0x5f, 0x41, 0x43, 0x54, 0x49, 0x56, 0x45, 0x10, 0xb0, 0x02, 0x12,
	0x33, 0x0a, 0x2e, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43, 0x45, 0x5f, 0x55, 0x53, 0x45,
	0x52, 0x5f, 0x41, 0x4c, 0x52, 0x45, 0x41, 0x44, 0x59, 0x5f, 0x48, 0x41, 0x56, 0x45, 0x5f, 0x50,
	0x45, 0x52, 0x53, 0x4f, 0x4e, 0x41, 0x4c, 0x5f, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43,
	0x45, 0x10, 0xb1, 0x02, 0x12, 0x1f, 0x0a, 0x1a, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43,
	0x45, 0x5f, 0x50, 0x4c, 0x55, 0x47, 0x49, 0x4e, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55,
	0x4e, 0x44, 0x10, 0xb2, 0x02, 0x12, 0x1d, 0x0a, 0x18, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41,
	0x43, 0x45, 0x5f, 0x49, 0x4e, 0x56, 0x49, 0x54, 0x45, 0x5f, 0x49, 0x4e, 0x56, 0x41, 0x4c, 0x49,
	0x44, 0x10, 0xb3, 0x02, 0x12, 0x32, 0x0a, 0x2d, 0x57, 0x4f, 0x52, 0x4b, 0x53, 0x50, 0x41, 0x43,
	0x45, 0x5f, 0x43, 0x41, 0x4e, 0x4e, 0x4f, 0x54, 0x5f, 0x49, 0x4e, 0x56, 0x49, 0x54, 0x45, 0x5f,
	0x54, 0x4f, 0x5f, 0x50, 0x45, 0x52, 0x53, 0x4f, 0x4e, 0x41, 0x4c, 0x5f, 0x57, 0x4f, 0x52, 0x4b,
	0x53, 0x50, 0x41, 0x43, 0x45, 0x10, 0xb4, 0x02, 0x12, 0x1f, 0x0a, 0x1a, 0x43, 0x52, 0x45, 0x44,
	0x49, 0x54, 0x53, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x48, 0x41, 0x53, 0x5f, 0x4e, 0x4f, 0x5f,
	0x50, 0x41, 0x52, 0x45, 0x4e, 0x54, 0x10, 0x90, 0x03, 0x12, 0x1b, 0x0a, 0x16, 0x43, 0x52, 0x45,
	0x44, 0x49, 0x54, 0x53, 0x5f, 0x4f, 0x55, 0x54, 0x5f, 0x4f, 0x46, 0x5f, 0x43, 0x52, 0x45, 0x44,
	0x49, 0x54, 0x53, 0x10, 0x91, 0x03, 0x12, 0x17, 0x0a, 0x12, 0x4f, 0x4e, 0x54, 0x4f, 0x4c, 0x4f,
	0x47, 0x59, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10, 0xf4, 0x03, 0x12,
	0x13, 0x0a, 0x0e, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e,
	0x44, 0x10, 0xd8, 0x04, 0x12, 0x18, 0x0a, 0x13, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x4e, 0x4f, 0x54,
	0x5f, 0x41, 0x55, 0x54, 0x48, 0x4f, 0x52, 0x49, 0x5a, 0x45, 0x44, 0x10, 0xd9, 0x04, 0x12, 0x2b,
	0x0a, 0x26, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x43, 0x4f, 0x4d, 0x50, 0x4c, 0x45, 0x54, 0x49, 0x4f,
	0x4e, 0x5f, 0x41, 0x44, 0x41, 0x50, 0x54, 0x4f, 0x52, 0x5f, 0x44, 0x4f, 0x45, 0x53, 0x5f, 0x4e,
	0x4f, 0x54, 0x5f, 0x45, 0x58, 0x49, 0x53, 0x54, 0x10, 0xda, 0x04, 0x12, 0x21, 0x0a, 0x1c, 0x43,
	0x48, 0x41, 0x54, 0x5f, 0x43, 0x4f, 0x4e, 0x54, 0x45, 0x58, 0x54, 0x5f, 0x4c, 0x45, 0x4e, 0x47,
	0x54, 0x48, 0x5f, 0x45, 0x58, 0x43, 0x45, 0x45, 0x44, 0x45, 0x44, 0x10, 0xdb, 0x04, 0x12, 0x20,
	0x0a, 0x1b, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x4d, 0x45, 0x53, 0x53, 0x41, 0x47, 0x45, 0x5f, 0x41,
	0x4c, 0x52, 0x45, 0x41, 0x44, 0x59, 0x5f, 0x45, 0x58, 0x49, 0x53, 0x54, 0x53, 0x10, 0xdc, 0x04,
	0x12, 0x1b, 0x0a, 0x16, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x4d, 0x45, 0x53, 0x53, 0x41, 0x47, 0x45,
	0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10, 0xdd, 0x04, 0x12, 0x1f, 0x0a,
	0x1a, 0x43, 0x48, 0x41, 0x54, 0x5f, 0x49, 0x4e, 0x54, 0x45, 0x52, 0x4e, 0x41, 0x4c, 0x5f, 0x53,
	0x45, 0x52, 0x56, 0x45, 0x52, 0x5f, 0x45, 0x52, 0x52, 0x4f, 0x52, 0x10, 0xbb, 0x05, 0x12, 0x16,
	0x0a, 0x11, 0x41, 0x49, 0x4d, 0x4f, 0x44, 0x45, 0x4c, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f,
	0x55, 0x4e, 0x44, 0x10, 0xbc, 0x05, 0x42, 0x2f, 0x5a, 0x2d, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6a, 0x75, 0x70, 0x79, 0x74, 0x65, 0x72, 0x2d, 0x6e, 0x61, 0x61,
	0x73, 0x2f, 0x6e, 0x61, 0x61, 0x73, 0x2d, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x73, 0x2f, 0x67, 0x6f,
	0x2f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_errors_proto_rawDescOnce sync.Once
	file_errors_proto_rawDescData = file_errors_proto_rawDesc
)

func file_errors_proto_rawDescGZIP() []byte {
	file_errors_proto_rawDescOnce.Do(func() {
		file_errors_proto_rawDescData = protoimpl.X.CompressGZIP(file_errors_proto_rawDescData)
	})
	return file_errors_proto_rawDescData
}

var file_errors_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_errors_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_errors_proto_goTypes = []any{
	(Error)(0),            // 0: errors.Error
	(*ErrorResponse)(nil), // 1: errors.ErrorResponse
}
var file_errors_proto_depIdxs = []int32{
	0, // 0: errors.ErrorResponse.code:type_name -> errors.Error
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_errors_proto_init() }
func file_errors_proto_init() {
	if File_errors_proto != nil {
		return
	}
	file_errors_proto_msgTypes[0].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_errors_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_errors_proto_goTypes,
		DependencyIndexes: file_errors_proto_depIdxs,
		EnumInfos:         file_errors_proto_enumTypes,
		MessageInfos:      file_errors_proto_msgTypes,
	}.Build()
	File_errors_proto = out.File
	file_errors_proto_rawDesc = nil
	file_errors_proto_goTypes = nil
	file_errors_proto_depIdxs = nil
}
