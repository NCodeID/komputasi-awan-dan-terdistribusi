# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Tidak ada error runtime saat pengujian. Kasus yang diperiksa adalah key di atas node terbesar harus tetap mendapatkan successor.
- Cara memperbaikinya: Node diurutkan, lalu dipilih node pertama dengan ID >= hash key. Jika tidak ada, fungsi mengembalikan node dengan ID terkecil (wrap-around).

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: Sebelum `node-medan-1` bergabung, `kurir-012` dimiliki node 136 (`node-surabaya-1`). Setelah bergabung, `kurir-012` dimiliki node 123 (`node-medan-1`). IP kurir tetap 192.168.1.21, sedangkan `kurir-001` tetap di node 102.
- Hasil sebelum & sesudah node keluar: Sebelum `node-jakarta-1` keluar, `kurir-005` dimiliki node 177 (10.0.0.1). Setelah keluar, `kurir-005` dimiliki node 40 (`node-bandung-1`, 10.0.0.3) melalui wrap-around, dengan IP kurir tetap 192.168.1.14. `kurir-001` tetap di node 102 dan `kurir-002` tetap di node 40.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
