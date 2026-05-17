if __name__ == "__main__":
    print("Średnia ważona - kalkulator\n")
    list = []
    weights = []
    user_input = ""
    while True:
        user_input = input("Podaj liczbę całkowitą:")
        if user_input == "exit" or user_input == "":
            break
        
        weight = input("Podaj wagę liczby:")

        list.append(int(user_input) * int(weight))
        weights.append(int(user_input))
        
    sum = 0
    weights_total = 0
    for i in list:
        sum += i

    for w in weights:
        weights_total += w

    avg = sum / w
    print(f"Twoja średnia ważona to: {avg}")
    print("Zamykanie programu...")
