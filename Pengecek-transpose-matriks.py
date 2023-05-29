#!/usr/bin/env python
# coding: utf-8

# In[2]:


# NIM/Nama : 16722552/Titan Wizatria
# Tanggal : 28 Oktober 2022
# Deskripsi : Program pengecek transpose matriks

# Algoritma
B1=int(input("Panjang baris M1: "))
K1=int(input("Panjang kolom M1: "))
M1 =[[0 for j in range(K1)] for i in range(B1)]
for i in range(B1):
    for j in range(K1):
        M1[i][j]=int(input("Masukkan baris ke-"+str(i + 1)+" kolom ke-"+str(j + 1)+" matriks M1: "))

print("")
B2=int(input("Panjang baris M2: "))
K2=int(input("Panjang kolom M2: "))
M2=[[0 for j in range(K2)] for i in range(B2)]
for i in range(B2):
    for j in range(K2):
        M2[i][j]=int(input("Masukkan baris ke-"+str(i + 1)+" kolom ke-"+str(j + 1)+" matriks M1: "))

print("")
M3=[[0 for j in range(B1)] for i in range(K1)]
B3=K1
K3=B1
for i in range (K1):
    for j in range(B1):
        M3[i][j]=M1[j][i]
if B3==B2 and K3==K2:
    for i in range(B2):
        for j in range(K2):
            if M2[i][j]!=M3[i][j]:
                transpose=False
            else:
                transpose=True
if B3!=B2 or K3!=K2:
    transpose=False
if transpose==True:
    print("Matriks M2 adalah transpose dari Matriks M1.")
else:
    print("Matriks M2 bukan transpose dari Matriks M1.")


# In[ ]:




