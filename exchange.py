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
kurz_str = kurz_str