# Pobranie danych od użytkownika
waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach (np. 1.80): "))

# Obliczenie BMI
BMI = waga / (wzrost * wzrost)

# Wyświetlenie wyniku BMI
print(f"Twoje BMI wynosi: {BMI:.2f}")

# Interpretacja wyniku
if BMI < 18.5:
    print("Masz niedowagę.")
elif BMI < 24.9:
    print("Masz prawidłową wagę.")
elif BMI < 29.9:
    print("Masz nadwagę.")
else:
    print("Masz otyłość.")