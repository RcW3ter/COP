import socket
import threading
import json

def handle_client(sock, address):
    print(f"[+] Connexion reçue depuis {address}")

    while True:
        raw = sock.recv(2048)
        if not raw:
            print(f"[-] Client {address} déconnecté")
            break

        try:
            cmd = json.loads(raw.decode())
        except json.JSONDecodeError:
            sock.send(b"Erreur: JSON invalide\n")
            continue

        action = cmd.get("action", "")

        if action == "payloads":
            sock.send(b"[+]Check out Payloadsn\n")
            break
        else:
            sock.send(f"[-]Commands non trouve: {action}\n".encode())

    sock.close()


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("0.0.0.0", 8080))  
serv.listen(5)
print("[+] Serveur à l'écoute sur le port 8080")

while True:
    client_sock, client_addr = serv.accept()
    ct = threading.Thread(target=handle_client, args=(client_sock, client_addr))
    ct.start()
