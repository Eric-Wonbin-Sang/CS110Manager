#I pledge on my honor that I have abided by the Stevens Honor System

#I also acknowledge that this program could have been done without oop, however, I wanted to get some practice with it
#Professor Ryan told me that'd be okay

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.lengthMonth = 0
        self.day = day
        self.year = year

        self.validMonth = self.get_validMonth()
        self.validDay = self.get_validDay()
        self.validYear = self.get_validYear()

    def get_lengthMonth(self):
        if ((self.month==4) |
                (self.month==6) |
                 (self.month==9) |
                  (self.month==11)):
            self.length = 30
        elif (self.month==2):
            self.lengthMonth =29
        else:
            self.lengthMonth =31

    def get_validMonth(self):
        if((self.month<1) | (self.month>12)):
            return False
        else:
            return True

    def get_validDay(self):
        self.get_lengthMonth()
        if ((self.day<1) | (self.day > self.lengthMonth)):
            return False
        else:
            return True

    def get_validYear(self):
        if ((self.year<1) | (self.year>9999)):
            return False
        else:
            return True

def main():
    date_user = str(input("Please enter a date in MM/DD/YYYY format"))
    mdy = date_user.split("/")
    for i in range(len(mdy)):
        mdy[i] = float(mdy[i])
    date = Date(mdy[0],mdy[1],mdy[2])
    if (date.validMonth & date.validDay & date.validYear):
        print("This is a valid date.")
    else:
        print("This is not a valid date.")
main()