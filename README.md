
# Sentimen Analisis dengan Flask dan Docker
Analisis sentimen menggunakan produk review di bukalapak. Untuk mengambil data tidak digunakan menggunakan scraping, melainkan crawling menggunakan link API yang ada.

## Audience
Platform ini bisa digunakan baik untuk para seller, di mana:
- Seller dapat melihat apakah feedback dari pelanggan terhadap produk yang dijual berisi komentar yang baik
- Dari sentimen yang ada seller dapat memperbaiki kualitas produk atau memperbaiki kualitas pelayanan
- Mengetahui seberapa banyak feedback positif dari konsumen

## Data
Data diambil dari web product review bukalapak yang ada [di sini](https://www.bukalapak.com/reviews/handphone/aksesoris-handphone/charger-177/k2a7ub-jual-batok-charger-samsung-2a-adaptor-2-ampere-samsung-oppo-xiaomi-kepala-charger-hp)

Data | Keterangan
:---: | :---
user | nama akun pengguna
review | review dari pengguna berupa teks
rate | rating dari pengguna dari 1-5
label | positif untuk rating 4-5 <br> negatif untuk rating 1-3

## Desain
Desain yang digunakan dalam data produk kali ini seperti gambar di bawah ini


## Display
Referensi tampilan display: [link](https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776)