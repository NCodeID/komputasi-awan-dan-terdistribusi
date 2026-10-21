"""
Tugas 6 - Simulasi Chord DHT (single-process, tanpa jaringan sungguhan)

Fungsi hashing & struktur data ring sudah disediakan.
Lengkapi TODO untuk lookup(), join(), dan leave().
"""

import hashlib

M_BITS = 8               # ruang identifier 0..255 (disederhanakan dari Chord asli yang pakai 160-bit)
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Hash string (ID node atau ID kurir) ke ruang identifier 0..RING_SIZE-1."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        # node_id (hasil hash) -> alamat IP node tersebut
        self.nodes: dict[int, str] = {}
        # key kurir (hasil hash) -> IP kurir yang disimpan node yang bertanggung jawab
        self.data: dict[int, tuple[str, str]] = {}  # hash -> (kurir_id, ip_kurir)

    def join(self, node_name: str, node_ip: str):
        """Tambahkan node baru ke ring. Pindahkan data yang seharusnya
        menjadi tanggung jawab node baru ini dari successor lamanya."""
        node_id = hash_id(node_name)

        # TODO 1: tambahkan node_id -> node_ip ke self.nodes.
        # TODO 2: cari successor LAMA dari node_id ini (successor sebelum node
        # baru bergabung, gunakan find_successor() dengan node_id INI dikecualikan
        # dulu dari self.nodes saat mencari).
        # TODO 3: pindahkan semua key di self.data yang seharusnya menjadi
        # tanggung jawab node baru (key dengan hash <= node_id, tapi masih
        # dipegang oleh successor lama) ke bawah tanggung jawab node baru.
        # (Untuk simulasi sederhana, cukup print log siapa mengambil alih apa -
        # tidak perlu benar-benar memindahkan struktur data kompleks.)
        print(f"[TODO] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")

        if node_id in self.nodes:
            print(f"[JOIN] Node '{node_name}' (id={node_id}) sudah ada di ring")
            return

        if not self.nodes:
            self.nodes[node_id] = node_ip
            print(f"[JOIN] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")
            return

        old_successor = self.find_successor(node_id)
        old_owners = {key_hash: self.find_successor(key_hash) for key_hash in self.data}
        self.nodes[node_id] = node_ip

        moved = []
        for key_hash, old_owner in old_owners.items():
            new_owner = self.find_successor(key_hash)
            if new_owner == node_id and old_owner != node_id:
                moved.append((key_hash, old_owner))

        print(f"[JOIN] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")
        print(f"Successor lama untuk id={node_id}: {old_successor}")
        if moved:
            for key_hash, old_owner in moved:
                kurir_id, _ = self.data[key_hash]
                print(f"Key '{kurir_id}' (hash={key_hash}) pindah dari node {old_owner} ke node {node_id}")
        else:
            print("Tidak ada key yang berpindah tanggung jawab")

    def leave(self, node_name: str):
        """Keluarkan sebuah node dari ring. Data yang dipegangnya harus
        berpindah ke successor-nya."""
        node_id = hash_id(node_name)

        # TODO 4: hapus node_id dari self.nodes.
        # TODO 5: cari successor BARU untuk tiap key yang tadinya dipegang
        # node ini, pindahkan ke successor tersebut.
        
        if node_id not in self.nodes:
            print(f"[LEAVE] Node '{node_name}' (id={node_id}) tidak ditemukan di ring")
            return

        held_keys = [
            key_hash
            for key_hash in self.data
            if self.find_successor(key_hash) == node_id
        ]
        leaving_ip = self.nodes[node_id]
        del self.nodes[node_id]

        print(f"[LEAVE] Node '{node_name}' (id={node_id}) keluar dari ring")

        if not self.nodes:
            for key_hash in held_keys:
                kurir_id, _ = self.data[key_hash]
                print(f"Key '{kurir_id}' (hash={key_hash}) tidak memiliki successor karena ring kosong")
            return

        if not held_keys:
            print("Tidak ada key yang berpindah tanggung jawab")
            return

        for key_hash in held_keys:
            new_owner = self.find_successor(key_hash)
            kurir_id, _ = self.data[key_hash]
            print(f"Key '{kurir_id}' (hash={key_hash}) pindah dari node {node_id} ({leaving_ip}) ke node {new_owner} ({self.nodes[new_owner]})")

    def find_successor(self, key_hash: int) -> int:
        """Cari node_id dengan nilai hash TERKECIL yang >= key_hash
        (successor menurut aturan Chord). Jika tidak ada, wrap-around
        ke node dengan hash terkecil di ring (karena ring melingkar)."""
        # TODO 6: implementasikan logika successor di atas menggunakan
        # self.nodes.keys(). Kembalikan node_id (bukan IP).
        
        if not self.nodes:
            raise ValueError("Ring kosong: tidak ada successor")

        node_ids = sorted(self.nodes)
        for node_id in node_ids:
            if node_id >= key_hash:
                return node_id
        return node_ids[0]

    def register_kurir(self, kurir_id: str, ip_kurir: str):
        """Simpan mapping ID Kurir -> IP di node yang bertanggung jawab."""
        key_hash = hash_id(kurir_id)
        # TODO 7: panggil find_successor(key_hash) untuk menentukan node
        # penanggung jawab, lalu simpan (kurir_id, ip_kurir) ke self.data[key_hash].
        
        if not self.nodes:
            raise ValueError("Ring kosong: tidak ada node penanggung jawab")

        owner = self.find_successor(key_hash)
        self.data[key_hash] = (kurir_id, ip_kurir)
        print(f"[REGISTER] Kurir '{kurir_id}' (hash={key_hash}) disimpan di node {owner}")

    def lookup(self, kurir_id: str) -> str | None:
        """Cari alamat IP terkini untuk sebuah ID Kurir."""
        key_hash = hash_id(kurir_id)
        # TODO 8: gunakan find_successor(key_hash) untuk menemukan node
        # penanggung jawab, lalu kembalikan ip_kurir dari self.data jika ada.
        
        if not self.nodes:
            return None

        owner = self.find_successor(key_hash)
        entry = self.data.get(key_hash)
        if entry is None:
            return None

        _, ip_kurir = entry
        print(f"[LOOKUP] '{kurir_id}' (hash={key_hash}) -> node {owner}, IP {ip_kurir}")
        return ip_kurir


def main():
    ring = ChordRing()

    # Skenario awal: 4 node bergabung
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")

    # Daftarkan beberapa kurir
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")
    ring.register_kurir("kurir-005", "192.168.1.14")
    ring.register_kurir("kurir-012", "192.168.1.21")

    print("\n--- Lookup sebelum perubahan topologi ---")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))
    print("kurir-012 ->", ring.lookup("kurir-012"))
    print("kurir-005 ->", ring.lookup("kurir-005"))

    print("\n--- Node baru bergabung ---")
    ring.join("node-medan-1", "10.0.0.5")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-012 ->", ring.lookup("kurir-012"))

    print("\n--- Sebuah node keluar ---")
    ring.leave("node-jakarta-1")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))
    print("kurir-005 ->", ring.lookup("kurir-005"))


if __name__ == "__main__":
    main()
