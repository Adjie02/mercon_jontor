import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Kelompok Mercon Jontor")

st.write("# Tugas Kelompok Mercon Jontor")

st.write("## Pendahuluan")
st.write("Sejak berlakunya Undang-Undang RI Nomor 23 Tahun 2014 tentang Pemerintahan Daerah, Indonesia menerapkan otonomi daerah yang memberikan keleluasaan bagi daerah untuk mengelola potensi lokal sebagai sumber pendapatan. Kebijakan ini bertujuan meningkatkan kesejahteraan masyarakat dan mengurangi ketimpangan antarwilayah. Pendapatan utama daerah berasal dari Pendapatan Asli Daerah (PAD), seperti pajak, retribusi, dan hasil pengelolaan kekayaan daerah. Namun, kontribusi PAD di Provinsi Jawa Barat masih rendah, sehingga bergantung pada dana transfer pemerintah pusat untuk pembiayaan pembangunan. Jawa Barat, dengan populasi terbesar di Indonesia mencapai 49.935.858   jiwa (BPS, 2020), memiliki potensi besar meningkatkan pendapatannya. Meski demikian, tingginya populasi juga meningkatkan pengeluaran pemerintah untuk pembangunan dan pelayanan publik. Karakteristik kota dan kabupaten di Jawa Barat beragam, mulai dari kota dengan dominasi sektor industri dan perdagangan hingga kabupaten yang bergantung pada sektor pertanian. Analisis pendapatan daerah penting untuk mengidentifikasi potensi dan tantangan fiskal sekaligus memberikan rekomendasi guna mendukung pembangunan berkelanjutan di seluruh wilayah Jawa Barat.")

st.write("## Deskripsi Data")
st.write("Jenis data yang digunakan termasuk kedalam data float, karena data tersebut menggambarkan kontribusi PAD atau transfer dana pusat berupa angka desimal.")

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
    'Kuningan' : 'Kabupaten Kuningan',
    'Cirebon' : 'Kabupaten Cirebon',
    'Majalengka' : 'Kabupaten Majalengka',
    'Sumedang' : 'Kabupaten Sumedang', 
    'Indramayu' : 'Kabupaten Indramayu',
    'Subang' : 'Kabupaten Subang',
    'Purwakarta' : 'Kabupaten Purwakarta',
    'Karawang' : 'Kabupateb Karawang',
    'Bekasi' : 'Kabupaten Bekasi',
    'Bandung Barat' : 'Kabupaten Bandung Barat',
    'Pangandaran' : 'Kabupaten Pangandaran',
    'Kota Bogor' : 'Kota Bogor',
    'Kota Sukabumi' : 'Kota Sukabumi',
    'Kota Bandung' : 'Kota Bandung',
    'Kota Cirebon' : 'Kota Cirebon',
    'Kota Bekasi' : 'Kota Bekasi',
    'Kota Depok' : 'Kota Depok',
    'Kota Cimahi' : 'Kota Cimahi',
    'Kota Tasimalaya' : 'Kota Tasikmalaya',
    'Kota Banjar' : 'Kota Banjar'
}

selected_kota = st.multiselect(
    'Silahkan Pilih Kabupaten/Kota yang akan ditampilkan:',
    options=kamus_ticker.keys(),
    default=['Bandung', 'Bogor'] 
)

selected_tahun = st.multiselect(
    'Silahkan Pilih Tahun yang akan ditampilkan:',
    options=[str(year) for year in range(2016, 2020)],  # Menambahkan tahun dalam format string
    default=['2016', '2017', '2018', '2019']
)

if selected_kota and selected_tahun:
    valid_kota = [kota for kota in selected_kota if kota in data.index]
 
    valid_tahun = [tahun for tahun in selected_tahun if tahun in data.columns]

    if valid_kota and valid_tahun:
        filtered_data = data.loc[valid_kota, valid_tahun]
        
        st.write("Tabel Data Pendapatan:")
        st.write(filtered_data)

        grafik = px.line(
            filtered_data.T,  
            title="Visualisasi Pendapatan Kabupaten/Kota",
            labels={'value': 'Pendapatan (Juta Rupiah)', 'index': 'Tahun'},
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Set1  
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
st.write("Berdasarkan data yang tersedia, total nilai untuk Provinsi Jawa Barat mengalami tren peningkatan dari tahun 2016 hingga 2019. Pada tahun 2016, total nilai tercatat sebesar 17,042,895,113, dan meningkat signifikan menjadi 19,759,789,101 pada tahun 2019. Peningkatan ini mencerminkan pertumbuhan yang stabil di berbagai kabupaten/kota di Jawa Barat. Kabupaten/Kota dengan nilai tertinggi selama periode tersebut adalah Kota Bandung dan Kota Bekasi. Pada tahun 2019, Kota Bekasi mencatatkan nilai tertinggi sebesar 3,273,595,338, mengungguli Kota Bandung yang mendominasi pada tahun-tahun sebelumnya dengan nilai tertinggi sebesar 2,578,457,421 di tahun 2017. Kota Bekasi menunjukkan peningkatan yang luar biasa dari tahun 2016 (1,686,600,487) hingga 2019, menandakan percepatan pembangunan atau kontribusi ekonomi yang signifikan. Di sisi lain, Kota Banjar secara konsisten memiliki nilai terendah dibandingkan kabupaten/kota lainnya, dengan nilai sebesar 116,321,781 pada tahun 2016 dan hanya sedikit meningkat menjadi 131,881,763 pada tahun 2019. Peningkatan ini relatif kecil dibandingkan wilayah lain, menunjukkan tantangan dalam pertumbuhan ekonomi atau faktor lain yang memengaruhi nilai tersebut. Secara keseluruhan, data ini menggambarkan adanya kesenjangan antara kabupaten/kota di Jawa Barat, dengan beberapa wilayah seperti Kota Bekasi dan Kota Bandung menunjukkan kontribusi yang dominan, sementara wilayah lainnya, seperti Kota Banjar, masih membutuhkan perhatian lebih untuk mendukung pertumbuhannya.")


st.write("## Kesimpulan")
st.write('''Sejak diberlakukannya Undang-Undang RI Nomor 23 Tahun 2014 tentang Pemerintahan Daerah, otonomi daerah memberikan kewenangan bagi setiap daerah untuk mengelola potensi lokal sebagai sumber pendapatan guna meningkatkan kesejahteraan masyarakat dan mengurangi ketimpangan antarwilayah. Namun, kontribusi Pendapatan Asli Daerah (PAD) di Provinsi Jawa Barat masih rendah, sehingga ketergantungan pada dana transfer pemerintah pusat masih tinggi.

Provinsi Jawa Barat, dengan populasi terbesar di Indonesia, memiliki potensi besar untuk meningkatkan pendapatan daerah melalui pengelolaan potensi ekonomi yang beragam. Tren peningkatan pendapatan di Jawa Barat dari tahun 2016 hingga 2019 menunjukkan pertumbuhan yang stabil, dengan nilai meningkat dari Rp17,04 triliun pada 2016 menjadi Rp19,76 triliun pada 2019. Kota Bekasi dan Kota Bandung mendominasi kontribusi ekonomi, dengan Kota Bekasi mencatatkan nilai tertinggi pada 2019 sebesar Rp3,27 triliun. Di sisi lain, Kota Banjar konsisten menjadi wilayah dengan nilai terendah, hanya meningkat dari Rp116,32 miliar pada 2016 menjadi Rp131,88 miliar pada 2019.

Kesenjangan ekonomi antarwilayah di Jawa Barat masih menjadi tantangan, dengan beberapa kota/kabupaten menunjukkan kontribusi ekonomi yang dominan, sementara wilayah lainnya membutuhkan perhatian lebih. Analisis ini menekankan pentingnya optimalisasi potensi lokal dan perencanaan strategis guna mendorong pertumbuhan ekonomi yang merata dan berkelanjutan di seluruh Jawa Barat.''')

st.write("## Referensi / Daftar Pustaka")
st.write("Badan Pusat Statistik Provinsi Jawa Barat. (2019). Pendapatan Pemerintah Kabupaten/Kota (Ribu Rupiah), 2018-2019. Diakses dari https://jabar.bps.go.id")
st.write ("Pratiwi, Y. E., & Hutajulu, D. M. (2022). Analisis Pendapatan Asli Daerah Provinsi Jawa Barat dengan Penerapan Error Correction Model. Ekonomi dan Bisnis: Berkala Publikasi, Gagasan Konseptual, Hasil Penelitian, Kajian, dan Terapan Teori. Universitas Tidar.")


