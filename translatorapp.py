import streamlit as st
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    st.title("Simple Translator App")

    # Masukan teks yang ingin diterjemahkan
    input_text = st.text_area("Enter Text to Translate", "")

    # Pilihan bahasa sumber dan tujuan
    source_language = st.selectbox("Select Source Language", ["auto", "en", "es", "fr", "id", "ja", "ko", "zh-CN"])
    target_language = st.selectbox("Select Target Language", ["en", "es", "fr", "id", "ja", "ko", "zh-CN"])

    # Tombol untuk menerjemahkan teks
    if st.button("Translate"):
        try:
            translated_text = translate_text(input_text, target_language)
            st.success(f"Translated Text: {translated_text}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
