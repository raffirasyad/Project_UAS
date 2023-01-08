# import module daftar nilai dari module
from models import daftar_nilai as daftar

def input_data(no):
    # mengimput seluruh data
    while True:
         try:
            nim = int(input("Masukkan Nim :"))
            if nim == '':
                print('Masukkan Nim, Tidak boleh dikosongkan !')
         except ValueError:
             print('Masukkan Nim dengan Angka !')
         else:
             break
    while True:
        nama = (input("Masukkan Nama :"))
        if nama == '':
             print('Nama tidak boleh kosong !')
        else:
             break
    while True:
         try:
            tugas = int(input("Masukkan tugas :"))
            if tugas == '':
                print('Masukkan tugas, Tidak boleh dikosongkan !')
         except ValueError:
             print('Masukkan tugas dengan Angka !')
         else:
             break
    while True:
         try:
            uts = int(input("Masukkan uts :"))
            if uts == '':
                print('Masukkan uts, Tidak boleh dikosongkan !')
         except ValueError:
             print('Masukkan uts dengan Angka !')
         else:
             break
    while True:
         try:
            uas = int(input("Masukkan uas :"))
            if uas == '':
                print('Masukkan uas, Tidak boleh dikosongkan !')
         except ValueError:
             print('Masukkan uas dengan Angka !')
         else:
             break
    daftar.tambah_data(no, nim, nama, tugas, uas, uts)
    