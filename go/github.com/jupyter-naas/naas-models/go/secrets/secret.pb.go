// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.32.0
// 	protoc        v3.19.5
// source: secret.proto

package secrets

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

type SecretError int32

const (
	SecretError_SECRET_NO_ERROR            SecretError = 0
	SecretError_SECRET_ALREADY_EXISTS      SecretError = 1
	SecretError_SECRET_NOT_FOUND           SecretError = 2
	SecretError_SECRET_MARKED_FOR_DELETION SecretError = 3
)

// Enum value maps for SecretError.
var (
	SecretError_name = map[int32]string{
		0: "SECRET_NO_ERROR",
		1: "SECRET_ALREADY_EXISTS",
		2: "SECRET_NOT_FOUND",
		3: "SECRET_MARKED_FOR_DELETION",
	}
	SecretError_value = map[string]int32{
		"SECRET_NO_ERROR":            0,
		"SECRET_ALREADY_EXISTS":      1,
		"SECRET_NOT_FOUND":           2,
		"SECRET_MARKED_FOR_DELETION": 3,
	}
)

func (x SecretError) Enum() *SecretError {
	p := new(SecretError)
	*p = x
	return p
}

func (x SecretError) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (SecretError) Descriptor() protoreflect.EnumDescriptor {
	return file_secret_proto_enumTypes[0].Descriptor()
}

func (SecretError) Type() protoreflect.EnumType {
	return &file_secret_proto_enumTypes[0]
}

func (x SecretError) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use SecretError.Descriptor instead.
func (SecretError) EnumDescriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{0}
}

type Secret struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name  *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
	Value *string `protobuf:"bytes,2,opt,name=value,proto3,oneof" json:"value,omitempty"` // Thinking of having strings only for simplicity. Kubernetes is doing that for pods env vars.
}

func (x *Secret) Reset() {
	*x = Secret{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Secret) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Secret) ProtoMessage() {}

func (x *Secret) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Secret.ProtoReflect.Descriptor instead.
func (*Secret) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{0}
}

func (x *Secret) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

func (x *Secret) GetValue() string {
	if x != nil && x.Value != nil {
		return *x.Value
	}
	return ""
}

type SecretResponseError struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error   *SecretError `protobuf:"varint,1,opt,name=error,proto3,enum=secrets.SecretError,oneof" json:"error,omitempty"`
	Message *string      `protobuf:"bytes,2,opt,name=message,proto3,oneof" json:"message,omitempty"`
}

func (x *SecretResponseError) Reset() {
	*x = SecretResponseError{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretResponseError) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretResponseError) ProtoMessage() {}

func (x *SecretResponseError) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretResponseError.ProtoReflect.Descriptor instead.
func (*SecretResponseError) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{1}
}

func (x *SecretResponseError) GetError() SecretError {
	if x != nil && x.Error != nil {
		return *x.Error
	}
	return SecretError_SECRET_NO_ERROR
}

func (x *SecretResponseError) GetMessage() string {
	if x != nil && x.Message != nil {
		return *x.Message
	}
	return ""
}

type SecretCreateRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Secret *Secret `protobuf:"bytes,1,opt,name=secret,proto3,oneof" json:"secret,omitempty"`
}

func (x *SecretCreateRequest) Reset() {
	*x = SecretCreateRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretCreateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretCreateRequest) ProtoMessage() {}

func (x *SecretCreateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretCreateRequest.ProtoReflect.Descriptor instead.
func (*SecretCreateRequest) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{2}
}

func (x *SecretCreateRequest) GetSecret() *Secret {
	if x != nil {
		return x.Secret
	}
	return nil
}

type SecretCreateResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *SecretResponseError `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *SecretCreateResponse) Reset() {
	*x = SecretCreateResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretCreateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretCreateResponse) ProtoMessage() {}

func (x *SecretCreateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretCreateResponse.ProtoReflect.Descriptor instead.
func (*SecretCreateResponse) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{3}
}

func (x *SecretCreateResponse) GetError() *SecretResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type SecretGetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *SecretGetRequest) Reset() {
	*x = SecretGetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretGetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretGetRequest) ProtoMessage() {}

func (x *SecretGetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretGetRequest.ProtoReflect.Descriptor instead.
func (*SecretGetRequest) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{4}
}

func (x *SecretGetRequest) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type SecretGetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Secret *Secret              `protobuf:"bytes,1,opt,name=secret,proto3,oneof" json:"secret,omitempty"`
	Error  *SecretResponseError `protobuf:"bytes,2,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *SecretGetResponse) Reset() {
	*x = SecretGetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretGetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretGetResponse) ProtoMessage() {}

func (x *SecretGetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretGetResponse.ProtoReflect.Descriptor instead.
func (*SecretGetResponse) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{5}
}

func (x *SecretGetResponse) GetSecret() *Secret {
	if x != nil {
		return x.Secret
	}
	return nil
}

func (x *SecretGetResponse) GetError() *SecretResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type SecretDeleteRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *SecretDeleteRequest) Reset() {
	*x = SecretDeleteRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretDeleteRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretDeleteRequest) ProtoMessage() {}

func (x *SecretDeleteRequest) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretDeleteRequest.ProtoReflect.Descriptor instead.
func (*SecretDeleteRequest) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{6}
}

func (x *SecretDeleteRequest) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type SecretDeleteResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *SecretResponseError `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *SecretDeleteResponse) Reset() {
	*x = SecretDeleteResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretDeleteResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretDeleteResponse) ProtoMessage() {}

func (x *SecretDeleteResponse) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretDeleteResponse.ProtoReflect.Descriptor instead.
func (*SecretDeleteResponse) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{7}
}

func (x *SecretDeleteResponse) GetError() *SecretResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type SecretListRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PageSize   *int32 `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3,oneof" json:"page_size,omitempty"`
	PageNumber *int32 `protobuf:"varint,2,opt,name=page_number,json=pageNumber,proto3,oneof" json:"page_number,omitempty"`
}

func (x *SecretListRequest) Reset() {
	*x = SecretListRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretListRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretListRequest) ProtoMessage() {}

func (x *SecretListRequest) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretListRequest.ProtoReflect.Descriptor instead.
func (*SecretListRequest) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{8}
}

func (x *SecretListRequest) GetPageSize() int32 {
	if x != nil && x.PageSize != nil {
		return *x.PageSize
	}
	return 0
}

func (x *SecretListRequest) GetPageNumber() int32 {
	if x != nil && x.PageNumber != nil {
		return *x.PageNumber
	}
	return 0
}

type SecretListResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Secrets []*Secret            `protobuf:"bytes,1,rep,name=secrets,proto3" json:"secrets,omitempty"`
	Error   *SecretResponseError `protobuf:"bytes,2,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *SecretListResponse) Reset() {
	*x = SecretListResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_secret_proto_msgTypes[9]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SecretListResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SecretListResponse) ProtoMessage() {}

func (x *SecretListResponse) ProtoReflect() protoreflect.Message {
	mi := &file_secret_proto_msgTypes[9]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SecretListResponse.ProtoReflect.Descriptor instead.
func (*SecretListResponse) Descriptor() ([]byte, []int) {
	return file_secret_proto_rawDescGZIP(), []int{9}
}

func (x *SecretListResponse) GetSecrets() []*Secret {
	if x != nil {
		return x.Secrets
	}
	return nil
}

func (x *SecretListResponse) GetError() *SecretResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

var File_secret_proto protoreflect.FileDescriptor

var file_secret_proto_rawDesc = []byte{
	0x0a, 0x0c, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x07,
	0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x1a, 0x0e, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x4f, 0x0a, 0x06, 0x53, 0x65, 0x63, 0x72, 0x65,
	0x74, 0x12, 0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48,
	0x00, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x19, 0x0a, 0x05, 0x76, 0x61,
	0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x05, 0x76, 0x61, 0x6c,
	0x75, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x42, 0x08,
	0x0a, 0x06, 0x5f, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x22, 0x7b, 0x0a, 0x13, 0x53, 0x65, 0x63, 0x72,
	0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12,
	0x2f, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x14,
	0x2e, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x45,
	0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01, 0x01,
	0x12, 0x1d, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x09, 0x48, 0x01, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x88, 0x01, 0x01, 0x42,
	0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x6d, 0x65,
	0x73, 0x73, 0x61, 0x67, 0x65, 0x22, 0x4e, 0x0a, 0x13, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x43,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x2c, 0x0a, 0x06,
	0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0f, 0x2e, 0x73,
	0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x48, 0x00, 0x52,
	0x06, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x88, 0x01, 0x01, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x73,
	0x65, 0x63, 0x72, 0x65, 0x74, 0x22, 0x59, 0x0a, 0x14, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x43,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x37, 0x0a,
	0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x73,
	0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72,
	0x72, 0x6f, 0x72, 0x88, 0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x22, 0x34, 0x0a, 0x10, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x48, 0x00, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a,
	0x05, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x8f, 0x01, 0x0a, 0x11, 0x53, 0x65, 0x63, 0x72, 0x65,
	0x74, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x2c, 0x0a, 0x06,
	0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0f, 0x2e, 0x73,
	0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x48, 0x00, 0x52,
	0x06, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x88, 0x01, 0x01, 0x12, 0x37, 0x0a, 0x05, 0x65, 0x72,
	0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x73, 0x65, 0x63, 0x72,
	0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x01, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x88, 0x01, 0x01, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x42, 0x08,
	0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x37, 0x0a, 0x13, 0x53, 0x65, 0x63, 0x72,
	0x65, 0x74, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d,
	0x65, 0x22, 0x59, 0x0a, 0x14, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x44, 0x65, 0x6c, 0x65, 0x74,
	0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x37, 0x0a, 0x05, 0x65, 0x72, 0x72,
	0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x73, 0x65, 0x63, 0x72, 0x65,
	0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88,
	0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x79, 0x0a, 0x11,
	0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x20, 0x0a, 0x09, 0x70, 0x61, 0x67, 0x65, 0x5f, 0x73, 0x69, 0x7a, 0x65, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x05, 0x48, 0x00, 0x52, 0x08, 0x70, 0x61, 0x67, 0x65, 0x53, 0x69, 0x7a, 0x65,
	0x88, 0x01, 0x01, 0x12, 0x24, 0x0a, 0x0b, 0x70, 0x61, 0x67, 0x65, 0x5f, 0x6e, 0x75, 0x6d, 0x62,
	0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x48, 0x01, 0x52, 0x0a, 0x70, 0x61, 0x67, 0x65,
	0x4e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x88, 0x01, 0x01, 0x42, 0x0c, 0x0a, 0x0a, 0x5f, 0x70, 0x61,
	0x67, 0x65, 0x5f, 0x73, 0x69, 0x7a, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x70, 0x61, 0x67, 0x65,
	0x5f, 0x6e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x22, 0x82, 0x01, 0x0a, 0x12, 0x53, 0x65, 0x63, 0x72,
	0x65, 0x74, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x29,
	0x0a, 0x07, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32,
	0x0f, 0x2e, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74,
	0x52, 0x07, 0x73, 0x65, 0x63, 0x72, 0x65, 0x74, 0x73, 0x12, 0x37, 0x0a, 0x05, 0x65, 0x72, 0x72,
	0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x73, 0x65, 0x63, 0x72, 0x65,
	0x74, 0x73, 0x2e, 0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88,
	0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x2a, 0x73, 0x0a, 0x0b,
	0x53, 0x65, 0x63, 0x72, 0x65, 0x74, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x13, 0x0a, 0x0f, 0x53,
	0x45, 0x43, 0x52, 0x45, 0x54, 0x5f, 0x4e, 0x4f, 0x5f, 0x45, 0x52, 0x52, 0x4f, 0x52, 0x10, 0x00,
	0x12, 0x19, 0x0a, 0x15, 0x53, 0x45, 0x43, 0x52, 0x45, 0x54, 0x5f, 0x41, 0x4c, 0x52, 0x45, 0x41,
	0x44, 0x59, 0x5f, 0x45, 0x58, 0x49, 0x53, 0x54, 0x53, 0x10, 0x01, 0x12, 0x14, 0x0a, 0x10, 0x53,
	0x45, 0x43, 0x52, 0x45, 0x54, 0x5f, 0x4e, 0x4f, 0x54, 0x5f, 0x46, 0x4f, 0x55, 0x4e, 0x44, 0x10,
	0x02, 0x12, 0x1e, 0x0a, 0x1a, 0x53, 0x45, 0x43, 0x52, 0x45, 0x54, 0x5f, 0x4d, 0x41, 0x52, 0x4b,
	0x45, 0x44, 0x5f, 0x46, 0x4f, 0x52, 0x5f, 0x44, 0x45, 0x4c, 0x45, 0x54, 0x49, 0x4f, 0x4e, 0x10,
	0x03, 0x42, 0x30, 0x5a, 0x2e, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x6a, 0x75, 0x70, 0x79, 0x74, 0x65, 0x72, 0x2d, 0x6e, 0x61, 0x61, 0x73, 0x2f, 0x6e, 0x61, 0x61,
	0x73, 0x2d, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x73, 0x2f, 0x67, 0x6f, 0x2f, 0x73, 0x65, 0x63, 0x72,
	0x65, 0x74, 0x73, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_secret_proto_rawDescOnce sync.Once
	file_secret_proto_rawDescData = file_secret_proto_rawDesc
)

func file_secret_proto_rawDescGZIP() []byte {
	file_secret_proto_rawDescOnce.Do(func() {
		file_secret_proto_rawDescData = protoimpl.X.CompressGZIP(file_secret_proto_rawDescData)
	})
	return file_secret_proto_rawDescData
}

var file_secret_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_secret_proto_msgTypes = make([]protoimpl.MessageInfo, 10)
var file_secret_proto_goTypes = []interface{}{
	(SecretError)(0),             // 0: secrets.SecretError
	(*Secret)(nil),               // 1: secrets.Secret
	(*SecretResponseError)(nil),  // 2: secrets.SecretResponseError
	(*SecretCreateRequest)(nil),  // 3: secrets.SecretCreateRequest
	(*SecretCreateResponse)(nil), // 4: secrets.SecretCreateResponse
	(*SecretGetRequest)(nil),     // 5: secrets.SecretGetRequest
	(*SecretGetResponse)(nil),    // 6: secrets.SecretGetResponse
	(*SecretDeleteRequest)(nil),  // 7: secrets.SecretDeleteRequest
	(*SecretDeleteResponse)(nil), // 8: secrets.SecretDeleteResponse
	(*SecretListRequest)(nil),    // 9: secrets.SecretListRequest
	(*SecretListResponse)(nil),   // 10: secrets.SecretListResponse
}
var file_secret_proto_depIdxs = []int32{
	0, // 0: secrets.SecretResponseError.error:type_name -> secrets.SecretError
	1, // 1: secrets.SecretCreateRequest.secret:type_name -> secrets.Secret
	2, // 2: secrets.SecretCreateResponse.error:type_name -> secrets.SecretResponseError
	1, // 3: secrets.SecretGetResponse.secret:type_name -> secrets.Secret
	2, // 4: secrets.SecretGetResponse.error:type_name -> secrets.SecretResponseError
	2, // 5: secrets.SecretDeleteResponse.error:type_name -> secrets.SecretResponseError
	1, // 6: secrets.SecretListResponse.secrets:type_name -> secrets.Secret
	2, // 7: secrets.SecretListResponse.error:type_name -> secrets.SecretResponseError
	8, // [8:8] is the sub-list for method output_type
	8, // [8:8] is the sub-list for method input_type
	8, // [8:8] is the sub-list for extension type_name
	8, // [8:8] is the sub-list for extension extendee
	0, // [0:8] is the sub-list for field type_name
}

func init() { file_secret_proto_init() }
func file_secret_proto_init() {
	if File_secret_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_secret_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Secret); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretResponseError); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretCreateRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretCreateResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretGetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretGetResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretDeleteRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretDeleteResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretListRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_secret_proto_msgTypes[9].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SecretListResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_secret_proto_msgTypes[0].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[1].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[2].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[3].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[4].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[5].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[6].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[7].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[8].OneofWrappers = []interface{}{}
	file_secret_proto_msgTypes[9].OneofWrappers = []interface{}{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_secret_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   10,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_secret_proto_goTypes,
		DependencyIndexes: file_secret_proto_depIdxs,
		EnumInfos:         file_secret_proto_enumTypes,
		MessageInfos:      file_secret_proto_msgTypes,
	}.Build()
	File_secret_proto = out.File
	file_secret_proto_rawDesc = nil
	file_secret_proto_goTypes = nil
	file_secret_proto_depIdxs = nil
}
