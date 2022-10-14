import unittest


class TestCaesar(unittest.TestCase):
    """
    Test the encryption and decryption functions.
    """

    examples = [
        ("abc123", "bcd234", 1),
        ("A B C", "D E F", 3),
        ("æøå 123", "æøå 123", 0),
        ("ÆØÅ 123", "BCD 567", 4),
        ("abc123", "xyz456", 23),
        ("#¤%&/()=", "#¤%&/()=", 7),
    ]

    def test_encryption(self):
        for plaintext, ciphertext, offset in self.examples:
            print(f"{plaintext} -> {ciphertext} (offset: {offset})")
            self.assertEqual(ciphertext, encrypt(plaintext, offset))

    def test_decryption(self):
        for plaintext, ciphertext, offset in self.examples:
            print(f"{ciphertext} -> {plaintext} (offset: {offset})")
            self.assertEqual(plaintext, decrypt(ciphertext, offset))

    def test_reflexivity(self):
        for plaintext, _, offset in self.examples:
            self.assertEqual(plaintext, decrypt(encrypt(plaintext, offset), offset))

    def test_encrypt_raises_error(self):
        with self.assertRaises(ValueError):
            encrypt("abc", 30)

        with self.assertRaises(ValueError):
            encrypt("abc", -1)

    def test_decrypt_raises_error(self):
        with self.assertRaises(ValueError):
            decrypt("abc", 30)

        with self.assertRaises(ValueError):
            decrypt("abc", -1)


if __name__ == "__main__":
    unittest.main()
