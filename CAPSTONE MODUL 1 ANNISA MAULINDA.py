# CAPSTONE PROJECT MODUL 1
# by ANNISA MAULINDA
# MEMBUAT APLIKASI DENGAN BASIS FITUR CRUD
# DATA NILAI SISWA


import random  #untuk menghasilkan angka-angka acak
import os #untuk berinteraksi dengan sistem operasi 
from tabulate import tabulate #memformat dan menampilkan data dalam bentuk table 

#----------  TO CLEAR SCREEN VIEW -------------
def clear_terminal() :  #digunakan untuk membersihkan tampilan terminal agar tampilannya bersih 
    os.system('clear')  #mengeksekusi perintah sistem operasi


#----------  LIST KOSONGS -------------
nomor_induk = []
nilai_uts = []
nilai_uas = []
keterangan = []

#random.randint digunakan untuk menghasilkan bilangan bulat acak dalam rentang tertentu 
def panjang_nis ():
    return random.randint(1000,9999) #kenapa ambil range angka segini karena mau NIS nya itu sebanyak 4 angka

def uts():
    return random.randint(50,99)
def uas():
    return random.randint(50,99)

jumlah_siswa = 3

#---------- UNTUK MENAMBAHKAN KE LIST KOSONG -------------

for i in range(jumlah_siswa): #for nya ini buat looping
    nis = panjang_nis()
    while nis in nomor_induk: #buat ngecek dia duplicate apa engga
        nis = panjang_nis()
    nomor_induk.append(nis)
    nilai_uts.append(uts())
    nilai_uas.append(uas())
    rata_rata = (nilai_uts[i]+nilai_uas[i])/2 # i - index 
    if rata_rata >=70:
        keterangan.append("LULUS")
    else:
        keterangan.append("TIDAK LULUS")

#---------- DICTIONARY SISWA -------------

daftar_siswa = {"NIS": [nomor_induk[0],nomor_induk[1],nomor_induk[2]],
                "Nama" : ["ANNISA", "JASMINE", "KEVIN"],
                "Jurusan" : ["HUBUNGAN INTERNASIONAL", "MATEMATIKA","BISNIS"],
                "Nilai UTS" : [nilai_uts[0],nilai_uts[1],nilai_uts[2]],
                "Nilai UAS" : [nilai_uas[0],nilai_uas[1],nilai_uas[2]],
                "Keterangan" : [keterangan[0],keterangan[1],keterangan[2]]
                }

#---------- LIST MENU -------------

def list_menu(): 
    print('''Silahkan Pilih Menu Yang Ingin Ditampilkan:
          1. Tampilkan Data Siswa                      
          2. Menambahkan Data Siswa
          3. Mengubah Data Siswa
          4. Menghapus Data Siswa
          5. Tampilan Data Seluruh Siswa
          6. Exit Program'''
    )
    
# list_menu()

#----------  TABLE SISWA -------------

def list_siswa(): #table seluruh siswa
    table = tabulate(daftar_siswa, headers="keys", tablefmt="pretty")
    print(table)
# list_siswa()

#----------  TABLE ONLY NIS -------------

def colomn_nis():
    nis_column = daftar_siswa["NIS"]  #Mengambil kolom NIS dari dict daftar_siswa dan mengakses nilainya 
    nis_dict = {"NIS": nis_column}  #Membentuk suatu dict yang memiliki key "NIS" dan value berupa kolom NIS yang telah diambil sebelumnya.
    table = tabulate(nis_dict, headers="keys", tablefmt="grid")
    print(table)


#----------  MENU NO.1 ------------- #melihat data siswa berdasarkan NIS yang diinput
def lihat_data(nis_input): 
    try:    #digunakan untuk menangani terjadinya kesalahan selama eksekusi
        nis_input = int(nis_input) 
        if nis_input in daftar_siswa["NIS"]: #untuk mengecek apakah NIS ada daftar_siswa
            index = daftar_siswa["NIS"].index(nis_input) #untuk mencari index dari NIS yang diinput 
            print("Data Siswa:")
            data = list(map(list, zip(*[(key, daftar_siswa[key][index]) for key in daftar_siswa])))  #table based on NIS 
            #zip function is used to transpose the data, and map(list, ...) is used to convert the tuples into lists.
            print(tabulate(data, tablefmt="grid"))
        
        else:
            clear_terminal()
            print(f"Tidak ada siswa dengan NIS {nis_input}")
            colomn_nis()
            nis_input = int(input('Masukkan NIS Yang Ingin Ditampilkan: '))
            lihat_data(nis_input)
    except: #jika terjadi kesalahan maka perintah dibawah diprint
        print("Masukkan NIS dengan angka yang benar")

# lihat_data()

#----------  MENU NO.2 ------------- #menambah data baru siswa
def hasil(nilai_uts, nilai_uas): #untuk menambah keterangan siswa yang baru ditambahkan sesuai denga  nilai yang disubmit 
    rata_rata = (nilai_uts + nilai_uas) / 2 #akan mendapatkan nilai rata2nya 
    if rata_rata >= 70:
        return "LULUS"
    else:
        return "TIDAK LULUS"

def tambah_data (): 
    while True:
        nama = str(input('Masukkan Nama:').upper())  #ditaro diluar looping biar tidak ikut ke loop kalo misalnya nilai yang dimasukkan bukan angka
        if not any(i.isdigit() for i in nama): #any >> untuk mengembalikan nilai True
            break
        else:
            print("Nama tidak boleh mengandung angka")
    while True:        
        jurusan = str(input('Masukkan Jurusan:').upper()) #jika apapun yang diinput nanti outputnya akan mengubah ke huruf kapital semua 
        if not any(i.isdigit() for i in jurusan):
                break
        else:
            print("Jurusan tidak boleh mengandung angka")
    while True:
        try:
            uts = int(input('Masukkan Nilai UTS:'))
            if 0 < uts <= 100: #kalau misalnya submit angka >100 akan keluar output seperti di bawah 
                break
            else:
                print('Masukkan Nilai UTS antara 0 dan 100')
        except:
            print('Masukkan Inputan Yang Benar') #akan kelur kalo misalnya yang disubmit bukan angka 
    while True:
        try:
            uas = int(input('Masukkan Nilai UAS:'))
            if 0 < uas <= 100:
                break
            else:
                print('Masukkan Nilai UAS antara 0 dan 100')
        except:
            print('Masukkan Inputan Yang Benar')
    nis = panjang_nis() #untuk generate nilai nis 
    while nis in nomor_induk: #buat ngecek dia duplicate apa engga
        nis = panjang_nis()
    keterangan = hasil(uts,uas)  #dapat keterangan dari nilai yang disubmit LULUS/TIDAK 
    daftar_siswa['NIS'].append(nis)
    daftar_siswa['Nama'].append(nama) 
    daftar_siswa['Jurusan'].append(jurusan)
    daftar_siswa['Nilai UTS'].append(uts)
    daftar_siswa['Nilai UAS'].append(uas)
    daftar_siswa['Keterangan'].append(keterangan)

    print('Data Siswa Berhasil Ditambahkan:')
    list_siswa() #untuk menampilkan data seluruh data siswa setelah ditambahkan 

# tambah_data()

#----------  MENU NO.3 ------------- #mengubah data siswa berdasarkan NIS tertentu 
def ubah_data (): 
    print('Masukkan NIS Yang Mau Diubah:')
    colomn_nis() #untuk menampilkan colomn NIS 
    nis_input = int(input('Masukkan Nomor Induk Siswa:'))
    if nis_input in daftar_siswa["NIS"]: #akan menampilkan data dari spesifik NIS 
        index = daftar_siswa["NIS"].index(nis_input) #untuk mencari index dari NIS yang diinput 
        print("Data Siswa:")
        data = list(map(list, zip(*[(key, daftar_siswa[key][index]) for key in daftar_siswa]))) #untuk menampilkan table 
         #zip function is used to transpose the data, and map(list, ...) is used to convert the tuples into lists.
        print(tabulate(data, tablefmt="grid"))
                    
        while True: 
            print('''Data Nilai:\n1. Nilai UTS\n2. Nilai UAS''') #dibuat pilihan untuk mengubah nilai UTS/UAS 
            user_choose = int(input('Pilih Data Nilai Yang Mau Diubah:'))
            if user_choose == 1:
                try:
                    uts_new = int(input('Masukkan Nilai UTS: '))
                    if 0 < uts_new <= 100:     
                        daftar_siswa['Nilai UTS'][index] = uts_new #kalau inputan benar akan mengubah data lama
                    else:
                        print('Masukkan Nilai UTS antara 0 dan 100')
                        continue
                except:
                    clear_terminal()
                    print("Mohon masukkan nilai UTS dalam bentuk angka.")
                    continue
            elif user_choose == 2:
                try:
                    uas_new = int(input('Masukkan Nilai UAS: '))
                    if 0 < uas_new <= 100:
                        daftar_siswa['Nilai UAS'][index] = uas_new #kalau inputan benar akan mengubah data lama
                    else:
                        print('Masukkan Nilai UAS antara 0 dan 100')
                        continue
                except:
                    clear_terminal()
                    print("Mohon masukkan nilai UAS dalam bentuk angka.")
                    continue
            else:
                print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
                continue

            rata_rata_baru = (daftar_siswa['Nilai UTS'][index] + daftar_siswa['Nilai UAS'][index]) / 2 #untuk mendapatkan keterangan baru dari nilai yang baru diinput 
            daftar_siswa['Keterangan'][index] = "LULUS" if rata_rata_baru >= 70 else "TIDAK LULUS"


            print('Data Siswa Berhasil Diubah') #akan menampilkan data baru setelah diubah dari spesifik NIS 
            data = list(map(list, zip(*[(key, daftar_siswa[key][index]) for key in daftar_siswa])))
            #zip function is used to transpose the data, and map(list, ...) is used to convert the tuples into lists.
            print(tabulate(data, tablefmt="grid"))
            # list_siswa()

            pilih_ubah = input("Mau ubah data lain (Y/N)? ") #pilihan untuk mengubah data lain atau engga 
            if pilih_ubah.upper() != "Y":
                break
    else:
        print('NIS Tidak Ditemukan ')

# ubah_data()

#----------  MENU NO.4 ------------- #menghapus data siswa berdasarkan NIS 
def hapus_siswa(): 
    clear_terminal()
    list_siswa() #akan menampilkan data seluruh siswa 
    while True:
        try:
            nis_input = int(input('Masukkan Nomor Induk Siswa Yang Ingin Dihapus:'))
        except: 
            print('Mohon Masukkan Inputan Yang Benar (Angka)')
            continue
        try:
            if nis_input in daftar_siswa["NIS"]:
                index = daftar_siswa["NIS"].index(nis_input) 
                for key in daftar_siswa:
                    daftar_siswa[key].pop(index) #removes key-value pair 
                print('Data Berhasil Dihapus')
                list_siswa() #akan menampilkan updated data siswa setelah dihapus
                break
            else:
                print('Data Siswa Tidak Ditemukan')
                break
        except: 
            print('Mohon Masukkan Inputan Yang Benar (Angka)')
            break


def user_choose():
    pilih = input("Pilih Menu Lain? (Y/N): ")
    clear_terminal()
    if pilih.upper() == "Y":
        clear_terminal()
        print('Anda memilih untuk melanjutkan.')
        return True #jika pengguna memilih untuk melanjutkan
    elif pilih.upper() == "N":
        print('Program Keluar. Terima Kasih!')
        return False #jika pengguna memilih untuk keluar dari program.
    else:
        print('Input tidak valid. Silakan pilih Y atau N.')
        return user_choose() #memberikan kesempatan kedua kepada pengguna untuk memasukkan input yang benar.


#----------  TO RUNNING THE PROGRAM  -------------

def main():
    print ("--- Selamat Datang di Sekolah Purwadhika ---") #ditaruh disini agar gak ikut ke looping setiap pilih menu baru
    while True:
        list_menu()
        try:
            menu = int(input('Pilih Menu Yang Diinginkan: '))
        except:
            clear_terminal()
            print("*** Mohon Masukkan Inputan Yang Benar (Angka) ***") #jika yang disubmit bukan angka
            continue   
        try:
            if menu == 1: #lihat data siswa based in NIS 
              while True:
                print('Berikut Daftar Nomor Induk Siswa:')
                colomn_nis()
                try:
                    nis_input = int(input('Masukkan NIS Yang Ingin Ditampilkan: '))
                    lihat_data(nis_input) #table informasi dari spesifik NIS yang disubmiut
                    break
                except:
                    clear_terminal()
                    print("*** Mohon Masukkan Inputan Yang Benar ***") #jika yang disubmit bukan angka
            elif menu == 2: #menambahkan data siswa baru 
                tambah_data()
            elif menu == 3: #mengubah data siswa based on NIS 
                while True:
                    try:
                        ubah_data()
                        break
                    except:
                        clear_terminal()
                        print("*** Mohon Masukkan Inputan Yang Benar ***")#jika yang disubmit bukan angka
            elif menu == 4: #meghapus data siswa based on nis 
                hapus_siswa()
            elif menu == 5 : #melihat data seluruh siswa 
                list_siswa()
            elif menu == 6: #user memilih untuk tidak melanjutkan 
                clear_terminal()
                print("Terima Kasih Telah Menggunakan Portal Siswa")
                input("Press Enter to continue...")
                clear_terminal()
                print ("--- Selamat Datang di Sekolah Purwadhika---")
                continue
            else:
                clear_terminal()
                print("*** Pilihan menu tidak valid. Silakan pilih nomor menu yang benar. ***") #jika yang disubmit tidak ada dimenu

            if not user_choose(): #jika stidak ingin melanjutkan
                clear_terminal()
                print("Terima Kasih Telah Menggunakan Portal Siswa")
                input("Press Enter to continue...")
                clear_terminal()
                print ("--- Selamat Datang di Sekolah Purwadhika ---")
                continue
        except:
            clear_terminal()
            print("*** Mohon Masukkan Inputan Yang Benar ***") #jika yang disubmit bukan angka

clear_terminal() # agar clean\ tidak ada command pembuka
# if __name__ == "__main__":
main()