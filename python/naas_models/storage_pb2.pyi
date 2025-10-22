import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_NO_ERROR: _ClassVar[StorageError]
    STORAGE_ALREADY_EXIST: _ClassVar[StorageError]
    STORAGE_NOT_FOUND: _ClassVar[StorageError]
    INTERNAL_SERVER_ERROR: _ClassVar[StorageError]

class ObjectError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_NO_ERROR: _ClassVar[ObjectError]
    OBJECT_ALREADY_EXIST: _ClassVar[ObjectError]
    OBJECT_SIZE_ERROR: _ClassVar[ObjectError]
    OBJECT_NOT_FOUND: _ClassVar[ObjectError]
    OBJECT_DIR_NOT_EMPTY: _ClassVar[ObjectError]

class CredentialsError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIALS_NO_ERROR: _ClassVar[CredentialsError]
STORAGE_NO_ERROR: StorageError
STORAGE_ALREADY_EXIST: StorageError
STORAGE_NOT_FOUND: StorageError
INTERNAL_SERVER_ERROR: StorageError
OBJECT_NO_ERROR: ObjectError
OBJECT_ALREADY_EXIST: ObjectError
OBJECT_SIZE_ERROR: ObjectError
OBJECT_NOT_FOUND: ObjectError
OBJECT_DIR_NOT_EMPTY: ObjectError
CREDENTIALS_NO_ERROR: CredentialsError

class Storage(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("name", "type", "prefix", "size", "lastmodified")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIED_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    prefix: str
    size: str
    lastmodified: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., prefix: _Optional[str] = ..., size: _Optional[str] = ..., lastmodified: _Optional[str] = ...) -> None: ...

class StorageResponseError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: StorageError
    message: str
    def __init__(self, code: _Optional[_Union[StorageError, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ObjectResponseError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: ObjectError
    message: str
    def __init__(self, code: _Optional[_Union[ObjectError, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ObjectStorageCredentialsResponseError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: CredentialsError
    message: str
    def __init__(self, code: _Optional[_Union[CredentialsError, str]] = ..., message: _Optional[str] = ...) -> None: ...

class StorageListRequest(_message.Message):
    __slots__ = ("storage", "object")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    object: Object
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class StorageListResponse(_message.Message):
    __slots__ = ("storage", "error")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    storage: _containers.RepeatedCompositeFieldContainer[Storage]
    error: StorageResponseError
    def __init__(self, storage: _Optional[_Iterable[_Union[Storage, _Mapping]]] = ..., error: _Optional[_Union[StorageResponseError, _Mapping]] = ...) -> None: ...

class StorageCreateRequest(_message.Message):
    __slots__ = ("storage",)
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class StorageCreateResponse(_message.Message):
    __slots__ = ("storage", "error")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    error: StorageResponseError
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., error: _Optional[_Union[StorageResponseError, _Mapping]] = ...) -> None: ...

class StorageDeleteRequest(_message.Message):
    __slots__ = ("storage",)
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class StorageDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: StorageResponseError
    def __init__(self, error: _Optional[_Union[StorageResponseError, _Mapping]] = ...) -> None: ...

class StorageListObjectRequest(_message.Message):
    __slots__ = ("storage", "object")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    object: Object
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class StorageListObjectResponse(_message.Message):
    __slots__ = ("object", "error")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    object: _containers.RepeatedCompositeFieldContainer[Object]
    error: StorageResponseError
    def __init__(self, object: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., error: _Optional[_Union[StorageResponseError, _Mapping]] = ...) -> None: ...

class ObjectCreateRequest(_message.Message):
    __slots__ = ("storage", "object")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    object: Object
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class ObjectCreateResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ObjectResponseError
    def __init__(self, error: _Optional[_Union[ObjectResponseError, _Mapping]] = ...) -> None: ...

class ObjectListRequest(_message.Message):
    __slots__ = ("storage", "object")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    object: Object
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class ObjectListResponse(_message.Message):
    __slots__ = ("object", "error")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    object: _containers.RepeatedCompositeFieldContainer[Object]
    error: ObjectResponseError
    def __init__(self, object: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., error: _Optional[_Union[ObjectResponseError, _Mapping]] = ...) -> None: ...

class ObjectGetRequest(_message.Message):
    __slots__ = ("storage", "object")
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    object: Object
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class ObjectGetResponse(_message.Message):
    __slots__ = ("object", "error")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    object: Object
    error: ObjectResponseError
    def __init__(self, object: _Optional[_Union[Object, _Mapping]] = ..., error: _Optional[_Union[ObjectResponseError, _Mapping]] = ...) -> None: ...

class ObjectDeleteRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: Object
    def __init__(self, object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class ObjectDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ObjectResponseError
    def __init__(self, error: _Optional[_Union[ObjectResponseError, _Mapping]] = ...) -> None: ...

class ObjectStorageS3Credentials(_message.Message):
    __slots__ = ("endpoint_url", "region_name", "access_key_id", "secret_key", "session_token", "expiration")
    ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    endpoint_url: str
    region_name: str
    access_key_id: str
    secret_key: str
    session_token: str
    expiration: str
    def __init__(self, endpoint_url: _Optional[str] = ..., region_name: _Optional[str] = ..., access_key_id: _Optional[str] = ..., secret_key: _Optional[str] = ..., session_token: _Optional[str] = ..., expiration: _Optional[str] = ...) -> None: ...

class ObjectStorageAzureCredentials(_message.Message):
    __slots__ = ("endpoint_url", "access_key_id", "secret_key")
    ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    endpoint_url: str
    access_key_id: str
    secret_key: str
    def __init__(self, endpoint_url: _Optional[str] = ..., access_key_id: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class ObjectStorageCredentials(_message.Message):
    __slots__ = ("s3",)
    S3_FIELD_NUMBER: _ClassVar[int]
    s3: ObjectStorageS3Credentials
    def __init__(self, s3: _Optional[_Union[ObjectStorageS3Credentials, _Mapping]] = ...) -> None: ...

class ObjectStorageCredentialsRequest(_message.Message):
    __slots__ = ("storage",)
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    storage: Storage
    def __init__(self, storage: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class ObjectStorageCredentialsResponse(_message.Message):
    __slots__ = ("credentials", "error")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credentials: ObjectStorageCredentials
    error: ObjectStorageCredentialsResponseError
    def __init__(self, credentials: _Optional[_Union[ObjectStorageCredentials, _Mapping]] = ..., error: _Optional[_Union[ObjectStorageCredentialsResponseError, _Mapping]] = ...) -> None: ...

class StorageObjectPublicUrlRequest(_message.Message):
    __slots__ = ("workspace_id", "storage_name", "prefix", "object_name")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    storage_name: str
    prefix: str
    object_name: str
    def __init__(self, workspace_id: _Optional[str] = ..., storage_name: _Optional[str] = ..., prefix: _Optional[str] = ..., object_name: _Optional[str] = ...) -> None: ...

class StorageObjectPublicUrlResponse(_message.Message):
    __slots__ = ("url", "error")
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    url: str
    error: ObjectResponseError
    def __init__(self, url: _Optional[str] = ..., error: _Optional[_Union[ObjectResponseError, _Mapping]] = ...) -> None: ...
