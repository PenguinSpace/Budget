"""
This program should include a class for a budget account that is able to track the user's personal
information as well as their financial information. Should allow user's to add what they spend and
perform necessary calculations as needed. The user should be able to find out how much they earn
per day, how much they spend per day, and be able to see what they spend the most on.
To Do:
    - can read in csv file or not
    - budget class
    - function to create a budget
    - able to track spending and most spent items
    - have functions to create graphs
    - identify savings goal
    - be able to calculate how allowed spending per day
    - Way to track what you spend on a day to day basis
    - able to read in a csv file

Completed:
    - Budget class
    - functions for adding and removing spending or earnings
    - __name__ == __main__

"""

import pandas as pd
import re


class Budget:

    def __init__(self):
        self.earnings = 0
        self.spending = 0
        self.spending_dict = {}
        self.earnings_dict = {}
        self.current_day = {}
        self.tax = 0.33
        self.create_budget()

    def calculate_total_spending(self):
        """
        calculates all the spending in spending_dict and adds it all up and
        returns the total amount. Checks to see if there is anything in dict
        before calculation
        :return: The total spending
        """
        if len(self.spending_dict) == 0:
            return 0

        else:
            total = 0

            for entry in self.spending_dict:
                total += self.spending_dict[entry]

            return total

    def calculate_earnings(self):
        """
        calculates all the earnings in spending_dict and adds it all up and
        returns the total amount. Checks to see if there is anything in dict
        before calculation
        :return: The total earnings
        """

        if len(self.earnings_dict) == 0:
            return 0

        else:
            total = 0

            for entry in self.earnings_dict:
                total += self.earnings_dict[entry]

            return total

    def add_spending(self, name, amount):
        """
        adds spending to the dictionary checks to see if the item already exists
        makes a new one if it doesn't and adds the amount to it. Also
        recalculates the total spending
        """

        # Works
        if name in self.spending_dict:
            self.spending_dict[name] += amount
            self.current_day[name] += amount

        else:
            self.spending_dict[name] = amount
            self.current_day[name] = amount

        self.spending = self.calculate_total_spending()

    def remove_spending(self, name):
        """
        removes a spending entry if it exists in spending_dict and recalculates
        the total spending.
        :param name: name of the entry
        :return: None
        """
        if name in self.spending_dict:
            del self.spending_dict[name]

        else:
            print("This entry does not exist")

    def add_earnings(self, name, amount):
        """
        adds earnings to the dictionary checks to see if the item already exists
        makes a new one if it doesn't and adds the amount to it
        """

        # Works
        if name in self.earnings_dict:
            self.earnings_dict[name] += amount

        else:
            self.earnings_dict[name] = amount

        self.earnings = self.calculate_earnings()

    def remove_earnings(self, name):
        """
        removes an earnings entry if it exists in spending_dict
        :param name: name of the entry
        :return: None
        """
        if name in self.earnings_dict:
            del self.earnings_dict[name]

        else:
            print("This entry does not exist")

    def create_budget(self):
        """
        Creates a budget using new or existing data. Asks the user
        for various financial data
        :return: a budget object
        """

        # check for CSV file
        ans = input("Do you have a CSV file of your budget?\n")
        if ans[0] == 'y' or ans[0] == 'Y':
            return self

        # have user input financial information
        else:
            # asks user to input their earning information
            print("\nStart by entering all your earnings!")
            ans1 = input("Would you like to add a earning?\n")
            answer = ans1

            while ans1[0] == 'y' or ans1[0] == 'Y':
                name = input("Please enter an earning type: ")
                amount = float(input("Please enter a price for the earning: "))
                self.add_earnings(name, amount)
                ans1 = input("Would you like to add another earning?\n")

            # asks user for their tax information for their earnings
            # if answer[0] == 'y' or answer[0] == 'Y':
            #     self.tax = input("Please enter your earnings' tax rate: ")

            # asks user to input their spending information
            ans2 = input("Would you like to add a spending?\n")

            while ans2[0] == 'y' or ans2[0] == 'Y':
                name = input("Please enter an item name: ")
                amount = float(input("Please enter a price for the spending item: "))
                self.add_spending(name, amount)
                ans2 = input("Would you like to add another spending?\n")

    def print_budget(self):
        """
        This function prints all the total earnings and spendings in the budget.
        It also prints out a summary of everything that was added to earnings_dict
        and spending_dict.
        :return: None
        """
        print("This is your total earnings after tax: {}".format(self.earnings * (1 - self.tax)))
        print("This is your total spending: {}".format(self.spending))
        print("This is your tax rate: {}\n".format(self.tax))

        print("This is a summary of all your earnings:")
        for entry in self.earnings_dict:
            print("{}: {}".format(entry, self.earnings_dict[entry]))

        print("\nThis is a summary of all your spendings:")
        for entry in self.spending_dict:
            print("{}: {}".format(entry, self.spending_dict[entry]))

    def csv_data(self, name):
        csv = pd.read_csv(name)


if __name__ == '__main__':
    my_budget = Budget()
    # my_budget.add_earnings("income", 2000)
    # my_budget.add_spending("coffee", 100)
    # my_budget.create_budget()

    # # making the earnings and spendings dicts into dataframes
    # data = [my_budget.earnings_dict]
    # # print(data)

    # df = pd.DataFrame(data, index=["Earnings"])
    # df = df.transpose()
    # print(df)
    my_budget.print_budget()






