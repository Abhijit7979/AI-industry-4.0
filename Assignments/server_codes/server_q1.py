from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def receive_message():
    # Get the JSON data from the request
    data = request.json
    message = data.get('message', '')

    # Print the received message to the command line
    print(f"Received message: {message}")

    # Respond to the client
    return jsonify({"status": "Message received!"})

if __name__ == '__main__':
    # Run the server on all available network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)