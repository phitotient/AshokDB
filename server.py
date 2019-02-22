import socket as sc
import json



if __name__=="__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)
