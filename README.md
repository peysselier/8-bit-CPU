# Mini CPU

64 registres de code
15 registres CPU

## Liste des opérations

- **ALU** : ADD, OR, XNOR, NAND, NOR, XOR, AND, SUB  
- **CODE** : LOAD, HALT, JUMP, JUMPIF  

---

## Syntaxes

### Opérations d'ALU

- `Ri` : registre de destination (écrit)
- `Rj` et `Rk` : registres opérés

**Exemple avec SUB :**

Dans `R3`, on calcule `R1 - R2`

---

### Opérations CODE

#### HALT

- Permet de couper la clock  
- S'écrit seul : HALT

---

#### LOAD

- Permet de mettre une valeur dans un registre  
- Syntaxe : LOAD Ri A

- `Ri` : registre écrit  
- `A` : nombre décimal  

---

#### JUMP

- Permet de changer la valeur de la clock  
- Syntaxe : JUMP B

- `B` : nouvelle valeur de la clock  

---

#### JUMPIF

- Permet de changer la valeur de la clock si le dernier résultat de l'ALU vaut 0  
- Syntaxe : JUMPIF B

- `B` : nouvelle valeur de la clock  
