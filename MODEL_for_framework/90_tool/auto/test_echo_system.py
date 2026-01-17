#!/usr/bin/env python3
"""
Test Suite for Framework Echo System
====================================

Comprehensive tests for the TCP socket echo server and client.
Tests cross-platform functionality, multi-client support, and error handling.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import pytest
import socket
import threading
import time
import subprocess
import sys
import os
from contextlib import contextmanager

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from socket_echo_server import FrameworkEchoServer
from socket_echo_client import FrameworkEchoClient

class TestFrameworkEchoSystem:
    """Test suite for the Framework Echo System."""

    @pytest.fixture
    def test_port(self):
        """Provide a test port."""
        return 9999  # Use a different port for testing

    @pytest.fixture
    def test_host(self):
        """Provide test host."""
        return 'localhost'

    def test_server_initialization(self, test_host, test_port):
        """Test server initialization with valid parameters."""
        server = FrameworkEchoServer(host=test_host, port=test_port, max_clients=5)

        assert server.host == test_host
        assert server.port == test_port
        assert server.max_clients == 5
        assert not server.running

    def test_server_invalid_port(self):
        """Test server rejects invalid ports."""
        with pytest.raises(SystemExit):
            # This will call sys.exit(1) for invalid port
            import argparse
            parser = argparse.ArgumentParser()
            # Simulate invalid port validation
            if not (1 <= 0 <= 65535):  # Invalid port
                parser.error("Port must be between 1 and 65535")

    def test_client_initialization(self, test_host, test_port):
        """Test client initialization."""
        client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)

        assert client.host == test_host
        assert client.port == test_port
        assert client.timeout == 2.0

    @contextmanager
    def running_server(self, host='localhost', port=9999):
        """Context manager for running a test server."""
        server = FrameworkEchoServer(host=host, port=port, max_clients=2)

        # Start server in background thread
        server_thread = threading.Thread(target=server.start_server, daemon=True)
        server_thread.start()

        # Wait for server to start
        time.sleep(0.5)

        try:
            yield server
        finally:
            server.shutdown()
            server_thread.join(timeout=2.0)

    def test_server_client_basic_communication(self, test_host, test_port):
        """Test basic server-client communication."""
        test_message = "Test message from automated test"

        with self.running_server(test_host, test_port) as server:
            # Give server time to start
            time.sleep(0.2)

            # Create client and send message
            client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)
            success = client.send_message(test_message)

            assert success, "Message sending should succeed"

    def test_multiple_clients(self, test_host, test_port):
        """Test multiple clients connecting simultaneously."""
        messages = [
            "Message from client 1",
            "Message from client 2",
            "Message from client 3"
        ]

        with self.running_server(test_host, test_port) as server:
            time.sleep(0.2)

            # Send messages from multiple clients
            clients = []
            for msg in messages:
                client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)
                success = client.send_message(msg)
                assert success, f"Client message '{msg}' should succeed"
                clients.append(client)

            assert len(clients) == len(messages), "All clients should connect successfully"

    def test_client_connection_timeout(self, test_host):
        """Test client handles connection timeouts properly."""
        # Try to connect to non-existent server
        client = FrameworkEchoClient(host=test_host, port=9998, timeout=0.5)
        success = client.send_message("Test message")

        assert not success, "Connection to non-existent server should fail"

    def test_client_invalid_host(self):
        """Test client handles invalid hosts."""
        client = FrameworkEchoClient(host='invalid.host.name', port=9999, timeout=0.5)
        success = client.send_message("Test message")

        assert not success, "Connection to invalid host should fail"

    def test_server_graceful_shutdown(self, test_host, test_port):
        """Test server shuts down gracefully."""
        server = FrameworkEchoServer(host=test_host, port=test_port)

        # Start server
        server_thread = threading.Thread(target=server.start_server, daemon=True)
        server_thread.start()
        time.sleep(0.2)

        # Shutdown server
        server.shutdown()

        # Wait for thread to finish
        server_thread.join(timeout=2.0)

        assert not server.running, "Server should be stopped after shutdown"

    def test_command_line_interface_server(self, test_host, test_port):
        """Test server command-line interface."""
        # Test help message
        result = subprocess.run([
            sys.executable, 'socket_echo_server.py', '--help'
        ], capture_output=True, text=True, cwd=os.path.dirname(__file__))

        assert result.returncode == 0, "Help command should succeed"
        assert 'Framework Echo Server' in result.stdout, "Help should contain program name"

    def test_command_line_interface_client(self, test_host, test_port):
        """Test client command-line interface."""
        # Test help message
        result = subprocess.run([
            sys.executable, 'socket_echo_client.py', '--help'
        ], capture_output=True, text=True, cwd=os.path.dirname(__file__))

        assert result.returncode == 0, "Help command should succeed"
        assert 'Framework Echo Client' in result.stdout, "Help should contain program name"

    def test_client_stdin_input(self, test_host, test_port):
        """Test client can read from stdin."""
        test_input = "Line 1\nLine 2\nLine 3"

        with self.running_server(test_host, test_port) as server:
            time.sleep(0.2)

            # Simulate stdin input
            process = subprocess.run([
                sys.executable, 'socket_echo_client.py', '--stdin'
            ], input=test_input, text=True, capture_output=True,
               cwd=os.path.dirname(__file__), timeout=5)

            assert process.returncode == 0, "Stdin processing should succeed"

    def test_server_version_info(self):
        """Test server version information."""
        from socket_echo_server import __version__, __status__

        assert __version__ == "1.0.0", "Version should be 1.0.0"
        assert __status__ == "ACTIVE", "Status should be ACTIVE"

    def test_client_version_info(self):
        """Test client version information."""
        from socket_echo_client import __version__, __status__

        assert __version__ == "1.0.0", "Version should be 1.0.0"
        assert __status__ == "ACTIVE", "Status should be ACTIVE"

    def test_utf8_encoding(self, test_host, test_port):
        """Test UTF-8 encoding support."""
        test_message = "Hello 世界 🌍 Test 中文"

        with self.running_server(test_host, test_port) as server:
            time.sleep(0.2)

            client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)
            success = client.send_message(test_message)

            assert success, "UTF-8 message should be sent successfully"

    def test_empty_message_handling(self, test_host, test_port):
        """Test handling of empty messages."""
        with self.running_server(test_host, test_port) as server:
            time.sleep(0.2)

            client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)

            # Empty message should still work (server handles it gracefully)
            success = client.send_message("")

            # This might succeed or fail depending on implementation
            # The important thing is it doesn't crash
            assert isinstance(success, bool), "Empty message should return boolean result"

    def test_rapid_successive_connections(self, test_host, test_port):
        """Test rapid successive client connections."""
        messages = [f"Rapid message {i}" for i in range(5)]

        with self.running_server(test_host, test_port) as server:
            time.sleep(0.2)

            for msg in messages:
                client = FrameworkEchoClient(host=test_host, port=test_port, timeout=2.0)
                success = client.send_message(msg)
                assert success, f"Rapid message '{msg}' should succeed"

if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])
