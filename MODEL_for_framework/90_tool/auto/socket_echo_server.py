#!/usr/bin/env python3
"""
Framework Echo Server - Cross-Platform TCP Socket Echo System
===============================================================

A cross-platform TCP socket server that echoes all received data with timestamps.
Works identically on Windows, Linux, and macOS for inter-process communication
and logging within the MODEL_for_framework ecosystem.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2

CHANGELOG:
- v1.0.0: Initial release with multi-client TCP socket support
- Added timestamped logging, graceful shutdown, and error handling
- Cross-platform compatibility with pure Python stdlib
"""

import socket
import threading
import logging
import signal
import sys
import argparse
from datetime import datetime
import os

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('framework_echo_server.log', mode='a')
    ]
)

class FrameworkEchoServer:
    """
    Cross-platform TCP socket echo server for the MODEL_for_framework.

    Features:
    - Multi-client support with threading
    - Real-time echoing with timestamps
    - Graceful shutdown handling
    - Configurable host and port
    - Comprehensive error handling
    """

    def __init__(self, host='localhost', port=8888, max_clients=10):
        """
        Initialize the echo server.

        Args:
            host (str): Host to bind to (default: localhost)
            port (int): Port to listen on (default: 8888)
            max_clients (int): Maximum concurrent clients (default: 10)
        """
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.server_socket = None
        self.running = False
        self.client_threads = []
        self.lock = threading.Lock()

        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        logging.info(f"Framework Echo Server v{__version__} initialized")
        logging.info(f"Configuration: {host}:{port}, max_clients={max_clients}")

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        logging.info(f"Received signal {signum}, initiating shutdown...")
        self.shutdown()

    def start_server(self):
        """Start the TCP echo server."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(self.max_clients)
            self.running = True

            logging.info(f"Framework Echo Server listening on {self.host}:{self.port}")
            print(f"🚀 Framework Echo Server v{__version__} started!")
            print(f"📡 Listening on {self.host}:{self.port}")
            print(f"👥 Max clients: {self.max_clients}")
            print(f"🛑 Press Ctrl+C to stop")
            print("=" * 50)

            while self.running:
                try:
                    client_socket, client_address = self.server_socket.accept()
                    client_thread = threading.Thread(
                        target=self._handle_client,
                        args=(client_socket, client_address),
                        daemon=True
                    )
                    client_thread.start()

                    with self.lock:
                        self.client_threads.append(client_thread)
                        # Clean up finished threads
                        self.client_threads = [t for t in self.client_threads if t.is_alive()]

                except OSError:
                    # Socket was closed during shutdown
                    break
                except Exception as e:
                    if self.running:  # Only log if not shutting down
                        logging.error(f"Error accepting client connection: {e}")

        except Exception as e:
            logging.error(f"Failed to start server: {e}")
            raise
        finally:
            self.shutdown()

    def _handle_client(self, client_socket, client_address):
        """
        Handle individual client connections.

        Args:
            client_socket: Client socket object
            client_address: Client address tuple (host, port)
        """
        client_info = f"{client_address[0]}:{client_address[1]}"
        logging.info(f"New client connected: {client_info}")

        try:
            while self.running:
                data = client_socket.recv(4096)
                if not data:
                    # Client disconnected
                    break

                # Decode and process the message
                try:
                    message = data.decode('utf-8').strip()
                    if message:  # Only process non-empty messages
                        self._log_message(message, client_info)
                except UnicodeDecodeError:
                    # Handle binary data or encoding issues
                    self._log_message(f"[BINARY DATA: {len(data)} bytes]", client_info)

        except ConnectionResetError:
            logging.info(f"Client {client_info} disconnected abruptly")
        except Exception as e:
            logging.error(f"Error handling client {client_info}: {e}")
        finally:
            client_socket.close()
            logging.info(f"Client {client_info} disconnected")

    def _log_message(self, message, client_info):
        """
        Log received messages with timestamps and client info.

        Args:
            message (str): The message to log
            client_info (str): Client identification string
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        # Console output with colors/formatting
        console_message = f"[{timestamp}] [{client_info}] {message}"
        print(console_message)

        # File logging
        logging.info(f"ECHO | {client_info} | {message}")

    def shutdown(self):
        """Gracefully shutdown the server."""
        if not self.running:
            return

        logging.info("Initiating server shutdown...")
        self.running = False

        # Close server socket
        if self.server_socket:
            try:
                self.server_socket.close()
            except Exception as e:
                logging.error(f"Error closing server socket: {e}")

        # Wait for client threads to finish
        with self.lock:
            for thread in self.client_threads:
                if thread.is_alive():
                    thread.join(timeout=1.0)

        logging.info("Framework Echo Server shutdown complete")
        print("\n🛑 Framework Echo Server stopped.")


def main():
    """Main entry point for the echo server."""
    parser = argparse.ArgumentParser(
        description="Framework Echo Server - Cross-platform TCP socket echo system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python socket_echo_server.py                    # Start on localhost:8888
  python socket_echo_server.py --port 9999       # Custom port
  python socket_echo_server.py --host 0.0.0.0    # Listen on all interfaces

Testing:
  echo "Hello Framework!" | nc localhost 8888     # Linux/macOS
  "Hello Framework!" | nc.exe localhost 8888      # Windows PowerShell
        """
    )

    parser.add_argument(
        '--host',
        default='localhost',
        help='Host to bind to (default: localhost)'
    )

    parser.add_argument(
        '--port',
        type=int,
        default=8888,
        help='Port to listen on (default: 8888)'
    )

    parser.add_argument(
        '--max-clients',
        type=int,
        default=10,
        help='Maximum concurrent clients (default: 10)'
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'Framework Echo Server v{__version__}'
    )

    args = parser.parse_args()

    # Validate arguments
    if not (1 <= args.port <= 65535):
        parser.error("Port must be between 1 and 65535")

    if args.max_clients < 1:
        parser.error("Max clients must be at least 1")

    # Create and start server
    server = FrameworkEchoServer(
        host=args.host,
        port=args.port,
        max_clients=args.max_clients
    )

    try:
        server.start_server()
    except KeyboardInterrupt:
        pass  # Handled by signal handler
    except Exception as e:
        logging.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
