number_of_month = int(input("Enter a number (1-12): "))

match number_of_month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 2:
        print("28/29 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case _:
        print("Incorrect number...")




