import unittest

from .adventure import CommandExecutor, GameOverException


class CommandTest(unittest.TestCase):
    def setUp(self):
        self.executor = CommandExecutor()

    def test_quit_raises_GameOverException(self):
        with self.assertRaises(GameOverException):
            self.executor.execure("quit")
