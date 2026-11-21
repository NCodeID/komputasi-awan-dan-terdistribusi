# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.

## Analisis Sistem Data Kependudukan

### 1. Rekomendasi deployment model

Menggunakan **Private Cloud** yang dikelola langsung oleh pemerintah untuk Sistem Data Kependudukan. Alasannya:

| Karakteristik NIST | Penerapan pada sistem |
|---|---|
| **On-demand self-service** | Tim pemerintah dapat membuat VM atau menambah kapasitas aplikasi secara otomatis sesuai kebutuhan, tetapi tetap mengikuti batas penggunaan dan aturan akses yang sudah ditentukan. |
| **Broad network access** | Berbagai instansi seperti Dukcapil, kepolisian, dan bank dapat mengakses layanan melalui jaringan yang sudah disediakan, misalnya menggunakan HTTPS. Namun, setiap akses tetap diperiksa agar hanya pihak yang memiliki izin yang dapat menggunakan layanan tersebut. |
| **Resource pooling** | Sumber daya seperti server, penyimpanan, dan jaringan milik pemerintah digunakan bersama sesuai kebutuhan setiap layanan. Akses ke database utama juga dipisahkan dan dibatasi agar data kependudukan tetap aman. |
| **Rapid elasticity** | Kapasitas server dan aplikasi dapat ditambah atau dikurangi sesuai jumlah pengguna. Saat terjadi lonjakan akses, seperti musim pemilu atau pendaftaran sekolah, pemerintah perlu menyiapkan kapasitas tambahan agar sistem tetap berjalan lancar tanpa membebani database utama. |
| **Measured service** | Penggunaan sumber daya seperti CPU, penyimpanan, bandwidth, dan jumlah permintaan dari setiap instansi dipantau dan dicatat. Tujuannya agar penggunaan dapat dikontrol, kapasitas bisa direncanakan, dan aktivitas akses dapat diawasi tanpa menyimpan data sensitif seperti NIK atau biometrik secara langsung dalam log. |

### 2. Rekomendasi service model

Sistem ini **tidak memakai satu service model untuk semua komponennya**. Komponen yang menyentuh data pribadi (NIK, biometrik, alamat) tetap dijalankan di **IaaS** supaya pemerintah memegang kendali penuh atas server, sistem operasi, dan penyimpanan. Komponen pendukung yang tidak menyimpan data sensitif boleh memakai **PaaS** atau **SaaS** agar tim tidak perlu mengurus infrastruktur sendiri. Pembagiannya sebagai berikut:

| Komponen sistem | Service model | Penerapan pada sistem |
|---|---|---|
| **Database inti kependudukan** (NIK, alamat, biometrik) | **IaaS** (private cloud) | Database berjalan di VM atau bare metal milik pemerintah. Tim melakukan instalasi pada sistem operasi, konfigurasi database, enkripsi data saat disimpan (*at-rest*), kunci enkripsi, dan isolasi jaringan. Komponen ini tidak diserahkan ke PaaS karena datanya paling sensitif dan lokasi fisiknya harus bisa diaudit. |
| **API verifikasi identitas** (dipakai Dukcapil daerah, kepolisian, dan bank untuk KYC) | **PaaS** (private cloud) | Platform mengurus deployment, scaling otomatis, dan pembagian beban, sehingga tim cukup fokus pada logika verifikasi dan aturan akses per instansi. Scaling otomatis menangani banyaknya permintaan verifikasi tanpa membebani database inti, sedangkan pembatasan laju permintaan per instansi tetap diterapkan. |
| **Portal publik pengecekan status** (mis. status permohonan dokumen) | **PaaS** (public cloud) atau **SaaS** | Portal hanya menampilkan status non-sensitif, seperti nomor tiket dan tahap proses, dan tidak memanggil database inti secara langsung; datanya dibaca dari replika atau cache khusus baca. Karena tidak menyimpan NIK maupun biometrik, portal aman diletakkan di public cloud agar lonjakan trafik musiman tertampung tanpa membebani private cloud. |
| **Pemantauan dan log akses (SIEM)** | **SaaS** atau **PaaS** | Pengumpulan metrik, log akses, dan peringatan diserahkan ke layanan terkelola. Sesuai poin 1, log hanya berisi metadata seperti waktu, instansi, dan endpoint, tanpa NIK atau biometrik, sehingga tidak ada data pribadi yang keluar dari kendali pemerintah. |
| **Cadangan dan pemulihan bencana** (*disaster recovery*) | **IaaS** (object storage private, di luar lokasi) | Cadangan disimpan di object storage terenkripsi dan direplikasi ke lokasi terpisah. Tetap IaaS karena salinan database inti berisi data mentah yang harus dikelola sendiri, bukan diserahkan ke layanan pihak ketiga. |
| **Notifikasi ke warga** (email/SMS status permohonan) | **SaaS** | Layanan pengiriman notifikasi berlangganan. Isi pesannya hanya nomor tiket dan tautan, bukan data pribadi kependudukan. |

 Kesimpulan pembagian:  **komponen yang menyimpan atau memproses data pribadi tetap di IaaS/private cloud, sedangkan komponen yang hanya menangani metadata atau status boleh memakai PaaS/SaaS.** Dengan begitu, skalabilitas tetap didapat dari layanan dapat terkelola tanpa menyerahkan data kependudukan ke infrastruktur yang tidak dikendalikan oleh negara.

### 3. Risiko spesifik dan mitigasinya

Penggunaan **Private Cloud** sebagai pusat data utama yang digabungkan dengan layanan **PaaS/SaaS luar** untuk kebutuhan pendukung memiliki beberapa risiko yang perlu diantisipasi:

1. **Server Private Cloud penuh saat akses melonjak bersamaan**
   * **Risiko:** Karena memakai Private Cloud milik pemerintah, jumlah server fisiknya terbatas. Saat musim pemilu atau pendaftaran sekolah, ribuan instansi (Dukcapil, bank, kepolisian) mengakses layanan secara bersamaan sehingga server berisiko penuh dan layanan verifikasi menjadi lambat atau mati (*downtime*).
   * **Mitigasi:** Menyiapkan cadangan kapasitas server jauh hari sebelum jadwal pemilu atau tahun ajaran baru. Selain itu, membatasi jumlah permintaan per detik dari tiap instansi dan menyimpan sementara hasil verifikasi yang sering dicek agar beban database utama berkurang.

2. **Data pribadi tidak sengaja ikut terkirim ke layanan luar**
   * **Risiko:** Pada rancangan poin 2, portal pengecekan status, pencatatan log, dan pengiriman notifikasi memakai layanan luar (PaaS/SaaS publik) agar lebih ringan. Jika terjadi kesalahan pengaturan sistem, data rahasia seperti NIK, nama, atau alamat bisa ikut terkirim dan tersimpan di server pihak ketiga tersebut.
   * **Mitigasi:** Menyaring data sebelum keluar dari jaringan pemerintah sehingga hanya nomor tiket dan status proses yang dikirim ke portal publik atau pesan notifikasi. Sistem pencatatan log juga diatur agar otomatis menyembunyikan angka NIK jika tidak sengaja tercatat.

3. **Penyalahgunaan akses jika sistem instansi mitra diretas**
   * **Risiko:** Karena sistem terhubung dengan ribuan instansi seperti bank dan Dukcapil daerah, jika akun atau sistem di salah satu daerah diretas, pelaku bisa memakai jalur akses tersebut untuk mengambil data kependudukan dalam jumlah besar.
   * **Mitigasi:** Mewajibkan jalur koneksi khusus yang terenkripsi serta verifikasi identitas perangkat untuk setiap instansi mitra. Sistem juga memantau pola akses secara rutin—jika ada instansi yang meminta data secara tidak wajar (misalnya ribuan data di tengah malam), aksesnya langsung diblokir sementara.

---

### 4. Perbandingan dengan alternatif yang ditolak

Alternatif yang ditolak dalam rancangan ini adalah **Public Cloud murni**, yaitu menaruh seluruh sistem—termasuk database inti NIK, alamat, dan data biometrik—di server milik penyedia layanan cloud komersial.

| Aspek Perbandingan | Pilihan Kami (Private Cloud + Layanan Luar Non-Sensitif) | Alternatif Ditolak (Public Cloud Murni) |
|---|---|---|
| **Kendali atas data rahasia** | **Penuh di tangan negara.** Server fisik, sistem, dan pengamanan database dikelola langsung oleh pemerintah. | **Terbatas.** Server fisik dikelola oleh perusahaan penyedia layanan cloud pihak ketiga. |
| **Keamanan & kepatuhan UU PDP** | **Tinggi.** Data pribadi warga tidak bercampur dengan pengguna umum dan lebih mudah diaudit oleh negara. | **Kurang sesuai.** Berisiko melanggar aturan karena data kependudukan berada di luar kendali penuh negara. |
| **Penanganan lonjakan akses** | **Cukup dan terukur.** Trafik portal publik dialihkan ke layanan luar, sedangkan akses verifikasi diatur batasannya. | **Sangat besar**, tetapi berlebihan jika harus mengorbankan keamanan data inti kependudukan. |

**Alasan Penolakan:**
Public Cloud murni ditolak karena bertentangan dengan syarat utama sistem, yaitu data kependudukan yang sangat rahasia wajib berada di bawah kendali penuh negara sesuai UU Perlindungan Data Pribadi. Kemudahan Public Cloud dalam menampung lonjakan akses sebenarnya sudah bisa ditutupi oleh rancangan kami, yaitu dengan memindahkan portal publik (yang tidak menyimpan data pribadi) ke layanan PaaS/SaaS luar. Dengan begitu, pemerintah tetap aman dari lonjakan pengunjung tanpa harus menyerahkan database kependudukan ke pihak luar.
