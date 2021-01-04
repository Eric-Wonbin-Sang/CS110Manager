#I pledge my honor that I have abided by the Stevens Honor System

import os
print(os.getcwd())
hw = open("Before.txt", "r")
hw_list = hw.readlines()
print(hw_list)
hw.close()
after = open("After.txt", "w")
for x in range(10):
    hw_list[x] = hw_list[x].title()
    after.write(hw_list[x])
print(hw_list)
