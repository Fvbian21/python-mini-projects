from datetime import datetime

def oblicz_roznice(start_str, end_str):
    try:
        start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
        delta = end_time - start_time

        dni = delta.days
        sekundy = delta.seconds
        godziny = sekundy // 3600
        minuty = (sekundy % 3600) // 60

        print(f"Minęło: {dni} dni, {godziny} godzin, {minuty} minut")
    except ValueError:
        print("Nieprawidłowy format daty. Użyj formatu YYYY-MM-DD HH:MM")

def main():
    print("=== Kalkulator czasu między datami ===")
    start = input("Podaj datę początkową (YYYY-MM-DD HH:MM): ")
    end = input("Podaj datę końcową (YYYY-MM-DD HH:MM): ")
    oblicz_roznice(start, end)

if __name__ == "__main__":
    main()