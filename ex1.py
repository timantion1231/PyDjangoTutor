# ex1
class exs:
    @staticmethod
    def ex1():
        a = [65, 54, 85, 58, 5454, 548, 656, 237, 57, 99, 98, 78]
        for i in a:
            if i % 2 == 0:
                print(i)
            elif i == 237:
                break
    @staticmethod
    def ex2():
        num1 = int(input("enter the random number\n"))
        num2 = int(input("enter the limit number\n"))
        if (num1 > num2):
            print("the 1-st number is bigger")
            if (num1 / num2 > 3):
                print("the 1-st number is bigger than 2-nd number more than 3 times")
        elif (num2 > num1):
            print("the 2-nd number is bigger")
