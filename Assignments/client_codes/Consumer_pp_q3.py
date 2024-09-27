import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://64.227.147.221:5556")  

    print("Consumer is ready to receive data...")

    while True:
        try:
            socket.send_string("REQUEST")
            message = socket.recv_string()
            if message == "NO_DATA":
                print("No data available. Waiting...")
                time.sleep(1)
            else:
                print(f"Received: {message}")
            time.sleep(0.5)  
        except KeyboardInterrupt:
            break

    socket.close()
    context.term()

if __name__ == "__main__":
    main()