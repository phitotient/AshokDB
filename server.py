import socket as sc
import json
import logging

SOCKET = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

if __name__=="__main__":
    with open('configs/config.json', 'r') as f:
        config = json.load(f)
        host=config["HOST"]
        port=config["PORT"]

    SOCKET.bind((host,port))
    SOCKET.listen(1)
    connection, address = SOCKET.accept()
    print('New connection from [{}]'.format(address))
    data = connection.recv(4096).decode()
