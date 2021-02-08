
# Sentimen Analisis dengan Flask dan Docker
<p align="justify">
Analisis sentimen menggunakan produk review di bukalapak. Untuk mengambil data tidak digunakan menggunakan scraping, melainkan crawling menggunakan link API yang ada.

## Audience
Platform ini bisa digunakan untuk para seller, di mana:
- Seller dapat melihat apakah feedback dari pelanggan terhadap produk yang dijual berisi komentar yang baik
- Dari sentimen yang ada seller dapat memperbaiki kualitas produk atau memperbaiki kualitas pelayanan
- Mengetahui seberapa banyak feedback positif dari pelanggan

## Data
Data diambil dari web product review bukalapak yang ada [di sini](https://www.bukalapak.com/reviews/handphone/aksesoris-handphone/charger-177/k2a7ub-jual-batok-charger-samsung-2a-adaptor-2-ampere-samsung-oppo-xiaomi-kepala-charger-hp)

Data | Keterangan
:---: | :---
user | Nama akun pengguna
review | Review dari pengguna berupa teks
rate | Rating dari pengguna dari 1-5
label | Positif (1) untuk rating 4-5 <br> Negatif (0) untuk rating 1-3

## Desain
Desain yang digunakan dalam data produk kali ini seperti gambar di bawah ini
<br>
![desain](https://github.com/anisaiue/Data-Product_Final-Task-Bootcamp-QTI/blob/main/README/Desain.png)


## Delivery
Referensi tampilan web: [link](https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776)
<br/>
**Tampilan home**
<br>
![home](https://github.com/anisaiue/Data-Product_Final-Task-Bootcamp-QTI/blob/main/README/home.jpeg)
<br>
<br>
**Tampilan hasil positif**
<br>
![positif](https://github.com/anisaiue/Data-Product_Final-Task-Bootcamp-QTI/blob/main/README/positif.jpeg)
<br>
<br>
**Tampilan hasil negatif**
<br>
![negatif](https://github.com/anisaiue/Data-Product_Final-Task-Bootcamp-QTI/blob/main/README/negatif.jpeg)
