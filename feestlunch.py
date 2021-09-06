croissant = 17
stokbrood = 2
kortingbon = 3
a = (croissant * 0.39) + (stokbrood * 2.78) - (kortingbon * 0.50)
print(a)
if a == (18.88):
    print("De feestlunch kost je bij de bakker " + str(a) + " euro voor de " + str(croissant) + ' croissantjes en de ' + str(stokbrood) + " stokbroden als " + str(kortingbon) + " kortingsbonnen nog geldig zijn!")