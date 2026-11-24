# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Private Cloud dipilih karena pemerintah perlu memiliki kendali penuh atas infrastruktur yang menyimpan data kependudukan. Untuk mengatasi lonjakan akses, pemerintah dapat menyiapkan kapasitas server tambahan dan membatasi jumlah permintaan dari setiap instansi. Sementara itu, portal publik dapat menggunakan layanan cloud dari pihak luar selama tidak memuat data sensitif.

## Diskusi service model per komponen
- Pemilihan service model disesuaikan dengan kebutuhan setiap komponen. IaaS digunakan untuk database utama dan cadangan data agar tetap berada di bawah kendali pemerintah. PaaS pada Private Cloud digunakan untuk API verifikasi identitas agar tim pengembang dapat lebih fokus pada pengembangan aplikasi tanpa harus mengurus infrastruktur secara langsung. Untuk layanan pendukung seperti portal publik, monitoring, pencatatan log, dan notifikasi, digunakan PaaS atau SaaS sesuai kebutuhan masing-masing.
- Beberapa risiko yang perlu diperhatikan adalah keterbatasan kapasitas server, kebocoran data pribadi ke layanan luar, dan penyalahgunaan akses oleh pihak yang tidak berwenang. Risiko tersebut dapat dikurangi melalui penambahan kapasitas server, penyaringan data, pembatasan akses, dan pemantauan aktivitas setiap instansi.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
