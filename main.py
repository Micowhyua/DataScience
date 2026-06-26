import pandas as pd
import matplotlib.pyplot as plt

def nilaiSiswa():
    # Membaca data dari file excel
    data = pd.read_excel('Data Siswa.xlsx')
    print("Tampil Nilai Siswa :")
    print(data)

    #2. Menghitung rata-rata tiap siswa
    data["Rata_rata"] = data[["Matematikan", "Bahasa indonesia", "Informatika"]].mean(axis=1)
    print("\nData dengan Rata-rata:")
    print(data)

    #3. Menentukan siswa dengan nilai rata-rata tertinggi
    tertinggi = data. loc[data["Rata_rata"].idxmax()]
    print("\nSiswa dengan nilai tertinggi:", tertinggi ["Nama"], "-", tertinggi ["Rata_rata"])

        # 4. Visualisasi nilai Matematika
    plt.bar(data["Nama"], data["Rata_rata"], color="black")
    plt.title("Grafik Nilai Rata_rata Siswa")
    plt.xlabel("Nama Siswa")
    plt.ylabel("Nilai")
    plt.show()

nilaiSiswa()
 