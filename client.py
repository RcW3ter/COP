import socket
import json
import argparse
import configparser

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parser = argparse.ArgumentParser(
                    prog='COP-Client',
                    description='Connect to COP server')

parser.add_argument('--ip',type=str ,required=False ,help='IP of the COP Server')
parser.add_argument('--default' ,action="store_true",help='Connect to default server')

args = parser.parse_args()

if args.default :
    config = configparser.ConfigParser()
    config.read("settings\\set_default.ini")

    ip = config["default"]["server_ip"]
elif args.ip :
    ip = args.ip


client.connect((ip, 8080))

while True :
    cmd = input('COP CMD >')

    if cmd == 'exit' :
        client.close()
        break

    instruction = {"action": cmd}
    client.send(json.dumps(instruction).encode())

    rep = client.recv(2048)
    print("Réponse du serveur :", rep.decode())
