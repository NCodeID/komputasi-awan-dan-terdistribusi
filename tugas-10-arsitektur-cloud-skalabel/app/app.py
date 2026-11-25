"""
Tugas 10 - Aplikasi sederhana untuk simulasi Load Balancing.
Mengembalikan ID instance-nya sendiri supaya distribusi beban bisa diamati.
"""

import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# TODO 1: ambil ID instance dari environment variable "INSTANCE_ID"
# (akan di-set berbeda per service di docker-compose.yml).
INSTANCE_ID = os.environ.get("INSTANCE_ID", "__BELUM_DI_SET__")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simulasikan sedikit beban kerja
        time.sleep(0.05)

        # TODO 2: kembalikan response berisi INSTANCE_ID, misalnya
        # body: f"Ditangani oleh instance: {INSTANCE_ID}\n"
        body = f"Ditangani oleh instance: {INSTANCE_ID}\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, format, *args):
        # Log singkat ke stdout supaya kelihatan di `docker compose logs`
        print(f"[{INSTANCE_ID}] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"Instance {INSTANCE_ID} berjalan di port {port}")
    server.serve_forever()