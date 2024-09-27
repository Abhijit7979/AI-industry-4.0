import zmq
import sys

def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://64.227.147.221:5560")

    if len(sys.argv) > 1:
        topic_filter = sys.argv[1]
    else:
        topic_filter = ""

    socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

    while True:
        try:
            message = socket.recv_string()
            print(f"Received: {message}")
        except KeyboardInterrupt:
            break

    socket.close()
    context.term()

if __name__ == "__main__":
    main()