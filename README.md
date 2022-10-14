# Description

Solution for a task to create a program for encryption and decryption using a Caesar cipher.
This uses a non-standard solution (i.e. not just modulo and `ord(char)`) in order to handle Norwegian characters, which are not in the same position as A-Z.

Limitations:

- This only handles numbers, A-Z and ÆØÅ.
- Special characters, such as spaces, are not mutated.

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
python caesar.py --help
```
