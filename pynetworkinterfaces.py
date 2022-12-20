import socket
import requests
import getpass
import datetime

# check if the 'requests' module is installed
try:
    import requests
except ImportError:
# if not, install it using pip
    import pip
    pip.main(['install', 'requests'])
    import requests

# get the hostname of the computer
hostname = socket.gethostname()

# get the network interfaces of the computer
interfaces = socket.if_nameindex()

# get the external IP address of the computer
external_ip = requests.get("https://api.ipify.org").text

# get the current user
user = getpass.getuser()

# get the current date and time
date_time = datetime.datetime.now()

# create a file to save the network information
filename = "network_interfaces_" + hostname
file = open(filename, "w")

# write the current user and date and time to the file
file.write("Network information for user '%s' on %s\n" % (user, date_time))
file.write("Hostname: %s\n" % hostname)
file.write("External IP address: %s\n" % external_ip)
file.write("Network interfaces:\n")
for interface in interfaces:
    file.write("%d: %s\n" % (interface[0], interface[1]))

# close the file
file.close()
