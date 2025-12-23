import os
import re

base_dir=os.path.dirname(os.path.abspath(__file__))
data_klasoru=os.path.join(base_dir,"data")
dosya_yolu=os.path.join(data_klasoru,"metin.txt")
if not os.path.exists(data_klasoru):
    os.makedirs(data_klasoru)

def okuma(dosya_yolu1):
    with open(dosya_yolu1, "r", encoding="utf-8") as file:
        veri = file.read()
        return veri

#okuma(dosya_yolu)
def yeni_satir_ekle(dosyayolu2,veri):
    with open(dosyayolu2,"a",encoding="utf-8")as file:
        file.write("\n"+veri)
        print("veri eklendi.")

def sifir_veri_ekleme(datayolu,veri):
    with open(datayolu,"w",encoding="utf-8")as file:
        file.write(veri)
        print("veri eklendi")


#data=input("Ekleyeceğiniz veriyi giriniz:")
#sifir_veri_ekleme(dosya_yolu,data)
#okuma(dosya_yolu)

def en_cok_gecen_kelime(metin):
    kelimeler = re.findall(r"\b\w+\b", metin.lower())
    sayac = {}

    for kelime in kelimeler:
        sayac[kelime] = sayac.get(kelime, 0) + 1

    return max(sayac, key=sayac.get)

metin = okuma(dosya_yolu)
sonuc = en_cok_gecen_kelime(metin)
print("En çok geçen kelime:", sonuc)

