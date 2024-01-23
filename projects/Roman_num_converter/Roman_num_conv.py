symbolDict = { 
    1:"I", 
    5:"V", 
    10:"X", 
    50:"L", 
    100:"C", 
    500:"D", 
    1000:"M" }

class convertToRoman:
    """Converts a number from 1 to 9999 into roman numberals
    """
    #Every 5 change symbol
    #every 4 = new symbol - 1
    #function to loop 1 through 10  
    def __init__(self):
        self.num = self
    def numConverstion(num):
        
        tempRN = ""
        while num > 0:
            if num >= 1000:
                tempRN += symbolDict[1000]
                num -= 1000
            elif num >= 900:
                tempRN += symbolDict[100] + symbolDict[1000]
                num -= 900
            elif num >= 500:
                tempRN += symbolDict[500]
                num -= 500
            elif num >= 400: 
                tempRN += symbolDict[100] + symbolDict[500]
                num -= 400
            elif (num >= 100):
                tempRN += symbolDict[100]
                num -= 100
            elif (num >= 90):
                tempRN += symbolDict[10] + symbolDict[100]
                num -= 90
            elif (num >= 50):
                tempRN += symbolDict[50]
                num -= 50
            elif (num >= 40): 
                tempRN += symbolDict[10] + symbolDict[10]
                num -= 40
            elif (num >= 10):
                tempRN += symbolDict[10]
                num -= 10
            elif (num >= 9):
                tempRN += symbolDict[1] + symbolDict[10]
                num -= 9
            elif num >= 5:
                tempRN += symbolDict[5]
                num -= 5
                print(num)
            elif num >= 4:
                tempRN += symbolDict[1] + symbolDict[5]
                num -= 4
            elif (num > 0):
                tempRN += symbolDict[1]
                num -= 1
        return tempRN

numToConvert = input("What number would you like to convert? (1 to 9999) ")
conv = convertToRoman.numConverstion(int(numToConvert))
print(conv)
doAgain = input("Do you want to print another number? y/n ")
while doAgain == "y":
        numToConvert = input("What number would you like to convert? ")
        conv = convertToRoman.numConverstion(int(numToConvert))
        print(conv)
        doAgain = input("Do you want to print another number? y/n ")
print(help(convertToRoman()))  