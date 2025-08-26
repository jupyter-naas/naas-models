# NAAS Models

Protocol Buffer definitions and generated client libraries for the [NAAS.ai](https://naas.ai) ecosystem.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python Package](https://img.shields.io/pypi/v/naas-models)](https://pypi.org/project/naas-models/)

## What is this?

Type-safe API contracts for NAAS.ai services. Uses Protocol Buffers for fast, validated communication between services and clients.

## Installation

**Python:**
```bash
pip install naas-models
```

**Go:**
```bash
go get github.com/jupyter-naas/naas-models/go
```

## Usage

**Python:**
```python
from naas_models import chat_pb2

message = chat_pb2.Message(
    chat_id=123,
    message="Hello, World!",
    type=chat_pb2.MessageType.HUMAN
)
```

**Go:**
```go
import "github.com/jupyter-naas/naas-models/go/chat"

message := &chat.Message{
    ChatId:  123,
    Message: "Hello, World!",
    Type:    chat.MessageType_HUMAN,
}
```

## Available APIs

- **Chat** - Messaging system
- **IAM** - Authentication & authorization  
- **AIModel** - AI model management
- **Asset** - File management
- **Storage** - Object storage
- **Workspace** - Multi-tenant workspaces
- **Credit** - Usage & billing
- **Secret** - Credential storage
- **Registry** - Service discovery
- **Ontology** - Knowledge graphs
- **Space** - Collaborative environments
- **Errors** - Error handling
- **Common** - Shared utilities

## Common Examples

**Authentication:**
```python
from naas_models import iam_pb2

profile = iam_pb2.Profile(
    user_id="550e8400-e29b-41d4-a716-446655440000",
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com"
)
```

**AI Model Request:**
```python
from naas_models import aimodel_pb2

request = aimodel_pb2.AIModelCompletionRequest(
    id="gpt-4",
    payload='{"messages": [{"role": "user", "content": "Hello"}]}'
)
```

**Asset Management:**
```python
from naas_models import asset_pb2

asset = asset_pb2.AssetCreation(
    workspace_id="ws-123",
    storage_name="my-storage",
    object_name="document.pdf"
)
```

**Workspace Creation:**
```python
from naas_models import workspace_pb2

workspace = workspace_pb2.WorkspaceCreation(
    name="My Team",
    primary_color="#1f2937",
    is_personal=False
)
```



## Development

```bash
# Clone and build
git clone --recursive https://github.com/jupyter-naas/naas-models.git
cd naas-models
make generate
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

AGPL v3.0 - see [LICENSE](LICENSE)