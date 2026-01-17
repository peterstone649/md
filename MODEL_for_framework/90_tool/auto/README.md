# Framework Auto Tools - TCP Socket Echo System

## Overview

The Framework Auto Tools provide a cross-platform TCP socket-based echo system for inter-process communication, logging, and debugging within the MODEL_for_framework ecosystem.

## Components

### 🔊 `socket_echo_server.py`
**Main echo server** that listens for TCP connections and echoes all received data with timestamps.

### 📤 `socket_echo_client.py`
**Test client** for sending messages to the echo server.

## Quick Start

### 1. Start the Echo Server

```bash
cd MODEL_for_framework/90_tool/auto
python socket_echo_server.py
```

**Output:**
```
🚀 Framework Echo Server v1.0.0 started!
📡 Listening on localhost:8888
👥 Max clients: 10
🛑 Press Ctrl+C to stop
==================================================
```

### 2. Send Test Messages

**From another terminal:**

```bash
# Linux/macOS
echo "Hello Framework!" | nc localhost 8888

# Windows PowerShell
"Hello Framework!" | nc.exe localhost 8888

# Using the client script
python socket_echo_client.py "Test message from client"
```

**Server output:**
```
[2026-01-17 08:03:15.123] [127.0.0.1:54321] Hello Framework!
[2026-01-17 08:03:16.456] [127.0.0.1:54322] Test message from client
```

## Usage Examples

### Basic Echo Server

```bash
# Default settings (localhost:8888)
python socket_echo_server.py

# Custom port
python socket_echo_server.py --port 9999

# Listen on all interfaces
python socket_echo_server.py --host 0.0.0.0

# Limit concurrent clients
python socket_echo_server.py --max-clients 5
```

### Client Usage

```bash
# Send single message
python socket_echo_client.py "Framework event logged"

# Send to custom server
python socket_echo_client.py --host 192.168.1.100 --port 9999 "Remote message"

# Read from stdin (pipe data)
cat logfile.txt | python socket_echo_client.py --stdin

# Interactive stdin mode
python socket_echo_client.py --stdin
# Then type messages and press Enter
```

### Integration Examples

#### Framework Tool Logging

```python
# In any framework tool
import socket

def log_to_echo_server(message):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 8888))
        client.send(f"TOOL: {message}".encode('utf-8'))
        client.close()
    except:
        pass  # Silent failure if server not running

# Usage
log_to_echo_server("Processing started")
log_to_echo_server("Task completed successfully")
```

#### CI/CD Integration

```yaml
# In GitHub Actions or other CI
- name: Log to echo server
  run: |
    echo "CI Build Started" | nc localhost 8888
    # ... build steps ...
    echo "CI Build Completed" | nc localhost 8888
```

#### Monitoring Script

```bash
#!/bin/bash
# monitor.sh - Continuous monitoring script

while true; do
    # Log system status
    echo "System check: $(date)" | nc localhost 8888

    # Log framework status
    if [ -f "MODEL_for_framework/README.md" ]; then
        echo "Framework files present" | nc localhost 8888
    fi

    sleep 300  # Check every 5 minutes
done
```

## Configuration

### Environment Variables

```bash
# Set custom defaults
export FRAMEWORK_ECHO_HOST=0.0.0.0
export FRAMEWORK_ECHO_PORT=9999
export FRAMEWORK_ECHO_MAX_CLIENTS=20
```

### Command Line Options

#### Server Options
- `--host HOST`: Host to bind to (default: localhost)
- `--port PORT`: Port to listen on (default: 8888)
- `--max-clients N`: Maximum concurrent clients (default: 10)

#### Client Options
- `--host HOST`: Server host to connect to
- `--port PORT`: Server port to connect to
- `--timeout SEC`: Connection timeout (default: 5.0)
- `--stdin`: Read messages from stdin

## Cross-Platform Compatibility

### ✅ Supported Platforms
- **Windows** 10/11 (PowerShell/Command Prompt)
- **Linux** (Ubuntu, CentOS, Alpine, etc.)
- **macOS** 12+ (Terminal)

### 🔧 Required Tools

#### Windows
```powershell
# Install Netcat for Windows (optional, for testing)
choco install netcat
```

#### Linux/macOS
```bash
# Netcat usually pre-installed
which nc || echo "Install netcat: apt install netcat / brew install netcat"
```

#### Python Requirements
- **Python 3.7+** (stdlib only, no external dependencies)
- **Built-in modules**: socket, threading, logging, argparse

## Troubleshooting

### Server Won't Start

**Port already in use:**
```bash
# Find process using port 8888
netstat -ano | findstr :8888  # Windows
lsof -i :8888                 # Linux/macOS

# Use different port
python socket_echo_server.py --port 9999
```

**Permission denied:**
```bash
# Use port > 1024 or run as administrator
python socket_echo_server.py --port 8080
```

### Client Connection Issues

**Connection refused:**
- Ensure server is running
- Check host and port settings
- Verify firewall settings

**Timeout errors:**
- Increase timeout: `--timeout 10.0`
- Check network connectivity

### Performance Issues

**High CPU usage:**
- Reduce max clients: `--max-clients 5`
- Check for runaway client connections

**Memory issues:**
- Monitor client thread cleanup
- Restart server periodically

## Security Considerations

### Local Network Only
- Server binds to `localhost` by default
- No external exposure without configuration
- Suitable for framework-internal communication

### Production Usage
- Consider authentication for multi-user environments
- Monitor resource usage
- Implement rate limiting if needed

## Logging

### Server Logs
- **Console output**: Real-time message display
- **File logging**: `framework_echo_server.log`
- **Format**: `[timestamp] [client] message`

### Log Rotation
```bash
# Manual log rotation
mv framework_echo_server.log framework_echo_server.log.$(date +%Y%m%d)
```

## Development

### Adding Features
- Extend `FrameworkEchoServer` class
- Add new command-line options
- Implement custom message processing

### Testing
```bash
# Run server in background
python socket_echo_server.py &
SERVER_PID=$!

# Run tests
python socket_echo_client.py "Test message 1"
python socket_echo_client.py "Test message 2"

# Stop server
kill $SERVER_PID
```

## Changelog

- **v1.0.0**: Initial release with multi-client TCP support
- Added timestamped logging and graceful shutdown
- Cross-platform compatibility with pure Python stdlib

## License

EUPL v1.2 - European Union Public Licence

## Contributing

See main framework [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution guidelines.
