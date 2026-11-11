# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan: Dalam sistem e-wallet, saldo disimpan di beberapa server (node) agar layanan tetap cepat dan tersedia. (sequential consistency) membuat semua server melihat urutan perubahan yang sama, tetapi setiap perubahan harus menunggu sinkronisasi antar-server sehingga respons menjadi lambat dan layanan bisa terganggu saat jaringan terputus. (eventual consistency) jauh lebih cepat dan tetap tersedia, tetapi pengguna bisa melihat saldo lama sesaat setelah top-up, sehingga transaksi bisa ditolak padahal dana cukup. Read-Your-Writes memastikan pengguna selalu melihat hasil perubahannya sendiri, sementara sinkronisasi antar-server tetap berjalan di latar belakang.
- Kesimpulan akhir & alasan: Sistem sebaiknya memakai eventual consistency di latar belakang ditambah jaminan Read-Your-Writes bagi setiap pengguna, dengan menggunakan cara ini server dapat menjaga kecepatan dan ketersediaan sambil memastikan pengguna melihat saldo terbaru dari transaksinya sendiri. Namun, operasi debit yang berisiko membuat saldo negatif atau pembayaran ganda sebaiknya tetap diurutkan melalui satu primary, sehingga tidak sepenuhnya mengandalkan eventual consistency.

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes: pembacaan naif dari Bandung menghasilkan `0.0` setelah top-up pertama sebesar Rp50.000 di Jakarta. Setelah replikasi, Bandung membaca `50000.0`. Pada top-up kedua sebesar Rp20.000, Bandung masih membaca `50000.0`, sedangkan Read-Your-Writes langsung menghasilkan `70000.0` melalui Jakarta.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
