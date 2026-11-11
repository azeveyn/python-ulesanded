
# ÜLESANNE 1 – Kuupäev ja vanus

from datetime import *

tana = date.today()

print("Tere! Täna on:")
print(tana)

print(tana.strftime("%d/%m/%Y"))
print(tana.strftime("%B %d, %Y"))
print(tana.strftime("%m/%d/%y"))
print(tana.strftime("%b-%d-%Y"))

print("Päev:", tana.day)
print("Kuu:", tana.month)
print("Aasta:", tana.year)

# Päevi kuu lõpuni
kuu_lopp = date(tana.year, tana.month, calendar.monthrange(tana.year, tana.month)[1])
print("Päevi kuu lõpuni:", (kuu_lopp - tana).days)

# Päevi aasta lõpuni
aasta_lopp = date(tana.year, 12, 31)
print("Päevi aasta lõpuni:", (aasta_lopp - tana).days)

# Vanuse arvutamine
sunnipaev = date(
    int(input("Sisesta sünniaasta: ")),
    int(input("Sisesta sünnikuu: ")),
    int(input("Sisesta sünnipäev: "))
)

aastad = tana.year - sunnipaev.year
kuud = tana.month - sunnipaev.month
paevad = tana.day - sunnipaev.day

if paevad < 0:
    kuud -= 1
    eelmine_kuu = tana.month - 1
    eelmine_aasta = tana.year
    if eelmine_kuu == 0:
        eelmine_kuu = 12
        eelmine_aasta -= 1
    paevad += calendar.monthrange(eelmine_aasta, eelmine_kuu)[1]

if kuud < 0:
    aastad -= 1
    kuud += 12

print("Sinu vanus:", aastad, "aastat,", kuud, "kuud ja", paevad, "päeva.")


# ÜLESANNE 2 – Tehted ja sulud

tehe1 = 3 + 8 / (4 - 2) * 4
tehe2 = 3 + 8 / 4 - 2 * 4
tehe3 = (3 + 8) / (4 - 2) * 4
tehe4 = 3 + 8 / ((4 - 2) * 4)

print("Tehe 1:", tehe1)
print("Tehe 2:", tehe2)
print("Tehe 3:", tehe3)
print("Tehe 4:", tehe4)

print("Sulud muudavad tehete järjekorda.")
print("Ilma sulgudeta arvutab Python korrutamise ja jagamise enne liitmist ja lahutamist.")


# ÜLESANNE 3 – Ruut ja ring

import math

R = float(input("Sisesta ringi raadius: "))

ruudu_kulg = R * 2

ruudu_pindala = ruudu_kulg ** 2
ruudu_umbermoot = ruudu_kulg * 4

ringi_pindala = math.pi * R ** 2
ringi_umbermoot = 2 * math.pi * R

print("Ruudu pindala:", ruudu_pindala)
print("Ruudu ümbermõõt:", ruudu_umbermoot)
print("Ringi pindala:", ringi_pindala)
print("Ringi ümbermõõt:", ringi_umbermoot)


# ÜLESANNE 4 – Maa ümbermõõt 2-eurostes müntides

import math

maa_raadius = 6378       # km
mundi_labimoot = 25.75   # mm

maa_umbermoot = 2 * math.pi * maa_raadius
maa_umbermoot_mm = maa_umbermoot * 1000000

muntide_arv = maa_umbermoot_mm / mundi_labimoot

print("Maa ümbermõõt:", round(maa_umbermoot, 2), "km")
print("Vajalik müntide arv:", round(muntide_arv))


# ÜLESANNE 5 – Kill-koll

sona1 = "kill-koll"
sona2 = "killadi-koll"

tekst = (sona1 + " ") * 2 + sona2 + " "
tekst = tekst + (sona1 + " ") * 2 + sona2 + " "
tekst = tekst + (sona1 + " ") * 3

print(tekst.upper())
print(sona1.upper())

# ÜLESANNE 6 – Laulusõnad suurte tähtedega

# Lisa siia ülesandes antud laulusõnad
laul = """
SISESTA SIIA OMA LAULUSÕNAD
"""

print(laul.upper())


# ÜLESANNE 7 – Ristküliku ümbermõõt ja pindala

a = float(input("Sisesta ristküliku esimene külg: "))
b = float(input("Sisesta ristküliku teine külg: "))

umbermoot = 2 * (a + b)
pindala = a * b

print("Ristküliku ümbermõõt:", umbermoot)
print("Ristküliku pindala:", pindala)


# ÜLESANNE 8 – Kütusekulu arvutamine

liitrid = float(input("Mitu liitrit kütust tankisid? "))
kilomeetrid = float(input("Mitu kilomeetrit sõitsid? "))

if kilomeetrid > 0:
    kulu = liitrid / kilomeetrid * 100
    print("Kütusekulu 100 km kohta:", round(kulu, 2), "l")
else:
    print("Kilomeetrite arv peab olema suurem kui 0.")


# ÜLESANNE 9 – Rulluisutajad

kiirus = 29.9

minutid = float(input("Mitu minutit rulluisutaja sõidab? "))

teepikkus = kiirus * minutid / 60

print("Rulluisutaja läbib", round(teepikkus, 2), "km.")


# ÜLESANNE 10 – Ajateisendus

minutid = int(input("Sisesta aeg minutites: "))

tunnid = minutid // 60
jaak = minutid % 60

print("Aeg:", tunnid, ":", str(jaak).zfill(2))
