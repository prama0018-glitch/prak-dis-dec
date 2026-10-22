from enum import Enum

class State(Enum):
    FOLLOWER = "FOLLOWER"
    CANDIDATE = "CANDIDATE"
    LEADER = "LEADER"

class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = State.FOLLOWER
        self.current_term = 0
        self.voted_for = None
        self.log = []

    def request_vote(self, candidate_id, term):
        if term < self.current_term:
            return False
        if term > self.current_term:
            self.current_term = term
            self.voted_for = None
            self.state = State.FOLLOWER
        if self.voted_for is None or self.voted_for == candidate_id:
            self.voted_for = candidate_id
            return True
        return False

    def start_election(self, nodes):
        self.current_term += 1
        self.state = State.CANDIDATE
        self.voted_for = self.node_id
        votes = 1
        print(f"Node {self.node_id} memulai election, term {self.current_term}.")
        for node in nodes:
            if node.node_id != self.node_id and node.request_vote(
                    self.node_id, self.current_term):
                votes += 1
                print(f"Node {node.node_id} memilih Node {self.node_id}.")
        majority = len(nodes) // 2 + 1
        print(f"Suara: {votes}/{len(nodes)}; mayoritas: {majority}.")
        if votes >= majority:
            self.state = State.LEADER
            print(f"Node {self.node_id} terpilih sebagai LEADER.")
            return True
        print("Pemilihan belum menghasilkan leader.")
        return False

    def send_heartbeat(self, nodes):
        if self.state != State.LEADER:
            return
        print(f"Leader Node {self.node_id} mengirim heartbeat.")
        for node in nodes:
            if node.node_id != self.node_id:
                node.current_term = self.current_term
                node.state = State.FOLLOWER

    def append_entry(self, entry):
        if self.state != State.LEADER:
            print("Hanya leader yang dapat menerima perintah.")
            return False
        self.log.append(entry)
        print(f"Log lokal leader ditambahkan: {entry}")
        return True

    def status(self):
        return (f"Node {self.node_id} | {self.state.value} | "
                f"term={self.current_term} | log={self.log}")

def simulate_raft():
    nodes = [RaftNode(i) for i in (1, 2, 3)]
    print("=== KONDISI AWAL ===")
    for n in nodes:
        print(n.status())
    candidate = nodes[1]  # kandidat Node 2 untuk contoh konsisten
    print("\n=== PEMILIHAN LEADER ===")
    success = candidate.start_election(nodes)
    if success:
        candidate.send_heartbeat(nodes)
        candidate.append_entry("contoh-perintah: x=10")
    print("\n=== KONDISI AKHIR ===")
    for n in nodes:
        print(n.status())
    return nodes, candidate if success else None
