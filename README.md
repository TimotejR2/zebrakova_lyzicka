# Žebrákové lyžičky

Tento projekt sa zameriava na počítanie pravdepodobnosti pomocou simulácie všetkých možných svetov, aby sme vypočítali pravdepodobnosť, že Žebrák už jedol s lyžičkou, ktorú si náhodne vyberieme.

---

## Zadanie
Úloha spočíva vo výpočte pravdepodobnosti, že náhodne vybratá lyžička bola už použitá Žebrákom.

---

## Použitie
Ak chcete spustiť skript, použite nasledujúci príkaz:
```bash
python3 main.py
```

---

## Výsledok
Výsledok bude uložený do nového súboru `result.txt`.

---

## Modifikácie
Nastavenia, ako počet lyžičiek a počet dní, môžete upraviť v súbore config.py.

---

## Presnosť 
Počet desatinných miest vo výsledku je určený nasledovným vzorcom:
```bash
počet_desatinných_miest = PRECISION + PRECISION * (poradové_číslo_dňa * 2)
```
Poznámka: Číslovanie dní začína od nuly.

## Licencia
Tento projekt je licencovaný pod licenciou GPL 3.0.