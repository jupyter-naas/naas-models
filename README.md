# NAAS Models

Protocol Buffer definitions and generated client libraries for the [NAAS.ai](https://naas.ai) API ecosystem.

## Overview

This repository contains the Protocol Buffer (`.proto`) definitions that define the data contracts for all NAAS.ai microservices and APIs. It automatically generates client libraries in multiple programming languages, enabling consistent and type-safe communication across the entire NAAS platform.

## Purpose

- **Single Source of Truth**: All API contracts are defined once in `.proto` files
- **Multi-Language Support**: Automatically generates client libraries for Python, Go, and other languages
- **Type Safety**: Ensures consistent data structures across all services
- **Validation**: Built-in validation rules using protoc-gen-validate

## Project Structure

```
naas-models/
├── protos/              # Protocol Buffer definitions
│   ├── aimodel.proto    # AI model management
│   ├── asset.proto      # Asset management
│   ├── chat.proto       # Chat messaging system
│   ├── common.proto     # Common shared types
│   ├── credit.proto     # Credit system
│   ├── errors.proto     # Error definitions
│   ├── iam.proto        # Identity and Access Management
│   ├── ontology.proto   # Ontology definitions
│   ├── registry.proto   # Service registry
│   ├── secret.proto     # Secret management
│   ├── space.proto      # Space management
│   ├── storage.proto    # Storage services
│   └── workspace.proto  # Workspace management
│
├── python/              # Python generated code
│   └── naas_models/
│       ├── *_pb2.py    # Generated protobuf classes
│       └── pydantic/    # Pydantic models for validation
│
├── go/                  # Go generated code
│   └── github.com/jupyter-naas/naas-models/go/
│       └── */          # Generated Go packages
│
└── lib/                 # Dependencies and tools
    └── protoc-gen-validate/  # Validation plugin
```

## Usage

### For Python Projects

Install the package:
```bash
pip install naas-models
```

Use in your code:
```python
from naas_models import chat_pb2
from naas_models.pydantic import chat_p2p

# Create a message
message = chat_pb2.Message(
    chat_id=123,
    message="Hello, World!",
    type=chat_pb2.MessageType.HUMAN
)

# Use Pydantic models for validation
pydantic_message = chat_p2p.Message.from_protobuf(message)
```

### For Go Projects

Import the package:
```go
import "github.com/jupyter-naas/naas-models/go/chat"

// Use the generated types
message := &chat.Message{
    ChatId:  123,
    Message: "Hello, World!",
    Type:    chat.MessageType_HUMAN,
}
```

## Available APIs

The following domain APIs are available:

- **AIModel**: AI model registration and management
- **Asset**: Digital asset management
- **Chat**: Real-time messaging and conversation management
- **Credit**: Usage credits and billing
- **Errors**: Standardized error responses
- **IAM**: User authentication and authorization
- **Ontology**: Knowledge graph and data relationships
- **Registry**: Service discovery and registration
- **Secret**: Secure credential storage
- **Space**: Collaborative workspace management
- **Storage**: File and object storage
- **Workspace**: User workspace configuration

## Development

### Prerequisites

- Docker and Docker Compose
- Make
- Git with submodules support

### Building from Source

1. Clone the repository with submodules:
```bash
git clone --recursive https://github.com/jupyter-naas/naas-models.git
cd naas-models
```

2. Generate all language bindings:
```bash
make generate
```

This will:
- Build the Docker container with protoc and plugins
- Generate Python protobuf classes and Pydantic models
- Generate Go packages with validation
- Apply necessary import patches

### Adding New Proto Definitions

1. Create your `.proto` file in the `protos/` directory
2. Follow the existing naming conventions and include validation rules
3. Run `make generate` to update all language bindings
4. Commit both the `.proto` file and generated code

### Docker Development Environment

For interactive development:
```bash
make bash
```

This gives you a shell with all necessary tools pre-installed.

## Validation

All messages include validation rules using [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate). These rules are automatically enforced in the generated code:

```protobuf
message User {
    string email = 1 [(validate.rules).string.email = true];
    int32 age = 2 [(validate.rules).int32 = {gte: 0, lte: 120}];
}
```

## Integration with NAAS.ai Services

This library is a core dependency for:
- NAAS.ai API Gateway
- All NAAS microservices
- Client SDKs and applications
- Third-party integrations

When the API contracts are updated here, all dependent services can update their dependency to get the latest types and validation rules.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes to the `.proto` files
4. Run `make generate` to update generated code
5. Test your changes
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions and support:
- Open an issue on GitHub
- Contact the NAAS.ai team
- Check the [NAAS.ai documentation](https://docs.naas.ai)