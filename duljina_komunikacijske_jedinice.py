# program koji ispisuje i vraća najdulju komunikacijsku jedinicu koje je dijete izgovorilo
import os

# ako netko ovo isproba samostalno, mora staviti path na put do vlastite mape u računalu
path = r"UPISITE VASU PUTANJU OVDJE"

def broj_rijeci(tekst):
    return len(tekst.strip().split())

for filename in os.listdir(path):
    if filename.endswith(".cha"):
        file_path = os.path.join(path, filename)
        with open(file_path, 'r', encoding='utf-8') as tekst:
            kom_jedinice = []
            najduza = ""
            najvise_rijeci = 0
            for line in tekst:
                if line.startswith("*CHI:"):
                    jedinica = line[5:].strip()
                    kom_jedinice.append(jedinica)
                    br_rijeci = broj_rijeci(jedinica)
                    if br_rijeci > najvise_rijeci:
                        najvise_rijeci = br_rijeci
                        najduza = jedinica
            print(f"{filename}, {najduza}")
