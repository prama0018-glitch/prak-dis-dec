from vclock import VectorClock
print("=== SIMULASI VECTOR CLOCK MENGGUNAKAN MODUL PYTHON ===")
# Inisialisasi 3 proses
p0 = VectorClock(num_processes=3, process_id=0)
p1 = VectorClock(num_processes=3, process_id=1)
p2 = VectorClock(num_processes=3, process_id=2)
print("Status Awal Clock:")
print(p0),print(p1),print(p2),print("-" * 45)
# Process 0 melakukan event lokal
p0.increment()
print("P0 melakukan event lokal:")
print(p0)
print("-" * 45)
# Process 0 mengirim pesan ke Process 1
msg_p0 = p0.send_message()
p1.receive_message(msg_p0)
print("P0 mengirim pesan ke P1:")
print(f"P0: {p0}")
print(f"P1: {p1}")
print("-" * 45)
# Process 2 melakukan event lokal
p2.increment()
print("P2 melakukan event lokal:")
print(p2)
print("-" * 45)
# Process 1 mengirim pesan ke Process 2
msg_p1 = p1.send_message()
p2.receive_message(msg_p1)
print("P1 mengirim pesan ke P2:")
print(f"P1: {p1}")
print(f"P2: {p2}")
print("-" * 45)
#Cek Kausalitas
print("Hasil Pengecekan Kausalitas:")
print(f"P0 happens before P1: {p0.happens_before(p1)}")
print(f"P1 happens before P0: {p1.happens_before(p0)}")
print(f"P0 is concurrent with P2: {p0.is_concurrent(p2)}")