# GameOfLifePyGame

Jest to implementacja "Gry w Życie Conwaya" korzystając z pythona 3.7 i biblioteki pygame.

## Instalacja

Do uruchomienia programu wystarczy nam python w wersji 3.7(w moim wypadku 3.7.7) i biblioteka pygame, aby ją zainstalować należy:

```bash
pip install pygame
```
lub skorzystać z pliku requirements.txt :
```bash
pip install -r requirements.txt 
```

## Uruchamianie

```python
python3 main.py
```

## Działanie
Kod działa w następujących krokach:
1. Generuje dwywymiarową tablicę o podanych wymiarach, w których znajdują się wartości 0 lub 1 (nieżywa/żywa).
2. Zależnie od zasad gry (Gdy martwa komórka posiada dokładnie 3 żywych sąsiadów, w następnej jednostce czasu staje się ona żywa.
Gdy natomiast żywa komórka posiada inną liczbę żywych sąsiadów od 2 lub 3, umiera.) zmieniane są wartości w poszczególnych polach. 
3. Każda kolejna generacja się zmienia w pojedynczej jednostce czasu aż dojdziemy do generacji w której wartości pozostają niezmienne.
