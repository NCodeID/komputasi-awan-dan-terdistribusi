# Tugas 4 (Pekan 4) — Komunikasi Antar Komponen

**Materi terkait:** Remote Procedure Call (RPC), Message-Oriented Middleware (MOM)/Message Queue.

## Studi Kasus

Modul **Pembayaran** dan modul **Pesanan** FoodGo harus berkomunikasi secara reliabel. Untuk beberapa operasi (mis. cek status saldo) respons dibutuhkan **seketika** (sinkron). Untuk operasi lain (mis. kirim notifikasi "pembayaran berhasil" ke modul kurir) sistem **tidak boleh menunggu** — modul pembayaran harus tetap responsif walau modul kurir sedang sibuk/down (asinkron).

## Pilihan Tugas

Kelompok **wajib memilih salah satu jalur** di bawah (boleh mengerjakan keduanya untuk nilai eksplorasi tambahan, tapi minimal satu harus selesai penuh dengan bukti jalan):

### Jalur A — RPC (Sinkron)

Skeleton di folder `rpc/` memakai `xmlrpc` — bagian dari Python standard library, **tidak perlu install apa pun**.

- `rpc/server.py`: mensimulasikan modul Pembayaran, expose fungsi `cek_saldo(user_id)` dan `proses_pembayaran(user_id, jumlah)` lewat RPC.
- `rpc/client.py`: mensimulasikan modul Pesanan yang memanggil fungsi RPC di atas dan menunggu hasilnya.

Jalankan (dua terminal terpisah, di laptop yang sama):
```bash
python3 rpc/server.py      # terminal 1
python3 rpc/client.py      # terminal 2
```

### Jalur B — Message Queue / MOM (Asinkron)

Skeleton di folder `mq/` memakai **RabbitMQ** yang dijalankan **lokal lewat Docker** (image resmi RabbitMQ, gratis, tidak perlu daftar akun apa pun) + library Python `pika`.

```bash
cd mq
docker compose up -d           # jalankan broker RabbitMQ lokal
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 consumer.py            # terminal 1: jalankan dulu consumer (modul kurir)
python3 publisher.py           # terminal 2: kirim event (modul pembayaran)
```

- `mq/publisher.py`: mensimulasikan modul Pembayaran yang mem-publish event `pembayaran_berhasil` tanpa menunggu balasan.
- `mq/consumer.py`: mensimulasikan modul Kurir/Notifikasi yang subscribe dan memproses event tersebut kapan pun siap.

Dashboard manajemen RabbitMQ (untuk lihat antrean secara visual) otomatis aktif di `http://localhost:15672` (login default `guest`/`guest`) — sertakan screenshot dashboard ini sebagai bukti tambahan.

## Tugas Kelompok

1. Lengkapi bagian `# TODO` di jalur yang dipilih.
2. Buktikan program benar-benar berjalan (screenshot 2 terminal berdampingan, atau video).
3. Untuk Jalur B, matikan dulu `consumer.py`, jalankan `publisher.py` beberapa kali, lalu nyalakan `consumer.py` — buktikan pesan **tetap diproses** (tidak hilang) karena antrean menyimpannya. Ini adalah inti pembelajaran *asynchronous decoupling*.
4. Tulis analisis: kenapa jalur ini (RPC atau MQ) cocok untuk skenario yang kalian pilih, dan apa yang terjadi jika dipakai untuk skenario yang salah (mis. RPC dipakai untuk notifikasi kurir → modul pembayaran ikut lambat kalau kurir down).

## Struktur Submission

```
tugas-04-rpc-message-queue/
├── README.md      # Analisis: kenapa sinkron/asinkron, hasil uji "pesan tidak hilang"
├── JURNAL.md
├── rpc/            # Jalur A (jika dikerjakan)
├── mq/             # Jalur B (jika dikerjakan)
└── bukti/
```

## Rubrik Penilaian (Tugas 4)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi berjalan (minimal 1 jalur) | 35% | RPC call sukses dapat balasan, ATAU pesan MQ sukses dikonsumsi |
| Bukti *asynchronous decoupling* (khusus Jalur B) / bukti sinkron blocking (Jalur A) | 25% | Skenario consumer mati lalu nyala lagi (B), atau bukti client menunggu response (A) |
| Analisis pemilihan pola komunikasi | 25% | Justifikasi tepat berdasarkan kebutuhan sinkron vs asinkron di skenario |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum RPC/message queue ke AI; **tidak boleh** meminta AI menuliskan isi `# TODO` di `rpc/server.py`, `rpc/client.py`, `mq/publisher.py`, atau `mq/consumer.py`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `JURNAL.md` wajib menjelaskan apa yang terjadi pada request RPC jika server mati di tengah proses (Jalur A), atau ke mana pesan "hilang sementara" tersimpan saat consumer mati (Jalur B) — jawaban generik/hafalan istilah tanpa mengaitkan ke hasil percobaan sendiri akan dinilai rendah.

## Analisis Pilihan Pola Komunikasi (Soal 4)

### Jalur A — RPC (Sinkron) untuk Operasi Cek Saldo & Proses Pembayaran

**Kenapa cocok untuk skenario FoodGo:**
1. **Konsistensi transaksional**: Pelanggan harus tahu seketika apakah pembayaran berhasil/gagal sebelum lanjut ke tahap berikutnya.
2. **Validasi real-time**: Cek saldo (`cek_saldo`) dan potong saldo (`proses_pembayaran`) harus atomik dan mengembalikan status akhir saldo (tidak bisa "nanti saja").
3. **Timeout terdefinisi**: Di Tugas 2 kita sudah menambahkan mekanisme timeout pada RPC untuk mencegah unlimited blocking.

**Risiko jika RPC dipakai untuk skenario yang salah (mis. notifikasi kurir):**  
Jika `OrderSvc` memanggil `NotifSvc` (kurir) via RPC sinkron:
1. **Modul Pembayaran/Pesanan ikut lambat/diblokir** saat kurir down atau lambat merespons, thread yang menangani pesanan tertahan menunggu balasan.
2. **Cascading failure**: Saat promo besar, ribuan pesanan masuk, kemudian semua thread tertahan di RPC ke kurir dan thread pool habis, lalu server crash (single point of failure).
3. **Tidak ada retry alami**: RPC sinkron tidak menyimpan permintaan, jika kurir restart maka event notifikasi hilang.

---

### Jalur B — Message Queue (Asinkron) untuk Event Notifikasi Pembayaran Berhasil

**Kenapa cocok untuk skenario FoodGo:**
1. **Fire and forget**: Publisher selesai segera setelah `basic_publish`, tidak peduli consumer hidup/mati (decoupling).
2. **Durabilitas pesan**: Dengan `durable=True` + `delivery_mode=2`, pesan `pembayaran_berhasil` tersimpan di disk broker. Jika `consumer.py` (kurir) mati saat publisher kirim, pesan tetap aman dan diproses saat consumer nyala lagi (asynchronous decoupling).
3. **Skalabilitas consumer**: Bisa jalankan banyak instance `consumer.py` (worker pool) untuk bagi beban notifikasi kurir saat trafik naik.

**Risiko jika MQ dipakai untuk skenario yang salah (mis. cek saldo/proses pembayaran):**  
Jika `OrderSvc` kirim "cek saldo" via MQ dan menunggu reply via queue balasan:
1. **Latensi tak terduga**: Antrean bisa penuh, consumer lambat, respons sampai hitungan detik/menit sehingga pelanggan mengalami loading lama di UI "Memproses pembayaran...".
2. **Kompleksitas request-reply palsu**: Perlu correlation ID, reply to queue, dan timeout handling (mirip RPC tapi lebih rapuh).
