import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from PIL import Image
import requests
from io import BytesIO


def set_custom_style():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4; /* Warna latar belakang */
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
            background-color: #008080; /* Warna tombol */
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #006666; /* Warna tombol saat hover */
        }
        .sidebar .sidebar-content {
            background-color: #dcdcdc; /* Warna sidebar */
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    set_custom_style()
    st.title("Selamat Datang di Aplikasi sdg label")
    st.markdown("---")
    st.markdown("### Pilih salah satu opsi di bawah ini:")

    upload_option = st.radio("", ("Masukkan Teks", "Unggah File PDF"))

    if upload_option == "Masukkan Teks":
        text_input = st.text_area("Masukkan Teks Panjang", value="")
        uploaded_file = None
    else:
        uploaded_file = st.file_uploader("Unggah File PDF", type="pdf")
        text_input = None

    if st.button("Kirim"):
        if text_input:
            st.success(f"Anda memasukkan teks panjang berikut:\n{text_input}")
            display_performance_plot()
            st.write("Penjelasan tentang performa model")
        elif uploaded_file is not None:
            st.success("Anda telah mengunggah file PDF.")
            display_performance_plot()
            st.write("Penjelasan tentang performa model")
        else:
            st.warning("Harap lengkapi input.")

    if uploaded_file is None and upload_option == "Unggah File PDF":
        st.warning("Anda belum mengunggah file PDF. Silakan unggah file PDF untuk melanjutkan.")
        st.text_area("Masukkan Teks Panjang", "") 

    st.sidebar.title("Hal yang Sering Dicari")

    # Dummy DataFrame
    data = {
        'Column1': ['Value1', 'Value2', 'Value3', 'Value4', 'Value5'],
        'Column2': ['ValueA', 'ValueB', 'ValueC', 'ValueD', 'ValueE']
    }
    df = pd.DataFrame(data)

    if df is not None:
        for column in df.columns:
            st.sidebar.markdown(f"#### {column}")
            for value in df[column].value_counts().head().index.tolist():
                st.sidebar.markdown(f"- {value}")
    st.title("17 SDGS")

    # List URL gambar dari berbagai sumber
    image_urls = [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/160",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170",
        "https://via.placeholder.com/170"
        # URL gambar dari sumber lainnya
    ]
    images = []  # Simpan semua gambar dalam list ini

    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                image = Image.open(BytesIO(response.content))
                images.append(image)
            except Exception as e:
                st.warning(f"Gagal membuka gambar dari {url}: {e}")
        else:
            st.warning(f"Gagal mengambil gambar dari {url}")

    col1, col2, col3, col4 = st.columns(4)

    for i, image in enumerate(images):
        col = col1 if i < 4 else col2 if i < 8 else col3 if i < 12 else col4
        caption = f"Gambar {i+1}"
        
        # Gunakan expander untuk menampilkan penjelasan saat gambar diklik
        with col:
            expander = st.expander(caption, expanded=False)
            expander.image(image, use_column_width=True)
            expander.write(f"Penjelasan tentang {caption}")  # Ganti dengan penjelasan sesuai dengan gambar yang diklik

def display_performance_plot():
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
