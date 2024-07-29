#!/usr/bin/env python
import subprocess
import threading
import os
import sys
from colorama import *

def comand_run(comand):
    subprocess.run(comand, shell=True)

init()

os.system(f"figlet steet")
print(f"{Fore.MAGENTA}             by inotsu\n\n{Fore.RESET}")

if len(sys.argv) < 2:
    print("Uso: [opção] [argumentos]")
    sys.exit(1)

if sys.argv[1] == "-d":
    dominio = sys.argv[2]
    comand_run(f"mkdir {dominio}")

    subfinder = f"subfinder -silent -d {dominio} -all -o {dominio}/subfinder.txt"
    assetfinder = f"assetfinder {dominio} > {dominio}/assetfinder.txt"

    t1 = threading.Thread(target=comand_run, args=(subfinder,))
    t2 = threading.Thread(target=comand_run, args=(assetfinder,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    comand_run(f"sort -u {dominio}/assetfinder.txt {dominio}/subfinder.txt > {dominio}/subdominios.txt")

elif sys.argv[1] == "-u":

    wayback = f"cat {sys.argv[2]} | waybackurls > wayback.txt"
    katana = f"cat {sys.argv[2]} | katana -silent -d 10 -o katana.txt"
    gau = f"cat {sys.argv[2]} | gau > gau.txt"

    t1 = threading.Thread(target=comand_run,args=(wayback,))
    t2 = threading.Thread(target=comand_run, args=(katana,))
    t3 = threading.Thread(target=comand_run, args=(gau,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    comand_run("sort -u gau.txt katana.txt wayback.txt > fullurls.txt")

elif sys.argv[1] == "-js":

    subprocess.run(f"cat {sys.argv[2]} | while read url; do python3 /usr/local/bin/SecretFinder/SecretFinder.py -i $url -o cli; done")

elif sys.argv[1] == "-h" or "--help":
    
    print("-d         scan de subdominios com base em dominio")
    print("-u         scan de urls com base em subdominios e dominios")
    print("-js        scan de javascript")
