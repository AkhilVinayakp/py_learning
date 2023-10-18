import socket

host = "localhost"  # Replace with the hostname or IP address of your server
port = 7000  # Replace with the port on which your server is listening

# Create a socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Receive and print data
    while True:
        data = client.recv(1024)  # Receive up to 1024 bytes of data
        if not data:
            break  # No more data received, exit the loop
        print(data.decode())  # Print the received data as a string

except ConnectionRefusedError:
    print(f"Failed to connect to {host}:{port}. Make sure the server is running.")

finally:
    client.close()  # Close the client socket when done
