import pandas as pd
import numpy as np

# Buat data tanggal 6 bulan ke belakang
tanggal = pd.date_range(start="2025-04-01", end="2025-09-30", freq="D")

# Buat kategori produk secara acak
kategori = np.random.choice(["Elektronik", "Pakaian", "Makanan"], size=len(tanggal))

# Buat jumlah penjualan acak (dengan variasi tergantung kategori)
np.random.seed(42)
penjualan = []
for k in kategori:
    if k == "Elektronik":
        penjualan.append(np.random.randint(300, 800))
    elif k == "Pakaian":
        penjualan.append(np.random.randint(100, 400))
    else:
        penjualan.append(np.random.randint(200, 600))

# Buat DataFrame
df = pd.DataFrame({
    "Tanggal": tanggal,
    "Kategori": kategori,
    "Penjualan": penjualan
})

# Simpan ke Excel
df.to_excel("penjualan_toko.xlsx", index=False)
print("✅ File 'penjualan_toko.xlsx' berhasil dibuat!")
print(df.head())