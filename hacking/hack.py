# -*- coding: utf-8 -*-
"""
@author: zejiran.
"""
import sys
import socket

args = sys.argv  # List of arguments.
if len(args) != 4:
    print("The script should be called with three arguments. The IP address, port, and message for sending.")
else:
    # Create a new socket.
    with socket.socket() as client_socket:
        # Connect to a host and a port using the socket.
        hostname = args[1]
        port = int(args[2])
        address = (hostname, port)
        client_socket.connect(address)
        # Send a message from the third command line argument to the host using the socket.
        message = args[3].encode()
        client_socket.send(message)
        # Receive the server's response.
        response = client_socket.recv(1024)
        response = response.decode()
        # Print the server’s response.
        print(response)
