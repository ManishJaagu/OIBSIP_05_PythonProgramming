from socket import *
from threading import *
from tkinter import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host_Ip = "127.0.0.1"
portNumber = 7500

client_socket.connect((host_Ip, portNumber))

window = Tk()
window.title(f"Connected to: {host_Ip} : {str(portNumber)}")

txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

lblYourMessage = Label(window, text="Your Message:")
lblYourMessage.grid(row=1, column=0, padx=10, pady=10, sticky=W)

txtYourMessage = Entry(window, width=50)
txtYourMessage.grid(row=2, column=0, padx=10, pady=10)

def sendMessage(event=None):
    client_message = txtYourMessage.get()
    if client_message.strip() != "":
        txtMessages.insert(END, f"\nYou: {client_message}")
        client_socket.send(client_message.encode("utf-8"))
        txtYourMessage.delete(0, END)  # Clear the entry after sending the message

btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=3, column=0, padx=10, pady=10)

# Bind the "Enter" key to the sendMessage function
txtYourMessage.bind("<Return>", sendMessage)

def receiveMessage():
    while True:
        try:
            serverMessage = client_socket.recv(1024).decode("utf-8")
            txtMessages.insert(END, f"\n{serverMessage}")
        except:
            print("An error occurred!")
            client_socket.close()
            break

receiveThread = Thread(target=receiveMessage)
receiveThread.daemon = True
receiveThread.start()

window.mainloop()
