import streamlit as st
import pandas as pd

list_matakuliah_humaniora = ['English 1', 'English 2', 'English 3', 'Pancasila', 'Civics', 'Religion', 'Bahasa Indonesia']
list_matakuliah_nonhumaniora = ['Algortima', 'Data Modeling', 'Database', 'Big Data Analyst', 'Probability And Statistic']

if 'list_matakuliah' not in st.session_state:
    st.session_state.list_matakuliah = {
        'Matakuliah': [],
        'Nilai_akhir': []
    }


st.title("Menghitung Grade Mata kuliah UMN!")
status = st.radio("Matakuliah jenis apa?", ["Humaniora", "Non Humaniora"]) 
if(status == "Humaniora"):
    matakuliah = st.selectbox("Masukkan nama mata kuliah", list_matakuliah_humaniora)
    nilai_tugas = st.number_input("Masukan Nilai Tugas", min_value=0, max_value=100)
    nilai_UTS = st.number_input("Masukan Nilai UTS", min_value=0, max_value=100)
    nilai_UAS = st.number_input("Masukan Nilai UAS", min_value=0, max_value=100)
    nilai_sikap = st.number_input("Masukan Nilai Sikap", min_value=0, max_value=100)

    nilai_akhir = (nilai_tugas * 0.3) + (nilai_UTS * 0.2) + (nilai_UAS * 0.3) + (nilai_sikap * 0.2)

    if(st.button('Hitung')):
        st.session_state.list_matakuliah['Matakuliah'].append(matakuliah)
        st.session_state.list_matakuliah['Nilai_akhir'].append(nilai_akhir)
        st.text('Nilai Akhir: {}'.format(nilai_akhir))
        if(nilai_akhir > 85):
            st.success('Grade: A')
        elif((nilai_akhir >= 80) and (nilai_akhir <85)):
            st.success('Grade: A-')
        elif((nilai_akhir >= 75) and (nilai_akhir <80)):
            st.success('Grade: B+')
        elif((nilai_akhir >= 70) and (nilai_akhir <75)):
            st.success('Grade: B')
        elif((nilai_akhir >= 65) and (nilai_akhir <70)):
            st.success('Grade: B-')
        elif((nilai_akhir >= 60) and (nilai_akhir <65)):
            st.success('Grade: C+')
        elif((nilai_akhir >= 55) and (nilai_akhir <60)):
            st.success('Grade: C')
        elif(nilai_akhir <55):
            st.error('Grade: D')
else:
    matakuliah = st.selectbox("Masukkan nama mata kuliah", list_matakuliah_nonhumaniora)
    nilai_tugas = st.number_input("Masukan Nilai Tugas", min_value=0, max_value=100)
    nilai_UTS = st.number_input("Masukan Nilai UTS", min_value=0, max_value=100)
    nilai_UAS = st.number_input("Masukan Nilai UAS", min_value=0, max_value=100)

    nilai_akhir = (nilai_tugas * 0.3) + (nilai_UTS * 0.3) + (nilai_UAS * 0.4)

    if(st.button('Hitung')):
        st.session_state.list_matakuliah['Matakuliah'].append(matakuliah)
        st.session_state.list_matakuliah['Nilai_akhir'].append(nilai_akhir)
        st.text('Nilai Akhir: {}'.format(nilai_akhir))
        if(nilai_akhir > 85):
            st.success('Grade: A')
        elif((nilai_akhir >= 80) and (nilai_akhir <85)):
            st.success('Grade: A-')
        elif((nilai_akhir >= 75) and (nilai_akhir <80)):
            st.success('Grade: B+')
        elif((nilai_akhir >= 70) and (nilai_akhir <75)):
            st.success('Grade: B')
        elif((nilai_akhir >= 65) and (nilai_akhir <70)):
            st.success('Grade: B-')
        elif((nilai_akhir >= 60) and (nilai_akhir <65)):
            st.success('Grade: C+')
        elif((nilai_akhir >= 55) and (nilai_akhir <60)):
            st.success('Grade: C')
        elif(nilai_akhir <55):
            st.error('Grade: D')

df = pd.DataFrame(st.session_state.list_matakuliah)
if(df.empty):
    st.text('Belum ada data')
else:
    st.write("Data Matakuliah")
    st.table(df)
    st.write("Rata-rata nilai akhir: {}".format(df['Nilai_akhir'].mean()))

    st.bar_chart(df,x='Matakuliah', y='Nilai_akhir',x_label='Matakuliah',y_label='Nilai Akhir', horizontal=True)


    