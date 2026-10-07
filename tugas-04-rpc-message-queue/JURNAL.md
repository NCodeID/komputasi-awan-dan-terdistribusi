# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- RPC & MQ (Keduanya), alasan: Agar service yang ada pada FoodGo dapat berjalan secara sinkron dan asinkron.

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok): ...
- Pada saat melakukan percobaan antar mesin firewall menghalangi akses dari Komputer A ke Komputer B.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: <br>
Setelah pengamatan uji coba mematikan consumer, menjalankan publisher, kemudian menyalakan consumer lagi adalah pesan tidak hilang

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
