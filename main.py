# a love code
# by yara elsakka
# 12.12.21
from string import *
from random import *

gameOptions = ["abdul", "hessa", "maya", "yazan"]
playerAnswer = input("guess my favorite friend!!!!!!!!\n")
print(playerAnswer)
if playerAnswer != "abdul" and playerAnswer != "hessa" and playerAnswer != "maya" and playerAnswer != "yazan":
    print(f"sorry,{playerAnswer} is not my favorite friend !! Please Try again :) ")
if playerAnswer == "abdul" or playerAnswer == "hessa" or playerAnswer == "maya" or playerAnswer == "yazan":
    print(f"correct!!!! {playerAnswer} is my favorite friend;)")


# end of code

