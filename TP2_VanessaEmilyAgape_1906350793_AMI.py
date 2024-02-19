import string
import matplotlib.pyplot as plt

list=[]
list_satulagi=[]
list_count=[]
list_stopwords=[]
counter=1

def awalan():
    print("Distribusi frekuensi kata: ")
    print("-"*36) #Menulis "-" sebanyak 36 kali
    print('{:4s}{:21s}{:}'.format("No","Kata","Frekuensi"))
    print("-"*36)

def ngesplit(x):
    x=x.lower()
    x=x.split(" ")
    return x

def tandabaca(x):
    tanda_baca=string.punctuation
    stop_words=list_stopwords
    for b in x:
        #Jika b masuk stop words
        if b in stop_words:
            continue
        #kalau ada tanda baca
        for c in b:
            if c in tanda_baca:
                #kalau tanda '-' dibiarkan
                if c=='-':
                    pass
                #selain itu diganti
                else:
                    b=b.replace(c,"")
        if b=='':
            continue
        elif b in list:
            list_satulagi.append(b)
            continue
        list.append(b)
        list_satulagi.append(b)
        #Kalau "-" masuk ke list karena ada emoticon, diremove dari list
        if "-" in list:
            list.remove("-")
        elif "-" in list_satulagi:
            list_satulagi.remove("-")
    return x

def frekuensi():
    counter2=0
    while (counter2<=len(list)):
        for b in list:
            if b=="":
                continue
            #counter2 untuk No.
            counter2+=1
            for d in list_satulagi:
                if d=="":
                    continue
                if b==d:
                    count=list_satulagi.count(d)
            #list_count untuk nampung frekuensi setiap kata
            list_count.append(count)
            print('{:3} {:21} {:}'.format(counter2,b,count))
        break
    
def stop_words():
    stop_word=open('TP2-stopword.txt', 'r')
    for i in stop_word.read().split('\n'):
        i=i.lower()
        list_stopwords.append(i)
      

#men-token kata
while counter==1:
    pesan=input("Pesan: ")
    stop_words()
    pesann=ngesplit(pesan)
    tandabaca(pesann)
    if pesan=="":
        counter-=1
        break
#menulis awalan tabel
awalan()
#menampilkan tabel
frekuensi()
print("-"*36)
#membuat matplotlib
plt.figure(figsize=(8,8))
plt.xlabel("Frekuensi")
plt.title("Frekuensi Kemunculan Kata")
plt.barh(list[::-1],list_count[::-1], align='center')
plt.show()
        
