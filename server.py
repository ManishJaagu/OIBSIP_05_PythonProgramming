""" Author- Jagu Manish || Python Programming Internship at Oasis Infobyte

------------------ TASK 5 - CHAT APPLICATION (BEGINNER) -----------------------
Description:
For Beginners: Create a basic text-based chat application in Python where two users can exchange messages in real-time using the command line. Implement a simple client-server model for message exchange.

For Advanced: Develop an advanced chat application with a graphical user interface (GUI) using Tkinter, PyQt, or a web framework. Add features like user authentication, multiple chat rooms, multimedia sharing (images, videos), message history, notifications, emojis, and encryption for data security.

Key Concepts and Challenges:
Networking (for Beginners): Learn socket programming for real-time communication between clients and a server.
User Interface (for Advanced): Design an intuitive, responsive interface for the chat application.
Authentication (for Advanced): Implement user registration and login to secure the chat.
Multimedia Sharing (for Advanced): Enable users to send and receive multimedia content.
Message History (for Advanced): Store and display message history for reference.
Notifications (for Advanced): Provide notifications for new messages, even when the chat window is minimized.
Emoji Support (for Advanced): Implement emoji support within messages.
Security (for Advanced): Ensure data security through encryption and other security measures.
"""
from socket import *
from threading import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host_Ip = "127.0.0.1"
portNumber = 7500

server_socket.bind((host_Ip, portNumber))
server_socket.listen(5)

print(f"Server started at {host_Ip} on port {portNumber}")

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                clients.remove(client)
                client.close()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    clients.append(client_socket)
    client_handler = Thread(target=handle_client, args=(client_socket,))
    client_handler.daemon = True
    client_handler.start()
