import click

alphabet = list("abcdefghijklmnopqrstuvwxyzæøå")


def offset_text(text: str, offset: int) -> str:
    """Offset each character by a given offset.

    Args:
        text: The text to offset.
        offset: The offset to use.

    Returns:
        The offset text.
    """
    if abs(offset) > len(alphabet):
        raise ValueError(f"Invalid offset: {offset}")

    if type(text) is not str:
        raise ValueError("Invalid text supplied")

    offset_text = ""
    for c in text:
        if c.isnumeric():
            offset_text += str((int(c) + offset) % 10)
        elif c.isalpha():
            position = alphabet.index(c.lower())
            new_position = (position + offset) % len(alphabet)
            if c.isupper():
                offset_text += alphabet[new_position].upper()
            else:
                offset_text += alphabet[new_position]
        else:
            offset_text += c
    return offset_text


def decrypt(ciphertext: str, offset: int) -> str:
    """Decrypts a ciphertext using a Caesar cipher.

    Args:
        ciphertext: The ciphertext to decrypt.
        offset: The offset to use for decryption.

    Returns:
        The decrypted ciphertext.
    """
    return offset_text(ciphertext, -offset)


def encrypt(plaintext: str, offset: int) -> str:
    """Encrypts a plaintext using a Caesar cipher.

    Args:
        plaintext: The plaintext to encrypt.
        offset: The offset to use for encryption.

    Returns:
        The encrypted plaintext.
    """
    return offset_text(plaintext, offset)


@click.command()
@click.argument(
    "input_file",
    type=click.File("r"),
)
@click.option("-t", "--target", type=str, help="The target file to write to.")
@click.option(
    "-e",
    "--encrypt",
    "action",
    flag_value="encrypt",
    default=True,
    help="Encrypt the input.",
)
@click.option(
    "-d", "--decrypt", "action", flag_value="decrypt", help="Decrypt the input."
)
@click.option(
    "-o",
    "--offset",
    type=int,
    default=1,
    help="The offset to use for encryption/decryption.",
)
@click.option(
    "--enc",
    type=str,
    default="utf-8",
    help="The encoding to use for the input/output file (defaults to UTF-8).",
)
@click.option("-v", "--verbose", is_flag=True, help="Print arguments and results.")
def caesar(
    action: str,
    offset: int,
    input_file: click.File,
    target: str,
    enc: str,
    verbose: bool,
):
    """
    Encrypt or decrypt a file using a Caesar cipher.
    If no output file is specified, the results are printed to the terminal.
    """

    if verbose:
        print(f"{action=} | {offset=} | encoding={enc}")
        print(f"Reading from file: {input_file.name}")

    with open(input_file.name, "r", encoding=enc) as f:
        input_text = f.read()

    if action == "encrypt":
        result = encrypt(input_text, offset)
    elif action == "decrypt":
        result = decrypt(input_text, offset)
    else:
        raise ValueError(f"Invalid action: {action}")

    if verbose:
        print(f"Output: {result}")

    if target:
        if verbose:
            print(f"Writing to file: {target}")
        with open(target, "w", encoding=enc) as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    caesar()
