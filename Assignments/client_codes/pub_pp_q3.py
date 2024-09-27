import zmq
import time
import random

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect("tcp://64.227.147.221:5555") 

    print("Publisher is ready to send data...")

    while True:
        try:
            data = f"Data {random.randint(1, 100)}"
            print(f"Sending: {data}")
            socket.send_string(data)
            time.sleep(1)  
        except KeyboardInterrupt:
            break

    socket.close()
    context.term()

if __name__ == "__main__":
    main()