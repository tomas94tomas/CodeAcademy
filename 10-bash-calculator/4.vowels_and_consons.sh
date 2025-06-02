#!/bin/bash

# ========================================
# =           simple calculator          =
# ========================================

echo "Įveskite vieną raidę:"
read simbolis
case "$simbolis" in
    [aeiouąęėįųūAEIOUĄĘĖĮŲŪ]) echo "Tai balsė.";;
    [bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]) echo "Tai priebalsė.";;
    *) echo "Neatpažintas simbolis.";;
esac