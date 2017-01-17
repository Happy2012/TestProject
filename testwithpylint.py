import unittest, database
from subprocess import Popen, PIPE
class ProductTestCase(unittest.TestCase):
    def testWithPyLint(self):
        cmd = 'pylint', '-rn', 'database'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')

if __name__ == '__main__':
    unittest.main()


