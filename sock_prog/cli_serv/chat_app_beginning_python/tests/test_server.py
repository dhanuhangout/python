"""Pytest module to test chat server."""
import os, sys
import unittest
import SocketServer

from mock import patch

C_DIR = os.getcwd()
SRC_DIR = '%s/../src/' % C_DIR

sys.path.append(SRC_DIR)
from server import RequestHandler as ReqHandlerObj


HOSTNAME = '127.0.0.1'
PORT = 8081


class TestChatServer(unittest.TestCase):
    """Test module to test chat server."""

    def setup(self):
        """Setup Test."""
        server_patch = mock.patch.object(
            SocketServer.ThreadingTCPServer,
            'ThreadingTCPServer',
            autospec=True)
        self._mock_tcpserver = server_patch.start()
        self.addCleanup(server_patch.stop)

    def test_process_input(self):
        """Test process_input."""
        with patch.object(
            ReqHandlerObj,
            'process_input') as mock_process_input:
            ReqHandlerObj.process_input()
            # Validate, the process_input is actually called.
            mock_process_input.assert_called()

    def test_users_command(self):
        """Test users_command."""
        with patch.object(
            ReqHandlerObj,
            'users_command') as mock_process_input:
            ReqHandlerObj.users_command()
            # Validate, the process_input is actually called.
            mock_process_input.assert_called()

    def test_messages_command(self):
        """Test messages_command."""
        with patch.object(
            ReqHandlerObj,
            'messages_command') as mock_process_input:
            ReqHandlerObj.messages_command()
            # Validate, the process_input is actually called.
            mock_process_input.assert_called()

    @patch('server.RequestHandler.quit_command', return_value=True)
    def test_quit_command(self, quit_command):
        """Test quit_command."""
        self.assertEqual(quit_command('quit'), True)


if __name__ == '__main__':
    unittest.main()
