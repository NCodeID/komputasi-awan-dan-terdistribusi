# Komputasi Awan & Sistem Terdistribusi — Repositori Tugas
 
Repositori ini berisi seluruh tugas mata kuliah **Sistem Terdistribusi & Komputasi Awan**, dari **Tugas 1** sampai **Tugas 15**, disusun per pekan mengikuti RPS. Semua tugas dirancang dengan tiga batasan ketat:

1. **Cukup laptop.** Tidak ada tugas yang mewajibkan sewa VM cloud berbayar. Simulasi "server", "VM", atau "cluster" dijalankan lokal memakai Docker/Docker Compose di laptop masing-masing. Untuk Tugas 12 (PaaS) mahasiswa memang perlu mendaftar akun **gratis** (free tier, tanpa kartu kredit/tagihan) di penyedia PaaS — dijelaskan detail di folder tugasnya.
2. **Kerja kelompok, tanggung jawab jelas.** Tiap tugas dikerjakan berkelompok (3–4 orang), dengan pembagian peran yang tercatat lewat commit history GitHub masing-masing anggota (bukan cuma commit dari satu orang).
3. **Penggunaan AI dibatasi di Level 2 (AI Assisted Idea Generation & Structuring)**, mengikuti kerangka 5-Level Penggunaan AI Telkom University. AI **boleh** dipakai untuk brainstorming ide awal atau membantu menyusun outline/struktur — **tidak boleh** dipakai untuk menghasilkan isi akhir (kode, analisis, diagram, teks README) yang tinggal disalin. Setiap tugas mewajibkan dokumentasi proses berpikir (*thought process*) dan log penggunaan AI (jika ada) sebagai verifikasi. Detail lengkap ada di [`RUBRIK-UMUM.md`](RUBRIK-UMUM.md).

**Mulai dari sini:** baca [`HANDBOOK.md`](HANDBOOK.md) — panduan lengkap cara fork, setup laptop (Git, Docker, Python), alur commit per kelompok, sampai cara submit tiap tugas.

## Struktur Repositori

```
.
├── HANDBOOK.md                              # Panduan lengkap untuk mahasiswa
├── RUBRIK-UMUM.md                           # Rubrik penilaian & aturan anti-AI yang berlaku di semua tugas
├── .github/workflows/                       # Berisi workflow contoh untuk Tugas 14 (GitHub Secrets)
├── tugas-01-identifikasi-masalah-pitfall/
├── tugas-02-perancangan-arsitektur/
├── tugas-03-multithreading-container/
├── tugas-04-rpc-message-queue/
├── tugas-05-koordinasi-konsensus/
├── tugas-06-penamaan-dht/
├── tugas-07-konsistensi-data/
├── tugas-08-uts/                            # UTS — bukan tugas take-home, lihat isinya
├── tugas-09-cloud-delivery-deployment/
├── tugas-10-arsitektur-cloud-skalabel/
├── tugas-11-implementasi-iaas/
├── tugas-12-implementasi-paas/
├── tugas-13-saas-twelve-factor/
├── tugas-14-keamanan-cloud/
└── tugas-15-studi-kasus-akhir/
```

Setiap folder `tugas-XX-.../` punya `README.md` sendiri berisi: studi kasus, tujuan belajar, langkah kerja, struktur submission, dan rubrik penilaian spesifik.

## Instruksi Singkat untuk Mahasiswa

1. **Fork** repositori ini ke akun GitHub kelompok (satu akun perwakilan kelompok, sebutkan anggota lain di `README.md` submission).
2. Setiap pekan, kerjakan tugas **di dalam folder `tugas-XX-...` yang sesuai** — jangan buat folder baru di root.
3. Ikuti struktur submission yang diminta di README masing-masing tugas (biasanya: `README.md` analisis, `src/` kode, `bukti/` screenshot atau video demo).
4. Commit sesering mungkin dengan pesan yang deskriptif — commit history adalah bagian dari penilaian (lihat [`RUBRIK-UMUM.md`](RUBRIK-UMUM.md)).
5. Jika memakai AI untuk brainstorming/structuring (Level 2), catat sesi pemakaiannya di bagian "Log Penggunaan AI" pada `JURNAL.md` tugas terkait.
6. **Sebelum deadline, buat git tag** menandai commit final tugas tersebut (mis. `tugas-03-submit`), push tag-nya, lalu **kumpulkan link permalink ke folder tugas pada tag tersebut** di assignment terkait di LMS (Moodle). Lihat tutorial lengkap + contoh di [`HANDBOOK.md`](HANDBOOK.md#25-cara-submit-tugas-git-tag--link-ke-lms-moodle) — **bukan** lewat Pull Request.

Selamat mengerjakan — pakai AI secukupnya untuk mencari ide, tapi pastikan tangan (dan otak) kalian sendiri yang menulis, mengetik, dan men-debug hasil akhirnya. 
