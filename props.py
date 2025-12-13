import argparse
import configparser
import socket

parser = argparse.ArgumentParser(
                    prog='COP-PROPS',
                    description='Set up preferencies')

parser.add_argument('--scan' ,action="store_true",help='Scan ip with open port 8080')
parser.add_argument('--set_default',type=str ,required=False ,help='IP ex: 192.168.1.---')

args = parser.parse_args()

if args.scan :
    FOUND_IP = []

    def check_port(ip, port=8080):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect((ip, port))
            FOUND_IP.append(ip)
            return True
        except:
            return False
        finally:
            sock.close()

    for i in range(1,255):
        check_port(f'192.168.1.{i}')

    print(FOUND_IP)

if args.set_default :
    config = configparser.ConfigParser()

    config["default"] = {
        "server_ip": args.set_default
    }

    with open("settings\\set_default.ini", "w") as f:
        config.write(f)
