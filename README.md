# Description

Solution for a task to create a program for encryption and decryption using a Caesar cipher.
This uses a non-standard solution (i.e. not just modulo and `ord(char)`) in order to handle Norwegian characters.

Limitations:

- This only handles numbers and the Norwegian alphabet.
- Special characters, such as whitespace or &"#%, are not mutated.

# Setup

Recommended method for setting up project:

```bash
# Set up virtual environment
python -m venv venv

# Activate virtual environment (depends on OS/IDE)
source venv/bin/activate # Linux
./venv/Scripts/activate # Windows

# Install dependencies
pip install -r requirements.txt
```

# Usage

```bash
# Get a list of options
python caesar.py --help

# Encrypt a file
python caesar.py input.txt -t output.txt -e -o 7

# Decrypt a file
python caesar.py input.txt -d -o 7
```
