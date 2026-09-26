# Tugas 2 (Pekan 2) — Perancangan Arsitektur untuk FoodGo

**Materi terkait:** Architectural style (Layered, SOA, Peer-to-Peer, Publish-Subscribe).

## Studi Kasus

Melanjutkan Tugas 1: FoodGo butuh sistem yang **decoupled** agar tim kurir dan tim resto tidak saling mengganggu ketika salah satu modul diperbarui/deploy ulang. Saat ini semua modul (pesanan, pembayaran, notifikasi kurir, katalog resto) berjalan sebagai satu aplikasi monolitik — sekali deploy, semua modul ikut restart dan berisiko downtime total.

## Tugas Kelompok

1. Pilih **satu** gaya arsitektur utama: **Service-Oriented Architecture (SOA)** atau **Publish-Subscribe**. Boleh dikombinasikan (mis. SOA untuk service inti + Pub-Sub untuk notifikasi), tapi harus dijustifikasi kenapa kombinasi ini yang dipilih.
2. Gambarkan minimal 4 komponen berikut dan interaksinya: modul Pesanan, modul Pembayaran, modul Kurir/Notifikasi, modul Katalog Resto (dan message broker/API gateway jika relevan).
3. Jelaskan alur satu skenario penuh secara end-to-end di diagram (misalnya: pelanggan buat pesanan → bayar → resto terima notifikasi → kurir ditugaskan) — tunjukkan komponen mana berkomunikasi dengan siapa, dan **jenis komunikasinya** (sinkron/asinkron, request-response/event).
4. Analisis tertulis: kenapa gaya ini mengatasi masalah *coupling* dari Tugas 1, dan apa trade-off-nya (mis. Pub-Sub menambah kompleksitas debugging karena alur tidak linear).

## Cara Membuat Diagram (Gratis, Cukup Laptop)

Tidak perlu software berbayar. Dua opsi:

**Opsi A — Mermaid di dalam Markdown (disarankan).** Ditulis sebagai teks biasa di `README.md`, otomatis dirender jadi diagram oleh GitHub — tidak perlu install apa pun.

````markdown
```mermaid
graph LR
  Client[Pelanggan] -->|HTTP request pesan| OrderSvc[Service Pesanan]
  OrderSvc -->|RPC sinkron| PaymentSvc[Service Pembayaran]
  OrderSvc -->|publish event OrderCreated| Broker[(Message Broker)]
  Broker -->|subscribe| NotifSvc[Service Notifikasi Kurir]
  Broker -->|subscribe| RestoSvc[Service Katalog Resto]
```
````

**Opsi B — draw.io / diagrams.net** (gratis, jalan di browser tanpa akun, atau app desktop offline di [app.diagrams.net](https://app.diagrams.net/)). Ekspor sebagai `.png` dan simpan di folder `diagram/`.

## Struktur Submission

```
tugas-02-perancangan-arsitektur/
├── README.md          # Analisis + diagram Mermaid (jika Opsi A) atau referensi ke diagram/
├── JURNAL.md
└── diagram/            # File .png/.drawio jika pakai Opsi B
```

## Rubrik Penilaian (Tugas 2)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan pemilihan gaya arsitektur | 20% | Justifikasi SOA/Pub-Sub sesuai kebutuhan *decoupling* di skenario |
| Kelengkapan & kejelasan diagram | 30% | Semua komponen kunci ada, jenis komunikasi (sinkron/asinkron) jelas ditandai |
| Analisis trade-off | 30% | Bukan hanya kelebihan — kekurangan/kompleksitas baru juga dibahas |
| Proses & kontribusi kelompok | 20% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh memakai AI untuk brainstorming komponen apa saja yang umum ada di gaya arsitektur SOA/Pub-Sub; **tidak boleh** meminta AI menggambar diagram final atau menuliskan analisis trade-off yang tinggal ditempel. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Diagram Mermaid/draw.io yang "terlalu generik" (identik dengan contoh tutorial di internet tanpa penyesuaian ke kasus FoodGo) akan dinilai rendah pada komponen kelengkapan & kejelasan diagram.


## Hasil Diskusi Kelompok
**1. Pemilihan Arsitektur**
<div style="text-align: justify">
Kami menerapkan SOA dan Pub-Sub untuk menjamin alur jalannya sistem kami. Dengan SOA, setiap layanan bersifat decoupled atau tidak terikat satu dengan yang lain, sehingga jika terjadi kendala pada satu layanan,maka layanan lain tetap dapat berjalan normal. Selain itu, model Pub-Sub kami pilih karena proses  yang ada berjalan asinkron, yang memungkinkan proses komunikasi menjadi lebih efisien melalui message broker.
</div>

**2. Diagram Arsitektur**
``` mermaid
graph LR
  Client[Aplikasi Client FoodGo]
  Gateway[API Gateway]
  OrderSvc[Service Pesanan]
  PaymentSvc[Service Pembayaran]
  Broker[Message Broker - RabbitMQ / Kafka]
  Topic[Topic: order.events]
  RestoSvc[Service Katalog Resto]
  NotifSvc[Service Notifikasi Kurir]
  NotifCustomerSvc[Service Notifikasi Pelanggan]

  Client -->|"1. HTTP Request (sinkron)"| Gateway
  Gateway -->|"2. Route Request"| OrderSvc
  OrderSvc <-->|"3. RPC Sinkron (gRPC + Timeout)"| PaymentSvc
  OrderSvc -->|"4. Publish Event: OrderPaid"| Broker
  Broker --> Topic
  Topic -->|"5a. Subscribe Event"| RestoSvc
  Topic -->|"5b. Subscribe Event"| NotifSvc
  Topic -->|"5c. Subscribe Event"| NotifCustomerSvc
  NotifCustomerSvc -.->|"6. Push Notification"| Client
```
<br/>

**3. Alur Sistem End-to-End**  
<div style="text-align: justify">
Skenario dimulai ketika pelanggan menekan tombol pesan di Aplikasi FoodGo, yang memicu pengiriman HTTP Request secara sinkron (request-response) menuju API Gateway untuk kemudian diteruskan ke Service Pesanan (OrderSvc). Karena transaksi finansial membutuhkan kepastian instan, OrderSvc langsung memanggil Service Pembayaran (PaymentSvc) melalui komunikasi RPC yang juga bersifat sinkron, lengkap dengan mekanisme timeout untuk mencegah sistem macet jika jaringan pembayaran lambat. Setelah pembayaran dinyatakan sukses, OrderSvc menyelesaikan tugas transaksionalnya dan beralih menggunakan komunikasi asinkron (event-driven) dengan publish sebuah pesan kejadian yaitu event OrderPaid ke dalam Message Broker pada topic "order.events". Kemudian tiga layanan service secara otomatis subscribe topik tersebut secara asinkron. Lalu RestoSvc menerima pesan untuk mulai memasak makanan di dapur, NotifSvc bereaksi untuk menugaskan kurir terdekat, dan NotifCustomerSvc mengambil data untuk pelacakan. Lalu pada akhirnya NotifCustomerSvc secara asinkron mengirimkan Push Notification kembali ke Aplikasi Client untuk mengabarkan kepada pelanggan bahwa pesanan dan pembayarannya sedang diproses dengan sukses.
</div>
<br/>

**4. Analisis Solusi Coupling dan Trade-Off**
<div style="text-align: justify">
<strong>Analisis Solusi Coupling:</strong><br/>
Arsitektur SOA memecah fungsi sistem menjadi layanan‑layanan yang terpisah (tidak monoltik) sehingga tidak saling “terikat” satu sama lain. arsitektur pub-sub sendiri berkomunikasi antar layanan dilakukan lewat message broker, jadi mereka tidak perlu terhubung secara langsung. Sistem harus dapat mengatasi keterlambatan, kegagalan pengiriman, dan kemungkinan pesan diproses lebih dari sekali.
</div>

<div style="text-align: justify">
<strong>Trade Off:</strong> <br/>
Menukar masalah coupling dengan kompleksitas debugging dan asinkronitas data. Karena alur komunikasi kini bersifat asinkron dan tidak linear, troubleshooting menjadi lebih sulit akibat jejak data tersebar di berbagai modul dan message broker. Selain itu, karena seluruh proses menjadi asinkron, validasi pembayaran tidak lagi terjadi secara real time.
</div>