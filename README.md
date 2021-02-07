# docker_start

I use this to start docker containers as per my requirements

#!/usr/bin/python3
import subprocess

print("1 : bwapp")
print("2 : juice_shop")
print("3 : dvwa")
print("4 : sqliLabs")
print("5 : sonarqube")

print("\n")
number = int(input("Enter a number corresponding to a docker image : "))
#print(number)

#docker run -dt --name bwapp -p 8001:80 --rm raesene/bwapp

def docker_run(arg1, arg2, arg3):
    p1 = subprocess.run(['docker', 'run', '-dt', '--name', arg1, '-p', arg2, '--rm', arg3], capture_output=True, text=True)
    return p1.stdout

switcher = {
        1 : ["bwapp", "localPort:80", "raesene/bwapp"],
        2 : ["juice_shop", "localPort:3000", "bkimminich/juice-shop"],
        3 : ["dvwa", "localPort:80", "vulnerables/web-dvwa"],
        4 : ["sqli", "localPort:80", "acgpiano/sqli-labs"],
        5 : ["sonarqube", "localPort:9000", "sonarqube"]
        }

def check_key(d, key):
    if key in switcher:
        print("Key Found")
        docker_run(d[key][0], d[key][1], d[key][2])
        print("Starting "+d[key][0])
    else:
        print("No key found")

check_key(switcher, number)
