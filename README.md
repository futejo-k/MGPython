## Bonusy pro rychlé
## Bonus 1 - Obrácené slovo a palindrom
Napište program, který obrátí slovo zadané uživatelem a zjistí, jestli je to palindrom (čte se stejně zepředu i zezadu).

**Zadání:**
- Program se zeptá uživatele na slovo (pomocí `input()`)
- Program vypíše slovo pozpátku
- Program vypíše, jestli je slovo palindrom
- Velikost písmen nehraje roli (*Kajak* je taky palindrom)

### Příklady
**Vstup:** `kajak`

**Výstup:**
```
kajak
Je to palindrom
```
---
**Vstup:** `python`

**Výstup:**
```
nohtyp
Neni to palindrom
```

Zkuste to i bez `[::-1]`, jen pomocí cyklu.

---
## Bonus 2 - Počítadlo samohlásek
Napište program, který spočítá, kolik samohlásek je ve větě zadané uživatelem.

**Zadání:**
- Program se zeptá uživatele na větu
- Samohlásky jsou: `a e i o u y` a také `á é ě í ó ú ů ý`
- Velká i malá písmena se počítají (pomůže `lower()`)
- Program vypíše počet samohlásek

### Příklady
**Vstup:** `Ahoj, jak se mas?`

**Výstup:**
```
Pocet samohlasek: 5
```
---
**Vstup:** `Programovani v Pythonu`

**Výstup:**
```
Pocet samohlasek: 8
```

---
## Bonus 3 - Seznam čísel a průměr
Napište program, který si čísla od uživatele ukládá do seznamu a pak s nimi počítá.

**Zadání:**
- Program začne s prázdným seznamem `cisla = []`
- Program se pořád dokola ptá na číslo (pomocí `int(input())`) a přidává ho do seznamu přes `append()`
- Program skončí po zadání čísla **0** (nula se do seznamu nepřidá)
- Poté program vypíše:
	- Celý seznam
	- Součet čísel
	- Průměr čísel
	- Seznam čísel, která jsou větší než průměr

### Příklady
**Vstup:**
```
4
8
15
16
23
42
0
```

**Výstup:**
```
Seznam: [4, 8, 15, 16, 23, 42]
Soucet: 108
Prumer: 18.0
Nad prumerem: [23, 42]
```
---
**Vstup:**
```
1
2
3
0
```

**Výstup:**
```
Seznam: [1, 2, 3]
Soucet: 6
Prumer: 2.0
Nad prumerem: [3]
```

---
## Bonus 4 - Bez duplicit
Napište program, který si pamatuje zadaná slova, ale každé jen jednou.

**Zadání:**
- Program se pořád dokola ptá na slovo
- Pokud slovo v seznamu ještě není, přidá ho (pomůže `in`)
- Pokud už tam je, nepřidá ho
- Program skončí po zadání slova **konec**, poté vypíše seznam

### Příklady
**Vstup:**
```
pes
kocka
pes
rybicka
kocka
konec
```

**Výstup:**
```
['pes', 'kocka', 'rybicka']
```

---
## Bonus 5 - Caesarova šifra
Napište program, který zašifruje slovo Caesarovou šifrou: každé písmeno se posune v abecedě o zadaný počet míst.

Co je to Caesarova šifra si můžete přečíst na Wikipedii [Caesarova šifra](https://cs.wikipedia.org/wiki/Caesarova_%C5%A1ifra)

**Zadání:**
- Program se zeptá na slovo (jen malá písmena bez diakritiky) a na posun (číslo)
- Abecedu si uložte jako řetězec `abeceda = "abcdefghijklmnopqrstuvwxyz"`
- Pozici písmene najdete pomocí `abeceda.index(pismeno)`
- Když se dojde na konec abecedy, pokračuje se znovu od začátku (`z` posunuté o 1 je `a`), pomůže operátor `%`
- Program vypíše zašifrované slovo

### Příklady
**Vstup:**
```
ahoj
3
```

**Výstup:**
```
dkrm
```
---
**Vstup:**
```
zebra
1
```

**Výstup:**
```
afcsb
```

Pro super rychlé: napište i dešifrování (posun opačným směrem).
