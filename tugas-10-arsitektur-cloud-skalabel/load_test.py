"""
Tugas 10 - Load Test Sederhana

Mengirim banyak request konkuren ke Load Balancer (http://localhost:8080)
dan menghitung berapa kali masing-masing instance app menangani request,
untuk membuktikan distribusi beban.
"""

import urllib.request
import threading
import time
from collections import Counter

TARGET_URL = "http://localhost:8080/"
TOTAL_REQUESTS = 300
CONCURRENCY = 30

hasil = Counter()
lock = threading.Lock()

# Semaphore dipakai untuk membatasi jumlah thread aktif (lihat TODO 3)
semaphore = threading.Semaphore(CONCURRENCY)


def kirim_request():
    # TODO 1: lakukan GET request ke TARGET_URL, baca body response
    # (yang berisi INSTANCE_ID dari app/app.py), lalu update `hasil`
    # (Counter) dengan lock supaya thread-safe.
    try:
        with urllib.request.urlopen(TARGET_URL, timeout=5) as resp:
            body = resp.read().decode()
            # TODO 2: ekstrak instance_id dari `body` sesuai format response
            # yang kalian buat di app.py, lalu:
            # with lock:
            #     hasil[instance_id] += 1

            # Kalau body-nya cuma "app1", ya langsung dipakai.
            # Kalau formatnya "Instance: app1", ambil bagian setelah titik dua.
            instance_id = body.strip().split(":")[-1].strip()
            with lock:
                hasil[instance_id] += 1
    except Exception as e:
        with lock:
            hasil["ERROR"] += 1
    finally:
        # Lepas "slot" supaya thread berikutnya boleh jalan
        semaphore.release()


def main():
    print(f"Mengirim {TOTAL_REQUESTS} request dengan concurrency {CONCURRENCY} ...")
    start = time.time()

    threads = []
    for _ in range(TOTAL_REQUESTS):
        # TODO 3: batasi jumlah thread aktif bersamaan sesuai CONCURRENCY
        # (mis. dengan semaphore, atau proses batch per CONCURRENCY thread).

        # Ambil slot dulu. Kalau sudah ada 30 thread aktif, loop akan
        # menunggu di sini sampai ada thread yang selesai.
        semaphore.acquire()

        t = threading.Thread(target=kirim_request)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    durasi = time.time() - start
    print(f"\nSelesai dalam {durasi:.2f} detik")
    print("Distribusi beban per instance:")
    for instance_id, jumlah in hasil.most_common():
        print(f"  {instance_id}: {jumlah} request")


if __name__ == "__main__":
    main()