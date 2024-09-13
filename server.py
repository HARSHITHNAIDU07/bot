import random
def receive_packet(packet):
    print(f"Receiver received packet {packet}")
    if random.random()<0.9:
        return True
    return False