import zmq
import time

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://64.227.147.221:5555")

    print("Client is running...")

    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")
        socket.send_string(message)
        
        # Wait for the server's acknowledgment
        response = socket.recv_string()
        print(f"Server response: {response}")
        
        if message == "exit":
            break

    print("Client is shutting down...")
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
