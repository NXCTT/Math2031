import numpy as np

print("===Tugas 1===\n")

Lat_soal = np.loadtxt("Data_Ls.csv",delimiter=",")
Kuis = np.loadtxt("Data_Kuis.csv",delimiter=",")
Lab = np.loadtxt("Data_Lab.csv",delimiter=",")
Proyek = np.loadtxt("Data_Project.csv",delimiter=",")
Jurnal = np.loadtxt("Data_Jurnal.csv",delimiter=",")
Ujian = np.loadtxt("Data_UTS_UAS.csv",delimiter=",")

Bobot_LS = np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01])
Nilai_LS = Lat_soal @ Bobot_LS
Nilai_LS = Nilai_LS.reshape((101,1))

Bobot_Kuis = np.array([0.02,0.02,0.02,0.02,0.02,0.02,0.02])
Nilai_Kuis = Kuis @ Bobot_Kuis
Nilai_Kuis = Nilai_Kuis.reshape((101,1))

Bobot_Lab = np.array([0.04,0.04])
Nilai_Lab = Lab @ Bobot_Lab
Nilai_Lab = Nilai_Lab.reshape((101,1))

Bobot_Proyek = np.array([0.075,0.075])
Nilai_Proyek = Proyek @ Bobot_Proyek
Nilai_Proyek = Nilai_Proyek.reshape((101,1))

Bobot_Jurnal = np.array([0.03,0.03])
Nilai_Jurnal = Jurnal @ Bobot_Jurnal
Nilai_Jurnal = Nilai_Jurnal.reshape((101,1))

Bobot_Ujian = np.array([0.25,0.25])
Nilai_Ujian = Ujian @ Bobot_Ujian
Nilai_Ujian = Nilai_Ujian.reshape((101,1))

Total_Nilai = Nilai_LS + Nilai_Kuis + Nilai_Lab + Nilai_Proyek + Nilai_Jurnal + Nilai_Ujian

print(f"Total nilai mahasiswa = \n{Total_Nilai}")

LS_mean = np.mean(Lat_soal,axis=0)
Kuis_mean = np.mean(Kuis,axis=0)
Lab_mean = np.mean(Lab,axis=0)
Proyek_mean = np.mean(Proyek,axis=0)
Jurnal_mean = np.mean(Jurnal,axis=0)
Ujian_mean = np.mean(Ujian,axis=0)

mean = np.mean(Total_Nilai)

print(f"Rata rata nilai LS mahasiswa = \n{LS_mean}")
print(f"Rata rata nilai Kuis mahasiswa = \n{Kuis_mean}")
print(f"Rata rata nilai Lab mahasiswa = {Lab_mean}")
print(f"Rata rata nilai Proyek mahasiswa = {Proyek_mean}")
print(f"Rata rata nilai Jurnal mahasiswa = {Jurnal_mean}")
print(f"Rata rata nilai Ujian mahasiswa = {Ujian_mean}")

print(f"Rata rata nilai mahasiswa = {mean}")

np.savetxt("Total_Nilai.csv",Total_Nilai,delimiter=",",fmt="%.2f")
