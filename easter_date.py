# Function for golden number calculation.
def golden_num(year):
    return year%19+1

# Function for epact calculation.
def epacti(year):
    return (11*golden_num(year)-3)%30

# Function for Orthodox Easter date calculation
# Gauss's algorithm.
def orth_easter_date(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 15)%30
    e = (2*b+4*c+6*d+6)%7
    easter = d + e + 4
    month = "April"
    if easter > 30:
        easter -= 30
        month = "May"
    result = str(easter) + " " + month
    return result

# Function for Catholic Easter date calculation
# Gauss's algorithm.
def cath_easter_date(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b+4*c+6*d+5)%7
    if (d+e) <= 9:
        easter = 22 + d + e
        month = "March"
    else:
        easter = d + e - 9
        month = "April"
    result = str(easter) + " " + month
    return result


if __name__ == '__main__':
    # Print Orthodox and Catholic Easter dates for years 2000-2100
    # and highlight with yellow color the years that have same easter date
    # on both calendars, by using colorama library.
    from colorama import Fore, Back, Style
    print("Year \t Orthodox \t Catholic")
    for year in range(2000, 2101):
        blank = ' '
        print(((Back.YELLOW + str(year)) if orth_easter_date(year)==cath_easter_date(year) else year),(Style.RESET_ALL), "\t", orth_easter_date(year),(14 - len(orth_easter_date(year)))*blank, cath_easter_date(year))
