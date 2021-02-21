from ciphers.algo import caeser, atbash
import unittest


class TestDecipherMethods(unittest.TestCase):
    def test_algos(self):
        # Basic algo should work for English alphabet
        self.assertEqual(
            atbash("Sld wl blf hloev zmb vjfzgrlm?"), "How do you solve any equation?"
        )
        self.assertEqual(
            caeser("Zhygvcyl obgu fvqrf ol mreb.", 13), "Multiply both sides by zero."
        )

    def test_bad_inputs(self):
        # Key cannot be None for Caeser cipher
        self.assertRaises(ValueError, caeser, "Some input", key=None)

    def test_empty_input(self):
        # Empty input should return as is
        self.assertEqual(atbash(""), "")
        self.assertEqual(caeser("", 1), "")

    def test_garbage_input(self):
        # Any input other than English alphabet should return as is
        self.assertEqual(
            atbash("!@##&%%()^$^)(*+_+(*#*@&|92049220-2940"),
            "!@##&%%()^$^)(*+_+(*#*@&|92049220-2940",
        )
        self.assertEqual(
            caeser("!@##&%%()^$^)(*+_+(*#*@&|92049220-2940", 1),
            "!@##&%%()^$^)(*+_+(*#*@&|92049220-2940",
        )


if __name__ == "__main__":
    unittest.main()