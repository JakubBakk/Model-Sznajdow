# Sznajd-Model
Model sznajdów jest to model bazujący na społecznym dowodzie słuszności. Jest to zasada, w imię której człowiek, nie wiedząc, jaka decyzja lub jaki pogląd jest słuszny (co może zależeć od różnych czynników), podejmuje decyzje lub przyjmuje poglądy takie same, jak większość grupy. W tym konkretnym modelu Sznajdów dwóch sąsiadów, którzy mają te same poglądy wpływają na swych sąsiadów, nadając im swoją opinię. Nie rozpatrujemy przypadku, gdy sąsiedzi mają różne opinie(co prowadzi do skłócenia swoich sąsiadów).
W tym projekcie stworzyłem taki model Sznajdów z założeniami zgodnymi dla każdego zadania:
- Grupa społeczna jest przedstawiona za pomocą dwuwymiarowej sieci z periodycznymi warunkami brzegowymi
- Istnieje opinia za(o wartości 1) oraz przeciw(wartość 0)
- W chwili początkowej sieć jest uzupełniana losowymi wartościami, które mają symulować rozkład opinii
- W każdym kroku czasowym wybierana jest dowolna para sąsiadów(zarówno pozioma jak i pionowa)
