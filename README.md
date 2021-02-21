# Welcome to Decipher :wave:

**A Streamlit Webapp demonstrating deciphering algorithms.**

The webapp allows the user to input a string encrypted using one of the two algorithms, namely Atbash and Caeser and decrypts them to plaintext. The app is only for educational purposes.

## How to run:

### Set up Local Environment

```python
  # Create virtual environment
  virtualenv venv

  # Activate environment
  source venv/bin/activate

  # Install dependencies
  pip install -r requirements.txt
```

### Run the Streamlit app

```python
streamlit run webapp.py

# App launching on port 8051...
```

## Add new algorithms

You can add a new deciphering algorithm in <i>ciphers.algo</i> and then add a configuration in ciphers.defaults as follows:

```python
CIPHER_OPTIONS = {
    "YourAlgo": {
        #This example will appear on screen as default
        "example": "Sld wl blf hloev zmb vjfzgrlm?",
        "requires_key": True,
        "key" : yourKey,
        "fn": yourAlgoFunction,
    },
}
```

## License

Licensed under the [GNU General Public License v3.0](https://github.com/tanmaylaud/decipher/blob/main/LICENSE)
