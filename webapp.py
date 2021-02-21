"""App Component passed to streamlit via run command"""
import streamlit as st
from ciphers.defaults import CIPHER_OPTIONS


st.header("Streamlit Decipher Demo")

st.write("""### Provide your encrypted text input and press Decipher""")

option = st.sidebar.selectbox(
    label="Cipher Options", options=list(CIPHER_OPTIONS.keys())
)

cipher = CIPHER_OPTIONS[option]

ciphertext = st.text_input(label="Encrypted input", value=cipher["example"])

if cipher["requires_key"]:
    key = st.sidebar.number_input(label="Provide Key", value=cipher["key"])
    if st.button("Decipher"):
        plaintext = cipher["fn"](ciphertext, key)
        st.write("### Plaintext:", plaintext)
else:
    if st.button("Decipher"):
        plaintext = cipher["fn"](ciphertext)
        st.write("### Plaintext:", plaintext)

st.sidebar.markdown(
    """To learn more about ciphers: \n
[Atbash](http://practicalcryptography.com/ciphers/atbash-cipher-cipher/) \n
[Caeser](http://practicalcryptography.com/ciphers/caesar-cipher/)
"""
)
