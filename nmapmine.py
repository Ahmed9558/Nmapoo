import nmap

scanner = nmap.PortScanner()

target = input('Please Enter an ip Address of the target: ')

scanner.scan(target,'1-1024','-sV')

print("The host name is: " + scanner[target].hostname())