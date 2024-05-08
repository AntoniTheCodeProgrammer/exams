def check(PESEL):
    weight = [1,3,7,9,1,3,7,9,1,3]
    S = 0
    R = 0
    for i in range(0,10):
        S += PESEL[i] * weight[i]
    M = S % 10
    if M == 0:
        R = 0
    else:
        R = 10 - M 
    if PESEL[10] == R:
        return True
    else: 
        return False

def gender(PESEL):
    if PESEL[10] % 2 == 0:
        return "K"
    else:
        return "M"
    
pytanie = input("Wprowadź 11-cyfrową wartość: ")
if len(pytanie) != 11 or not pytanie.isdigit():
    print("Wprowadź poprawną 11-cyfrową wartość!")
else:
    PESEL = [int(number) for number in pytanie]
    print("Lista cyfr:", PESEL)

    if gender(PESEL) == "K":
        print("Kobieta")
    else:
        print("Meżczyzna")

    if check(PESEL):
        print("PESEL poprawny")
    else:
        print("PESEL niepoprawny")