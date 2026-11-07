## Úkol 1 - FizzBuzz (budeme dělat společně na hodině)
Napište program, který vypíše čísla od 1 do 100 včetně.
**Pravidla:**
- Pokud je číslo dělitelné 3, vypíše se *Fizz*
- Pokud je číslo dělitelné 5, vypíše se *Buzz*
- Pokud je číslo dělitelné 3 a 5 zároveň, vypíše se *FizzBuzz*
- Jinak se vypíše číslo samotné

---

## Úkol 2 - Statistika sudých a lichých čísel
Napište program, který se pořád dokola ptá na čísla a pak znich dělá statistiku.
**Zadání"**
- Program se ptá pořád dokola na číselný vstup (pomocí `int(input())`)
- Ze zadaných čísel se počítají statistiky:
	- Počet sudých zadaných čísel
	- Počet lichých zadaných čísel
	- Největší zadané číslo
	- Nejmenší zadané číslo
- Program skončí po zadání čísla **0**, poté vypíše statistiky

### Příklady
**Vstup:**
```
5
6
7979
456
0489
456
454
0
```

**Výstup:**
```
Pocet sudych: 4
Pocet lichych: 3
Nejvyssi zadane cislo: 7979
Nejnizsi zadane cislo: 5
```
---
**Vstup:**
```
1
2
3
4
5
6
7
8
9
10
0
```

**Výstup:**
```
Pocet sudych: 5
Pocet lichych: 5
Nejvyssi zadane cislo: 10
Nejnizsi zadane cislo: 1
```

## Bonusy pro rychlé
## Bonus 1 - Kámen, nůžky, papír
Napište program, ve kterém bude hráč hrát s počítačem hru *Kámen, nůžky, papír* na tři výhry.

**Zadání:**
- Počítač si vybere svůj tah: kámen - 1, nůžky - 2, papír - 3
- Program se zeptá uživatele na jeho tah
- Program vypíše, co hraje počítač
- Program vypíše, kdo vyhrál toto kolo, případně remízu
- Program vypíše poměr výher mezi počítačem a hráčem
- Pokud počítač nebo hráč vyhrál potřetí, vypíše program kdo vyhrál a poměr výher a poté skončí

---
## Bonus 2 - Collatzův problém
Napište program, který vypíše průběh Collatzova problému pro číslo zadané uživatelem

Co je to Collatzův problém si můžete přečíst na Wikipedii [Collatzův problém](https://cs.wikipedia.org/wiki/Collatz%C5%AFv_probl%C3%A9m)

**Pravidla:**
- Pokud je číslo sudé, vydělí se dvěma
- Pokud je číslo liché, vynásobí se třemi a poté se přičte jedna
- Pokud je číslo 1, program skončí
- Každé číslo se vypíše

### Příklady
**Vstup:** `20`

**Výstup:**
```
20
10.0
5.0
16.0
8.0
4.0
2.0
1.0
```
---
**Vstup:** `9`

**Výstup:**
```
9
28
14.0
7.0
22.0
11.0
34.0
17.0
52.0
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
```

Pokud chcete, můžete čísla vypisovat bez desitinného místa
