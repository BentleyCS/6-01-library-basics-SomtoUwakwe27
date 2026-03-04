#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)
import analytics
import CSP_5_01_Searching
from CSP_5_01_Searching import binarySearch, linearSearch


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    newPrices = []
    for i in range(len(rawPrices)):
        newPrices.append(float(round(analytics.apply_markup(rawPrices[i], .15))))
    return newPrices

# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    average = []
    highest = []
    for i in range(len(n)):
        average.append(analytics.get_average(n))
        highest.append(analytics.get_highest(n))
    aver = average[0]
    high = highest[0]
    return [high, aver]


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(list):
   sanitize = []
   for i in range(len(list)):
       sanitize.append(analytics.clean_text(list[i]))
   return sanitize
# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(list):
    high = []
    for i in range(len(list)):
        high.append(analytics.filter_threshold(list, 100))
        break
    return high

# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(list, target):

    sanit = analytics.clean_text(list)
    order = True
    for i in range(len(sanit)):
        if sanit[i] < sanit[i-1]:
            order = False

    if order == True:
        binary = binarySearch(list,target)
        return binary

    elif order == False:
        for i in range(len(sanit)):
            if sanit[i] == target:
                return i
        return -1