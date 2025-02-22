import httpx

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025'

r = httpx.get(url)



lines = r.text.split("\n")
row = ""

for line in lines:
    if "|EUR|" in line:
        row = line

row_arr = row.split("|")
kurz_str = row_arr[-1]
kurz_str = kurz_str.replace(",", ".")
kurz = float(kurz_str)

while True:
    print("Vyberte typ konverze. 1 = EUR -> CZK. 2 = CZK -> EUR")
    konverze = input()
    try:
        konverze = int(konverze)
        if konverze == 1 or konverze == 2:
            break
        else:
            print("Zadejte cislo 1 nebo 2")
            continue
    except:
        print("Zadejte cislo")
        continue

while True:
    print("Zadejte castku: ")
    castka = input()
    try:
        castka = float(castka)
        if castka > 0:
            break
        else:
            print("Zadejte kladne cislo")
            continue
    except:
        print("Zadejte cislo")
        continue

if konverze == 1:
    vysledek = castka * kurz
elif konverze == 2:
    vysledek = castka / kurzex
else:
    print("Neco se pokazilo")

print(f"Vysledek je {vysledek}")