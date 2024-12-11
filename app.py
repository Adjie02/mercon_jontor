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

st.write("## Visualisasi Pendapatan Kabupaten/Kota di Jawa Barat")
st.write("Berikut Bentuk Visualisasi Berdasarkan Pendapatan Kabupaten/Kota di Provinsi Jawa Barat")

data_path = "Pend_JawaBarat.xlsx.csv"
data = pd.read_csv(data_path, delimiter=';', skiprows=2)
data = data.rename(columns={"Unnamed: 0": "Kabupaten/Kota"})
data.set_index("Kabupaten/Kota", inplace=True)

kamus_ticker = {
    'Bogor' : 'Kabupaten Bogor',
    'Sukabumi' : 'Kabupaten Sukabumi',
    'Cianjur' : 'Kabupaten Cianjur',
    'Bandung' : 'Kabupaten Bandung',
    'Garut' : 'Kabupaten Garut',
    'Tasikmalaya' : 'Kabupaten Tasikmalaya',
    'Ciamis' : 'Kabupaten Ciamis',
    'Kuningan' : 'Kabupaten Kuningan'
}

selected_kota = st.multiselect(
    'Silahkan Pilih Kabupaten/Kota yang akan ditampilkan:',
    options=kamus_ticker.keys(),
    default=['Bandung', 'Bogor']  # Menggunakan nama yang sesuai dengan kamus_ticker
)

# Pilih periode (tahun) yang diinginkan
selected_tahun = st.multiselect(
    'Silahkan Pilih Tahun yang akan ditampilkan:',
    options=[str(year) for year in range(2016, 2020)],  # Menambahkan tahun dalam format string
    default=['2016', '2017', '2018', '2019']
)

# Filter data berdasarkan kabupaten/kota dan tahun yang dipilih
if selected_kota and selected_tahun:
    # Memastikan bahwa kabupaten/kota yang dipilih ada dalam data index
    valid_kota = [kota for kota in selected_kota if kota in data.index]
 
    # Memastikan bahwa tahun yang dipilih ada dalam kolom data
    valid_tahun = [tahun for tahun in selected_tahun if tahun in data.columns]

    if valid_kota and valid_tahun:
        filtered_data = data.loc[valid_kota, valid_tahun]
        
        # Debugging: menampilkan data yang telah difilter
        st.write("Tabel Data Pendapatan:")
        st.write(filtered_data)

        # Visualisasi data dengan Plotly
        st.write("#Visualisasi Pendapatan Kabupaten/Kota di Jawa Barat:")
        grafik = px.line(
            filtered_data.T,  # Transpose agar tahun menjadi sumbu x
            title="Pendapatan Kabupaten/Kota di Jawa Barat (2016-2019)",
            labels={'value': 'Pendapatan (Juta Rupiah)', 'index': 'Tahun'},
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Set1  # Menambahkan variasi warna
        )

        grafik.update_layout(
            xaxis_title="Tahun",
            yaxis_title="Pendapatan (Juta Rupiah)",
            legend_title="Kabupaten/Kota"
        )
        st.plotly_chart(grafik)
    else:
        st.write("Kabupaten/Kota atau Tahun yang dipilih tidak valid.")
else:
    st.write("Silahkan pilih minimal satu kabupaten/kota dan satu tahun untuk visualisasi.")
    
st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")


