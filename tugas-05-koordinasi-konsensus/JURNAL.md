# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: memahami alur pesan tiga jenis (ELECTION, OK, COORDINATOR) dan kapan harus memanggil `start_election()` kembali.


## Skenario 1: Start normal
- Leader yang terpilih: Node 5 (ID tertinggi)
- Log/observasi (dari `bukti/log1.txt`–`log5.txt`):

1. Semua node start berurutan (lihat timestamp "Listening di port"):
   - Node 1: 18:17:29.006
   - Node 2: 18:17:29.868
   - Node 3: 18:17:30.545
   - Node 4: 18:17:31.239
   - Node 5: 18:17:32.195

2. Setelah sleep 1 detik di `main()`, setiap node memanggil `start_election()`:
   - Node 1 mengirim ELECTION ke nodes 2,3,4,5 --> menerima OK dari node 2
   - Node 2 mengirim ELECTION ke nodes 3,4,5 --> menerima OK dari node 3
   - Node 3 mengirim ELECTION ke nodes 4,5 --> menerima OK dari node 4
   - Node 4 mengirim ELECTION ke node 5 --> menerima OK dari node 5
   - Node 5 tidak memiliki peer lebih tinggi --> `higher_peers` kosong --> tidak kirim ELECTION --> timeout 2 detik --> `declare_leader()`

3. Node 5 broadcast COORDINATOR ke semua node:
   - Semua node 1–4 menerima COORDINATOR dari node 5 dan set `leader_id = 5`:
     - Node 1: 18:17:34.243
     - Node 2: 18:17:34.244
     - Node 3: 18:17:34.244
     - Node 4: 18:17:34.244

4. COORDINATOR dikirim ulang beberapa kali (karena multiple ELECTION dari node 1–4 yang memicu multiple `declare_leader` di node 5):
   - Node 5 log menampilkan "Menjadi leader, broadcast COORDINATOR" lagi di 18:17:35.194
   - Semua node menerima COORDINATOR kedua sekitar 18:17:35.195–35.197

5. Monitoring berjalan normal: Setiap 3 detik, node 1–4 mengirim PING ke node 5

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: Node 4 (ID tertinggi kedua setelah node 5 mati)
- Berapa lama waktu sampai leader baru terdeteksi: Ketika Node 5 tidak merespons (dimatikan), sistem  mendeteksi hal tersebut dan Node 4 secara otomatis terpilih sebagai leader baru dalam waktu sekitar 3 detik. Proses ini mengikuti mekanisme algoritma Bully, di mana node dengan ID tertinggi yang masih aktif akan menjadi leader baru setelah sistem apabila leader sebelumnya bermasalah (down).

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| Tidak memakai AI | Tidak memakai AI | Tidak memakai AI | Tidak memakai AI | Tidak memakai AI |