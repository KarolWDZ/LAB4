Wprowadzenie
Wielokryterialne podejmowanie decyzji (MCDM – Multiple-Criteria Decision Making) obejmuje metody pozwalające oceniać alternatywy opisane wieloma kryteriami. W praktyce umożliwia to wybór najlepszej opcji w sytuacjach,
gdzie decyzja zależy od wielu czynników, takich jak koszty, zyski, czas realizacji czy ryzyko.

Biblioteka pymcdm w języku Python dostarcza narzędzia do normalizacji danych, wyznaczania wag oraz stosowania metod decyzyjnych, takich jak TOPSIS, SPOTIS, VIKOR czy PROMETHEE. Celem niniejszego raportu jest wykonanie analizy porównawczej metod TOPSIS i SPOTIS dla przykładowego zbioru danych.

Konfiguracja analizy
W analizie wykorzystano cztery alternatywy (A1–A4) oraz cztery kryteria:

– koszt (minimalizowany)
– zysk (maksymalizowany)
– czas realizacji (minimalizowany)
– ryzyko (minimalizowane)

Macierz decyzyjna została przygotowana w postaci tablicy numpy. Wagi kryteriów ustalono jako: 0.3, 0.3, 0.2, 0.2. Typy kryteriów określono jako: -1, 1, -1, -1.

Przed zastosowaniem metod MCDM wykonano normalizację danych metodą min-max, dostępną w bibliotece pymcdm.

Do obliczeń wykorzystano dwie metody:
– TOPSIS – metoda oparta na odległości od rozwiązania idealnego i anty-idealnego,
– SPOTIS – metoda oparta na odległości od punktu referencyjnego.

Wyniki analizy
Wyniki uzyskane metodą TOPSIS wskazały następujący ranking alternatyw (od najlepszej):

A2

A4

A1

A3

Wyniki metody SPOTIS (niższa wartość = lepsza alternatywa) również wskazały identyczny ranking:

A2

A4

A1

A3

Wnioski
Obie metody – TOPSIS i SPOTIS – wskazały tę samą najlepszą alternatywę (A2). Oznacza to, że alternatywa A2 charakteryzuje się najlepszym kompromisem pomiędzy kosztami, zyskiem, czasem realizacji i ryzykiem.
Alternatywa A4 również wypada korzystnie, natomiast A1 i A3 są oceniane słabiej.
