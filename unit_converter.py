import argparse

def convert_meters_to_feet(meters):
    feet = meters * 3.2808
    return feet

def main():
    parser = argparse.ArgumentParser(description="Konwertuj metry na stopy")
    parser.add_argument('--metry', type=float, required=True, help='Wartość w metrach do przeliczenia')
    args = parser.parse_args()

    feet = convert_meters_to_feet(args.metry)
    print(f"{args.metry} metrów to {feet:.2f} stopy")

if __name__ == "__main__":
    main()