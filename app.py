import streamlit as st

def hitung_luas(p, l):
    return p * l

with st.form("luas"):
    panjang = st.text_input("Panjang:")
    lebar = st.text_input("Lebar:")
    if st.form_submit_button("Hitung Luas"):
        st.write(f"Hasil: {hitung_luas}")