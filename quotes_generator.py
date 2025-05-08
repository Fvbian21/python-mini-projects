import random

# Lista cytatów do wyboru
quotes = [
    "Nie czekaj na idealny moment. Chwytaj chwile i działaj!",
    "Każdy dzień to nowa szansa, by zmienić swoje życie.",
    "Sukces to suma małych wysiłków powtarzanych codziennie.",
    "Nie musisz być wielki, żeby zacząć — ale musisz zacząć, by być wielki.",
    "Zrób dziś coś, czego przyszły Ty Ci podziękuje."
]

# Funkcja wybierająca losowy cytat
def get_random_quote():
    return random.choice(quotes)

# Główna logika programu
def main():
    quote = get_random_quote()
    print("💬 Dzisiaj wybrany cytat:")
    print(f'"{quote}"')

if __name__ == "__main__":
    main()
