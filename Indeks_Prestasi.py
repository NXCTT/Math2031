import numpy as np

A = np.loadtxt("Total_Nilai.csv",delimiter=",")
# A = A.astype(float)

B = np.array([])

count_A = 0
count_A_min = 0
count_B_plus = 0
count_B = 0
count_B_min = 0
count_C_Plus = 0
count_C = 0
count_C_min = 0
count_D = 0
count_F = 0

for i in A :
    if i >= 91 :
        x = "A"
        B = np.append(B,x)
        count_A += 1
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
print(f"Total yang dapat nilai B- = {count_B_min}")
print(f"Total yang dapat nilai C+ = {count_C_Plus}")
print(f"Total yang dapat nilai C = {count_C}")
print(f"Total yang dapat nilai C- = {count_C_min}")
print(f"Total yang dapat nilai D = {count_D}")
print(f"Total yang dapat nilai F = {count_F}")

# B = B.reshape(((len(B),1)))

# print(B)