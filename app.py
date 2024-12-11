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


st.write("## Analisis")
st.write("Berdasarkan data yang tersedia, total nilai untuk Provinsi Jawa Barat mengalami tren peningkatan dari tahun 2016 hingga 2019. Pada tahun 2016, total nilai tercatat sebesar 17,042,895,113, dan meningkat signifikan menjadi 19,759,789,101 pada tahun 2019. Peningkatan ini mencerminkan pertumbuhan yang stabil di berbagai kabupaten/kota di Jawa Barat.
Kabupaten/Kota dengan nilai tertinggi selama periode tersebut adalah Kota Bandung dan Kota Bekasi. Pada tahun 2019, Kota Bekasi mencatatkan nilai tertinggi sebesar 3,273,595,338, mengungguli Kota Bandung yang mendominasi pada tahun-tahun sebelumnya dengan nilai tertinggi sebesar 2,578,457,421 di tahun 2017. Kota Bekasi menunjukkan peningkatan yang luar biasa dari tahun 2016 (1,686,600,487) hingga 2019, menandakan percepatan pembangunan atau kontribusi ekonomi yang signifikan.
Di sisi lain, Kota Banjar secara konsisten memiliki nilai terendah dibandingkan kabupaten/kota lainnya, dengan nilai sebesar 116,321,781 pada tahun 2016 dan hanya sedikit meningkat menjadi 131,881,763 pada tahun 2019. Peningkatan ini relatif kecil dibandingkan wilayah lain, menunjukkan tantangan dalam pertumbuhan ekonomi atau faktor lain yang memengaruhi nilai tersebut.
Secara keseluruhan, data ini menggambarkan adanya kesenjangan antara kabupaten/kota di Jawa Barat, dengan beberapa wilayah seperti Kota Bekasi dan Kota Bandung menunjukkan kontribusi yang dominan, sementara wilayah lainnya, seperti Kota Banjar, masih membutuhkan perhatian lebih untuk mendukung pertumbuhannya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")


