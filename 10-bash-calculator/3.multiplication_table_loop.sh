#!/bin/bash

# ========================================
# =           simple calculator          =
# ========================================

echo "Įrašykite skaičių, kuriam skaičiuoti lentelę (1–10):"
read skaicius
indeksas=1
while [ "$indeksas" -le 10 ]
do
    echo "$skaicius x $indeksas = $((skaicius * indeksas)) "
    ((indeksas++))
done