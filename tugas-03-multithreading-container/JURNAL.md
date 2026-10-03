# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 10 dari 100 pesanan
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): nilai `processed_count` digunakan bersamaan bersama oleh beberapa thread. Tanpa lock, beberapa thread membaca nilai `processed_count` secara bersamaan sebelum salah satu thread menyimpan hasil perubahannya. Karena hal tersebut, hasil increment dari salah satu thread dapat tertimpa oleh thread lain.

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: 100 dari 100 pesanan
- Hasil processed_count setelah perbaikan
Dengan penambahan fitur lock maka saat thread melakukan perubahan, thread lainnya akan menunggu hingga perubahan tersebut selesai sehingga tidak akan terjadi saling timpa menimpa

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: 
- Tidak ada.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
