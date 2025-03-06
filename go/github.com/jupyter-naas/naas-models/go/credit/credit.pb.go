// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.5
// 	protoc        v5.26.1
// source: credit.proto

package credit

import (
	_ "github.com/envoyproxy/protoc-gen-validate/validate"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type CreditTransaction struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Scenario      *string                `protobuf:"bytes,1,opt,name=scenario,proto3,oneof" json:"scenario,omitempty"`
	User          *string                `protobuf:"bytes,2,opt,name=user,proto3,oneof" json:"user,omitempty"`
	Plan          *string                `protobuf:"bytes,3,opt,name=plan,proto3,oneof" json:"plan,omitempty"`
	Type          *string                `protobuf:"bytes,4,opt,name=type,proto3,oneof" json:"type,omitempty"`
	Meta_1Desc    *string                `protobuf:"bytes,5,opt,name=meta_1_desc,json=meta1Desc,proto3,oneof" json:"meta_1_desc,omitempty"`
	Meta_1        *string                `protobuf:"bytes,6,opt,name=meta_1,json=meta1,proto3,oneof" json:"meta_1,omitempty"`
	Meta_2Desc    *string                `protobuf:"bytes,7,opt,name=meta_2_desc,json=meta2Desc,proto3,oneof" json:"meta_2_desc,omitempty"`
	Meta_2        *string                `protobuf:"bytes,8,opt,name=meta_2,json=meta2,proto3,oneof" json:"meta_2,omitempty"`
	Meta_3Desc    *string                `protobuf:"bytes,9,opt,name=meta_3_desc,json=meta3Desc,proto3,oneof" json:"meta_3_desc,omitempty"`
	Meta_3        *string                `protobuf:"bytes,10,opt,name=meta_3,json=meta3,proto3,oneof" json:"meta_3,omitempty"`
	Quantity      *float32               `protobuf:"fixed32,11,opt,name=quantity,proto3,oneof" json:"quantity,omitempty"`
	Unit          *string                `protobuf:"bytes,12,opt,name=unit,proto3,oneof" json:"unit,omitempty"`
	UnitPrice     *float32               `protobuf:"fixed32,13,opt,name=unit_price,json=unitPrice,proto3,oneof" json:"unit_price,omitempty"`
	Credit        *float32               `protobuf:"fixed32,14,opt,name=credit,proto3,oneof" json:"credit,omitempty"`
	CreditDollar  *float32               `protobuf:"fixed32,15,opt,name=credit_dollar,json=creditDollar,proto3,oneof" json:"credit_dollar,omitempty"`
	DateExtract   *string                `protobuf:"bytes,16,opt,name=date_extract,json=dateExtract,proto3,oneof" json:"date_extract,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreditTransaction) Reset() {
	*x = CreditTransaction{}
	mi := &file_credit_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreditTransaction) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreditTransaction) ProtoMessage() {}

func (x *CreditTransaction) ProtoReflect() protoreflect.Message {
	mi := &file_credit_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreditTransaction.ProtoReflect.Descriptor instead.
func (*CreditTransaction) Descriptor() ([]byte, []int) {
	return file_credit_proto_rawDescGZIP(), []int{0}
}

func (x *CreditTransaction) GetScenario() string {
	if x != nil && x.Scenario != nil {
		return *x.Scenario
	}
	return ""
}

func (x *CreditTransaction) GetUser() string {
	if x != nil && x.User != nil {
		return *x.User
	}
	return ""
}

func (x *CreditTransaction) GetPlan() string {
	if x != nil && x.Plan != nil {
		return *x.Plan
	}
	return ""
}

func (x *CreditTransaction) GetType() string {
	if x != nil && x.Type != nil {
		return *x.Type
	}
	return ""
}

func (x *CreditTransaction) GetMeta_1Desc() string {
	if x != nil && x.Meta_1Desc != nil {
		return *x.Meta_1Desc
	}
	return ""
}

func (x *CreditTransaction) GetMeta_1() string {
	if x != nil && x.Meta_1 != nil {
		return *x.Meta_1
	}
	return ""
}

func (x *CreditTransaction) GetMeta_2Desc() string {
	if x != nil && x.Meta_2Desc != nil {
		return *x.Meta_2Desc
	}
	return ""
}

func (x *CreditTransaction) GetMeta_2() string {
	if x != nil && x.Meta_2 != nil {
		return *x.Meta_2
	}
	return ""
}

func (x *CreditTransaction) GetMeta_3Desc() string {
	if x != nil && x.Meta_3Desc != nil {
		return *x.Meta_3Desc
	}
	return ""
}

func (x *CreditTransaction) GetMeta_3() string {
	if x != nil && x.Meta_3 != nil {
		return *x.Meta_3
	}
	return ""
}

func (x *CreditTransaction) GetQuantity() float32 {
	if x != nil && x.Quantity != nil {
		return *x.Quantity
	}
	return 0
}

func (x *CreditTransaction) GetUnit() string {
	if x != nil && x.Unit != nil {
		return *x.Unit
	}
	return ""
}

func (x *CreditTransaction) GetUnitPrice() float32 {
	if x != nil && x.UnitPrice != nil {
		return *x.UnitPrice
	}
	return 0
}

func (x *CreditTransaction) GetCredit() float32 {
	if x != nil && x.Credit != nil {
		return *x.Credit
	}
	return 0
}

func (x *CreditTransaction) GetCreditDollar() float32 {
	if x != nil && x.CreditDollar != nil {
		return *x.CreditDollar
	}
	return 0
}

func (x *CreditTransaction) GetDateExtract() string {
	if x != nil && x.DateExtract != nil {
		return *x.DateExtract
	}
	return ""
}

type Balance struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Balance       *float32               `protobuf:"fixed32,1,opt,name=balance,proto3,oneof" json:"balance,omitempty"`
	BalanceDollar *float32               `protobuf:"fixed32,2,opt,name=balance_dollar,json=balanceDollar,proto3,oneof" json:"balance_dollar,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Balance) Reset() {
	*x = Balance{}
	mi := &file_credit_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Balance) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Balance) ProtoMessage() {}

func (x *Balance) ProtoReflect() protoreflect.Message {
	mi := &file_credit_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Balance.ProtoReflect.Descriptor instead.
func (*Balance) Descriptor() ([]byte, []int) {
	return file_credit_proto_rawDescGZIP(), []int{1}
}

func (x *Balance) GetBalance() float32 {
	if x != nil && x.Balance != nil {
		return *x.Balance
	}
	return 0
}

func (x *Balance) GetBalanceDollar() float32 {
	if x != nil && x.BalanceDollar != nil {
		return *x.BalanceDollar
	}
	return 0
}

var File_credit_proto protoreflect.FileDescriptor

var file_credit_proto_rawDesc = string([]byte{
	0x0a, 0x0c, 0x63, 0x72, 0x65, 0x64, 0x69, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x06,
	0x63, 0x72, 0x65, 0x64, 0x69, 0x74, 0x1a, 0x0e, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xdb, 0x05, 0x0a, 0x11, 0x43, 0x72, 0x65, 0x64, 0x69,
	0x74, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1f, 0x0a, 0x08,
	0x73, 0x63, 0x65, 0x6e, 0x61, 0x72, 0x69, 0x6f, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00,
	0x52, 0x08, 0x73, 0x63, 0x65, 0x6e, 0x61, 0x72, 0x69, 0x6f, 0x88, 0x01, 0x01, 0x12, 0x17, 0x0a,
	0x04, 0x75, 0x73, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x04, 0x75,
	0x73, 0x65, 0x72, 0x88, 0x01, 0x01, 0x12, 0x17, 0x0a, 0x04, 0x70, 0x6c, 0x61, 0x6e, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x09, 0x48, 0x02, 0x52, 0x04, 0x70, 0x6c, 0x61, 0x6e, 0x88, 0x01, 0x01, 0x12,
	0x17, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x48, 0x03, 0x52,
	0x04, 0x74, 0x79, 0x70, 0x65, 0x88, 0x01, 0x01, 0x12, 0x23, 0x0a, 0x0b, 0x6d, 0x65, 0x74, 0x61,
	0x5f, 0x31, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x48, 0x04, 0x52,
	0x09, 0x6d, 0x65, 0x74, 0x61, 0x31, 0x44, 0x65, 0x73, 0x63, 0x88, 0x01, 0x01, 0x12, 0x1a, 0x0a,
	0x06, 0x6d, 0x65, 0x74, 0x61, 0x5f, 0x31, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x48, 0x05, 0x52,
	0x05, 0x6d, 0x65, 0x74, 0x61, 0x31, 0x88, 0x01, 0x01, 0x12, 0x23, 0x0a, 0x0b, 0x6d, 0x65, 0x74,
	0x61, 0x5f, 0x32, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x18, 0x07, 0x20, 0x01, 0x28, 0x09, 0x48, 0x06,
	0x52, 0x09, 0x6d, 0x65, 0x74, 0x61, 0x32, 0x44, 0x65, 0x73, 0x63, 0x88, 0x01, 0x01, 0x12, 0x1a,
	0x0a, 0x06, 0x6d, 0x65, 0x74, 0x61, 0x5f, 0x32, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x48, 0x07,
	0x52, 0x05, 0x6d, 0x65, 0x74, 0x61, 0x32, 0x88, 0x01, 0x01, 0x12, 0x23, 0x0a, 0x0b, 0x6d, 0x65,
	0x74, 0x61, 0x5f, 0x33, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x18, 0x09, 0x20, 0x01, 0x28, 0x09, 0x48,
	0x08, 0x52, 0x09, 0x6d, 0x65, 0x74, 0x61, 0x33, 0x44, 0x65, 0x73, 0x63, 0x88, 0x01, 0x01, 0x12,
	0x1a, 0x0a, 0x06, 0x6d, 0x65, 0x74, 0x61, 0x5f, 0x33, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x09, 0x48,
	0x09, 0x52, 0x05, 0x6d, 0x65, 0x74, 0x61, 0x33, 0x88, 0x01, 0x01, 0x12, 0x1f, 0x0a, 0x08, 0x71,
	0x75, 0x61, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x02, 0x48, 0x0a, 0x52,
	0x08, 0x71, 0x75, 0x61, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x88, 0x01, 0x01, 0x12, 0x17, 0x0a, 0x04,
	0x75, 0x6e, 0x69, 0x74, 0x18, 0x0c, 0x20, 0x01, 0x28, 0x09, 0x48, 0x0b, 0x52, 0x04, 0x75, 0x6e,
	0x69, 0x74, 0x88, 0x01, 0x01, 0x12, 0x22, 0x0a, 0x0a, 0x75, 0x6e, 0x69, 0x74, 0x5f, 0x70, 0x72,
	0x69, 0x63, 0x65, 0x18, 0x0d, 0x20, 0x01, 0x28, 0x02, 0x48, 0x0c, 0x52, 0x09, 0x75, 0x6e, 0x69,
	0x74, 0x50, 0x72, 0x69, 0x63, 0x65, 0x88, 0x01, 0x01, 0x12, 0x1b, 0x0a, 0x06, 0x63, 0x72, 0x65,
	0x64, 0x69, 0x74, 0x18, 0x0e, 0x20, 0x01, 0x28, 0x02, 0x48, 0x0d, 0x52, 0x06, 0x63, 0x72, 0x65,
	0x64, 0x69, 0x74, 0x88, 0x01, 0x01, 0x12, 0x28, 0x0a, 0x0d, 0x63, 0x72, 0x65, 0x64, 0x69, 0x74,
	0x5f, 0x64, 0x6f, 0x6c, 0x6c, 0x61, 0x72, 0x18, 0x0f, 0x20, 0x01, 0x28, 0x02, 0x48, 0x0e, 0x52,
	0x0c, 0x63, 0x72, 0x65, 0x64, 0x69, 0x74, 0x44, 0x6f, 0x6c, 0x6c, 0x61, 0x72, 0x88, 0x01, 0x01,
	0x12, 0x26, 0x0a, 0x0c, 0x64, 0x61, 0x74, 0x65, 0x5f, 0x65, 0x78, 0x74, 0x72, 0x61, 0x63, 0x74,
	0x18, 0x10, 0x20, 0x01, 0x28, 0x09, 0x48, 0x0f, 0x52, 0x0b, 0x64, 0x61, 0x74, 0x65, 0x45, 0x78,
	0x74, 0x72, 0x61, 0x63, 0x74, 0x88, 0x01, 0x01, 0x42, 0x0b, 0x0a, 0x09, 0x5f, 0x73, 0x63, 0x65,
	0x6e, 0x61, 0x72, 0x69, 0x6f, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x75, 0x73, 0x65, 0x72, 0x42, 0x07,
	0x0a, 0x05, 0x5f, 0x70, 0x6c, 0x61, 0x6e, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x74, 0x79, 0x70, 0x65,
	0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x5f, 0x31, 0x5f, 0x64, 0x65, 0x73, 0x63,
	0x42, 0x09, 0x0a, 0x07, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x5f, 0x31, 0x42, 0x0e, 0x0a, 0x0c, 0x5f,
	0x6d, 0x65, 0x74, 0x61, 0x5f, 0x32, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x42, 0x09, 0x0a, 0x07, 0x5f,
	0x6d, 0x65, 0x74, 0x61, 0x5f, 0x32, 0x42, 0x0e, 0x0a, 0x0c, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x5f,
	0x33, 0x5f, 0x64, 0x65, 0x73, 0x63, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x6d, 0x65, 0x74, 0x61, 0x5f,
	0x33, 0x42, 0x0b, 0x0a, 0x09, 0x5f, 0x71, 0x75, 0x61, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x42, 0x07,
	0x0a, 0x05, 0x5f, 0x75, 0x6e, 0x69, 0x74, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x75, 0x6e, 0x69, 0x74,
	0x5f, 0x70, 0x72, 0x69, 0x63, 0x65, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x63, 0x72, 0x65, 0x64, 0x69,
	0x74, 0x42, 0x10, 0x0a, 0x0e, 0x5f, 0x63, 0x72, 0x65, 0x64, 0x69, 0x74, 0x5f, 0x64, 0x6f, 0x6c,
	0x6c, 0x61, 0x72, 0x42, 0x0f, 0x0a, 0x0d, 0x5f, 0x64, 0x61, 0x74, 0x65, 0x5f, 0x65, 0x78, 0x74,
	0x72, 0x61, 0x63, 0x74, 0x22, 0x73, 0x0a, 0x07, 0x42, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x65, 0x12,
	0x1d, 0x0a, 0x07, 0x62, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x02,
	0x48, 0x00, 0x52, 0x07, 0x62, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x65, 0x88, 0x01, 0x01, 0x12, 0x2a,
	0x0a, 0x0e, 0x62, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x65, 0x5f, 0x64, 0x6f, 0x6c, 0x6c, 0x61, 0x72,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x02, 0x48, 0x01, 0x52, 0x0d, 0x62, 0x61, 0x6c, 0x61, 0x6e, 0x63,
	0x65, 0x44, 0x6f, 0x6c, 0x6c, 0x61, 0x72, 0x88, 0x01, 0x01, 0x42, 0x0a, 0x0a, 0x08, 0x5f, 0x62,
	0x61, 0x6c, 0x61, 0x6e, 0x63, 0x65, 0x42, 0x11, 0x0a, 0x0f, 0x5f, 0x62, 0x61, 0x6c, 0x61, 0x6e,
	0x63, 0x65, 0x5f, 0x64, 0x6f, 0x6c, 0x6c, 0x61, 0x72, 0x42, 0x2f, 0x5a, 0x2d, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x6a, 0x75, 0x70, 0x79, 0x74, 0x65, 0x72, 0x2d,
	0x6e, 0x61, 0x61, 0x73, 0x2f, 0x6e, 0x61, 0x61, 0x73, 0x2d, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x73,
	0x2f, 0x67, 0x6f, 0x2f, 0x63, 0x72, 0x65, 0x64, 0x69, 0x74, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
})

var (
	file_credit_proto_rawDescOnce sync.Once
	file_credit_proto_rawDescData []byte
)

func file_credit_proto_rawDescGZIP() []byte {
	file_credit_proto_rawDescOnce.Do(func() {
		file_credit_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_credit_proto_rawDesc), len(file_credit_proto_rawDesc)))
	})
	return file_credit_proto_rawDescData
}

var file_credit_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_credit_proto_goTypes = []any{
	(*CreditTransaction)(nil), // 0: credit.CreditTransaction
	(*Balance)(nil),           // 1: credit.Balance
}
var file_credit_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_credit_proto_init() }
func file_credit_proto_init() {
	if File_credit_proto != nil {
		return
	}
	file_credit_proto_msgTypes[0].OneofWrappers = []any{}
	file_credit_proto_msgTypes[1].OneofWrappers = []any{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_credit_proto_rawDesc), len(file_credit_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_credit_proto_goTypes,
		DependencyIndexes: file_credit_proto_depIdxs,
		MessageInfos:      file_credit_proto_msgTypes,
	}.Build()
	File_credit_proto = out.File
	file_credit_proto_goTypes = nil
	file_credit_proto_depIdxs = nil
}
