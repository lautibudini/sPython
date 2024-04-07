#Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
#luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
celcius = float(input("ingrese una temperatura en grados celcius"))
celcius = ((celcius* 9)/5) + 32
print(f"la temperatura ingresada en celcuis convertida en fahrenheit es : {celcius}")