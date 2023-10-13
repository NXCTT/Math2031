import numpy as np

A = np.loadtxt("Total_Nilai.csv",delimiter=",") # Mengambil data total nilai mahasiswa
A = A.reshape(((len(A)),1))

mean = np.mean(A)

print(f"Rata rata nilai mahasiswa = {mean}")

Lat_soal = np.loadtxt("Data_Ls.csv",delimiter=",") # Mengambil data nilai LS mahasiswa
Kuis = np.loadtxt("Data_Kuis.csv",delimiter=",") # Mengambil data nilai Kuis mahasiswa
Lab = np.loadtxt("Data_Lab.csv",delimiter=",") # Mengambil data nilai Lab mahasiswa
Proyek = np.loadtxt("Data_Project.csv",delimiter=",") # Mengambil data nilai Proyek mahasiswa
Jurnal = np.loadtxt("Data_Jurnal.csv",delimiter=",") # Mengambil data nilai Jurnal mahasiswa
Ujian = np.loadtxt("Data_UTS_UAS.csv",delimiter=",") # Mengambil data nilai UTS & UAS mahasiswa

LS_mean = np.mean(Lat_soal,axis=0)
Kuis_mean = np.mean(Kuis,axis=0)      # Merata ratakan nilai mahasiswa pertugas sesuai jenis tugas masing masing
Lab_mean = np.mean(Lab,axis=0)
Proyek_mean = np.mean(Proyek,axis=0)
Jurnal_mean = np.mean(Jurnal,axis=0)
Ujian_mean = np.mean(Ujian,axis=0)

print(f"Rata rata nilai LS mahasiswa = \n{LS_mean}")
print(f"Rata rata nilai Kuis mahasiswa = \n{Kuis_mean}")
print(f"Rata rata nilai Lab mahasiswa = {Lab_mean}") # Menampilkan rata rata nilai pertugas mahasiswa
print(f"Rata rata nilai Proyek mahasiswa = {Proyek_mean}")
print(f"Rata rata nilai Jurnal mahasiswa = {Jurnal_mean}")
print(f"Rata rata nilai Ujian mahasiswa = {Ujian_mean}")

Bobot_LS = np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01]) # 7 x 1% = 7%
Nilai_LS = Lat_soal @ Bobot_LS
Nilai_LS = Nilai_LS.reshape((101,1))

Bobot_Kuis = np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01]) # 7 x 1% = 7%
Nilai_Kuis = Kuis @ Bobot_Kuis
Nilai_Kuis = Nilai_Kuis.reshape((101,1))

Bobot_Lab = np.array([0.01,0.01]) # 2 x 1% = 2%
Nilai_Lab = Lab @ Bobot_Lab
Nilai_Lab = Nilai_Lab.reshape((101,1))

Bobot_Proyek = np.array([0.01,0.01]) # 2 x 1% = 2%
Nilai_Proyek = Proyek @ Bobot_Proyek
Nilai_Proyek = Nilai_Proyek.reshape((101,1))

Bobot_Jurnal = np.array([0.26,0.26]) # 2 x 26% = 52%
Nilai_Jurnal = Jurnal @ Bobot_Jurnal
Nilai_Jurnal = Nilai_Jurnal.reshape((101,1))

Bobot_Ujian = np.array([0.15,0.15]) # 2 x 15% = 30% 
Nilai_Ujian = Ujian @ Bobot_Ujian
Nilai_Ujian = Nilai_Ujian.reshape((101,1))      # Total = 7% + 7% + 2% + 2% + 52% + 30% = 100%

Total_Nilai = Nilai_LS + Nilai_Kuis + Nilai_Lab + Nilai_Proyek + Nilai_Jurnal + Nilai_Ujian # Membuat total nilai dari bobot baru

np.savetxt("Total_NIlai_Baru.csv",Total_Nilai,delimiter=",",fmt="%.2f") # Menyimpan total nilai baru dalam file csv

print(Total_Nilai)

new_mean = np.mean(Total_Nilai)

print(f"Rata rata nilai mahasiswa (Baru) = {new_mean}") # Menunjukkan rata rata nilai baru setelah diubah bobotnya 

B = np.array([]) # Membuat array baru untuk menampung daftar IP seluruh mahasiswa

count_A = 0
count_A_min = 0
count_B_plus = 0
count_B = 0  # Untuk menghitung jumlah mahasiswa yang mendapat IP perkategori.
count_B_min = 0
count_C_Plus = 0
count_C = 0
count_C_min = 0
count_D = 0
count_F = 0

for i in Total_Nilai : # For untuk mengambil semua nilai dalam vektor total nilai
    if i >= 91 : # Membuat kondisi nilai
        x = "A"  # Pengkategorian nilai sesuai kondisi 
        B = np.append(B,x) # Memuat IP kedalam array baru
        count_A += 1 # Menambahkan 1 kedalam hitungan yang mendapat kategori IP tersebut
    elif 86 <= i < 91 :
        x = "A-"
        B = np.append(B,x)
        count_A_min += 1
    elif 81 <= i < 86 :
        x = "B+"
        B = np.append(B,x)
        count_B_plus += 1
    elif 76 <= i < 81 :
        x = "B"
        B = np.append(B,x)
        count_B += 1
    elif 71 <= i < 76 :
        x = "B-"
        B = np.append(B,x)
        count_B_min += 1
    elif 61 <= i < 71 :
        x = "C+"
        B = np.append(B,x)
        count_C_Plus += 1
    elif 51 <= i < 61 :
        x = "C"
        B = np.append(B,x)
        count_C += 1
    elif 46 <= i < 51 :
        x = "C-"
        B = np.append(B,x)
        count_C_min += 1
    elif 41 <= i < 46 :
        x = "D"
        B = np.append(B,x)
        count_D += 1
    elif i < 41 :
        x = "F"
        B = np.append(B,x)
        count_F += 1

print(f"Total yang dapat nilai A = {count_A}")
print(f"Total yang dapat nilai A- = {count_A_min}")
print(f"Total yang dapat nilai B+ = {count_B_plus}")
print(f"Total yang dapat nilai B = {count_B}")
print(f"Total yang dapat nilai B- = {count_B_min}")  # Menampilkan Total mahasiswa per kategori IP
print(f"Total yang dapat nilai C+ = {count_C_Plus}")
print(f"Total yang dapat nilai C = {count_C}")
print(f"Total yang dapat nilai C- = {count_C_min}")
print(f"Total yang dapat nilai D = {count_D}")
print(f"Total yang dapat nilai F = {count_F}")

B = B.reshape(((len(B)),1)) # Untuk merapikan vektor IP dalam bentuk 1 kolom

print(B) # Menampilkan IP untuk kemudian dicopy paste ke file excel
