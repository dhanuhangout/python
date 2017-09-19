"""Pytest module to test chat server."""
import os, sys

C_DIR = os.getcwd()
SRC_DIR = '%s/src/' % C_DIR

sys.path.append(SRC_DIR)
from client import ChatServer as ServObj


class TestChatServer(object):
    """Test module to test chat server."""

    @classmethod
    def setup_class(cls):
        """Setup Class."""
        print "\nsetup_class class:%s" % cls.__name__
        cls.ServObj('127.0.0.1', 8001)

    def test_bubble_sort(self):
        """Test Bubble Sort."""
        print "\ntest_bubble_sort <====================== actual test code"
        list_obj = [5, 3, 4, 1, 2]
        assert SortObj.bubble_sort(list_obj) == [1, 2, 3, 4, 5]
