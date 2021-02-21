"""App Component passed to streamlit via run command"""
import streamlit as st
from ciphers.defaults import CIPHER_OPTIONS

# Add a Header to the app
st.header("Streamlit Decipher Demo")
# Provide some basic steps
st.write("""### Provide your encrypted text input and press Decipher""")
# Select a cipher from options
option = st.sidebar.selectbox(
    label="Cipher Options", options=list(CIPHER_OPTIONS.keys())
)

cipher = CIPHER_OPTIONS[option]
# Take the encrypted text as input
ciphertext = st.text_input(label="Encrypted input", value=cipher["example"])
# If cipher requires key, then provide it
if cipher["requires_key"]:
    key = st.sidebar.number_input(label="Provide Key", value=cipher["key"])
    if st.button("Decipher"):
        plaintext = cipher["fn"](ciphertext, key)
        st.write("### Plaintext:", plaintext)
# Else compute decryption without key
elif st.button("Decipher"):
    plaintext = cipher["fn"](ciphertext)
    st.write("### Plaintext:", plaintext)

st.sidebar.markdown(
    """To learn more about ciphers: \n
[Atbash](http://practicalcryptography.com/ciphers/atbash-cipher-cipher/) \n
[Caeser](http://practicalcryptography.com/ciphers/caesar-cipher/)
"""
)
