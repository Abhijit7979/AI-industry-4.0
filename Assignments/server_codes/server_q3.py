import zmq
import queue
import threading

def receive_data(socket, data_queue):
    while True:
        message = socket.recv_string()
        print(f"Received: {message}")
        data_queue.put(message)

def send_data(socket, data_queue):
    while True:
        message = socket.recv_string()
        if message == "REQUEST":
            if not data_queue.empty():
                data = data_queue.get()
                socket.send_string(data)
            else:
                socket.send_string("NO_DATA")

def main():
    context = zmq.Context()

    # Socket to receive data from publisher
    receiver = context.socket(zmq.SUB)
    receiver.bind("tcp://*:5555")
    receiver.setsockopt_string(zmq.SUBSCRIBE, "")

    # Socket to send data to consumer
    sender = context.socket(zmq.REP)
    sender.bind("tcp://*:5556")

    data_queue = queue.Queue()

    # Start receive thread
    receive_thread = threading.Thread(target=receive_data, args=(receiver, data_queue))
    receive_thread.daemon = True
    receive_thread.start()

    # Start send thread
    send_thread = threading.Thread(target=send_data, args=(sender, data_queue))
    send_thread.daemon = True
    send_thread.start()

    print("Server is running...")
    
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Shutting down...")

    receiver.close()
    sender.close()
    context.term()

if __name__ == "__main__":
    main()