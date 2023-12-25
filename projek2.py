import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

def set_custom_style():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9; /* Warna latar belakang */
            color: #333333; /* Warna teks utama */
            margin: 0;
            padding: 0;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }
        .title {
            color: #2e4057; /* Warna judul */
            text-align: center;
            margin-bottom: 20px;
            font-size: 36px; /* Ukuran judul */
        }
        .btn {
            display: block;
            width: 120px;
            margin: 0 auto;
            margin-top: 20px;
            padding: 12px;
            text-align: center;
            background-color: #4CAF50; /* Warna tombol */
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #45a049; /* Warna tombol saat hover */
        }
        .sidebar .sidebar-content {
            background-color: #f4f4f4; /* Warna sidebar */
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def highlight_keyword(text, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    split_text = pattern.split(text)
    highlighted_text = pattern.sub(lambda match: f"**{match.group()}**", text)
    return highlighted_text

def main():
    set_custom_style()
    st.title("Selamat Datang di Aplikasi sdg label")
    st.markdown("---")
    st.markdown("### Pilih salah satu opsi di bawah ini:")

    # Pilihan untuk memasukkan teks atau file PDF
    upload_option = st.radio("", ("Masukkan Teks", "Unggah File PDF"))

    if upload_option == "Masukkan Teks":
        text_input = st.text_area("Masukkan Teks Panjang", value="")  # Empty text area
        uploaded_file = None
    else:
        uploaded_file = st.file_uploader("Unggah File PDF", type="pdf")
        text_input = None

    if st.button("Kirim"):
        if text_input:
            st.success(f"Anda memasukkan teks panjang berikut:\n{text_input}")
            keyword_to_search = "health"  
            highlighted_text = highlight_keyword(text_input, keyword_to_search)
            st.markdown(f"### Bagian yang berkaitan dengan '{text_input}':")
            st.markdown(highlighted_text)
        elif uploaded_file is not None:
            st.success("Anda telah mengunggah file PDF.")
            # Operasi dengan file PDF
        else:
            st.warning("Harap lengkapi input.")

    # Menampilkan pesan jika pengguna memilih 'Unggah File PDF' tetapi tidak mengunggah file
    if uploaded_file is None and upload_option == "Unggah File PDF":
        st.warning("Anda belum mengunggah file PDF. Silakan unggah file PDF untuk melanjutkan.")
        st.text_area("Masukkan Teks Panjang", "")  # Kotak teks kosong

    st.sidebar.title("Hal yang Sering Dicari")
    st.sidebar.markdown("- Contoh 1")
    st.sidebar.markdown("- Contoh 2")
    st.sidebar.markdown("- Contoh 3")

    st.header("Performa Model (Line Plot)")

    data = {
        'Epoch': np.arange(1, 11),
        'Loss': np.random.uniform(0.1, 0.5, 10),
        'Accuracy': np.random.uniform(0.6, 0.9, 10)
    }
    df = pd.DataFrame(data)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss', color=color)
    ax1.plot(df['Epoch'], df['Loss'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Accuracy', color=color)  
    ax2.plot(df['Epoch'], df['Accuracy'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    st.pyplot(fig)

if __name__ == "__main__":
    main()
