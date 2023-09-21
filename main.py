import ex1

if __name__ == '__main__':
    proga = -1
    while proga != 0:
        proga = int(input("enter the ex num\n1: ex1\n2: ex2\n0: exit\n"))
        if proga == 1:
            ex1.exs.ex1()
        elif proga == 2:
            ex1.exs.ex2()

