import zmq
import time

def main():
    context = zmq.Context()

    # Socket facing  
    frontend = context.socket(zmq.XSUB)
    frontend.bind("tcp://*:5559")

    # Socket facing subscribers
    backend = context.socket(zmq.XPUB)
    backend.bind("tcp://*:5560")

    # Create a poller
    poller = zmq.Poller()
    poller.register(frontend, zmq.POLLIN)
    poller.register(backend, zmq.POLLIN)

    while True:
        try:
            events = dict(poller.poll(1000))

            if frontend in events:
                message = frontend.recv_multipart()
                backend.send_multipart(message)

            if backend in events:
                message = backend.recv_multipart()
                frontend.send_multipart(message)

        except KeyboardInterrupt:
            break

    frontend.close()
    backend.close()
    context.term()

if __name__ == "__main__":
    main()