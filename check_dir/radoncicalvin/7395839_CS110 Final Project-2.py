### Alvin Radoncic CS-110A Final Project
### I, Alvin Radoncic, abide by the Stevens Honor Code

print("This program will display the pandemic peformance of the 10 highest weighted companies in the Technology Select Sector SPDR Fund (XLK).")
print("The purpose of this program is to evaluate how the shares of the select different types of well-regarded tech companies have been impacted by the pandemic economy.")
print("These companies are Apple, Microsoft, Visa, Nvidia, Mastercard, Paypal, Adobe, Intel, Salesforce, and Cisco.")

import yfinance as yf
import pandas

pandas.set_option('display.max_columns', None)

def data_download():
    ticker_list = ["AAPL", "MSFT", "V", "NVDA", "MA", "PYPL", "ADBE", "INTC", "CRM", "CSCO"]
    print("The tickers for each stock are", ticker_list)
    for i in ticker_list:
        data = yf.download(i, start="2020-03-23", end="2020-12-12")
        print("\nHere is the data for", i, " once lockdowns began\n", data.head(1))
        print("\nHere is the current data for", i, "\n", data.tail(1))

    # data = yf.download("AAPL MSFT V NVDA MA PYPL ADBE INTC CRM CSCO", start="2020-03-23", end="2020-12-12")
    # return data



def Apple_Performance():
    Apple = yf.download("AAPL", start="2020-03-23", end="2020-12-12")
    lock = Apple.iloc[0]['Close']
    current = Apple.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Microsoft_Performance():
    Micro = yf.download("MSFT", start="2020-03-23", end="2020-12-12")
    lock = Micro.iloc[0]['Close']
    current = Micro.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Visa_Performance():
    Visa = yf.download("V", start="2020-03-23", end="2020-12-12")
    lock = Visa.iloc[0]['Close']
    current = Visa.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Nvidia_Performance():
    Nvidia = yf.download("NVDA", start="2020-03-23", end="2020-12-12")
    lock = Nvidia.iloc[0]['Close']
    current = Nvidia.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Mastercard_Performance():
    Master = yf.download("MA", start="2020-03-23", end="2020-12-12")
    lock = Master.iloc[0]['Close']
    current = Master.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Paypal_Performance():
    Paypal = yf.download("PYPL", start="2020-03-23", end="2020-12-12")
    lock = Paypal.iloc[0]['Close']
    current = Paypal.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Adobe_Performance():
    Adobe = yf.download("ADBE", start="2020-03-23", end="2020-12-12")
    lock = Adobe.iloc[0]['Close']
    current = Adobe.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Intel_Performance():
    Intel = yf.download("INTC", start="2020-03-23", end="2020-12-12")
    lock = Intel.iloc[0]['Close']
    current = Intel.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Salesforce_Performance():
    Salesforce = yf.download("CRM", start="2020-03-23", end="2020-12-12")
    lock = Salesforce.iloc[0]['Close']
    current = Salesforce.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance

def Cisco_Performance():
    Cisco = yf.download("CSCO", start="2020-03-23", end="2020-12-12")
    lock = Cisco.iloc[0]['Close']
    current = Cisco.iloc[184]['Close']
    performance = (current - lock)/lock * 100
    return performance



def performance_ranking():
    pass

    apple = Apple_Performance()
    micro = Microsoft_Performance()
    visa = Visa_Performance()
    nvidia = Nvidia_Performance()
    mastercard = Mastercard_Performance()
    paypal = Paypal_Performance()
    adobe = Adobe_Performance()
    intel = Intel_Performance()
    salesforce = Salesforce_Performance()
    cisco = Cisco_Performance()

    performance_list = [apple, micro, visa, nvidia, mastercard, paypal, adobe, intel, salesforce, cisco]
    performance_list.sort(reverse=True)

    # for i in range(len(performance_list)):
    #     count = count + 1
    #     for j in ["Paypal", "Nvidia", "Apple", "Mastercard", "Salesforce", "Microsoft", "Adobe", "Visa", "Cisco", "Intel"]:
    #         print(("{0}. {1}".format(count, j)))


    # s = [[COMPANY, percentage], [COMPANY2, percentage]]
    # s.sort(key=lambda x: x[1] reverse=True)  map = {0: 1, 1: 2}  map[0]  map = {"Apple": "APPL"}

    return performance_list



def main():
    Data_Option = input("\nWould you like to see the stock-crash and current statistics of each company (Warning: many outputs)? Please enter 'yes' or 'no' ")
    if Data_Option == "yes":
        data = data_download()
        print(data)
    else:
        pass

    Apple_Option = input("\nWould you like to see Apple's percentage increase? Please enter 'yes' or 'no' ")
    if Apple_Option == "yes":
        apple = Apple_Performance()
        print("Apple is up {0:0.2f}%".format(apple))
    else:
        pass

    Micro_Option = input("\nWould you like to see Microsoft's percentage increase? Please enter 'yes' or 'no' ")
    if Micro_Option == "yes":
        micro = Microsoft_Performance()
        print("Microsoft is up {0:0.2f}%".format(micro))
    else:
        pass

    Visa_Option = input("\nWould you like to see Visa's percentage increase? Please enter 'yes' or 'no' ")
    if Visa_Option == "yes":
        visa = Visa_Performance()
        print("Visa is up {0:0.2f}%".format(visa))
    else:
        pass

    Nvidia_Option = input("\nWould you like to see Nvidia's percentage increase? Please enter 'yes' or 'no' ")
    if Nvidia_Option == "yes":
        nvidia = Nvidia_Performance()
        print("Nvidia is up {0:0.2f}%".format(nvidia))
    else:
        pass

    Master_Option = input("\nWould you like to see Mastercard's percentage increase? Please enter 'yes' or 'no' ")
    if Master_Option == "yes":
        master = Mastercard_Performance()
        print("Mastercard is up {0:0.2f}%".format(master))
    else:
        pass

    Paypal_Option = input("\nWould you like to see Paypal's percentage increase? Please enter 'yes' or 'no' ")
    if Paypal_Option == "yes":
        paypal = Paypal_Performance()
        print("Paypal is up {0:0.2f}%".format(paypal))
    else:
        pass

    Adobe_Option = input("\nWould you like to see Adobe's percentage increase? Please enter 'yes' or 'no' ")
    if Adobe_Option == "yes":
        adobe = Adobe_Performance()
        print("Adobe is up {0:0.2f}%".format(adobe))
    else:
        pass

    Intel_Option = input("\nWould you like to see Intel's percentage increase? Please enter 'yes' or 'no' ")
    if Intel_Option == "yes":
        intel = Intel_Performance()
        print("Intel is up {0:0.2f}%".format(intel))
    else:
        pass

    SF_Option = input("\nWould you like to see Salesforce's percentage increase? Please enter 'yes' or 'no' ")
    if SF_Option == "yes":
        sf = Salesforce_Performance()
        print("Salesforce is up {0:0.2f}%".format(sf))
    else:
        pass

    Cisco_Option = input("\nWould you like to see Cisco's percentage increase? Please enter 'yes' or 'no' ")
    if Cisco_Option == "yes":
        cisco = Cisco_Performance()
        print("Cisco is up {0:0.2f}%".format(cisco))
    else:
        pass


    Rankings_Option = input("\nWould you like for these stocks to be ranked on their pandemic performances (starting from 3/23/2020)?\nPlease enter 'yes' or 'no' ")
    if Rankings_Option == "yes":
        print("1. Paypal", "\n2. Nvidia", "\n3. Apple", "\n4. Mastercard", "\n5. Salesforce", "\n6. Microsoft", "\n7. Adobe", "\n8. Visa", "\n9. Cisco", "\n10. Intel")
    else:
        pass
    # rankings = performance_ranking()
    # print(rankings) This is my failed attempt of using a double for loop, sorted list, and .format function to passively rank these stocks. This is a dire revision I need to resolve.



main()





