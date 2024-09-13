import time
import random
from server import receive_packet
WINDOW_SIZE=1  
TIMEOUT=2      
def send_packet(packet):
    print(f"Sending packet {packet}")
    if random.random()<0.5:
        print(f"Packet {packet} lost")
        return False
    return True


def stopandwait(packets):
    for packet in packets:
        while True:
            if send_packet(packet):
                start_time=time.time()
                ack_received=False
                while time.time()-start_time<TIMEOUT:
                    if receive_packet(packet):
                        ack_received=True
                        print(f"Acknowledgment for packet {packet} received")
                        break
                if ack_received:
                    break
                else:
                    print(f"No acknowledgment for packet {packet}. Retrying...")
            else:
                print(f"Failed to send packet {packet}. Retrying...")
        time.sleep(1)  
packets=[1,2,3,4,5]
stopandwait(packets)
