import sys


# Gib alle Zahlen von 1 - 100 aus: Die while-Schleife
def task_1():
    # this would be way easier using "for i in range(1, 101): print(i)" but ok, guess i'll use while
    i = 1
    while i <= 100:
        print(i)
        i += 1


# Ersetze in dieser Schleife alle Zahlen die durch drei teilbar sind durch den String "Digital"
def task_2():
    i = 1
    while i <= 100:
        if i % 3 == 0:
            print("Digital")
        else:
            print(str(i))
        i += 1


# Ersetze in einer Schleife, die Zahlen die durch fünf teilbar sind durch "History"
def task_3():
    for i in range(1, 101):
        if i % 5 == 0:
            print("History")
        else:
            print(str(i))


# Kombiniere die Schritte 2 und 3 mit einem Elif, sodass du nicht doppelt ausgibst
def task_4():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Digital")
        elif i % 5 == 0:
            print("History")
        else:
            print(str(i))


# Ersetze Zahlen die durch 3 Teilbar sind durch den String "Digital", Zahlen die durch 5 teilbar sind durch den String "History" und Zahlen, die durch beides teilbar sind durch den String "Digital History"
def task_5():
    for i in range(1, 101):
        printstring = ""
        if i % 3 == 0:
            printstring += "Digital "
        if i % 5 == 0:
            printstring += "History"
        if printstring == "":
            printstring = str(i)
        print(printstring)


# call task function dependent on user input
def call_task(task):
    match task:
        case 1:
            task_1()
        case 2:
            task_2()
        case 3:
            task_3()
        case 4:
            task_4()
        case 5:
            task_5()
        case _:
            print(
                "Task not available! \n Currently available Tasks are 1, 2, 3, 4, and 5"
            )


# handle user arguments
def main(call_opts):
    argumentlist = call_opts[1:]
    for arg in argumentlist:
        if arg.isnumeric():
            call_task(int(arg))
        else:
            print("please use 'python zusaetzliche-uebungen.py [task_number]'!")


# entrypoint
if __name__ == "__main__":
    main(sys.argv)
