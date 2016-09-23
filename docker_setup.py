#Script to setup docker on Ubuntu 14.04
import os
import subprocess
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--num", dest="number",
        help="The number of container in a host.")

parser.add_option("-s", "--subnet", dest="subnet", 
        help="The ip addresses of containers are assigned from this subnet. Ex. 172.20.0.1/16")
(options, args)= parser.parse_args()
cmd = "sudo apt-get update"
proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while proc.poll() is None:
   	output = proc.stdout.readline().strip()
	print output
output = proc.communicate()[0]
proc.wait()
cmd = "sudo apt-get install -y docker.io"
proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while proc.poll() is None:
   	output = proc.stdout.readline().strip()
	print output
output = proc.communicate()[0]
proc.wait()
print("\nDone installing Docker!")

print("Intalling bridge-utils..")
proc= subprocess.Popen("sudo apt-get install -y bridge-utils", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
print("Done.")
print("Assigning the subnet... (changing the ip address of docker0)")
proc= subprocess.Popen("sudo ip link set docker0 down", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo brctl delbr docker0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo brctl addbr docker0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo ip a add " + options.subnet + " dev docker0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo ip link set docker0 up", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo restart docker", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while proc.poll() is None:
   	output = proc.stdout.readline()
output = proc.communicate()[0]
print("Done changing the ip address!")
os.system("sudo start docker")


print("\nLoading the Image... ")
cmd = "sudo docker load < /proj/SENSS/dk.agent.latest.tar"
proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
proc.wait()
proc= subprocess.Popen("sudo docker images", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = proc.communicate()[0]
hosts=[]
for i in range(1,int(options.number)+1):
	hosts.append("cont"+ str(i))

print("\nCreating Containers...")
for x in hosts:
	cmd = "sudo docker run -itd -v /users/svshanka/flooder:/flooder --privileged --name="+ x + " svshanka/my-ubuntu:latest /bin/bash"
	proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	proc.wait()
	print("Container " + x + " UP!")









