import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('estimasi_kekuatan_tekan_beton.sav', 'rb'))

st.title('Estimasi Kekuatan Tekan Beton')

# Input data menggunakan streamlit
CementComponent = st.number_input('Input takaran semen(kilogram)')
BlastFurnaceSlag = st.number_input('Input takaran BlastFurnaceSlag (kilogram)')
FlyAshComponent = st.number_input('Input takaran Fly Ash(kilogram)')
WaterComponent = st.number_input('Input takaran air(liter)')
SuperplasticizerComponent = st.number_input('Input takaran Superplasticizer(kilogram)')
CoarseAggregateComponent = st.number_input('Input takaran material kasar (kerikil, pecahan batu),(kilogram)')
FineAggregateComponent = st.number_input('Input takaran material halus (pasir),(kilogram)')
Age = st.number_input('Input umur beton saat dilakukan test(dalam hari)')

if (Age>=365):
    Age = 365

predict = ''

if st.button('Estimasi'):
    # Ubah input menjadi array 2D
    input_data = np.array([CementComponent, BlastFurnaceSlag, FlyAshComponent, WaterComponent, SuperplasticizerComponent, CoarseAggregateComponent, FineAggregateComponent, Age]).reshape(1, -1)

    # Lakukan prediksi
    predict = model.predict(input_data)

    # Tampilkan hasil prediksi
    if (Age==0):
        predict=0
    st.write('Estimasi Kekuatan Tekan Beton:', predict,'MPa(megapascal)')
