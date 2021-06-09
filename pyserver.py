# import os
# from http.server import HTTPServer, CGIHTTPRequestHandler
# # Make sure the server is created at current directo
# os.
# # Create server object listening the port 80
# server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# # Start the web server
# server_object.serve_forever()

import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 80

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

# while True:
#     # Wait for client connections
#     client_connection, client_address = server_socket.accept()
#
#     # Get the client request
#     request = client_connection.recv(1024).decode()
#     print(request)
#
#     # Send HTTP response
#     response = 'HTTP/1.0 200 OK\n\nHELLO SCRIBETECH'
#     client_connection.sendall(response.encode())
#     client_connection.close()

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()

    # Get the content of htdocs/index.html
    fin = open('./index.html')
    content = fin.read()
    fin.close()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()