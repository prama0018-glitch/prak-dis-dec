from raft_module import simulate_raft

nodes, leader = simulate_raft()
print("\n=== RINGKASAN ===")
print(f"Leader terpilih: Node {leader.node_id}" if leader
      else "Tidak ada leader yang terpilih.")
