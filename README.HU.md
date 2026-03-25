🇬🇧 [English version](README.md)
# Knowledge-injection-ai
**Ne az AI „emlékezzen” – a rendszered kezelje a tudást.**

Ez a projekt egy egyszerű koncepciót mutat be arra, hogyan lehet strukturált tudást adni AI rendszereknek futásidőben.

Ahelyett, hogy a modellt tartósan tanítanánk (fine-tuning), a rendszer minden egyes feladathoz külön biztosítja a szükséges tudást, strukturált formában.

A beinjektált tudás tartalmazhat:
- szabályokat
- korlátozásokat
- validációs követelményeket
- példákat
- feladatleírást

Ezáltal az AI viselkedése:
- könnyebben kontrollálható
- ellenőrizhető (auditálható)
- különböző modellek között összehasonlítható

---

## Miért nem fine-tuning?

- nehezen kontrollálható  
- nem auditálható  
- nem verziózható  

---

## Miért futásidejű tudás?

- jól kontrollálható  
- tesztelhető  
- modellfüggetlen  

---

## Use case architektúra

knowledge/ → prompt builder → LLM → validáció → eredmény  

---

## Repository struktúra

- knowledge/
  - examples/
  - constraints.md
  - rules.md
  - validation.md
  - task.md
- prompt_builder.py

---

## Komponensek

### examples/
Futtatható példákat tartalmaz, amelyek az elvárt működést írják le.  
Minden példa tartalmaz egy bemenetet és a hozzá tartozó elvárt kimenetet.

### task.md
Meghatározza, hogy az AI-nak pontosan milyen feladatot kell végrehajtania.

### constraints.md
Meghatározza, mit NEM tehet az AI  
(pl. nincs hallucináció, nincs találgatás).

### rules.md
Meghatározza, hogyan viselkedjen az AI, és milyen formátumban adja vissza az eredményt.

### validation.md
Meghatározza, mit tekintünk helyes kimenetnek.

---

## Példa használat

```python
from prompt_builder import build_prompt

prompt = build_prompt(
    knowledge_path="knowledge"
)

print(prompt)
```
## Jó ha tudod
Ha az LLM támogatja az anyanyelvedet, akkor azon is használhatod.  
Magyarul is kipróbáltam, és jól működött.