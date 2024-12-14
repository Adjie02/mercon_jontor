import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Kelompok Mercon Jontor")

st.write("# Tugas Kelompok Mercon Jontor")

st.write("## Pendahuluan")
st.write("Sejak berlakunya Undang-Undang RI Nomor 23 Tahun 2014 tentang Pemerintahan Daerah, Indonesia menerapkan otonomi daerah yang memberikan keleluasaan bagi daerah untuk mengelola potensi lokal sebagai sumber pendapatan. Kebijakan ini bertujuan meningkatkan kesejahteraan masyarakat dan mengurangi ketimpangan antarwilayah. Pendapatan utama daerah berasal dari Pendapatan Asli Daerah (PAD), seperti pajak, retribusi, dan hasil pengelolaan kekayaan daerah. Namun, kontribusi PAD di Provinsi Jawa Barat masih rendah, sehingga bergantung pada dana transfer pemerintah pusat untuk pembiayaan pembangunan. Jawa Barat, dengan populasi terbesar di Indonesia mencapai 49.935.858   jiwa (BPS, 2020), memiliki potensi besar meningkatkan pendapatannya. Meski demikian, tingginya populasi juga meningkatkan pengeluaran pemerintah untuk pembangunan dan pelayanan publik. Karakteristik kota dan kabupaten di Jawa Barat beragam, mulai dari kota dengan dominasi sektor industri dan perdagangan hingga kabupaten yang bergantung pada sektor pertanian. Analisis pendapatan daerah penting untuk mengidentifikasi potensi dan tantangan fiskal sekaligus memberikan rekomendasi guna mendukung pembangunan berkelanjutan di seluruh wilayah Jawa Barat.")

st.write("## Deskripsi Data")
st.write("Tuliskan di bagian ini deskripsi tentang data yang digunakan.")

st.write("## Visualisasi")
st.write("Buat visualisasi yang menurut kelompok kalian perlu ditampilkan.")
st.write("Gunakan juga elemen-elemen interaktif `streamlit`.")
# Load the data
data_path = "Pend_JawaBarat.xlsx.csv"
data = pd.read_csv(data_path, delimiter=';', skiprows=2)
data = data.rename(columns={"Unnamed: 0": "Kabupaten/Kota"})
data.set_index("Kabupaten/Kota", inplace=True)

# Title
st.title("Visualisasi Pendapatan Kabupaten/Kota di Jawa Barat")

# Sidebar for user selection
selected_cities = st.sidebar.multiselect(
    "Pilih Kabupaten/Kota untuk Visualisasi",
    options=data.index,
    default=data.index[:5]
)

# Filter data based on selection
filtered_data = data.loc[selected_cities]

# Main area: Display line chart
st.subheader("Pendapatan Per Tahun")
fig, ax = plt.subplots()
filtered_data.T.plot(ax=ax)
ax.set_title("Pendapatan Kabupaten/Kota (2016-2019)")
ax.set_ylabel("Pendapatan (Ribu Rupiah)")
ax.set_xlabel("Tahun")
st.pyplot(fig)

# Display data table
st.subheader("Data Tabel")
st.dataframe(filtered_data)

# Judul aplikasi
st.title('Data Statistik BPS')

# Meng-upload file Excel
uploaded_file = st.file_uploader("Pend_Jawabarat.xlsx", type="xlsx")
if uploaded_file is not None:
    # Membaca file Excel dengan pandas
    df_Pend_JawaBarat = pd.read_excel('Pend_JawaBarat.xlsx')
    
    # Menampilkan data
    st.write(df)

    # Menampilkan informasi dataset
    st.write(f"Jumlah baris: {df.shape[0]}")
    st.write(f"Jumlah kolom: {df.shape[1]}")

st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")


<<<<<<< HEAD
#Zahra


#Sukma


#Rendi
n
=======
>>>>>>> 800a206efe8551696ed33b1abb1818d49f4f7f77
