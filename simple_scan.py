import socket
from datetime import datetime

#Write the adress to Scan
host = input('Digite o site ou ip que deseja escanear: ')
#Translate a host name to Ipv4 adress
ip = socket.gethostbyname(host)

#Scan begin
print('-'*80)
print(f'              Escaneando o IP: {ip}')
print('-'*80)

#Start time
t1 = datetime.now()

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it create sock stream
        result = sock.connect_ex((ip, port))
        if result == 0:
            #if a socket is listening it will print out the port number
            print(f'\n Port {port} Is Open -------------> ')
            sock.close()
        else:
            print(f'\n Port {port} Is Close :-(')

    except:
        pass

#Ports to scan
scan(80)
scan(22)
scan(25)


t2 = datetime.now()
#Total time of scan
print(f'O tempo total do scan foi: {t2 - t1}')