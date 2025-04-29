import random
import string

def generate_password(length):
    # Dostępne znaki: litery małe, litery duże, cyfry, znaki specjalne
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generowanie hasła
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Podaj długość hasła: "))
        if length < 7:
            print("Długość hasła musi mieć co najmniej 7 znaków.")
        else:
            password = generate_password(length)
            print(f"Twoje wygenerowane hasło: {password}")
    except ValueError:
        print("Proszę podać poprawną liczbę.")

if __name__ == "__main__":
    main()