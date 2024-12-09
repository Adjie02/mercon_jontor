import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Kelompok Mercon Jontor")

st.write("# Tugas Kelompok Mercon Jontor")

st.write("## Pendahuluan")
st.write("Tuliskan di bagian ini latar belakang data apa yang dipilih, mengapa kelompok memilih data ini, dsb.")

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

st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")


