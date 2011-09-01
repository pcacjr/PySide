import unittest
from PySide.QtCore import *

class MyIODevice (QIODevice):
    def readData(self, amount):
        return "\0a" * (amount/2)

    def atEnd(self):
        return False

class TestBug944 (unittest.TestCase):

    def testIt(self):
        device = MyIODevice()
        device.open(QIODevice.ReadOnly)
        s = QTextStream(device)
        self.assertEqual(s.read(4), "\0a\0a")

if __name__ == "__main__":
    unittest.main()