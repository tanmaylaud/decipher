from ciphers.algo import caeser, atbash
import unittest


class TestDecipherMethods(unittest.TestCase):
    def test_algos(self):
        self.assertEqual(
            atbash("Sld wl blf hloev zmb vjfzgrlm?"), "How do you solve any equation?"
        )
        self.assertEqual(
            caeser("Zhygvcyl obgu fvqrf ol mreb.", 13), "Multiply both sides by zero."
        )


if __name__ == "__main__":
    unittest.main()