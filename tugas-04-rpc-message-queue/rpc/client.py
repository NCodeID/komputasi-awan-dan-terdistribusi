"""
Tugas 4 - Jalur A: RPC Client (simulasi modul Pesanan)
Jalankan server.py di terminal lain terlebih dahulu.
"""

import xmlrpc.client as xc
import time


def main():
    # TODO 1: buat ServerProxy ke http://localhost:8000
    proxy = xc.ServerProxy("http://localhost:8000")

    print("Memanggil cek_saldo('user1') ... menunggu respons sinkron")
    start = time.time()
    # TODO 2: panggil proxy.cek_saldo("user1") dan cetak hasilnya + waktu tempuh
    #         (buktikan client BENAR-BENAR menunggu sampai server membalas)
    hasil = proxy.cek_saldo("user1")
    elapsed = time.time() - start
    print(f"Hasil: {hasil}, Waktu tempuh: {elapsed:.4f} detik")

    print("Memanggil proses_pembayaran('user1', 20000) ...")
    # TODO 3: panggil proxy.proses_pembayaran("user1", 20000) dan cetak hasilnya
    hasil = proxy.proses_pembayaran("user1", 20000)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
