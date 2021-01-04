import csv
import matplotlib.pyplot as plt

label_list = ['AMGN', 'ALLK']
csv_path_list = [
   '/Users/eshitajain/Downloads/AMGN.csv',
   '/Users/eshitajain/Downloads/ALLK.csv'
]
count = 0
for csv_path in csv_path_list:
   date_list = []
   price_list = []
   with open(csv_path) as csv_file:
       for row in list(csv.reader(csv_file))[1:]:
           date_list.append(row[0])
           price_list.append(float(row[4]))
   plt.plot(date_list, price_list, label=label_list[count])
   count += 1
plt.xlabel('Date')
plt.xticks(rotation=70)
plt.ylabel('Closing Price')
plt.title('Weekly Difference Between Amgen and Allakos stocks from Dec.2019 to Dec.2020')
plt.legend()
plt.grid()


def main():
    try:
        n = input("\nAre you aware of Nasdaq's recent Diversity Requirements?"
                   "\nEnter \'Yes\' or \'No\': ")
        if n == 'No':
            print('As of December, Nasdaq will require companies that wish to stay listed to have a diverse board of directors. This can be done by having at least two women, POCs, LGBTQ+, or a combination of the three.'
                  '\nAmgen and Allakos are two biotechnology companies listed on the Nasdaq.'
                  '\nCurrently, Amgen has a diverse board of directors, meaning it already meets the new Nasdaq requirements and will remain on the index.'
                  '\nAllakos, however, has an all-male board of directors. Let us take a look at the difference in their stock prices.'
                  '\nWe will see whether or not having a diverse board of directors is beneficial for companies.')
            plt.show()
        elif n == 'Yes':
            m = input('Have you heard of the two biotechnology companies Amgen and Allakos?'
                      '\nEnter \'Yes\' or \'No\': ')
            if m == 'Yes':
                a = input("Which company do you think currently meets Nasdaq's New Diversity Requirements?"
                          "\nEnter \'Amgen\' or \'Allakos\': ")
                if a == 'Amgen':
                    print('Correct! Let us take a look at the difference in their stock prices.'
                        '\nWe will see whether or not having a diverse board is beneficial for companies.')
                    plt.show()
                elif a == 'Allakos':
                    print('Sorry, that is incorrect. Allakos has an all-male board of directors. Let us take a look at the difference in their stock prices.'
                          '\nWe will see whether or not having a diverse board of directors is beneficial for companies.')
                    plt.show()
                else:
                    print("\nError: User has entered an invalid entry.")
                    main()
            elif m == 'No':
                print('Amgen and Allakos are two biotechnology companies listed in the Nasdaq. While Amgen has a diverse board of directors and already meets the new Nasdaq requirements,'
                      '\nAllakos has an all male board of directors. Let us take a look at the difference in their stock prices.'
                      '\nWe will see whether or not having a diverse board of directors is beneficial for companies.')
                plt.show()
            else:
                print("\nError: User has entered an invalid entry.")
                main()
        else:
            print("\nError: User has entered an invalid entry.")
            main()
    except ValueError:
        print("\nError: User has entered an invalid entry.")
        main()
main()

