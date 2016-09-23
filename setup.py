import sys
import json
import paramiko
hosts=["hosting1","hosting2","hosting3","univ1","univ2","univ3"]
f=open("/proj/SENSS/config","r")
for line in f:
        if "username" in line:
                uname=line.strip().split("-")[1]
        if "password" in line:
                passw=line.strip().split("-")[1]
        if "project_name" in line:
                project_name=line.strip().split("-")[1]
        if "exp_name" in line:
                exp_name=line.strip().split("-")[1]
        if "containers" in line:
                n=line.strip().split("-")[1]
        if "docker_image_location" in line:
                docker_image_location=line.strip().split("-")[1]
        if "docker_setup" in line:
                docker_setup_location=line.strip().split("-")[1]
failed=[]
i=20
for host in hosts:
        try:
                url=host+"."+exp_name+"."+project_name
                print url
                command_to_execute="sudo python "+docker_setup_location+"  -n "+str(n)+" -s "+str(i)+".0.0.1/16"+" -d "+docker_image_location
                print command_to_execute
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(url,username=uname, password=passw, timeout=3)
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command_to_execute)
                print ssh_stdout.readlines()
                i=i+1
        except Exception as e:
                print e
                failed.append(host)
