from ciphers.defaults import CIPHER_OPTIONS
import streamlit as st

st.header("Streamlit Decipher Demo")
option = st.sidebar.radio(label="Cipher Options", options=list(CIPHER_OPTIONS.keys()))
cipher = CIPHER_OPTIONS[option]
ciphertext = st.text_area(label="Provide encrypted input", value=cipher["example"])
key = None
if cipher["requires_key"]:
    key = st.sidebar.number_input(label="Provide Key", value=cipher["key"])
    if st.button("Decipher"):
        plaintext = cipher["fn"](ciphertext, key)
        st.write("### Plaintext:", plaintext)
else:
    if st.button("Decipher"):
        plaintext = cipher["fn"](ciphertext)
        st.write("### Plaintext:", plaintext)
