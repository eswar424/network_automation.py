from netmiko import ConnectHandler
import psutil
 
#First create the device object using a dictiona
with open('devices.txt') as routers:
	for ip in routers:
		routers = {
			"device_type": "cisco_ios",
			"ip": "sandbox-iosxe-latest-1.cisco.com",
			"username": "developer",
			"password": "C1sco12345"
		}
            
		net_connect = ConnectHandler(**routers)
            
		print("connect to" + ip)
		print('-'*79)
		output = net_connect.send_command('sh ip int brief')
		print(output)
		print()
		print("-"*79)
result05=psutil.net_io_counters(pernic=True)
print(result05)
net_connect.disconnect()