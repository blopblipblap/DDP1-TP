import csv
import operator
def impor(file): #fungsi untuk impor data dari csv
    try:
        with open(file) as file_csv:
            baca_csv=csv.reader(file_csv, delimiter=',')
            for baris in baca_csv:
                dict[baris[0]]=[baris[0],baris[1],baris[2],baris[3]]
            print("Terimpor", len(baris), "baris")
        return dict
    except FileNotFoundError:
        print("Maaf, file", file, "tidak ada:)")

def tulisan(): #fungsi untuk header
    print("#"*5)
    print("BudayaKB Lite v1.0")
    print("~Kalau bukan kita yang melestarikan budaya, siapa lagi?~")
    print("#"*5)
          
def carinama(a): #fungsi untuk mencari data berdasarkan nama
    if a in dict:
        gabung=",".join(dict[a]) #menggabungkan isi list dengan ","
        print(gabung, end="\n")
    else:
        print("Maaf, tidak ada nama", a, "di BudayaKB Lite:)")
        
def caritipe(a): #fungsi untuk mencari data berdasarkan tipe
    counter=0
    for key, value in dict.items(): #kalau isi list_tipe sudah terisi
        if value[1]==a: #jika diiterasi ada tipe yang sama
            counter+=1
            gabung=",".join(dict[key])
            print(gabung, end="\n")
        elif value[1]!=a: #jika diiterasi tipe belum sama
            continue
    if counter==0: #jika tipe tidak ada di program
        print('Maaf, tidak ada tipe', a, "di BudayaKB Lite:)")
    else:
        print("*Ditemukan", counter, a+"*")
        
def cariprov(a): #fungsi untuk mencari data berdasarkan provinsi
    counter=0
    for key, value in dict.items(): #kalau isi list_prov sudah terisi
        if value[2]==a: #jika diiterasi ada prov yang sama
            counter+=1
            gabung=",".join(dict[key])
            print(gabung, end="\n")
        elif value[2]!=a: #jika diiterasi prov belum sama
            continue
    if counter==0: #jika prov tidak ada di program
        print('Maaf, tidak ada provinsi', a, "di BudayaKB Lite:)")
    else:
        print("*Ditemukan", counter, "warisan budaya*")
        
def tambah(a): #fungsi untuk menambah data budaya
    a_spl=a.split(";;;")
    if len(a_spl)<4 or len(a_spl)>4: #jika data yang ingin dimasukkan tidak tepat 4
        print("Tolong masukan tepat 4 info:)")
    else:
        dict[a_spl[0]]=[a_spl[0],a_spl[1],a_spl[2],a_spl[3]] #menambah item baru kedalam dict
        print(a_spl[0], "ditambahkan")
    return dict

def update(a): #fungsi untuk update data budaya
    a_spl=a.split(";;;")
    if len(a_spl)<4 or len(a_spl)>4: #jika data yang ingin dimasukkan tidak tepat 4
        print("Tolong masukan 4 info:)")
    elif a_spl[0] not in dict: #jika nama/key tidak ada di dict
        print(a_spl[0], "tidak ada di Budaya KB Lite, mau tambahkan? IYA/TIDAK")
        b=input("Masukkan perintah: ")
        if b=="TIDAK": #Kalau input TIDAK
            return 0
        else: #Kalau input IYA
            tambah(a)
            return
    else:
        dict_update[a_spl[0]]=[a_spl[0],a_spl[1],a_spl[2],a_spl[3]] #membuat dict baru bernama dict_update
        dict.update(dict_update) #mengupdate dict dengan dict.update
        print(a_spl[0], "diupdate")
    return dict

def hapus(a): #fungsi untuk menghapus data budaya
    if a not in dict: #jika yang ingin dihapus tidak ada di dict
        print(a, "tidak ada di BudayaKB Lite:)")
    else:
        del dict[a] #menghapus key,value dari dict
        print(a, "telah dihapus")
        
def stat(): #fungsi untuk menampilkan jumlah total warisan budaya
    banyak_key=len(dict) 
    print("Terdapat", banyak_key, "warisan budaya.")

def stattipe(): #fungsi untuk menampilkan jumlah warisan budaya per tipe
    for key,value in dict.items():
        list_tipe.append(value[1]) #ditambah dulu (HANYA TIPE)
    for a in list_tipe: #diiterasi lewat list_tipe
        count=list_tipe.count(a)
        list_stattipe.append((a,count)) #menambah tuple (tipe, count) kedalam list_stattipe
    print(sorted(set(list_stattipe), key=operator.itemgetter(1), reverse=True)) #agar data tidak dobel. itemgetter 1= untuk mengurutkan dari besar-kecil berdasarkan index 1
    return list_stattipe

def statprov(): #fungsi untuk menampilkan jumlah warisan budaya per provinsi
    for key,value in dict.items():
        list_prov.append(value[2]) #ditambah dulu (HANYA PROV)
    for a in list_prov: #diiterasi lewat list_prov
        count=list_prov.count(a)
        list_statprov.append((a,count)) #menambah tuple (prov, count) kedalam list_statprov
    print(sorted(set(list_statprov), key=operator.itemgetter(1), reverse=True)) #agar data tidak dobel
    return list_statprov

def ekspor(a): #fungsi untuk ekspor data ke csv
    with open(a, 'w', newline='') as file_baru: #'w' adalahh write
        nulis_baru=csv.writer(file_baru, delimiter=",") #delimiter: untuk memisahkan data dengan ','
        list_value=[]
        for b in dict.values(): #mengiterasi value dict
            list_value.append(b) #dan menambah value ke list_value
        for c in list_value:
            nulis_baru.writerow(c) #menulis dalam baris value yang ada
        print("Terekspor", len(list_value), "baris")
        
def tolong(): #program tambahan untuk menampilkan perintah-perintah yang ada
    print("IMPOR: mengimpor csv file")
    print("EKSPOR: mengekspor kedalam csv file")
    print("CARINAMA: mencari data berdasarkan nama")
    print("CARITIPE: mencari data berdasarkan tipe")
    print("CARIPROV: mencari data berdasarkan provinsi")
    print("TAMBAH: menambah data baru")
    print("UPDATE: menyunting data yang ada")
    print("HAPUS: menghapus data yang ada")
    print("STAT: memberitahu jumlah data yang ada")
    print("STATTIPE: membertiahu jumlah data yang ada berdasarkan tipe")
    print("STATPROV: memberitahu jumlah data yang ada berdasarkan provinsi")
    print("KELUAR: keluar dari program")
    
       
dict={}
dict_update={}
list_prov=[]
list_tipe=[]
list_stattipe=[]
list_statprov=[]
counter=1
tulisan()
while(counter==1):
    a=input("Masukkan perintah: ")
    if "IMPOR" in a:
        a_impor=a[6:]
        impor(a_impor)
    elif "CARINAMA" in a:
        a_split=a[9:]
        carinama(a_split)
    elif "CARITIPE" in a:
        a_split=a[9:]
        caritipe(a_split)
    elif "CARIPROV" in a:
        a_split=a[9:]
        cariprov(a_split)
    elif "TAMBAH" in a:
        a_split=a[7:]
        tambah(a_split)
    elif "UPDATE" in a:
        a_split=a[7:]
        update(a_split)
    elif "HAPUS" in a:
        a_split=a[6:]
        hapus(a_split)
    elif a=="STAT":
        stat()
    elif a=="STATTIPE":
        stattipe()
    elif a=="STATPROV":
        statprov()
    elif "EKSPOR" in a:
        a_split=a[7:]
        ekspor(a_split)
    elif "KELUAR" in a:
        print("~Sampai jumpa, jangan lupa mencintai warisan budaya Indonesia!~")
        counter=0
        break
    else:
        print("Maaf command", a, "tidak ada:). Ingin bantuan? IYA/TIDAK")
        b=input("Masukkan perintah: ")
        if b=="IYA":
            tolong()
        else:
            pass
    print("#"*5)
        
        
