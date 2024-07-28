#!/usr/bin/env python
import os
import threading
import sys

os.system("figlet steet")
print("             by inotsu\n\n")

if sys.argv[1] == "-d":
    dominio = sys.argv[2]
    os.system(f"mkdir {dominio}")
    threading.Thread(target=os.system(f"assetfinder {dominio} > {dominio}/assetfinder.txt"))
    os.system(f"subfinder -silent -d {dominio} -all -o {dominio}/subfinder.txt")
    os.system(f"sort -u {dominio}/assetfinder.txt {dominio}/subfinder.txt > {dominio}/subdominios.txt")
elif sys.argv[1] == "-u":
    threading.Thread(target=os.system(f"cat {sys.argv[2]} | waybackurls > wayback.txt"))
    threading.Thread(target=os.system(f"cat {sys.argv[2]} | katana -silent -d 10 -o katana.txt"))
    os.system(f"cat {sys.argv[2]} | gau > gau.txt")
    os.system("sort -u gau.txt katana.txt wayback.txt > fullurls.txt")
elif sys.argv[1] == "-js":
    os.system(f"cat {sys.argv[2]} | while read url; do python3 /usr/local/bin/SecretFinder/SecretFinder.py -i $url -o cli; done")
elif sys.argv[1] == "-h" or "--help":
    print("-d         scan de subdominios com base em dominio")
    print("-u         scan de urls com base em subdominios e dominios")
    print("-js        scan de javascript")