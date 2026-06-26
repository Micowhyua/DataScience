# 📈 Prediksi Penjualan Menggunakan Linear Regression

Proyek ini merupakan implementasi sederhana dari Data Science untuk melakukan analisis dan prediksi data penjualan menggunakan algoritma **Linear Regression**. Tujuan utama dari proyek ini adalah mempelajari bagaimana data historis penjualan dapat digunakan untuk memprediksi tren penjualan di masa mendatang sehingga dapat membantu pengambilan keputusan bisnis berbasis data.

## ✨ Fitur

* Membaca dan memproses dataset penjualan dari file Excel.
* Melakukan analisis data penjualan historis.
* Melatih model Linear Regression untuk prediksi penjualan.
* Menampilkan visualisasi data penjualan dan hasil prediksi.
* Membandingkan data aktual dengan hasil prediksi model.
* Menghasilkan prediksi penjualan berdasarkan pola data sebelumnya.

## 🛠 Teknologi yang Digunakan

### Bahasa Pemrograman

* Python

### Library Data Processing

* Pandas

### Machine Learning

* Scikit-Learn (Linear Regression)

### Visualisasi Data

* Matplotlib

### Komputasi Numerik

* NumPy

## 📚 Library yang Digunakan

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
```

### Fungsi Masing-Masing Library

* **Pandas** digunakan untuk membaca, mengolah, dan menganalisis data penjualan dari file Excel.
* **Linear Regression** dari Scikit-Learn digunakan untuk membangun model prediksi penjualan.
* **Matplotlib** digunakan untuk membuat visualisasi data dan grafik hasil prediksi.
* **NumPy** digunakan untuk melakukan operasi numerik dan manipulasi array.

## 📂 Struktur Proyek

```text
DATA SCIENCE AP/
│
├── Data Siswa.xlsx          # Dataset tambahan untuk latihan analisis data
├── penjualan_toko.xlsx      # Dataset utama penjualan toko
├── generate.py              # Script untuk menghasilkan atau mempersiapkan data
├── prediction_sales.py      # Implementasi model prediksi penjualan
└── main.py                  # Program utama untuk menjalankan aplikasi
```

## ⚙️ Instalasi

Clone repository:

```bash
git clone https://github.com/Micowhyua/DataScience.git
cd nama-repository
```

Install seluruh dependency:

```bash
pip install pandas numpy matplotlib scikit-learn openpyxl
```

atau menggunakan file requirements:

```bash
pip install -r requirements.txt
```

## ▶️ Menjalankan Program

```bash
python main.py
```

## 📊 Model Machine Learning

Proyek ini menggunakan algoritma **Linear Regression** untuk mempelajari hubungan antara data penjualan historis dan memprediksi nilai penjualan pada periode berikutnya berdasarkan pola yang ditemukan dari data sebelumnya.

## 📈 Visualisasi

Program menghasilkan beberapa visualisasi seperti:

* Grafik data penjualan historis.
* Garis regresi hasil pelatihan model.
* Perbandingan antara data aktual dan data prediksi.
* Tren penjualan dari waktu ke waktu.

## 🎯 Tujuan Proyek

* Memahami proses analisis data menggunakan Python.
* Mempelajari implementasi dasar Machine Learning.
* Menggunakan Linear Regression untuk kasus prediksi penjualan.
* Mengembangkan kemampuan visualisasi data untuk kebutuhan analisis bisnis.
* Meningkatkan pemahaman mengenai workflow Data Science mulai dari pengolahan data hingga prediksi.

## 📄 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran, penelitian, dan pengembangan portfolio di bidang Data Science dan Machine Learning.
