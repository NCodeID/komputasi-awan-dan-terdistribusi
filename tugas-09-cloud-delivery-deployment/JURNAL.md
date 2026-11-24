# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Private Cloud dipilih karena pemerintah perlu memiliki kendali penuh atas infrastruktur yang menyimpan data kependudukan. Untuk mengatasi lonjakan akses, pemerintah dapat menyiapkan kapasitas server tambahan dan membatasi jumlah permintaan dari setiap instansi. Sementara itu, portal publik dapat menggunakan layanan cloud dari pihak luar selama tidak memuat data sensitif.

## Diskusi service model per komponen
- Prinsip pembagian layanan: Kami sepakat memisahkan komponen berdasarkan tingkat sensitivitas datanya agar tetap patuh pada UU PDP tanpa mengorbankan skalabilitas saat lonjakan akses.
- Komponen data sensitif (IaaS & PaaS Private Cloud): Database inti kependudukan (NIK, alamat, biometrik) dan *disaster recovery* ditempatkan di IaaS *private cloud* agar negara memegang kendali penuh hingga level OS, enkripsi, dan audit fisik. Sementara itu, API verifikasi identitas menggunakan PaaS di atas *private cloud* untuk mempermudah *auto-scaling* dan *rate limiting* antar-instansi.
- Komponen non-sensitif (PaaS & SaaS Publik): Portal publik pengecekan status dan layanan notifikasi (email/SMS) dialihkan ke PaaS/SaaS publik karena hanya memproses nomor tiket/status tanpa menyentuh data pribadi warga. Begitu pula SIEM/logging yang dibatasi hanya mencatat metadata akses.
- Beberapa risiko yang perlu diperhatikan adalah keterbatasan kapasitas server, kebocoran data pribadi ke layanan luar, dan penyalahgunaan akses oleh pihak yang tidak berwenang. Risiko tersebut dapat dikurangi melalui penambahan kapasitas server, penyaringan data, pembatasan akses, dan pemantauan aktivitas setiap instansi.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
