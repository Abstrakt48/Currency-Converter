import sys


def code():
    typeOfMoney = int(
        input(
            "\nWhat type of money?\n1.Pounds \n2.Dollars \n3.Euros \n4.Japanese Yen\n"
        ))

    #pounds

    if typeOfMoney == 1:

        Money = float(input("How much money do you want to convert?\n"))
        dollar = "{:.2f}".format(Money * 1.37)
        euro = "{:.2f}".format(Money * 1.14)
        yen = "{:.2f}".format(Money * 146.53)
        print(f"£{Money} is ${dollar}, €{euro} and ¥{yen}")

        restart = input("\nDo you want to restart this program? [y/n]\n")

        if restart == "y":
            code()
            set.clear()
        else:
            sys.exit()

    #dollars

    if typeOfMoney == 2:

        Money = float(input("How much money do you want to convert?\n"))
        pounds = "{:.2f}".format(Money * 0.73)
        euro = "{:.2f}".format(Money * 0.83)
        yen = "{:.2f}".format(Money * 105.38)
        print(f"${Money} is £{pounds}, €{euro} and ¥{yen}")

        restart = input("\nDo you want to restart this program? [y/n]\n")

        if restart == "y":
            code()
            set.clear()
        else:
            sys.exit()

    #euros

    if typeOfMoney == 3:

        Money = float(input("How much money do you want to convert?\n"))
        dollars = "{:.2f}".format(Money * 1.21)
        pound = "{:.2f}".format(Money * 0.88)
        yen = "{:.2f}".format(Money * 127.76)
        print(f"€{Money} is ${dollars}, £{pound} and ¥{yen}")

        restart = input("\nDo you want to restart this program? [y/n]\n")

        if restart == "y":
            code()
            set.clear()
        else:
            sys.exit()

    #yen

    if typeOfMoney == 4:

        Money = float(input("How much money do you want to convert?\n"))
        dollars = "{:.2f}".format(Money * 0.0095)
        pound = "{:.2f}".format(Money * 0.0068)
        euro = "{:.2f}".format(Money * 0.0078)
        print(f"¥{Money} is ${dollars}, £{pound} and €{euro}")

        restart = input("\nDo you want to restart this program? [y/n]\n")

        if restart == "y":
            code()
            set.clear()


code()
