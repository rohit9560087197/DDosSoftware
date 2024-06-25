class PacketHandler:
    def __init__(self):
        print("Packet Handler Initialized")

    def process_packet(self, packet):
        # Simulate packet processing
        print(f"Processing packet: {packet}")

class Packet_1_18_2(PacketHandler):
    def __init__(self):
        super().__init__()
        print("Packet_1_18_2 Initialized")
