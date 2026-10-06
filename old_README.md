# Python

---

## Úkol 1 – Domeček

Napište program, který nakreslí domeček ze znaků `X`. Program se uživatele zeptá na šířku a výšku domečku a pak ho vykreslí.

### Pravidla

- Šířka a výška musí být celá čísla od **3 do 69** (včetně).
- Šířka musí být **liché číslo** (3, 5, 7, ...). Pokud není, program napíše chybu a skončí (příkaz `exit()`).
- **Střecha** je trojúhelník ze znaků `X` - střecha je uvnitř dutá.
- **Tělo** je obdélník – tělo je duté.

>TIP: Střecha má tolik řádků, kolik je polovina šířky (zaokrouhleno dolů)

### Příklady

**Vstup:** `7 4`
```
   X
  X X
 X   X
XXXXXXX
X     X
X     X
XXXXXXX
```

**Vstup:** `5 3`
```
  X
 X X
XXXXX
X   X
XXXXX
```

### Chybné vstupy

| Situace | Výpis programu |
|---|---|
| Uživatel zadá písmeno místo čísla | `Chyba: zadej cela cisla!` |
| Číslo je mimo rozsah 3–69 | `Chyba: cisla musi byt v rozsahu 3 az 69!` |
| Šířka je sudá | `Chyba: sirka musi byt liche cislo!` |

>TIP: Pro skončení programu se používá příkaz `exit()`

### Bonus – plot

Pokud jsou šířka a výška stejné, zeptejte se uživatele, jestli chce přidat plot. Pokud ano, načtěte velikost plotu (musí být alespoň 1 a méně než výška). Plot se vykreslí vedle domečku.

Plot velikosti 4 k domečku 5x5 vypadá takto:
```
  X
 X X
XXXXX
X   X-|-|
X   X | |
X   X | |
XXXXX-|-|
```

---

## Úkol 2 – Sierpińského trojúhelník

Napište program, který vypíše Sierpińského trojúhelník. Je to **fraktál** – vzor, který se sám opakuje v menším měřítku donekonečna. Výšku zadá uživatel.

Doporučené výšky: **8, 16 nebo 32**.

### Jak to funguje

Pro každý řádek `r` (od 0 do výšky - 1) a sloupec `s` (od 0 do `r`):
- Spočítejte kombinační číslo `C(r, s)`.
- Pokud je `C(r, s)` **liché** → vytiskne se `* ` (hvězdička + mezera)
- Jinak se vytiskne `  ` (dvě mezery)

### Jak spočítat C(r, s)

Kombinační číslo `C(r, s)` se počítá takhle (okopírujte si to na úplný začátek programu)

```python
def kombinacni_cislo(r, s):
    c = 1
    for i in range(s):
        c = c * (r - i) // (i + 1)
    return c
```

V samotném programu poté stačí napsat toto:

```python
kombinacni_cislo(r, s)
```

> `c` je samotné kombinační číslo, `s` je sloupec, `r` je řádek
> Například `C(4, 2) = 6` (sudé → mezera), `C(5, 1) = 5` (liché → `*`).

### Postup řešení

1. Načtení výšky od uživatele.
2. Vnější cyklus: pro každý řádek `r` od `0` do `výška - 1`.
4. Vnitřní cyklus: pro každý sloupec `s` od `0` do `r`.
5. Výpočet kombinačního čísla `C(r, s)`. Pokud je liché, vytiskne se `'* '`, jinak `'  '`.
6. Na konci řádku `print()` pro nový řádek.

### Příklad výstupu

**Výška 8:**
```
*
* *      
*   *     
* * * *    
*       *   
* *     * *  
*   *   *   * 
* * * * * * * *
```

**Výška 16:**
```
*               
* *              
*   *             
* * * *            
*       *           
* *     * *          
*   *   *   *         
* * * * * * * *        
*               *       
* *             * *      
*   *           *   *     
* * * *         * * * *    
*       *       *       *   
* *     * *     * *     * *  
*   *   *   *   *   *   *   *
* * * * * * * * * * * * * * * *
```

### Bonus
Vycentrujete trojúhelník.
