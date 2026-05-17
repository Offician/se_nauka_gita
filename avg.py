if __name__ == "__main__":
    print("Średnia arytmetyczna - kalkulator\n")
    list = []
    user_input = ""
    while True:
        user_input = input("Podaj liczbę całkowitą:")
        if user_input == "exit" or user_input == "":
            break
        user_input = int(user_input)
        list.append(user_input)
        
    sum = 0
    for i in list:
        sum += i
    avg = sum / list.__len__()
    print(f"Twoja średnia to: {avg}")
    print("Zamykanie programu...")