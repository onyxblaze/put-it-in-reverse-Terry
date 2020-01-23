import socket
import re

with open('logfile.txt' , 'r') as f:
    #Input the file to be read 'logfile.txt'.

    raw_data = f.read()
    #Reads everything in file and puts into lines.

    regex = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
    #RegExp to identify IP address.

    host = raw_data.strip().split('|')
    #Removes trailing and leading characters of string and '|' symbol.

    foundip = re.findall( regex, raw_data )
    #Uses regexp to find IP addresses in file.

    foundip = sorted(set(foundip))
    #Ignore duplicate IP addresses to avoid multiple host names.

for host in foundip:
    try:
        resolve = socket.gethostbyaddr(host)
        name = resolve[0]
        name, _, addrlist = resolve
        #Resolves found IP addresses to DNS name and removes alias DNS.

        raw_data = raw_data.replace(host , "%s ( %s )" % (host, name))
        #Call to replace IP addresses found in the given file with host and DNS name.

        with open('logfile.txt', 'w') as f:
            f.write(raw_data)
            #Rewrites the found IP address with host and DNS name.

    except socket.error as exc:
        pass
        #Ignores IP addresses in the file that couldn't be resolved instead of displaying error.
    f.close()
