#I pledge my honor that I have abided by the Stevens Honor Code - Tyson Werner

Before = open("/Users/tyson/PycharmProjects/rewritingfiles/Before.txt", "r")
After = open("/Users/tyson/PycharmProjects/rewritingfiles/After.txt", "w")
for i in Before:
    name = i.upper()
    print(name, file=After)
Before.close()
After.close()


