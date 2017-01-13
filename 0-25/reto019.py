"""
Created on 29/11/2012

@author: mizzt
"""

from time import time


class ContadorBisiesto:
    def __init__(self, initialValue=1):
        self.i = initialValue

    def inc(self):
        if self.i == 4:
            self.i = 1
        else:
            self.i += 1

    def isBisiesto(self):
        return self.i == 4


def metodo1():
    cont = ContadorBisiesto(1)
    year = 1901  # Year
    month = 1  # Month
    dw = 2  # Day of the week: 1=Monday 7=Sunday
    day = 1  # Day of the month

    sundays = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while year <= 2000:

        # Sunday first of month check
        if dw == 7 and day == 1:
            sundays += 1

        # Days pass by...
        dw += 1
        day += 1

        # Weekday check
        if dw > 7:
            dw = 1

        # New year check
        if day > days[12 - 1] and month == 12:
            day = 1
            month = 1
            year += 1
            cont.inc()

            if cont.isBisiesto():
                if year % 400 == 0:
                    days[2 - 1] = 29
                else:
                    if year % 100 == 0:
                        days[2 - 1] = 28
                    else:
                        days[2 - 1] = 29

            else:
                days[2 - 1] = 28

                # print("Feliz anyo ",year, cont.i)

        # New month check
        if day > days[month - 1]:
            day = 1
            month += 1

    print(sundays)


if __name__ == '__main__':
    ini = time()
    metodo1()
    print("Tiempo: ", time() - ini, "sg")
