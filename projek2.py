import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def set_custom_style():
    # Mengatur tampilan CSS
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
        /* Tambahkan gaya tambahan di sini sesuai kebutuhan */
        </style>
        """,
        unsafe_allow_html=True,
    )

def show_bar_plot(dataframe):
    # Fungsi untuk menampilkan barplot jumlah SDGs yang banyak dicari
    st.subheader("Barplot Jumlah SDGs yang Banyak Dicari")
    st.markdown("Grafik ini menunjukkan jumlah SDGs yang banyak dicari dalam DataFrame.")
    
    sdg_counts = dataframe['SDG'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sdg_counts.index, y=sdg_counts.values)
    plt.xlabel('SDG')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    st.pyplot()

def main():
    set_custom_style()
    st.title("Selamat Datang di Aplikasi sdg label")
    st.markdown("---")

    page = st.sidebar.radio("Pilih Halaman:", ("Labelling", "Tren"))

    if page == "Labelling":
        st.title("Halaman Labelling")
        st.markdown("### Pilih salah satu opsi di bawah ini:")

        upload_option = st.radio("", ("Masukkan Teks", "Unggah File Excel atau CSV"))

        if upload_option == "Masukkan Teks":
            text_input = st.text_area("Masukkan Teks Panjang", value="", key="text_input_area")
            uploaded_file = None

            # Validasi panjang teks yang dimasukkan
            if text_input.strip():  
                word_count = len(text_input.split())
            else:
                word_count = 0

            if word_count < 50:  # Periksa jumlah kata
                st.warning("Mohon masukkan minimal 50 kata untuk melanjutkan.")
                st.text("Jumlah kata yang dimasukkan: " + str(word_count))
                st.text("Tombol 'Kirim' akan aktif setelah memasukkan minimal 50 kata.")
                st.button("Kirim", disabled=True)
            else:
                st.button("Kirim")

                # Simpan teks dalam DataFrame
                df = pd.DataFrame({'Text': [text_input]})
                # Lakukan operasi untuk menentukan label SDGs berdasarkan DataFrame
                # sdg_label_text = Fungsi_untuk_menentukan_label_SDG(df)

        else:
            uploaded_file = st.file_uploader("Unggah File Excel atau CSV (satu kolom)", type=["csv", "xlsx"])
            text_input = None

            if uploaded_file is not None:
                try:
                    # Baca file CSV atau Excel
                    if uploaded_file.type == 'application/vnd.ms-excel':
                        df = pd.read_csv(uploaded_file)
                    else:
                        df = pd.read_excel(uploaded_file)

                    st.success("Anda telah berhasil mengunggah file.")
                    if len(df.columns) == 1:
                        st.write(df)  # Tampilkan konten file yang diunggah
                        # Lakukan operasi untuk menentukan label SDGs berdasarkan file CSV atau Excel
                        # sdg_label_text = Fungsi_untuk_menentukan_label_SDG(df)
                    else:
                        st.warning("Mohon unggah file dengan hanya satu kolom data.")

                    st.markdown("*Catatan: Pastikan file yang diunggah hanya memiliki satu kolom data untuk hasil yang akurat.*")

                except Exception as e:
                    st.warning(f"Terjadi kesalahan dalam membaca file. Pesan kesalahan: {str(e)}")

    elif page == "Tren":
        st.title("Halaman Tren")
        st.markdown("### Analisis Tren SDGs")

        # Ambil data dari file atau sumber lain
        # Misalnya, Anda telah memiliki DataFrame df yang berisi data dari file yang diunggah

        # Tampilkan barplot jumlah SDGs yang banyak dicari
        if 'SDG' in df.columns:  # Pastikan kolom SDG ada dalam DataFrame
            show_bar_plot(df)
        else:
            st.warning("Kolom 'SDG' tidak ditemukan dalam DataFrame.")

if __name__ == "__main__":
    main()
