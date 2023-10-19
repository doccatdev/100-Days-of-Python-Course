# Exercise 13 : Making Change

PENNY_COINS = 1
NICKEL_COINS = 5
DIME_COINS = 10
QUARTER_COINS = 25
LOONIE_COINS = 100
TONIE_COINS = 200

change = input("Masukan kembalian yang ingin dipecahkan $")
change = int(change)

print(" ", change // TONIE_COINS, "toonies")
change = change % TONIE_COINS