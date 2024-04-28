import sys
import socket
import threading
import time

def connect(s):
    while True:
        r_msg = s.recv(1024)
        if not r_msg:
            break
        if r_msg == '':
            break
        else:
            print("Server>>>  "+ str(r_msg))
        if not flag:
            break

def receive(s):
    global flag
    while True:
        s_msg = input().encode('utf-8')
        if s_msg == '':
            pass
        if s_msg.decode() == 'exit':
            print("wan exit")
            break
        else:
            encrypted_msg = encrypt(s_msg.decode(), 4)
            s.sendall(encrypted_msg)

    flag = False

def encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message.encode('utf-8')

if __name__ == '__main__':
    start_time = time.monotonic()
    if 3 != len(sys.argv):
        print("usage: %s [ip adress][port] " % sys.argv[0])
        sys.exit(0)
    flag = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((sys.argv[1], int(sys.argv[2])))
    thread1 = threading.Thread(target=connect, args=([s]))
    thread2 = threading.Thread(target=receive, args=([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
