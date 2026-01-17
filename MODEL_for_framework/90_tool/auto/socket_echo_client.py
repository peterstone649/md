#!/usr/bin/env python3
"""
Framework Echo Client - Test Client for TCP Socket Echo Server
===============================================================

A simple TCP client for testing the Framework Echo Server.
Sends messages to the echo server and displays responses.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import socket
import sys
import argparse
from datetime import datetime

__version__ = "1.0.0"
__status__ = "ACTIVE"

class FrameworkEchoClient:
    """
    Simple TCP client for testing the Framework Echo Server.
    """

    def __init__(self, host='localhost', port=8888, timeout=5.0):
        """
        Initialize the echo client.

        Args:
            host (str): Server host (default: localhost)
            port (int): Server port (default: 8888)
            timeout (float): Connection timeout in seconds
        """
        self.host = host
        self.port = port
        self.timeout = timeout

    def send_message(self, message):
        """
        Send a message to the echo server.

        Args:
            message (str): Message to send

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create socket and connect
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(self.timeout)
            client_socket.connect((self.host, self.port))

            # Send message
            client_socket.send(message.encode('utf-8'))

            # Close connection immediately (fire and forget)
            client_socket.close()

            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"[{timestamp}] 📤 Message sent: {message}")
            return True

        except socket.timeout:
            print(f"❌ Connection timeout after {self.timeout} seconds")
            return False
        except ConnectionRefusedError:
            print(f"❌ Connection refused. Is the server running on {self.host}:{self.port}?")
            return False
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return False

    def send_from_stdin(self):
        """
        Read messages from stdin and send them to the server.
        """
        print("📝 Reading from stdin. Press Ctrl+D (Unix) or Ctrl+Z+Enter (Windows) to end.")
        try:
            for line in sys.stdin:
                message = line.strip()
                if message:  # Skip empty lines
                    self.send_message(message)
        except KeyboardInterrupt:
            print("\n🛑 Stopped reading from stdin.")
        except Exception as e:
            print(f"❌ Error reading from stdin: {e}")

def main():
    """Main entry point for the echo client."""
    parser = argparse.ArgumentParser(
        description="Framework Echo Client - Test client for TCP socket echo server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python socket_echo_client.py "Hello Framework!"          # Send single message
  python socket_echo_client.py --port 9999 "Test message"  # Custom port
  echo "Message" | python socket_echo_client.py            # From stdin
  python socket_echo_client.py --stdin                     # Interactive stdin mode

Server must be running first:
  python socket_echo_server.py
        """
    )

    parser.add_argument(
        'message',
        nargs='?',
        help='Message to send (if not using --stdin)'
    )

    parser.add_argument(
        '--host',
        default='localhost',
        help='Server host (default: localhost)'
    )

    parser.add_argument(
        '--port',
        type=int,
        default=8888,
        help='Server port (default: 8888)'
    )

    parser.add_argument(
        '--stdin',
        action='store_true',
        help='Read messages from stdin instead of command line'
    )

    parser.add_argument(
        '--timeout',
        type=float,
        default=5.0,
        help='Connection timeout in seconds (default: 5.0)'
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'Framework Echo Client v{__version__}'
    )

    args = parser.parse_args()

    # Validate arguments
    if not (1 <= args.port <= 65535):
        parser.error("Port must be between 1 and 65535")

    if args.timeout <= 0:
        parser.error("Timeout must be positive")

    # Create client
    client = FrameworkEchoClient(
        host=args.host,
        port=args.port,
        timeout=args.timeout
    )

    if args.stdin:
        # Read from stdin
        client.send_from_stdin()
    elif args.message:
        # Send single message
        success = client.send_message(args.message)
        sys.exit(0 if success else 1)
    else:
        parser.error("Must provide either a message or use --stdin")

if __name__ == "__main__":
    main()
