alphabet = list("abcdefghijklmnopqrstuvwxyzæøå")


def decrypt(ciphertext: str, offset: int) -> str:
    """Decrypts a ciphertext using a Caesar cipher.

    Args:
        ciphertext: The ciphertext to decrypt.
        offset: The offset to use for decryption.

    Returns:
        The decrypted ciphertext.
    """
    if offset < 0 or offset > len(alphabet):
        raise ValueError(f"Invalid offset: {offset}")

    plaintext = ""
    for c in ciphertext:
        if c.isnumeric():
            plaintext += str((int(c) - offset) % 10)
        elif c.isalpha():
            position = alphabet.index(c.lower())
            new_position = (position - offset) % len(alphabet)
            if c.isupper():
                plaintext += alphabet[new_position].upper()
            else:
                plaintext += alphabet[new_position]
        else:
            plaintext += c
    return plaintext


def encrypt(plaintext: str, offset: int) -> str:
    """Encrypts a plaintext using a Caesar cipher.

    Args:
        plaintext: The plaintext to encrypt.
        offset: The offset to use for encryption.

    Returns:
        The encrypted plaintext.
    """
    if offset < 0 or offset > len(alphabet):
        raise ValueError(f"Invalid offset: {offset}")

    ciphertext = ""
    for c in plaintext:
        if c.isnumeric():
            ciphertext += str((int(c) + offset) % 10)
        elif c.isalpha():
            position = alphabet.index(c.lower())
            new_position = (position + offset) % len(alphabet)
            if c.isupper():
                ciphertext += alphabet[new_position].upper()
            else:
                ciphertext += alphabet[new_position]
        else:
            ciphertext += c
    return ciphertext


if __name__ == "__main__":
    print("hei")
    foo = "abc ABC æøå ÆØÅ 01 89"
    print(f"foo: {foo}")
    print(f"encrypted: {encrypt(foo, 3)}")
    print(f"decrypted: {decrypt(encrypt(foo, 3), 3)}")
