#!/bin/bash

# ========================================
# =           simple calculator          =
# ========================================
echo "Įveskite pirmą reikšmę"
read a

echo "Įveskite antrą reikšmę "
read b

echo "Kokį veiksmą norite atlikti? (+, -, *, /)."
read veiksmas

case "$veiksmas" in
    +|-|\*|/)
        if [ "$veiksmas" = "/" ] && [ "$b" = "0" ]; then
            echo "Klaida: dalyba iš nulio neleidžiama."
            exit 1
        fi
        rezultatas=$(awk "BEGIN { res = $a $veiksmas $b; if (res == int(res)) printf \"%d\", res; else printf \"%.2f\", res }");;
    *) echo "Kažkokią nesąmonę įvedei. ALT F4 initiated"; exit 1;;
esac

echo "Rezultatas: $rezultatas"

case "$rezultatas" in
    420) echo "Smoke weed everyday LOL";;
    404) echo "PAGE NOT FOUND";;
    *) ;;
esac