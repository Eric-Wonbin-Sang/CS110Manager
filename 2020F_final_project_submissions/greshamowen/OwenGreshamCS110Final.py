# CS 110 Final Project
# Owen Gresham
# 12-13-2020
# I pledge my honor that I have abided by the Stevens Honor System
# - Owen Gresham
# This program provides methods to be performed on a spreadsheet
# containing the performance of companies that have had an initial
# public offering since 9/15/2020 during their first week of being public
# (only contains companies whose offer amount met or exceeded $100,000,000)


import csv


class Company:
    def __init__(self, name, ticker, date, hq, sector, industry,
                 offer, d1o, d1c, d2c, d6c, chng_d1,
                 chng_d1_after_open, chng_d2, chng_d3, chng_d4, chng_d5, chng_d6,
                 chng_d1o_to_d6c, chng_d1c_to_d6c, chng_d2c_to_d6c):    # 'd' means day, 'c' means close, 'o' means open

        self.name = name
        self.ticker = ticker
        self.date = int(date)
        self.hq = hq
        self.sector = sector
        self.industry = industry
        self.offer = float(offer)
        self.d1o = float(d1o)
        self.d1c = float(d1c)
        self.d2c = float(d2c)
        self.d6c = float(d6c)
        self.chng_d1 = float(chng_d1)
        self.chng_d1_after_open = float(chng_d1_after_open)
        self.chng_d2 = float(chng_d2)
        self.chng_d3 = float(chng_d3)
        self.chng_d4 = float(chng_d4)
        self.chng_d5 = float(chng_d5)
        self.chng_d6 = float(chng_d6)
        self.chng_d1o_to_d6c = float(chng_d1o_to_d6c)
        self.chng_d1c_to_d6c = float(chng_d1c_to_d6c)
        self.chng_d2c_to_d6c = float(chng_d2c_to_d6c)


    def getName(self):
        return self.name


    def getTicker(self):
        return self.ticker


    def getHQ(self):
        return self.hq


    def getDate(self):
        return self.date


    def getSector(self):
        return self.sector


    def getIndustry(self):
        return self.industry


    def getOffer(self):
        return self.offer


    def getD1O(self):
        return self.d1o


    def getD1C(self):
        return self.d1c


    def getD2C(self):
        return self.d2c


    def getD6C(self):
        return self.d6c


    def getChngD1(self):
        return self.chng_d1


    def getChngD1AfterOpen(self):
        return self.chng_d1_after_open


    def getChngD2(self):
        return self.chng_d2


    def getChngD3(self):
        return self.chng_d3


    def getChngD4(self):
        return self.chng_d4


    def getChngD5(self):
        return self.chng_d5


    def getChngD6(self):
        return self.chng_d6


    def getChngD1OToD6C(self):
        return self.chng_d1o_to_d6c


    def getChngD1CToD6C(self):
        return self.chng_d1c_to_d6c


    def getChngD2CToD6C(self):
        return self.chng_d2c_to_d6c


def create_company_list(data):
    r = csv.reader(data)
    companies = []
    for rowindex, row in enumerate(r):
        if rowindex != 0:
            companies.append(Company(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                 row[7], row[8], row[9], row[10], row[11], row[12], row[13],
                                 row[14], row[15], row[16], row[17], row[18], row[19], row[20]))
    return companies


def printCompanyData(co):
    print("{0:35}{1:8}{2:^10}{3:10}{4:25}{5:32}${6:<9.2f}${7:<9.2f}".format(co.getName(), co.getTicker(), co.getDate(),
                                                                             co.getHQ(), co.getSector(), co.getIndustry(), co.getOffer(), co.getD1O()),
        "${0:<9.2f}${1:<9.2f}${2:<7.2f}{3:9.2f}%{4:9.2f}%{5:9.2f}%".format(co.getD1C(), co.getD2C(), co.getD6C(), co.getChngD1() * 100,
                                                                                 co.getChngD1AfterOpen() * 100, co.getChngD2() * 100),
        "{0:8.2f}%{1:9.2f}%{2:9.2f}% {3:9.2f}% {4:10.2f}% {5:12.2f}%{6:13.2f}%".format(co.getChngD3() * 100, co.getChngD4() * 100, co.getChngD5() * 100,
                                                                              co.getChngD6() * 100, co.getChngD1OToD6C() * 100,
                                                                              co.getChngD1CToD6C() * 100, co.getChngD2CToD6C() * 100))


def header():
    print("{0:35}{1:8}{2:10}{3:10}{4:25}{5:32}{6:10}{7:10}".format("Company", "Ticker", "IPO Date", "Country",
                                                                           "Sector", "Industry", "Offer", "Day 1"),
          "{0:10}{1:10}{2:7}{3:>10}{4:>10}{5:>10}".format("Day 1", "Day 2", "Day 6", "% Change", "% Change", "% Change"),
          "{0:>9}{1:>10}{2:>10} {3:>10}   {4:>10}    {5:>10}  {6:>12}".format("% Change", "% Change", "% Change", "% Change", "% Change",
                                                               "% Change", "% Change", "% Change"))
    print(" " * 120 + "Price     Open       Close     Close     Close       Day 1     Day 1     Day 2     Day 3     " +
                      "Day 4     Day 5      Day 6   D1 Open to   D1 Close to   D2 Close to")
    print(" " * 181 + "From Open" + " " * 54 + "D6 Close      D6 Close      D6 Close")
    print("-" * 280)


def performanceBy(list, category, sort, evaluate, startDate, endDate):
    newList = []
    sum = 0
    try:
        if category == "country":
            for i in list:
                if i.getHQ().lower() == sort and i.getDate() >= startDate and i.getDate() <= endDate:
                    newList.append(i)
            for i in newList:
                sum += i.getChngD1OToD6C()
        elif category == "sector":
            for i in list:
                if i.getSector().lower() == sort and i.getDate() >= startDate and i.getDate() <= endDate:
                    newList.append(i)
            for i in newList:
                sum += i.getChngD1OToD6C()
        elif category == "industry":
            for i in list:
                if i.getIndustry().lower() == sort and i.getDate() >= startDate and i.getDate() <= endDate:
                    newList.append(i)
            for i in newList:
                sum += i.getChngD1OToD6C()
        else:
            return "Invalid Input"
        print("Average over first week: {0:6.2f}%".format((sum/len(newList)) * 100))
        print()
        header()
        for i in newList:
            printCompanyData(i)
        return
    except ZeroDivisionError:
        return "No company in that " + category


def firstChoice():
    sort = ""
    category = input("Would you like to sort by country, sector, or industry? ").lower()
    if category == "country":
        sort = input("Choose a country:\n  Australia\n  China\n  Cyprus\n  UAE\n  UK\n  US\n").lower()
    elif category == "sector":
        sort = input("Choose a sector:\n  Basic Materials\n"
                     "  Communication Services\n"
                     "  Consumer Cyclical\n"
                     "  Consumer Defensive\n"
                     "  Financial Services\n"
                     "  Healthcare\n"
                     "  Real Estate\n"
                     "  Technology\n").lower()
    elif category == "industry":
        sort = input("Choose an industry:\n  Asset Management\n"
                     "  Banks-Regional\n"
                     "  Biotech\n"
                     "  Computer Hardware\n"
                     "  Credit Services\n"
                     "  Diagnostics & Research\n"
                     "  Education and Training Services\n"
                     "  Entertainment\n"
                     "  Health Info Services\n"
                     "  Insurance-Property & Casualty\n"
                     "  Internet Content & Info\n"
                     "  Internet Retail\n"
                     "  Medical Care Facilities\n"
                     "  Medical Devices\n"
                     "  Mortgage Finance\n"
                     "  Packaging\n"
                     "  Precious Metal & Mining\n"
                     "  REIT\n"
                     "  Semiconductors\n"
                     "  Software-Application\n"
                     "  Software-Infrastructure\n"
                     "  Solar\n"
                     "  Specialty Retail\n").lower()
    start = input("Enter the start date (YYYYMMDD). If no specific start, enter 0: ")
    end = input("Enter the end date (YYYYMMDD). If no specific end, enter 1: ")
    if end == "1":
        end = 99999999
    return category, sort, start, end


def secondChoice(companies):
    try:
        ticker = input("Enter the ticker of a company that went public from 9/15 to 12/4. "
                       "You can also enter 'all' to see all companies that went public in this time period or a more specific time period\n")
        print()
        if ticker.lower() == "all":
            sum = 0
            counter = 0
            try:
                start = int(input("Enter the start date (YYYYMMDD). If no specific start, enter 0: "))
                end = int(input("Enter the end date (YYYYMMDD). If no specific end, enter 1: "))
            except ValueError:
                print("Invalid Input")
                return
            if end == 1:
                end = 99999999
            header()
            for i in companies:
                if i.getDate() >= start and i.getDate() <= end:
                    sum += i.getChngD1OToD6C()
                    counter += 1
                    printCompanyData(i)
            print("Average over first week: {0:6.2f}%".format((sum/counter) * 100))
        else:
            for i in companies:
                if i.getTicker() == ticker.upper():
                    header()
                    printCompanyData(i)
                    return
            print("No such ticker")
    except ZeroDivisionError:
        print("No companies")
        return


def main():
    data = open("C:/Users/oweng/PycharmProjects/CS110_Final/IPOcsvData.csv")
    companies = create_company_list(data)
    print("This program analyzes companies which have had an initial public offering since 09/15/2020")
    print("and planned to raise at least $100,000,000 in their offering.\n")
    print("Enter 1 for the average change in the stock price for companies of a specific country, sector, "
          "or industry during their first week as a public company")
    print("Enter 2 to get general data for a specific stock, or all stocks that had an IPO in a specific time frame")
    selection = input()
    if selection == "1":
        chosen = firstChoice()
        print("\n", performanceBy(companies, chosen[0], chosen[1], 18, int(chosen[2]), int(chosen[3])))
    elif selection == "2":
        secondChoice(companies)
    else:
        print("Invalid selection")


main()

