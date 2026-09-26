# Jurnal Proses — Tugas 2

## 23/09/2026
- Opsi arsitektur yang dipertimbangkan: Pub-Sub
- Kenapa akhirnya pilih [SOA/Pub-Sub]:  
Alasan memilih kombinasi SOA dan Pub-Sub: 
SOA digunakan untuk interaksi yang membutuhkan validasi seketika (request-response sinkron), yaitu dari pelanggan ke modul pesanan, dan modul pesanan ke modul pembayaran. Sedangkan Pub-Sub dipilih karena arsitektur ini menerapkan sistem message broker. Modul Pesanan sebagai publisher tidak perlu terikat secara langsung dengan Modul Kurir atau Resto sebagai subscriber. Jika Modul Kurir mengalami gangguan atau crash, Modul Pesanan tidak akan ikut terganggu , karena pesan akan ditampung sementara oleh broker sampai subscriber kembali aktif.

- Mengapa bisa mengatasi coupling:  
    1. Kelebihan:  
    - Jika tim Modul Resto sedang melakukan deploy versi baru dan servernya restart, Modul pesanan tetap bisa menerima order dari pelanggan. Order tersebut akan tertahan di Message Broker / Antrian dan baru diproses ketika servernya menyala kembali. Tidak seperti sebelumnya bila server down, maka akan terjadi downtime total.  
    - Jika beban service notifikasi kurir sedang tinggi, sistem bisa memperbanyak hanya instance server Modul Kurir-nya saja.

    2. Trade Off:  
    - Menukar masalah coupling dengan kompleksitas debugging dan asinkronitas data. Karena alur komunikasi kini bersifat asinkron dan tidak linear, troubleshooting menjadi lebih sulit akibat jejak data tersebar di berbagai modul dan message broker. Selain itu, karena seluruh proses menjadi asinkron, validasi pembayaran tidak lagi terjadi secara real time.

- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): 


    Penambahan API Gateway

        Versi 1: Langsung dari Client ke OrderSvc.
        Versi 2: Ditambahkan API Gateway sebagai titik masuk utama untuk semua request HTTP.
        Alasan: Menyediakan layer untuk:
            Routing request ke service yang tepat.
            Load balancing.
            Rate limiting.
            Autentikasi/otorisasi.
            Monitoring dan logging.

    Penambahan Service Notifikasi Pelanggan (NotifCustomerSvc)

        Versi 1: Hanya ada NotifSvc (notifikasi kurir).
        Versi 2: Ditambahkan NotifCustomerSvc untuk mengirim notifikasi ke pelanggan (misal: konfirmasi pesanan).
        Alasan: Meningkatkan pengalaman pengguna dengan memberikan feedback real-time.

    Penambahan Topic Explicit (Topic: order.events)

        Versi 1: Event langsung dari Broker ke service lain.
        Versi 2: Event dipublikasikan ke Topic terlebih dahulu, kemudian di-subscribe oleh service lain.
        Alasan: Memisahkan konsep "publisher" dan "subscriber" untuk fleksibilitas lebih besar (misal: menambahkan subscriber baru tanpa mengubah publisher).

    Penambahan Detail RPC (gRPC + Timeout)

        Versi 1: Hanya "RPC sinkron".
        Versi 2: Ditambahkan detail teknis (gRPC + timeout).
        Alasan: Memberikan konteks teknis lebih jelas tentang protokol dan batasan waktu.



## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 23/09/2026 | Groq | Apa yang membuat service dikatakan coupled | Temporal Coupling, Database Coupling, Schema Coupling, Infrastruktur. | mengaplikasikan informasi dari AI yang ada kepada studi kasus yand diberikan |
| 23/09/2026 | Gemini | Apakah urutan Pub-Sub konsisten | Tidak dijamin jika dikirim secara bersamaan | menambahkan  | Melihat studi kasus dan mempertimbangkan ringkasan AI |