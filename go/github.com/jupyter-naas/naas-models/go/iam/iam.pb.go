// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.35.1
// 	protoc        v5.26.1
// source: iam.proto

package iam

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	errors "github.com/jupyter-naas/naas-models/go/errors"
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

type TokenData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	UserId *string  `protobuf:"bytes,1,opt,name=user_id,json=userId,proto3,oneof" json:"user_id,omitempty"`
	Scopes []string `protobuf:"bytes,2,rep,name=scopes,proto3" json:"scopes,omitempty"`
}

func (x *TokenData) Reset() {
	*x = TokenData{}
	mi := &file_iam_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *TokenData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TokenData) ProtoMessage() {}

func (x *TokenData) ProtoReflect() protoreflect.Message {
	mi := &file_iam_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TokenData.ProtoReflect.Descriptor instead.
func (*TokenData) Descriptor() ([]byte, []int) {
	return file_iam_proto_rawDescGZIP(), []int{0}
}

func (x *TokenData) GetUserId() string {
	if x != nil && x.UserId != nil {
		return *x.UserId
	}
	return ""
}

func (x *TokenData) GetScopes() []string {
	if x != nil {
		return x.Scopes
	}
	return nil
}

type Profile struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	UserId            *string `protobuf:"bytes,1,opt,name=user_id,json=userId,proto3,oneof" json:"user_id,omitempty"`
	FirstName         *string `protobuf:"bytes,2,opt,name=first_name,json=firstName,proto3,oneof" json:"first_name,omitempty"`
	LastName          *string `protobuf:"bytes,3,opt,name=last_name,json=lastName,proto3,oneof" json:"last_name,omitempty"`
	Company           *string `protobuf:"bytes,4,opt,name=company,proto3,oneof" json:"company,omitempty"`
	Role              *string `protobuf:"bytes,5,opt,name=role,proto3,oneof" json:"role,omitempty"`
	Timezone          *string `protobuf:"bytes,6,opt,name=timezone,proto3,oneof" json:"timezone,omitempty"`
	ProfilePictureUrl *string `protobuf:"bytes,7,opt,name=profile_picture_url,json=profilePictureUrl,proto3,oneof" json:"profile_picture_url,omitempty"`
	UserPresentation  *string `protobuf:"bytes,8,opt,name=user_presentation,json=userPresentation,proto3,oneof" json:"user_presentation,omitempty"`
	TargetedUse       *string `protobuf:"bytes,9,opt,name=targeted_use,json=targetedUse,proto3,oneof" json:"targeted_use,omitempty"`
	ProductUpdates    *bool   `protobuf:"varint,10,opt,name=product_updates,json=productUpdates,proto3,oneof" json:"product_updates,omitempty"`
	Phone             *string `protobuf:"bytes,11,opt,name=phone,proto3,oneof" json:"phone,omitempty"`
}

func (x *Profile) Reset() {
	*x = Profile{}
	mi := &file_iam_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Profile) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Profile) ProtoMessage() {}

func (x *Profile) ProtoReflect() protoreflect.Message {
	mi := &file_iam_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Profile.ProtoReflect.Descriptor instead.
func (*Profile) Descriptor() ([]byte, []int) {
	return file_iam_proto_rawDescGZIP(), []int{1}
}

func (x *Profile) GetUserId() string {
	if x != nil && x.UserId != nil {
		return *x.UserId
	}
	return ""
}

func (x *Profile) GetFirstName() string {
	if x != nil && x.FirstName != nil {
		return *x.FirstName
	}
	return ""
}

func (x *Profile) GetLastName() string {
	if x != nil && x.LastName != nil {
		return *x.LastName
	}
	return ""
}

func (x *Profile) GetCompany() string {
	if x != nil && x.Company != nil {
		return *x.Company
	}
	return ""
}

func (x *Profile) GetRole() string {
	if x != nil && x.Role != nil {
		return *x.Role
	}
	return ""
}

func (x *Profile) GetTimezone() string {
	if x != nil && x.Timezone != nil {
		return *x.Timezone
	}
	return ""
}

func (x *Profile) GetProfilePictureUrl() string {
	if x != nil && x.ProfilePictureUrl != nil {
		return *x.ProfilePictureUrl
	}
	return ""
}

func (x *Profile) GetUserPresentation() string {
	if x != nil && x.UserPresentation != nil {
		return *x.UserPresentation
	}
	return ""
}

func (x *Profile) GetTargetedUse() string {
	if x != nil && x.TargetedUse != nil {
		return *x.TargetedUse
	}
	return ""
}

func (x *Profile) GetProductUpdates() bool {
	if x != nil && x.ProductUpdates != nil {
		return *x.ProductUpdates
	}
	return false
}

func (x *Profile) GetPhone() string {
	if x != nil && x.Phone != nil {
		return *x.Phone
	}
	return ""
}

type ImpersonateUserRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to User:
	//
	//	*ImpersonateUserRequest_UserId
	//	*ImpersonateUserRequest_Email
	User isImpersonateUserRequest_User `protobuf_oneof:"user"`
}

func (x *ImpersonateUserRequest) Reset() {
	*x = ImpersonateUserRequest{}
	mi := &file_iam_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ImpersonateUserRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ImpersonateUserRequest) ProtoMessage() {}

func (x *ImpersonateUserRequest) ProtoReflect() protoreflect.Message {
	mi := &file_iam_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ImpersonateUserRequest.ProtoReflect.Descriptor instead.
func (*ImpersonateUserRequest) Descriptor() ([]byte, []int) {
	return file_iam_proto_rawDescGZIP(), []int{2}
}

func (m *ImpersonateUserRequest) GetUser() isImpersonateUserRequest_User {
	if m != nil {
		return m.User
	}
	return nil
}

func (x *ImpersonateUserRequest) GetUserId() string {
	if x, ok := x.GetUser().(*ImpersonateUserRequest_UserId); ok {
		return x.UserId
	}
	return ""
}

func (x *ImpersonateUserRequest) GetEmail() string {
	if x, ok := x.GetUser().(*ImpersonateUserRequest_Email); ok {
		return x.Email
	}
	return ""
}

type isImpersonateUserRequest_User interface {
	isImpersonateUserRequest_User()
}

type ImpersonateUserRequest_UserId struct {
	UserId string `protobuf:"bytes,1,opt,name=user_id,json=userId,proto3,oneof"`
}

type ImpersonateUserRequest_Email struct {
	Email string `protobuf:"bytes,2,opt,name=email,proto3,oneof"`
}

func (*ImpersonateUserRequest_UserId) isImpersonateUserRequest_User() {}

func (*ImpersonateUserRequest_Email) isImpersonateUserRequest_User() {}

type ImpersonateUserResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Error *errors.ErrorResponse `protobuf:"bytes,1,opt,name=error,proto3,oneof" json:"error,omitempty"`
	Token *string               `protobuf:"bytes,2,opt,name=token,proto3,oneof" json:"token,omitempty"`
}

func (x *ImpersonateUserResponse) Reset() {
	*x = ImpersonateUserResponse{}
	mi := &file_iam_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ImpersonateUserResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ImpersonateUserResponse) ProtoMessage() {}

func (x *ImpersonateUserResponse) ProtoReflect() protoreflect.Message {
	mi := &file_iam_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ImpersonateUserResponse.ProtoReflect.Descriptor instead.
func (*ImpersonateUserResponse) Descriptor() ([]byte, []int) {
	return file_iam_proto_rawDescGZIP(), []int{3}
}

func (x *ImpersonateUserResponse) GetError() *errors.ErrorResponse {
	if x != nil {
		return x.Error
	}
	return nil
}

func (x *ImpersonateUserResponse) GetToken() string {
	if x != nil && x.Token != nil {
		return *x.Token
	}
	return ""
}

var File_iam_proto protoreflect.FileDescriptor

var file_iam_proto_rawDesc = []byte{
	0x0a, 0x09, 0x69, 0x61, 0x6d, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x03, 0x69, 0x61, 0x6d,
	0x1a, 0x0e, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x0c, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x4d,
	0x0a, 0x09, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x44, 0x61, 0x74, 0x61, 0x12, 0x1c, 0x0a, 0x07, 0x75,
	0x73, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x06,
	0x75, 0x73, 0x65, 0x72, 0x49, 0x64, 0x88, 0x01, 0x01, 0x12, 0x16, 0x0a, 0x06, 0x73, 0x63, 0x6f,
	0x70, 0x65, 0x73, 0x18, 0x02, 0x20, 0x03, 0x28, 0x09, 0x52, 0x06, 0x73, 0x63, 0x6f, 0x70, 0x65,
	0x73, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x75, 0x73, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x22, 0xc6, 0x04,
	0x0a, 0x07, 0x50, 0x72, 0x6f, 0x66, 0x69, 0x6c, 0x65, 0x12, 0x1c, 0x0a, 0x07, 0x75, 0x73, 0x65,
	0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x06, 0x75, 0x73,
	0x65, 0x72, 0x49, 0x64, 0x88, 0x01, 0x01, 0x12, 0x22, 0x0a, 0x0a, 0x66, 0x69, 0x72, 0x73, 0x74,
	0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x09, 0x66,
	0x69, 0x72, 0x73, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x20, 0x0a, 0x09, 0x6c,
	0x61, 0x73, 0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x02,
	0x52, 0x08, 0x6c, 0x61, 0x73, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1d, 0x0a,
	0x07, 0x63, 0x6f, 0x6d, 0x70, 0x61, 0x6e, 0x79, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x48, 0x03,
	0x52, 0x07, 0x63, 0x6f, 0x6d, 0x70, 0x61, 0x6e, 0x79, 0x88, 0x01, 0x01, 0x12, 0x17, 0x0a, 0x04,
	0x72, 0x6f, 0x6c, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x48, 0x04, 0x52, 0x04, 0x72, 0x6f,
	0x6c, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1f, 0x0a, 0x08, 0x74, 0x69, 0x6d, 0x65, 0x7a, 0x6f, 0x6e,
	0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x48, 0x05, 0x52, 0x08, 0x74, 0x69, 0x6d, 0x65, 0x7a,
	0x6f, 0x6e, 0x65, 0x88, 0x01, 0x01, 0x12, 0x33, 0x0a, 0x13, 0x70, 0x72, 0x6f, 0x66, 0x69, 0x6c,
	0x65, 0x5f, 0x70, 0x69, 0x63, 0x74, 0x75, 0x72, 0x65, 0x5f, 0x75, 0x72, 0x6c, 0x18, 0x07, 0x20,
	0x01, 0x28, 0x09, 0x48, 0x06, 0x52, 0x11, 0x70, 0x72, 0x6f, 0x66, 0x69, 0x6c, 0x65, 0x50, 0x69,
	0x63, 0x74, 0x75, 0x72, 0x65, 0x55, 0x72, 0x6c, 0x88, 0x01, 0x01, 0x12, 0x30, 0x0a, 0x11, 0x75,
	0x73, 0x65, 0x72, 0x5f, 0x70, 0x72, 0x65, 0x73, 0x65, 0x6e, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x48, 0x07, 0x52, 0x10, 0x75, 0x73, 0x65, 0x72, 0x50, 0x72,
	0x65, 0x73, 0x65, 0x6e, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x88, 0x01, 0x01, 0x12, 0x26, 0x0a,
	0x0c, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x65, 0x64, 0x5f, 0x75, 0x73, 0x65, 0x18, 0x09, 0x20,
	0x01, 0x28, 0x09, 0x48, 0x08, 0x52, 0x0b, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x65, 0x64, 0x55,
	0x73, 0x65, 0x88, 0x01, 0x01, 0x12, 0x2c, 0x0a, 0x0f, 0x70, 0x72, 0x6f, 0x64, 0x75, 0x63, 0x74,
	0x5f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x73, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x08, 0x48, 0x09,
	0x52, 0x0e, 0x70, 0x72, 0x6f, 0x64, 0x75, 0x63, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x73,
	0x88, 0x01, 0x01, 0x12, 0x19, 0x0a, 0x05, 0x70, 0x68, 0x6f, 0x6e, 0x65, 0x18, 0x0b, 0x20, 0x01,
	0x28, 0x09, 0x48, 0x0a, 0x52, 0x05, 0x70, 0x68, 0x6f, 0x6e, 0x65, 0x88, 0x01, 0x01, 0x42, 0x0a,
	0x0a, 0x08, 0x5f, 0x75, 0x73, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x66,
	0x69, 0x72, 0x73, 0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x42, 0x0c, 0x0a, 0x0a, 0x5f, 0x6c, 0x61,
	0x73, 0x74, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x63, 0x6f, 0x6d, 0x70,
	0x61, 0x6e, 0x79, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x72, 0x6f, 0x6c, 0x65, 0x42, 0x0b, 0x0a, 0x09,
	0x5f, 0x74, 0x69, 0x6d, 0x65, 0x7a, 0x6f, 0x6e, 0x65, 0x42, 0x16, 0x0a, 0x14, 0x5f, 0x70, 0x72,
	0x6f, 0x66, 0x69, 0x6c, 0x65, 0x5f, 0x70, 0x69, 0x63, 0x74, 0x75, 0x72, 0x65, 0x5f, 0x75, 0x72,
	0x6c, 0x42, 0x14, 0x0a, 0x12, 0x5f, 0x75, 0x73, 0x65, 0x72, 0x5f, 0x70, 0x72, 0x65, 0x73, 0x65,
	0x6e, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x42, 0x0f, 0x0a, 0x0d, 0x5f, 0x74, 0x61, 0x72, 0x67,
	0x65, 0x74, 0x65, 0x64, 0x5f, 0x75, 0x73, 0x65, 0x42, 0x12, 0x0a, 0x10, 0x5f, 0x70, 0x72, 0x6f,
	0x64, 0x75, 0x63, 0x74, 0x5f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x73, 0x42, 0x08, 0x0a, 0x06,
	0x5f, 0x70, 0x68, 0x6f, 0x6e, 0x65, 0x22, 0x66, 0x0a, 0x16, 0x49, 0x6d, 0x70, 0x65, 0x72, 0x73,
	0x6f, 0x6e, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x12, 0x23, 0x0a, 0x07, 0x75, 0x73, 0x65, 0x72, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x42, 0x08, 0xfa, 0x42, 0x05, 0x72, 0x03, 0xb0, 0x01, 0x01, 0x48, 0x00, 0x52, 0x06, 0x75,
	0x73, 0x65, 0x72, 0x49, 0x64, 0x12, 0x1f, 0x0a, 0x05, 0x65, 0x6d, 0x61, 0x69, 0x6c, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x09, 0x42, 0x07, 0xfa, 0x42, 0x04, 0x72, 0x02, 0x60, 0x01, 0x48, 0x00, 0x52,
	0x05, 0x65, 0x6d, 0x61, 0x69, 0x6c, 0x42, 0x06, 0x0a, 0x04, 0x75, 0x73, 0x65, 0x72, 0x22, 0x7a,
	0x0a, 0x17, 0x49, 0x6d, 0x70, 0x65, 0x72, 0x73, 0x6f, 0x6e, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65,
	0x72, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x30, 0x0a, 0x05, 0x65, 0x72, 0x72,
	0x6f, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x73, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x48,
	0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x88, 0x01, 0x01, 0x12, 0x19, 0x0a, 0x05, 0x74,
	0x6f, 0x6b, 0x65, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x05, 0x74, 0x6f,
	0x6b, 0x65, 0x6e, 0x88, 0x01, 0x01, 0x42, 0x08, 0x0a, 0x06, 0x5f, 0x65, 0x72, 0x72, 0x6f, 0x72,
	0x42, 0x08, 0x0a, 0x06, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x42, 0x2c, 0x5a, 0x2a, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6a, 0x75, 0x70, 0x79, 0x74, 0x65, 0x72,
	0x2d, 0x6e, 0x61, 0x61, 0x73, 0x2f, 0x6e, 0x61, 0x61, 0x73, 0x2d, 0x6d, 0x6f, 0x64, 0x65, 0x6c,
	0x73, 0x2f, 0x67, 0x6f, 0x2f, 0x69, 0x61, 0x6d, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_iam_proto_rawDescOnce sync.Once
	file_iam_proto_rawDescData = file_iam_proto_rawDesc
)

func file_iam_proto_rawDescGZIP() []byte {
	file_iam_proto_rawDescOnce.Do(func() {
		file_iam_proto_rawDescData = protoimpl.X.CompressGZIP(file_iam_proto_rawDescData)
	})
	return file_iam_proto_rawDescData
}

var file_iam_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_iam_proto_goTypes = []any{
	(*TokenData)(nil),               // 0: iam.TokenData
	(*Profile)(nil),                 // 1: iam.Profile
	(*ImpersonateUserRequest)(nil),  // 2: iam.ImpersonateUserRequest
	(*ImpersonateUserResponse)(nil), // 3: iam.ImpersonateUserResponse
	(*errors.ErrorResponse)(nil),    // 4: errors.ErrorResponse
}
var file_iam_proto_depIdxs = []int32{
	4, // 0: iam.ImpersonateUserResponse.error:type_name -> errors.ErrorResponse
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_iam_proto_init() }
func file_iam_proto_init() {
	if File_iam_proto != nil {
		return
	}
	file_iam_proto_msgTypes[0].OneofWrappers = []any{}
	file_iam_proto_msgTypes[1].OneofWrappers = []any{}
	file_iam_proto_msgTypes[2].OneofWrappers = []any{
		(*ImpersonateUserRequest_UserId)(nil),
		(*ImpersonateUserRequest_Email)(nil),
	}
	file_iam_proto_msgTypes[3].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_iam_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_iam_proto_goTypes,
		DependencyIndexes: file_iam_proto_depIdxs,
		MessageInfos:      file_iam_proto_msgTypes,
	}.Build()
	File_iam_proto = out.File
	file_iam_proto_rawDesc = nil
	file_iam_proto_goTypes = nil
	file_iam_proto_depIdxs = nil
}
