// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.32.0
// 	protoc        v3.19.5
// source: storage.proto

package storage

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

type StorageError int32

const (
	StorageError_STORAGE_NO_ERROR StorageError = 0
)

// Enum value maps for StorageError.
var (
	StorageError_name = map[int32]string{
		0: "STORAGE_NO_ERROR",
	}
	StorageError_value = map[string]int32{
		"STORAGE_NO_ERROR": 0,
	}
)

func (x StorageError) Enum() *StorageError {
	p := new(StorageError)
	*p = x
	return p
}

func (x StorageError) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (StorageError) Descriptor() protoreflect.EnumDescriptor {
	return file_storage_proto_enumTypes[0].Descriptor()
}

func (StorageError) Type() protoreflect.EnumType {
	return &file_storage_proto_enumTypes[0]
}

func (x StorageError) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use StorageError.Descriptor instead.
func (StorageError) EnumDescriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{0}
}

type ObjectError int32

const (
	ObjectError_OBJECT_NO_ERROR ObjectError = 0
)

// Enum value maps for ObjectError.
var (
	ObjectError_name = map[int32]string{
		0: "OBJECT_NO_ERROR",
	}
	ObjectError_value = map[string]int32{
		"OBJECT_NO_ERROR": 0,
	}
)

func (x ObjectError) Enum() *ObjectError {
	p := new(ObjectError)
	*p = x
	return p
}

func (x ObjectError) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (ObjectError) Descriptor() protoreflect.EnumDescriptor {
	return file_storage_proto_enumTypes[1].Descriptor()
}

func (ObjectError) Type() protoreflect.EnumType {
	return &file_storage_proto_enumTypes[1]
}

func (x ObjectError) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use ObjectError.Descriptor instead.
func (ObjectError) EnumDescriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{1}
}

type Storage struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	WorkspaceId *string `protobuf:"bytes,1,opt,name=workspace_id,json=workspaceId,proto3,oneof" json:"workspace_id,omitempty"`
	Name        *string `protobuf:"bytes,2,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *Storage) Reset() {
	*x = Storage{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Storage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Storage) ProtoMessage() {}

func (x *Storage) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Storage.ProtoReflect.Descriptor instead.
func (*Storage) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{0}
}

func (x *Storage) GetWorkspaceId() string {
	if x != nil && x.WorkspaceId != nil {
		return *x.WorkspaceId
	}
	return ""
}

func (x *Storage) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type Object struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *Object) Reset() {
	*x = Object{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Object) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Object) ProtoMessage() {}

func (x *Object) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Object.ProtoReflect.Descriptor instead.
func (*Object) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{1}
}

func (x *Object) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type StorageResponseError struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error   *StorageError `protobuf:"varint,1,opt,name=error,proto3,enum=storage.StorageError,oneof" json:"error,omitempty"`
	Message *string       `protobuf:"bytes,2,opt,name=message,proto3,oneof" json:"message,omitempty"`
}

func (x *StorageResponseError) Reset() {
	*x = StorageResponseError{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageResponseError) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageResponseError) ProtoMessage() {}

func (x *StorageResponseError) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageResponseError.ProtoReflect.Descriptor instead.
func (*StorageResponseError) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{2}
}

func (x *StorageResponseError) GetError() StorageError {
	if x != nil && x.Error != nil {
		return *x.Error
	}
	return StorageError_STORAGE_NO_ERROR
}

func (x *StorageResponseError) GetMessage() string {
	if x != nil && x.Message != nil {
		return *x.Message
	}
	return ""
}

type ObjectResponseError struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error   *ObjectError `protobuf:"varint,1,opt,name=error,proto3,enum=storage.ObjectError,oneof" json:"error,omitempty"`
	Message *string      `protobuf:"bytes,2,opt,name=message,proto3,oneof" json:"message,omitempty"`
}

func (x *ObjectResponseError) Reset() {
	*x = ObjectResponseError{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ObjectResponseError) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ObjectResponseError) ProtoMessage() {}

func (x *ObjectResponseError) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ObjectResponseError.ProtoReflect.Descriptor instead.
func (*ObjectResponseError) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{3}
}

func (x *ObjectResponseError) GetError() ObjectError {
	if x != nil && x.Error != nil {
		return *x.Error
	}
	return ObjectError_OBJECT_NO_ERROR
}

func (x *ObjectResponseError) GetMessage() string {
	if x != nil && x.Message != nil {
		return *x.Message
	}
	return ""
}

type StorageCreateRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Storage *Storage `protobuf:"bytes,1,opt,name=storage,proto3,oneof" json:"storage,omitempty"`
}

func (x *StorageCreateRequest) Reset() {
	*x = StorageCreateRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageCreateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageCreateRequest) ProtoMessage() {}

func (x *StorageCreateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageCreateRequest.ProtoReflect.Descriptor instead.
func (*StorageCreateRequest) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{4}
}

func (x *StorageCreateRequest) GetStorage() *Storage {
	if x != nil {
		return x.Storage
	}
	return nil
}

type StorageCreateResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *StorageResponseError `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *StorageCreateResponse) Reset() {
	*x = StorageCreateResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageCreateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageCreateResponse) ProtoMessage() {}

func (x *StorageCreateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageCreateResponse.ProtoReflect.Descriptor instead.
func (*StorageCreateResponse) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{5}
}

func (x *StorageCreateResponse) GetError() *StorageResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type StorageGetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *StorageGetRequest) Reset() {
	*x = StorageGetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageGetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageGetRequest) ProtoMessage() {}

func (x *StorageGetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageGetRequest.ProtoReflect.Descriptor instead.
func (*StorageGetRequest) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{6}
}

func (x *StorageGetRequest) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type StorageGetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Storage *Storage              `protobuf:"bytes,1,opt,name=storage,proto3,oneof" json:"storage,omitempty"`
	Error   *StorageResponseError `protobuf:"bytes,2,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *StorageGetResponse) Reset() {
	*x = StorageGetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageGetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageGetResponse) ProtoMessage() {}

func (x *StorageGetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageGetResponse.ProtoReflect.Descriptor instead.
func (*StorageGetResponse) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{7}
}

func (x *StorageGetResponse) GetStorage() *Storage {
	if x != nil {
		return x.Storage
	}
	return nil
}

func (x *StorageGetResponse) GetError() *StorageResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type StorageDeleteRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name *string `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
}

func (x *StorageDeleteRequest) Reset() {
	*x = StorageDeleteRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageDeleteRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageDeleteRequest) ProtoMessage() {}

func (x *StorageDeleteRequest) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageDeleteRequest.ProtoReflect.Descriptor instead.
func (*StorageDeleteRequest) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{8}
}

func (x *StorageDeleteRequest) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

type StorageDeleteResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *StorageResponseError `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *StorageDeleteResponse) Reset() {
	*x = StorageDeleteResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[9]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageDeleteResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageDeleteResponse) ProtoMessage() {}

func (x *StorageDeleteResponse) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[9]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageDeleteResponse.ProtoReflect.Descriptor instead.
func (*StorageDeleteResponse) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{9}
}

func (x *StorageDeleteResponse) GetError() *StorageResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type StorageListRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PageSize   *int32 `protobuf:"varint,1,opt,name=page_size,json=pageSize,proto3,oneof" json:"page_size,omitempty"`
	PageNumber *int32 `protobuf:"varint,2,opt,name=page_number,json=pageNumber,proto3,oneof" json:"page_number,omitempty"`
}

func (x *StorageListRequest) Reset() {
	*x = StorageListRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[10]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageListRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageListRequest) ProtoMessage() {}

func (x *StorageListRequest) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[10]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageListRequest.ProtoReflect.Descriptor instead.
func (*StorageListRequest) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{10}
}

func (x *StorageListRequest) GetPageSize() int32 {
	if x != nil && x.PageSize != nil {
		return *x.PageSize
	}
	return 0
}

func (x *StorageListRequest) GetPageNumber() int32 {
	if x != nil && x.PageNumber != nil {
		return *x.PageNumber
	}
	return 0
}

type StorageListResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Directories []*Storage            `protobuf:"bytes,1,rep,name=directories,proto3" json:"directories,omitempty"`
	Error       *StorageResponseError `protobuf:"bytes,2,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *StorageListResponse) Reset() {
	*x = StorageListResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[11]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StorageListResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StorageListResponse) ProtoMessage() {}

func (x *StorageListResponse) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[11]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StorageListResponse.ProtoReflect.Descriptor instead.
func (*StorageListResponse) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{11}
}

func (x *StorageListResponse) GetDirectories() []*Storage {
	if x != nil {
		return x.Directories
	}
	return nil
}

func (x *StorageListResponse) GetError() *StorageResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

type ObjectCreateRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Storage *Storage `protobuf:"bytes,1,opt,name=storage,proto3,oneof" json:"storage,omitempty"`
	Object  *Object  `protobuf:"bytes,2,opt,name=object,proto3,oneof" json:"object,omitempty"`
}

func (x *ObjectCreateRequest) Reset() {
	*x = ObjectCreateRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[12]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ObjectCreateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ObjectCreateRequest) ProtoMessage() {}

func (x *ObjectCreateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[12]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ObjectCreateRequest.ProtoReflect.Descriptor instead.
func (*ObjectCreateRequest) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{12}
}

func (x *ObjectCreateRequest) GetStorage() *Storage {
	if x != nil {
		return x.Storage
	}
	return nil
}

func (x *ObjectCreateRequest) GetObject() *Object {
	if x != nil {
		return x.Object
	}
	return nil
}

type ObjectCreateResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *StorageResponseError `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
}

func (x *ObjectCreateResponse) Reset() {
	*x = ObjectCreateResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_storage_proto_msgTypes[13]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ObjectCreateResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ObjectCreateResponse) ProtoMessage() {}

func (x *ObjectCreateResponse) ProtoReflect() protoreflect.Message {
	mi := &file_storage_proto_msgTypes[13]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ObjectCreateResponse.ProtoReflect.Descriptor instead.
func (*ObjectCreateResponse) Descriptor() ([]byte, []int) {
	return file_storage_proto_rawDescGZIP(), []int{13}
}

func (x *ObjectCreateResponse) GetError() *StorageResponseError {
	if x != nil {
		return x.Error
	}
	return nil
}

var File_storage_proto protoreflect.FileDescriptor

var file_storage_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x1a, 0x0e, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61,
	0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x64, 0x0a, 0x07, 0x53, 0x74, 0x6f, 0x72,
	0x61, 0x67, 0x65, 0x12, 0x26, 0x0a, 0x0c, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0b, 0x77, 0x6f, 0x72,
	0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x49, 0x64, 0x88, 0x01, 0x01, 0x12, 0x17, 0x0a, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x88, 0x01, 0x01, 0x42, 0x0f, 0x0a, 0x0d, 0x5f, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61,
	0x63, 0x65, 0x5f, 0x69, 0x64, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x2a,
	0x0a, 0x06, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01,
	0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x7d, 0x0a, 0x14, 0x53, 0x74,
	0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72,
	0x6f, 0x72, 0x12, 0x30, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0e, 0x32, 0x15, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72,
	0x61, 0x67, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f,
	0x72, 0x88, 0x01, 0x01, 0x12, 0x1d, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x88, 0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a,
	0x08, 0x5f, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x22, 0x7b, 0x0a, 0x13, 0x4f, 0x62, 0x6a,
	0x65, 0x63, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72,
	0x12, 0x2f, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0e, 0x32,
	0x14, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74,
	0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01,
	0x01, 0x12, 0x1d, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x48, 0x01, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x88, 0x01, 0x01,
	0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x6d,
	0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x22, 0x53, 0x0a, 0x14, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x2f,
	0x0a, 0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x10, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x48, 0x00, 0x52, 0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x88, 0x01, 0x01, 0x42,
	0x0a, 0x0a, 0x08, 0x5f, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x22, 0x5b, 0x0a, 0x15, 0x53,
	0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x38, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x74,
	0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72,
	0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01, 0x01, 0x42, 0x08,
	0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x35, 0x0a, 0x11, 0x53, 0x74, 0x6f, 0x72,
	0x61, 0x67, 0x65, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x17, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x22,
	0x95, 0x01, 0x0a, 0x12, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x47, 0x65, 0x74, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x2f, 0x0a, 0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x48, 0x00, 0x52, 0x07, 0x73, 0x74, 0x6f,
	0x72, 0x61, 0x67, 0x65, 0x88, 0x01, 0x01, 0x12, 0x38, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65,
	0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x01, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01,
	0x01, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x42, 0x08, 0x0a,
	0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x38, 0x0a, 0x14, 0x53, 0x74, 0x6f, 0x72, 0x61,
	0x67, 0x65, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e, 0x61, 0x6d,
	0x65, 0x22, 0x5b, 0x0a, 0x15, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x44, 0x65, 0x6c, 0x65,
	0x74, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x38, 0x0a, 0x05, 0x65, 0x72,
	0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x73, 0x74, 0x6f, 0x72,
	0x61, 0x67, 0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f,
	0x72, 0x88, 0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x7a,
	0x0a, 0x12, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x20, 0x0a, 0x09, 0x70, 0x61, 0x67, 0x65, 0x5f, 0x73, 0x69, 0x7a,
	0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x48, 0x00, 0x52, 0x08, 0x70, 0x61, 0x67, 0x65, 0x53,
	0x69, 0x7a, 0x65, 0x88, 0x01, 0x01, 0x12, 0x24, 0x0a, 0x0b, 0x70, 0x61, 0x67, 0x65, 0x5f, 0x6e,
	0x75, 0x6d, 0x62, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x48, 0x01, 0x52, 0x0a, 0x70,
	0x61, 0x67, 0x65, 0x4e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x88, 0x01, 0x01, 0x42, 0x0c, 0x0a, 0x0a,
	0x5f, 0x70, 0x61, 0x67, 0x65, 0x5f, 0x73, 0x69, 0x7a, 0x65, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x70,
	0x61, 0x67, 0x65, 0x5f, 0x6e, 0x75, 0x6d, 0x62, 0x65, 0x72, 0x22, 0x8d, 0x01, 0x0a, 0x13, 0x53,
	0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x12, 0x32, 0x0a, 0x0b, 0x64, 0x69, 0x72, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x69, 0x65,
	0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x0b, 0x64, 0x69, 0x72, 0x65, 0x63,
	0x74, 0x6f, 0x72, 0x69, 0x65, 0x73, 0x12, 0x38, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1d, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e,
	0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45,
	0x72, 0x72, 0x6f, 0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01, 0x01,
	0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x22, 0x8b, 0x01, 0x0a, 0x13, 0x4f,
	0x62, 0x6a, 0x65, 0x63, 0x74, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x2f, 0x0a, 0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x74,
	0x6f, 0x72, 0x61, 0x67, 0x65, 0x48, 0x00, 0x52, 0x07, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65,
	0x88, 0x01, 0x01, 0x12, 0x2c, 0x0a, 0x06, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x0f, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x4f, 0x62,
	0x6a, 0x65, 0x63, 0x74, 0x48, 0x01, 0x52, 0x06, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x88, 0x01,
	0x01, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x42, 0x09, 0x0a,
	0x07, 0x5f, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x22, 0x5a, 0x0a, 0x14, 0x4f, 0x62, 0x6a, 0x65,
	0x63, 0x74, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x12, 0x38, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1d, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x2e, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67,
	0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48, 0x00,
	0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65,
	0x72, 0x72, 0x6f, 0x72, 0x2a, 0x24, 0x0a, 0x0c, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65, 0x45,
	0x72, 0x72, 0x6f, 0x72, 0x12, 0x14, 0x0a, 0x10, 0x53, 0x54, 0x4f, 0x52, 0x41, 0x47, 0x45, 0x5f,
	0x4e, 0x4f, 0x5f, 0x45, 0x52, 0x52, 0x4f, 0x52, 0x10, 0x00, 0x2a, 0x22, 0x0a, 0x0b, 0x4f, 0x62,
	0x6a, 0x65, 0x63, 0x74, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x13, 0x0a, 0x0f, 0x4f, 0x42, 0x4a,
	0x45, 0x43, 0x54, 0x5f, 0x4e, 0x4f, 0x5f, 0x45, 0x52, 0x52, 0x4f, 0x52, 0x10, 0x00, 0x42, 0x30,
	0x5a, 0x2e, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6a, 0x75, 0x70,
	0x79, 0x74, 0x65, 0x72, 0x2d, 0x6e, 0x61, 0x61, 0x73, 0x2f, 0x6e, 0x61, 0x61, 0x73, 0x2d, 0x6d,
	0x6f, 0x64, 0x65, 0x6c, 0x73, 0x2f, 0x67, 0x6f, 0x2f, 0x73, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_storage_proto_rawDescOnce sync.Once
	file_storage_proto_rawDescData = file_storage_proto_rawDesc
)

func file_storage_proto_rawDescGZIP() []byte {
	file_storage_proto_rawDescOnce.Do(func() {
		file_storage_proto_rawDescData = protoimpl.X.CompressGZIP(file_storage_proto_rawDescData)
	})
	return file_storage_proto_rawDescData
}

var file_storage_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_storage_proto_msgTypes = make([]protoimpl.MessageInfo, 14)
var file_storage_proto_goTypes = []interface{}{
	(StorageError)(0),             // 0: storage.StorageError
	(ObjectError)(0),              // 1: storage.ObjectError
	(*Storage)(nil),               // 2: storage.Storage
	(*Object)(nil),                // 3: storage.Object
	(*StorageResponseError)(nil),  // 4: storage.StorageResponseError
	(*ObjectResponseError)(nil),   // 5: storage.ObjectResponseError
	(*StorageCreateRequest)(nil),  // 6: storage.StorageCreateRequest
	(*StorageCreateResponse)(nil), // 7: storage.StorageCreateResponse
	(*StorageGetRequest)(nil),     // 8: storage.StorageGetRequest
	(*StorageGetResponse)(nil),    // 9: storage.StorageGetResponse
	(*StorageDeleteRequest)(nil),  // 10: storage.StorageDeleteRequest
	(*StorageDeleteResponse)(nil), // 11: storage.StorageDeleteResponse
	(*StorageListRequest)(nil),    // 12: storage.StorageListRequest
	(*StorageListResponse)(nil),   // 13: storage.StorageListResponse
	(*ObjectCreateRequest)(nil),   // 14: storage.ObjectCreateRequest
	(*ObjectCreateResponse)(nil),  // 15: storage.ObjectCreateResponse
}
var file_storage_proto_depIdxs = []int32{
	0,  // 0: storage.StorageResponseError.error:type_name -> storage.StorageError
	1,  // 1: storage.ObjectResponseError.error:type_name -> storage.ObjectError
	2,  // 2: storage.StorageCreateRequest.storage:type_name -> storage.Storage
	4,  // 3: storage.StorageCreateResponse.error:type_name -> storage.StorageResponseError
	2,  // 4: storage.StorageGetResponse.storage:type_name -> storage.Storage
	4,  // 5: storage.StorageGetResponse.error:type_name -> storage.StorageResponseError
	4,  // 6: storage.StorageDeleteResponse.error:type_name -> storage.StorageResponseError
	2,  // 7: storage.StorageListResponse.directories:type_name -> storage.Storage
	4,  // 8: storage.StorageListResponse.error:type_name -> storage.StorageResponseError
	2,  // 9: storage.ObjectCreateRequest.storage:type_name -> storage.Storage
	3,  // 10: storage.ObjectCreateRequest.object:type_name -> storage.Object
	4,  // 11: storage.ObjectCreateResponse.error:type_name -> storage.StorageResponseError
	12, // [12:12] is the sub-list for method output_type
	12, // [12:12] is the sub-list for method input_type
	12, // [12:12] is the sub-list for extension type_name
	12, // [12:12] is the sub-list for extension extendee
	0,  // [0:12] is the sub-list for field type_name
}

func init() { file_storage_proto_init() }
func file_storage_proto_init() {
	if File_storage_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_storage_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Storage); i {
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
		file_storage_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Object); i {
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
		file_storage_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageResponseError); i {
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
		file_storage_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ObjectResponseError); i {
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
		file_storage_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageCreateRequest); i {
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
		file_storage_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageCreateResponse); i {
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
		file_storage_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageGetRequest); i {
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
		file_storage_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageGetResponse); i {
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
		file_storage_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageDeleteRequest); i {
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
		file_storage_proto_msgTypes[9].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageDeleteResponse); i {
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
		file_storage_proto_msgTypes[10].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageListRequest); i {
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
		file_storage_proto_msgTypes[11].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StorageListResponse); i {
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
		file_storage_proto_msgTypes[12].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ObjectCreateRequest); i {
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
		file_storage_proto_msgTypes[13].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ObjectCreateResponse); i {
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
	file_storage_proto_msgTypes[0].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[1].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[2].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[3].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[4].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[5].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[6].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[7].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[8].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[9].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[10].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[11].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[12].OneofWrappers = []interface{}{}
	file_storage_proto_msgTypes[13].OneofWrappers = []interface{}{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_storage_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   14,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_storage_proto_goTypes,
		DependencyIndexes: file_storage_proto_depIdxs,
		EnumInfos:         file_storage_proto_enumTypes,
		MessageInfos:      file_storage_proto_msgTypes,
	}.Build()
	File_storage_proto = out.File
	file_storage_proto_rawDesc = nil
	file_storage_proto_goTypes = nil
	file_storage_proto_depIdxs = nil
}
