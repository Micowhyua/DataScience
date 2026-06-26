
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def prediction():

    #membaca file excel
    df = pd.read_excel('penjualan_toko.xlsx')

    # ubah ukuran kolom tanggal menjadi  tipe datetime
    df ['tanggal'] = pd.to_datetime(df['tanggal'])

    # ubah kategori jadi angka (ecoding)
    df ['Kategori_Code'] = df['Kategori'].astype('category').cat.codes

    # gunakan urutan waktu sebagai fitur numerik
    df['Hari_Ke'] = (df['Tanggal'] - df['Tanggal'].min()).dt.days

    # fitur dan target 
    x = df[['Hari_Ke', 'Kategori_Code']]
    y = df['Penjualan']

    # latih model regression linear
    model = LinearRegression()
    model.fit(x, y)

    print('\nModel Selesai Dilatih :')
    print('koefisien regresi :', model.coef_)
    print('intercept :', model.intercept_)

    # prediksi 30 hari kedepan untuk kategori elektronik
    future_days = 30
    hari_baru = np.arange(df['Hari_Ke'].max() + 1, df['Hari_Ke'].max() + future_days + 1)

    kategori_baru = np.zeros(future_days)

    x_future = np.column_stack((hari_baru, kategori_baru))
    y_pred_future = model.predict(x_future)

    future_dates = pd.date_range(df['Tanggal'].max() + pd.Timedelta(days=1), periods=future_dates)

    prediksi_df = pd.DataFrame({
        "Tanggal" : future_dates,
        "Kategori" : "Elektronik",
        "Prediksi_Penjualan" : y_pred_future
    })

    print("Prediksi 19 hari ke depan : ")
    print(prediksi_df.head(10))

    # visualisasi grafik
    plt.figure(figsize=(10,5))
    plt.plot(df['Tanggal'], df['Penjualan'],label="Penjualan aktual")

prediction()