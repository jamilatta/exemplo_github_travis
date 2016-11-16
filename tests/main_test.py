import unittest

from github_travis.main import soma

class TestSomaFunction(unittest.TestCase):

    def test_sum_a_b(self):
        a = 5
        b = 10

        self.assertEqual(soma(5, 10), 15)

if __name__ == '__main__':
    unittest.main()