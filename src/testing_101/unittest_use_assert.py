import unittest


class TestUseAssert(unittest.TestCase):
    def test_use_assert(self):
        assert 1 + 2 == 4

    def test_use_assertEqual(self):
        self.assertEqual(1 + 2, 4)


if __name__ == "__main__":
    unittest.main()
