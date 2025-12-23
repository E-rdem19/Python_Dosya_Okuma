# Python Dosya Okuma

Bu depo, Python ile farklı dosya türlerini (txt, CSV, JSON ve ikili dosyalar) güvenli ve doğru bir şekilde okumak için örnekler, yardımcı fonksiyonlar ve en iyi uygulamaları içerir. Eğitim amaçlı hazırlanmıştır ve dosya okuma ile ilgili sık karşılaşılan sorunları (kodlama hataları, büyük dosyalar, hata yönetimi) nasıl çözeceğinizi gösterir.

## İçerik

- examples/: Örnek Python betikleri
- utils/: Dosya okuma yardımcı fonksiyonları (örnekler)
- data/: Örnek veri dosyaları (isteğe bağlı)

## Gereksinimler

- Python 3.8+
- (Opsiyonel) requirements.txt içindeki paketler

## Kullanım

Aşağıdaki örnekler temel kullanım senaryolarını gösterir.

1) Basit metin dosyası okuma

```python
# examples/read_text.py
with open('data/example.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print(text)
```

2) Sat��r satır okuma (bellek dostu)

```python
# examples/read_lines.py
with open('data/large_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        process(line)
```

3) CSV okuma (csv modülü)

```python
import csv

with open('data/example.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

4) JSON okuma

```python
import json

with open('data/example.json', 'r', encoding='utf-8') as f:
    obj = json.load(f)
print(obj)
```

5) Hata yönetimi ve kodlama tespiti

```python
def safe_read(path, encodings=('utf-8', 'latin-1', 'cp1254')):
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode file: {path}")
```

## Büyük dosyalar ve performans

- Dosyayı parça parça okumak için `read()` yerine `for line in f` kullanın.
- Bellek sınırları olan ortamlarda generator tabanlı işlemler tercih edin.

## Test ve örnekler

- examples/ içindeki betikleri çalıştırarak örnekleri deneyin.

## Katkı

Katkı sağlamak isterseniz: bir issue açın veya pull request gönderin. Kod standartlarına uyun ve küçük, açıklayıcı commit mesajları kullanın.

## Lisans

Varsayılan olarak MIT lisansı önerilir; isterseniz projeye uygun lisansı ekleyin.

---

README içeriğini repository'nin köküne README.md olarak ekle. Kullanmak istediğiniz özel başlık, Türkçe/İngilizce çeviri veya ek örnekler varsa belirtin, ben güncelleyeyim.
