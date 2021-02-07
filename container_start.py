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
        1 : ["bwapp", "8001:80", "raesene/bwapp"],
        2 : ["juice_shop", "8002:3000", "bkimminich/juice-shop"],
        3 : ["dvwa", "8005:80", "vulnerables/web-dvwa"],
        4 : ["sqli", "8006:80", "acgpiano/sqli-labs"],
        5 : ["sonarqube", "8007:9000", "sonarqube"]
        }

def check_key(d, key):
    if key in switcher:
        print("Key Found")
        docker_run(d[key][0], d[key][1], d[key][2])
        print("Starting "+d[key][0])
    else:
        print("No key found")

check_key(switcher, number)
