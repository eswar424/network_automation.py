from netmiko import ConnectHandler
#First create the device object using a dictiona

csr = {
		"device_type": "cisco_ios",
		"ip": "sandbox-iosxe-latest-1.cisco.com",
		"username": "developer",
		"password": "C1sco12345"
}
net_connect = ConnectHandler(**csr)
            
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,devices, *rest = hostname.split(" ")
print(hostname)
print(devices)
print("Backing up" + devices)
filename = 'devices3.txt'
# showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file=open(filename,"a")
# log_file.write(showrun)
# log_file.write('/n')
log_file.write(showvlan)
log_file.write('/n')
log_file.write(showver)
log_file.write('/n')