import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization

# -----------------------------
# 1. PRZYGOTOWANIE DANYCH
# -----------------------------

# Macierz decyzyjna: wiersze = alternatywy, kolumny = kryteria
X = np.array([
    [100, 50, 12, 3],   # A1
    [120, 60, 10, 2],   # A2
    [90,  55, 14, 4],   # A3
    [110, 65, 11, 3],   # A4
])

# Wagi kryteriów
w = np.array([0.3, 0.3, 0.2, 0.2])

# Typy kryteriów: 1 = maksymalizowane, -1 = minimalizowane
types = np.array([-1, 1, -1, -1])

# -----------------------------
# 2. NORMALIZACJA DANYCH
# -----------------------------

X_norm = minmax_normalization(X, types)

# -----------------------------
# 3. METODA TOPSIS
# -----------------------------

topsis = TOPSIS()
scores_topsis = topsis(X_norm, w, types)

print("Wyniki TOPSIS:", scores_topsis)
print("Ranking TOPSIS (od najlepszego):", np.argsort(-scores_topsis) + 1)

# -----------------------------
# 4. METODA SPOTIS
# -----------------------------

# Punkt referencyjny: wartości idealne i anty-idealne
ref_points = np.array([
    [80, 40, 8, 1],    # idealne wartości
    [130, 70, 16, 5],  # najgorsze wartości
])

spotis = SPOTIS()
scores_spotis = spotis(X, w, types, ref_points)

print("\nWyniki SPOTIS:", scores_spotis)
print("Ranking SPOTIS (od najlepszego):", np.argsort(scores_spotis) + 1)
