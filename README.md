# AI Password & Entropy Security Engine

An advanced Python-based password generator and security analysis tool. This project generates cryptographically secure passwords and evaluates password strength using pattern entropy analysis and natural language feedback rules.

## Features
- **Cryptographically Secure:** Uses Python's `secrets` module rather than standard random generators.
- **Customizable Rules:** Control length, uppercase, lowercase, numbers, and special symbols.
- **AI/Entropy Strength Estimator:** Calculates Shannon entropy bits and provides human-readable security ratings.
- **Phonetic & Passphrase Mode:** Generate pronounceable passwords or multi-word passphrases.

## Usage
```bash
pip install -r requirements.txt
python app.py
