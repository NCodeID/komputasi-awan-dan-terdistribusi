"""
Tugas 4 - Jalur A: RPC Server (simulasi modul Pembayaran)
Memakai xmlrpc.server dari Python standard library - tidak perlu install apa pun.
"""

from xmlrpc.server import SimpleXMLRPCServer

# Simulasi "database" saldo user
saldo_user = {
    "user1": 50000,
    "user2": 120000,
}


def cek_saldo(user_id: str) -> float:
    """Kembalikan saldo user_id saat ini."""
    # TODO 1: kembalikan saldo dari dict `saldo_user`.
    # Jika user_id tidak ada, putuskan sendiri perilakunya (mis. return 0 atau raise error)
    # dan jelaskan keputusan ini di README.md.
    return saldo_user.get(user_id, 0)


def proses_pembayaran(user_id: str, jumlah: float) -> dict:
    """Kurangi saldo user sejumlah `jumlah`. Kembalikan status hasil."""
    # TODO 2: validasi saldo cukup, kurangi saldo_user[user_id], dan kembalikan
    # dict berisi minimal {"status": "sukses"/"gagal", "saldo_akhir": ...}
    if user_id not in saldo_user:
        return {"status": "gagal", "saldo_akhir": 0, "pesan": "User tidak ditemukan"}
    
    if saldo_user[user_id] < jumlah:
        return {"status": "gagal", "saldo_akhir": saldo_user[user_id], "pesan": "Saldo tidak cukup"}
    
    saldo_user[user_id] -= jumlah
    return {"status": "sukses", "saldo_akhir": saldo_user[user_id]}


def main():
    # TODO 3: buat SimpleXMLRPCServer di localhost port 8000,
    # daftarkan fungsi cek_saldo & proses_pembayaran, lalu serve_forever().
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_function(cek_saldo, "cek_saldo")
    server.register_function(proses_pembayaran, "proses_pembayaran")
    print("RPC server modul Pembayaran berjalan di port 8000...")
    server.serve_forever()


if __name__ == "__main__":
    main()
