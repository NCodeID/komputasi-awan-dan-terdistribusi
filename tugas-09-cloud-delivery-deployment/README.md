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
