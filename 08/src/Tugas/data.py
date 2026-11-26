import sqlite3

conn = sqlite3.connect("toko.db")
cur = conn.cursor()

data = [
    (50, "BRG01", "Keyboard Mekanik", True, 450000.50),
    (20, "BRG02", "Mouse Wireless", True, 175000.0),
    (0,  "BRG03", "Monitor 24 Inch", False, 1850000.75),
    (35, "BRG04", "Headset Gaming", True, 320000.0),
    (10, "BRG05", "Webcam Full HD", True, 275500.25),
]
cur.executemany(
    "INSERT INTO produk (stok, kode, nama, tersedia, harga) VALUES (?, ?, ?, ?, ?)",
    data,
)
conn.commit()
conn.close()
print("5 data berhasil dimasukkan")