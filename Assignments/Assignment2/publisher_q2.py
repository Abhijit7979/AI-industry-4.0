import zmq
import time
import random

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect("tcp://64.227.147.221:5559")

    topics = ["sports", "weather", "news"]

    while True:
        try:
            topic = random.choice(topics)
            message = f"{topic} update: {random.randint(1, 100)}"
            print(f"Sending: {message}")
            socket.send_string(message)
            time.sleep(1)
        except KeyboardInterrupt:
            break

    socket.close()
    context.term()

if __name__ == "__main__":
    main()