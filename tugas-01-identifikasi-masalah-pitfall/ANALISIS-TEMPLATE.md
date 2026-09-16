# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| NATAN WINSON PRATAMA | 103072400025 | 1 |
| BERTRAND LIANTO | 103072400019 | 2 |
| NAYOTTAMA LUCKY MUSTAFA | 103072430011 | 3 |

## Pitfall 1: The Network is Reliable — ditulis oleh NATAN WINSON PRATAMA

**Bukti di skenario:** "# network is always reliable, no need for retry"

**Kenapa ini keliru:** Sejauh yang saya ketahui ketika sebuah _client_ melakukan koneksi terhadap suatu server tentunya ada beberapa hal yang perlu diperhatikan seperti _packet loss_, _downtime_ yang dimana hal - hal ini dapat membuktikan bahwasannya sebuah jaringan tidak lah 100% reliable  

**Dampak ke FoodGo:** Dalam studi kasus FoodGo apabila terjadi packet loss dan juga downtime maka beberapa fitur yang ada seperti pesanan dan pembayaran tentunya akan mengalami penurun kecepatan akses dan bahkan tidak dapat diakses sama sekali.

**Solusi desain awal:** Menyediakan fungsi coba lagi (dalam bentuk button atau _swipe up to refresh_).

**Trade-off:** Apabila kita lihat dalam segi UX (User Experience) ketika fitur ini disediakan, apabila ketika tombol ditekan dan sistem tetap menampilkan error atau tidak terload maka pengguna dapat merasa kesal .
Lalu apabila tombol ditekan secara terus - menerus (spam) dalam jumlah yang banyak maka traffic server akan jauh lebih besar yang mengakibatkan aplikasi menjadi lebih lambat.

---

## Pitfall 2: [Latency is Zero] — ditulis oleh BERTRAND LIANTO

**Bukti di skenario:** "tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)."

**Kenapa ini keliru:** Karena untuk melakukan pemanggilan antar service diperlukan waktu yang tidak terjadi secara instan, sehingga diperlukan adanya timeout bila sebuah pemanggilan sebuah service melewati batas waktu tertentu.

**Dampak ke FoodGo:** Bila sebuah pemanggilan sebuah service tidak ada timeout, maka akan ada banyak permintaan yang masuk, yang menyebabkan server kewalahan sehingga aplikasi akan menjadi sangat lambat.

**Solusi desain awal:** Memberikan timeout pada sebuah pemanggilan service sehingga ketika ada permintaan yang membutuhkan waktu yang sangat lama, maka permintaan itu akan dihapus sehingga permintaan yang masuk akan jauh lebih sedikit, dan aplikasi akan menjadi lebih ringan. 

**Trade-off:** Tidak ada trade off.

---

## Pitfall 3: [nama pitfall] — ditulis oleh NAYOTTAMA LUCKY MUSTAFA

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
