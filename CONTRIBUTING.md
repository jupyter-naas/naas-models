# Contributing

Thank you for your interest in contributing to NAAS Models! This document outlines the process and best practices for contributing to the project.

## Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone. Please read our Code of Conduct before participating in our community.

## Getting Started

1. **Fork the repository** or clone locally
2. **Initialize submodules** by running `git submodule init && git submodule update`
3. **Set up the development environment** using Docker and `make`

## Development Workflow

1. Pick an issue to work on on [GitHub](https://github.com/jupyter-naas/naas-models/issues)

2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes following the project's [coding standards](#coding-standards)

4. Regenerate code after protobuf changes:
   ```bash
   make generate
   ```

5. Ensure all tests pass:
   ```bash
   make test
   ```

6. Update documentation as needed

7. Commit your changes with clear, descriptive commit messages:
   ```bash
   git commit -m "feat(chat): add message threading support"
   ```

8. Push your branch to your fork and [submit a pull request](#pull-request-process)

## Project Structure

NAAS Models follows a contract-first architecture:

```
naas-models/
├── protos/                 # Protocol Buffer definitions
│   ├── aimodel.proto      # AI model management
│   ├── asset.proto        # Asset management
│   ├── chat.proto         # Chat messaging system
│   ├── iam.proto          # Identity and Access Management
│   └── ...                # Other domain APIs
├── python/                # Python generated code
│   └── naas_models/
│       ├── *_pb2.py      # Generated protobuf classes
│       └── pydantic/     # Pydantic models for validation
├── go/                    # Go generated code
│   └── github.com/jupyter-naas/naas-models/go/
└── docs/                  # Documentation
    ├── api-reference/     # API documentation
    ├── examples/          # Usage examples
    └── getting-started/   # Tutorials
```

Each protobuf file can contain:
- `messages`: Core data structures
- `enums`: Status and type definitions
- `validation rules`: Input validation using protoc-gen-validate
- `documentation`: Inline comments for API docs

## Coding Standards

### General Guidelines

1. **Follow protocol buffer best practices**
   - Use semantic field numbering
   - Include comprehensive validation rules
   - Maintain backward compatibility
   - Document all messages and fields

2. **Keep messages focused and well-defined**
   - Each message should represent a clear domain concept
   - Use appropriate field types and constraints

3. **Use descriptive names**
   - Use meaningful message and field names
   - Follow `snake_case` for field names
   - Follow `PascalCase` for message names

4. **Document your schemas**
   - Add comments to all messages and fields
   - Include validation rules and constraints
   - Provide usage examples in comments

5. **Validation rules**
   - Use protoc-gen-validate for input validation
   - Include appropriate constraints (length, format, range)
   - Validate UUIDs, emails, and other structured data

## Protocol Buffer Development

When developing new protobuf definitions, follow these guidelines:

### Creating Messages

Define clear, well-structured messages:

```protobuf
// User represents a person in the NAAS ecosystem.
//
// Users can authenticate via email/password or API keys.
// Each user belongs to one or more workspaces.
message User {
    // Unique identifier (UUID v4 format)
    string id = 1 [(validate.rules).string.uuid = true];
    
    // Primary email address (must be unique)
    string email = 2 [(validate.rules).string.email = true];
    
    // Display name (1-100 characters)
    string name = 3 [(validate.rules).string = {min_len: 1, max_len: 100}];
    
    // Account creation timestamp
    optional string created_at = 4 [(validate.rules).string = {ignore_empty: true}];
}
```

### Adding Validation Rules

Include comprehensive validation for all fields:

1. **String validation**: length, format, patterns
2. **Numeric validation**: ranges, positive values
3. **Enum validation**: defined values only
4. **UUID validation**: proper UUID format
5. **Email validation**: valid email format

### Maintaining Compatibility

1. Never remove or change existing field numbers
2. Use `optional` for new fields
3. Deprecate fields instead of removing them
4. Add new enums at the end with higher numbers

### Request/Response Patterns

Follow consistent patterns for API operations:

```protobuf
// List operation
message EntityListRequest {
    optional int32 page_size = 1;
    optional int32 page_number = 2;
    // Domain-specific filters
}

message EntityListResponse {
    repeated Entity entities = 1;
    optional int32 page_number = 2;
    optional errors.ErrorResponse error = 3;
}

// CRUD operations
message EntityCreateRequest {
    optional EntityCreation entity = 1;
}

message EntityCreateResponse {
    optional Entity entity = 1;
    optional errors.ErrorResponse error = 2;
}
```

## Testing

All contributions should include appropriate tests:

1. **Validation tests** for protobuf message validation
2. **Generation tests** to ensure code generates correctly
3. **Integration tests** for multi-language compatibility

Test your changes in both Python and Go:

```bash
# Test Python bindings
cd python && poetry install --with dev
poetry run python -c "from naas_models import chat_pb2; print('Python OK')"

# Test Go bindings
cd go && go mod tidy
go build ./...
```

## Documentation

Good documentation is essential:

1. **Inline comments** in protobuf files
2. **API documentation** for new domains
3. **Usage examples** in Python and Go
4. **Migration guides** for breaking changes
5. **Update existing docs** affected by your changes

## Pull Request Process

1. **Submit your PR** against the `main` branch
2. **Fill out the PR template** with a description of changes
3. **Link related issues** using keywords like "Fixes #123"
4. **Ensure CI passes** including code generation and tests
5. **Request reviews** from maintainers
6. **Address feedback** promptly
7. **Squash commits** before merging if requested

We aim to review PRs within 1-2 business days. Thank you for contributing to NAAS Models!
