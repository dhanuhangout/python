"""Pytest module to test chat client."""
import unittest
import os, sys
import SocketServer

C_DIR = os.getcwd()
SRC_DIR = '%s/../src/' % C_DIR

sys.path.append(SRC_DIR)
from client import ChatClient as CliObj
from server import ChatServer as ServObj
from server import RequestHandler as ReqHandler


class TestChatClient(unittest.TestCase):
    """Test module to test chat client."""

    @staticmethod
    def setup(self):
        """Setup Class."""
        print "\nsetup class:%s" % cls.__name__

    def test_names_command(self):
        """Test names command."""
        print "\ntest_names_command <====================== actual test code"
        self.ServObj = ServObj(('127.0.0.1', 8001), ReqHandler).serve_forever()
        self.CliObj = CliObj(host='127.0.0.1', port=8001, nickname='customer')
        self.CliObj.output.write('/names\r\n')
        '''readline = self.CliObj.input.readline().strip()
        print readline
        self.assertIn('customer', readline)'''


if __name__ == '__main__':
	unittest.main()