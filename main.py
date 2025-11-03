from game import play_loop
from tutorial import run_tutorial

def get_key_blocking():
    k = input("Press key (1-4): ").strip()
    return k[:1] if k else ""

def menu():
    print("\nAudio Echo Memory")
    print("[1] Tutorial  [2] Play  [q] Quit")
    return input("> ").strip()

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            run_tutorial(get_key_blocking)
        elif choice == "2":
            score, high = play_loop(get_key_blocking)
            print(f"Game over. Score={score}, HighScore={high}")
        elif choice.lower() == "q":
            break
