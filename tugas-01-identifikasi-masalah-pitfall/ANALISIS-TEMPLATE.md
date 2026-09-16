# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| NATAN WINSON PRATAMA | 103072400025 | 1 |
| BERTRAND LIANTO | 103072400019 | 2 |
| NAYOTTAMA LUCKY MUSTAFA | 103072430011 | 3 |

## Pitfall 1: [nama pitfall] — ditulis oleh NATAN WINSON PRATAMA

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Pitfall 2: [nama pitfall] — ditulis oleh BERTRAND LIANTO

(ulangi struktur di atas)

---

## Pitfall 3: [Single Point of Failure akibat Arsitektur Monolitik] — ditulis oleh NAYOTTAMA LUCKY MUSTAFA

**Bukti di skenario:** "satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama."

**Kenapa ini keliru:** Jika arsitektur di design [monolitik](https://binus.ac.id/bekasi/2025/06/arsitektur-monolithic/), tidak ada sekat pemisah antar modul. Selain itu, sistem monolitik sulit untuk di scale secara spesifik (misalkan FoodGo membutuhkan tambahan server untuk layanan payment, maka pada arsitektur monolitik resource seluruh aplikasi harus ditingkatkan, bukan hanya pada bagian payment).

**Dampak ke FoodGo:** Karena semua berjalan di proses yang sama, masalah di satu titik akan meruntuhkan seluruh sistem. Jadi misalkan ketika modul pesanan kehabisan thread akibat tertahan oleh modul pembayaran, menyebabkan seluruh CPU dan RAM tersedot di server tersebut. Akibatnya, server backend crash total dan seluruh fitur (bahkan notifikasi kurir yang tidak ada hubungannya dengan pembayaran) ikut mati secara bersamaan, sehingga harus di-restart manual.

**Solusi desain awal:** Mempertahankan arsitektur monolitik namun memisahkan proses penanganan beban kerja dengan menggunakan Docker. Penerapan Docker pada arsitektur monolitik memberikan isolasi proses melalui container yang berjalan secara terpisah, jadi gangguan pada satu proses tidak secara langsung memengaruhi proses lainnya (misal, apabila proses pembayaran mengalami crash, container web utama yang bertugas menerima pesanan tetap dapat berjalan). Selain itu, Docker juga mendukung auto-recover atau reload otomatis melalui konfigurasi.

**Trade-off:** Tambahan kompleksitas operasional dan pelacakan log.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
