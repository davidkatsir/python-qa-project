experience = int(input('Enter your experience: (range of 1-5): '))

match experience:
    case 1:
        print("You're a beginner.")
    case 2:
        print("You're an intermediate.")
    case 3 | 4 | 5:
        print("You're an expert.")
    case _:
        print("There is an invalid choice.")
