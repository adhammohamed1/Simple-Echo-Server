import socket
import string_processing

HOST = "localhost"
PORT = 9999

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

for i in range(5):

    print("(" + str(i+1) + ")")

    # Generate a random string to send to the server
    data = string_processing.random_string(10)

    # Send the data to the server
    s.sendall( data.encode('utf-8') )
    print("Sent     :", data)

    # Receive the processed data from the server
    processed_data = s.recv(1024).decode('utf-8')
    print("Received :", processed_data + "\n")

# Close the socket
s.close()