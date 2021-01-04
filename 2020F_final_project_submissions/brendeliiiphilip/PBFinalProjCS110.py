class Data:

   def __init__(self, month, file, wait, dayTime, data, Time, Day, count):
       self.month = month
       self.file = file
       ###file2 = '
       ## This data was sourced from thrill-data.com
       self.wait = wait
       self.dayTime = dayTime
       self.data = data
       self.Time = Time
       self.Day = Day
       self.count = 0
       for i in data:

           filler = i.split(',')
           dayTime.append(filler[1].split())
           # print(dayTime)
           Time.append(dayTime[count][1].split(':'))

           Day.append(dayTime[count][0].split('-'))
           # creates a separate list that holds the day and the time
           wait.append(int(filler[2]))
           count += 1


   def mean(self, lst):
       avg = sum(lst) / len(lst)
       return avg


   def timeConvert(self, time):
       time = str(time).split(':')
       AMPM = ' '
       if int(time[0]) == 24:
           AMPM = 'AM'
           changedtime = str(12) + ':' + time[1] + ' ' + AMPM
       elif int(time[0]) > 12:
           AMPM = 'PM'
           changedtime = str(int(time[0]) - 12) + ':' + time[1] + ' ' + AMPM
       else:
           AMPM = 'AM'
           changedtime = str(int(time[0])) + ':' + time[1] + ' ' + AMPM


       return changedtime


   def findWait(self, waitofday, inp):
       self.waitofday = waitofday
       self.shortesttime = 0
       self.longesttime= 0
       for j in range(len(self.dayTime)):

           if int(inp) == int((self.dayTime[int(j)][0]).split('-')[2]):

               self.waitofday.append(int(self.wait[j]))

               if min(waitofday) == int(self.wait[j]):
                   self.shortesttime = self.dayTime[int(j)][1]

               if max(waitofday) == int(self.wait[j]):
                   self.longesttime = self.dayTime[int(j)][1]

       self.shortest = [min(self.waitofday), self.shortesttime]





def main():
   print("This program will provide you with monthly and daily data for the wait time of the Haunted Mansion attraction in Disney World. (With data sourced from 2019 by Thrill-Data.com")
   month = input("What month would you like to see the data for? (1-12) ")
   file = ['/Users/pjbrendel/Desktop/CS 110/DisneyDataJan.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataFeb.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataMar.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataApr.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataMay.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataJun.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataJul.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataAug.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataSep.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataOct.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataNov.txt','/Users/pjbrendel/Desktop/CS 110/DisneyDataDec.txt']
   file = file[int(month) - 1]
   data = open(file, 'r')
   D = Data(month, file, [], [], data, [], [], 0)
   print("The average wait for this month was:", sum(D.wait) / len(D.wait))
   inp = str(input("Input what day of the month you would like to find wait time data for: "))
   D.findWait([], inp)
   print("The shortest wait time on", (D.month + '/' + inp), "was", D.shortest[0], "minutes long at the time",
         D.timeConvert(D.shortest[1]) + '.', "The average wait time for", (D.month + '/' + inp), "was",
         round(D.mean(D.waitofday)), "minutes", "and the longest wait was", max(D.waitofday), "minutes at",
         D.timeConvert(D.longesttime) + '.', end=' ')

main()
