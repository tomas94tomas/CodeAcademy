#!/bin/bash

# ========================================
# =           simple calculator          =
# ========================================

echo "Įveskite norimą skaičių lentelės generavimui :"
read a
for i in $(seq 1 10)
do
    echo "$a padauginta iš $i yra $((a * i)) "
done