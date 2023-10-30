import csv  # import csv
import os  # import modul os (cls)
from pathlib import Path  # import modul path
from datetime import datetime as tanggal  # import datetime untuk tanggal
import pandas as pd

def addData():
    os.system('cls')
    with open('mobil.csv', 'a', newline='') as file:
        csvTambah = csv.writer(file)
        merk = input("Masukkan merk : ")
        type = input("Masukkan type : ")
        tahun = input("masukkan tahun : ")
        csvTambah.writerow([
            merk,type,tahun
        ])
        file.close()
        os.system('cls')
        print("Data Berhasil ditambahkan!! \n")
        input("\nenter untuk lanjutkan")
        os.system('cls')
        menu()

def getData():
    df = pd.read_csv('mobil.csv')      
    df.index = range(1, len(df)+1,)
    print(df)

def showData():
    os.system('cls')
    getData()
    input("\n enter untuk lanjutkan")
    menu()


def editData():
    os.system('cls')    
    getData()
    df = pd.read_csv('mobil.csv')
    edit = int(input("pilih nomor yang ingin diedit: "))
    merkBaru = input("masukkan merk baru: ")
    typeBaru = input("masukkan type baru: ")
    tahunBaru = int(input("masukkan tahun baru: "))

    df.at[edit-1, 'status'] = merkBaru
    df.at[edit-1, 'type'] = typeBaru
    df.at[edit-1, 'tahun'] = tahunBaru

    # Menyimpan perubahan ke file CSV
    df.to_csv('mobil.csv', index=False)
    print("data berhasil diedit")
    input("\n enter untuk lanjutkan")
    menu()


def delData():
    os.system('cls')
    getData()
    df = pd.read_csv('mobil.csv')
    hapus = int(input("pilih nomor yang ingin dihapus : "))
    data = df.drop(hapus-1)
    # Mengatur ulang indeks
    df.reset_index(drop=True, inplace=True)
    # Menyimpan perubahan ke file CSV
    data.to_csv('mobil.csv', index=False)
    print("data berhasil dihapus")
    input("\n enter untuk lanjutkan")
    menu()
    

def menu():
    listmenu = input("[1. tambah data][2.lihat data][3.edit data][4.hapus data][5.keluar] masukkan menu:")    
    if listmenu == '1':
        if not(Path('mobil.csv').is_file()):
            #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
            with open('mobil.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['merk','type','tahun'],  delimiter=',') 
                header.writeheader()
        addData()
    elif listmenu == '2':        
        showData()
    elif listmenu == '3':
        editData()
    elif listmenu == '4':
        delData()
    elif listmenu == '5':
        os.system('cls')
        exit()    
    else :
        print("inputan salah")
        menu()
 
if __name__ == "__main__":
    menu()

