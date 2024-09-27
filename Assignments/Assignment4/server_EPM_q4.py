import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://*:5555")

    print("Server is running...")

    while True:
        message = socket.recv_string()
        print(f"Received message: {message}")
        
        # Send an acknowledgment back to the client
        socket.send_string("Message received")
        
        if message == "exit":
            break

    print("Server is shutting down...")
    socket.close()
    context.term()

if __name__ == "__main__":
    main()