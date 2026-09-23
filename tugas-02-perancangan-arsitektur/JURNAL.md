# Jurnal Proses — Tugas 2

## 23/09/2026
- Opsi arsitektur yang dipertimbangkan: Pub-Sub
- Kenapa akhirnya pilih [SOA/Pub-Sub]:
Alasan memilih Pub-Sub: 
Kami memilih arsitektur (Pub-Sub) karena arsitektur ini menerapkan sistem message broker. Modul Pesanan sebagai publisher tidak perlu terikat secara langsung dengan Modul Kurir atau Resto sebagai subscriber. Jika Modul Kurir mengalami gangguan atau crash, Modul Pesanan tidak akan ikut terganggu , karena pesan akan ditampung sementara oleh broker sampai subscriber kembali aktif.

- Mengapa bisa mengatasi coupling:
Kelebihan <br>
- Jika tim Modul Resto sedang melakukan deploy versi baru dan servernya restart, Modul pesanan tetap bisa menerima order dari pelanggan. Order tersebut akan tertahan di Message Broker / Antrian dan baru diproses ketika servernya menyala kembali. Tidak seperti sebelumnya bila server down, maka akan terjadi downtime total.
- Jika beban kurir sedang tinggi, sistem bisa memperbanyak hanya instance server Modul Kurir-nya saja

- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 23/09/2026 | Groq | Apa yang membuat service dikatakan coupled | Temporal Coupling, Database Coupling, Schema Coupling, Infrastruktur. | mengaplikasikan informasi dari AI yang ada kepada studi kasus yand diberikan |
| 23/09/2026 | Gemini | Apakah urutan Pub-Sub konsisten | Tidak dijamin jika dikirim secara bersamaan | menambahkan  | Melihat studi kasus dan mempertimbangkan ringkasan AI |