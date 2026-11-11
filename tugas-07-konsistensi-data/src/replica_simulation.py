"""
Tugas 7 (opsional) - Simulasi Replikasi Dua Server (Jakarta & Bandung)

Mensimulasikan delay replikasi dan masalah inconsistent read,
lalu memperbaikinya dengan mekanisme Read-Your-Writes sederhana.
"""

import time
import threading

REPLICATION_DELAY = 2.0  # detik, simulasi lambatnya sinkronisasi antar server


class Replica:
    def __init__(self, name: str):
        self.name = name
        self.saldo: dict[str, float] = {}
        self.last_write_version: dict[str, int] = {}

    def write(self, user_id: str, saldo_baru: float, version: int):
        self.saldo[user_id] = saldo_baru
        self.last_write_version[user_id] = version
        print(f"[{self.name}] WRITE saldo {user_id} = {saldo_baru} (versi {version})")

    def read(self, user_id: str) -> float:
        return self.saldo.get(user_id, 0.0)


class ReplicationSystem:
    def __init__(self):
        self.jakarta = Replica("Jakarta")
        self.bandung = Replica("Bandung")
        self.version_counter = 0

    def top_up(self, user_id: str, jumlah: float):
        """Top-up selalu ditulis dulu ke server Jakarta (mis. server terdekat pelanggan)."""
        self.version_counter += 1
        version = self.version_counter
        saldo_baru = self.jakarta.read(user_id) + jumlah
        self.jakarta.write(user_id, saldo_baru, version)

        # TODO 1: replikasi ke Bandung TERTUNDA (simulasikan dengan
        # threading.Timer(REPLICATION_DELAY, ...) yang memanggil
        # self.bandung.write(user_id, saldo_baru, version) setelah delay.
        threading.Timer(REPLICATION_DELAY, self.bandung.write, args=(user_id, saldo_baru, version)).start()
        print(f"Replikasi ke Bandung tertunda {REPLICATION_DELAY} detik")

    def baca_saldo_naif(self, user_id: str, server: str) -> float:
        """Baca saldo TANPA mekanisme Read-Your-Writes - bisa saja stale."""
        replica = self.jakarta if server == "Jakarta" else self.bandung
        return replica.read(user_id)

    def baca_saldo_read_your_writes(self, user_id: str, server: str, versi_minimal: int) -> float:
        """TODO 2: implementasikan Read-Your-Writes -
        jika replika yang dituju versi datanya < versi_minimal (client pernah
        melihat versi lebih baru sebelumnya), tunggu/redirect ke replika yang
        sudah punya versi tersebut (di sini cukup simulasikan dengan polling
        sampai versi replika >= versi_minimal, atau redirect ke Jakarta)."""
        replica = self.jakarta if server == "Jakarta" else self.bandung
        if replica.last_write_version.get(user_id, 0) < versi_minimal:
            print(f"[Read-Your-Writes] Versi {replica.name} belum cukup; baca dari Jakarta")
            replica = self.jakarta
        if replica.last_write_version.get(user_id, 0) < versi_minimal:
            raise ValueError(f"Versi minimal {versi_minimal} untuk {user_id} belum tersedia")
        return replica.read(user_id)


def main():
    system = ReplicationSystem()
    user_id = "user1"

    print("=== Skenario NAIF (tanpa Read-Your-Writes) ===")
    system.top_up(user_id, 50000)
    time.sleep(0.5)  # pelanggan langsung pesan makanan < REPLICATION_DELAY detik kemudian
    saldo_naif = system.baca_saldo_naif(user_id, "Bandung")
    assert saldo_naif == 0.0, "Skenario naif harus menunjukkan saldo yang belum direplikasi"
    print("Baca saldo dari Bandung (naif):", saldo_naif)
    print("-> Harusnya 50000, tapi karena delay replikasi, hasilnya bisa 0 (BUG)")

    time.sleep(REPLICATION_DELAY + 0.5)
    saldo_sinkron = system.baca_saldo_naif(user_id, "Bandung")
    assert saldo_sinkron == 50000
    print("Baca saldo dari Bandung setelah replikasi:", saldo_sinkron)

    print("\n=== Skenario dengan Read-Your-Writes ===")
    system.top_up(user_id, 20000)
    versi_terakhir = system.version_counter
    # TODO 3: panggil baca_saldo_read_your_writes dan tunjukkan hasilnya SELALU benar
    # walau dipanggil segera setelah top_up (< REPLICATION_DELAY detik).
    print("Baca saldo dari Bandung sebelum replikasi kedua:", system.baca_saldo_naif(user_id, "Bandung"))
    saldo_ryw = system.baca_saldo_read_your_writes(user_id, "Bandung", versi_terakhir)
    assert saldo_ryw == 70000, "Read-Your-Writes harus mencakup top-up terakhir klien"
    print("Baca saldo dengan Read-Your-Writes:", saldo_ryw)

    time.sleep(REPLICATION_DELAY + 0.5)
    saldo_sinkron = system.baca_saldo_read_your_writes(user_id, "Bandung", versi_terakhir)
    assert saldo_sinkron == 70000
    print("Baca saldo dari Bandung setelah replikasi kedua:", saldo_sinkron)


if __name__ == "__main__":
    main()
