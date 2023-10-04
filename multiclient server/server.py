### TO HANDLE MULTIPLE CLIENTS ON A SERVER YOU WILL HAVE TO MAKE USE OF THREADS,
### AND RUN EACH CLIENT ON A DIFFERENT THREAD :)

''' 1. YOU BASICALLY HAVE TO CREATE A SOCKET FIRST 
       using the socket.socket() which is found in the socket library'''
''' 2. THEN YOU HAVE TO BIND THAT SOCKET TO AN ADDRESS 
       and to do that you have to get the server(localhost in our case) and port number'''
''' 3. THEN YOU WILL START LISTENING TO THE CLIENT
       using server.listen()'''
''' 4. THEN YOU HAVE TO ACCEPT THE CONNECTION
       using server.accept() which will written a tuple containing the connection object 
       and adress from where the connection came'''
''' 5. SINCE THIS IS A MULTI CLIENT HANDLING SERVER WE WILL HAVE TO USE THREADS TO TALK TO MULTIPLE CLIENTS
       create a thread using threading.Thread() which is found in threading library 
       then run the thread with the function that handles the clients
       after receiving the disconnect message from the client close the connection'''

import socket as skt
import threading 

#STEP 1
try:
    server = skt.socket()
    print("Socket created successfully!!")
    print(server)
except skt.error as err:
    print("Error: ", err)

HEADER = 64 #size of message in bytes
PORT = 5050
SERVER = skt.gethostbyname(skt.gethostname()) #host
ADDR = (SERVER, PORT) #address of server     Socket = IP address + Port number of a computer
DISCONNECT_MSG = "!end" 

#STEP 2
server.bind(ADDR) #socket is bound to the address

def handle_client(c,ad):    #this function will handle all of the communication between the client and the server
    #this function will run for each client
    print(f"[NEW CONNECTION] {ad} connected... ")
    connected = True
    while connected:
        msg = c.recv(64).decode() #decode()- decodes the message recieved from the client in byte format to utf-8 format so that it is human readable.
        if msg == DISCONNECT_MSG:
            connected = False
        t = ad[1]
        print(f"[CLIENT at {t}]: {msg}")
        msg = input(f"[SERVER of {t}]: ")
        if msg == DISCONNECT_MSG:
            connected = False
        c.send(msg.encode())
    c.close()

def start():    #this function is used to start listening I.E. handle new connection...
    #STEP 3
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}...")
    while True:
        #STEP 4
        conn, addr = server.accept()    
        '''when a new connection is set-up, the address of the connection is stored (ie client) 
        conn is connection object and will help send data back to connection (ie client)
        when connection is established start a new thread (via func handle_client())'''
        #STEP 5
        thread = threading.Thread(target = handle_client, args =(conn,addr))
        thread.start()  #This start is not the start function() but is the function of the threading library used for starting a thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}...")

        
print("[STARTING] server is starting... ")
start()
