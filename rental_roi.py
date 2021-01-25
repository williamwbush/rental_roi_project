class Rental_roi():

    def __init__(self, monthly_income=0, monthly_expenses=0, monthly_cf=0, annual_cf=0, 
                investment=0, coc_roi=0):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.monthly_cf = monthly_cf
        self.annual_cf = annual_cf
        self.investment = investment
        self.coc_roi = coc_roi

    def welcome(self):
        '''Welcome message'''

        print('\nWelcome!')
        print('\nTo calculate the cash on cash return on investment (ROI) for your rental property,' 
            ' let\'s first look at your sources of income.'
            '\n\nPlease exclude any currency signs, commas, or decimal points in your inputs.')

    def income(self):
        '''Ask user to input various sources of income. Calculate and print total income.'''

        rental = self.__user_input("monthly rental", "income")
        
        # give user option to input income from laundry, storage, or miscellaneous sources
        other_income = input('\nDo you have any income from laundry, storage, or miscellaneous' 
            'sources? Type \'yes\' or \'no\'.\n').lower()
        while other_income not in ['yes','no']:
            other_income = input('\nPlease type "yes" or "no".\n').lower()
        if other_income == 'yes':
            laundry = self.__user_input("monthly laundry", "income")
            storage = self.__user_input("monthly storage", "income")
            miscellaneous = self.__user_input("monthly miscellaneous", "income")
        elif other_income == 'no':
            laundry, storage, miscellaneous = 0, 0, 0
        
        self.monthly_income = sum([rental, laundry, storage, miscellaneous])
        
        # calculate length of number in string form for formatting purposes
        len_inc = len(str(self.monthly_income))
        # print monthly income with dashes above and below matching statement length
        print('\n' + '-'*(31 + len_inc + (len_inc - 1)//3) + '\nYour total monthly income is $' + 
            format(self.monthly_income, ',') + '.\n' + '-'*(31 + len_inc + (len_inc - 1)//3))

    def expenses(self):
        '''Ask user to input various expenses. Calculate and print total expenses.'''
        
        print('\nLet\'s look at your expenses.')

        tax = self.__user_input('monthly tax', 'expense')
        insurance = self.__user_input('monthly insurance', 'expense')
        
        # give user option to input utility expenses
        utilities = input('\nDo you have any utility expenses? Type "yes" or "no".\n').lower()
        while utilities not in ['yes','no']:
            utilities = input('\nPlease type "yes" or "no".\n').lower()
        if utilities == 'yes':
            electricity = self.__user_input("monthly electricity", "expense")
            water = self.__user_input("monthly water", "expense")
            sewer = self.__user_input("monthly sewer", "expense")
            garbage = self.__user_input("monthly garbage", "expense")
            gas = self.__user_input("monthly gas", "expense")
        elif utilities == 'no':
            electricity, water, sewer, garbage, gas = 0, 0, 0, 0, 0
        
        hoa = self.__user_input("monthly homeowner's association", "expense")
        
        # give user option to input lawn and snow expenses
        lawn_snow = input('\nDo you have any lawncare or snow expenses? Type "yes" or ' 
            '"no".\n').lower()
        while lawn_snow not in ['yes','no']:
            lawn_snow = input('\nPlease type "yes" or "no".\n').lower()
        if lawn_snow == 'yes':  
            lawn = self.__user_input("monthly lawncare", "expense")
            snow = self.__user_input("monthly snow", "expense")
        elif lawn_snow == 'no':
            lawn, snow = 0, 0
        
        vacancy = self.__user_input("monthly vacancy", "expense")
        repairs = self.__user_input("monthly repairs", "expense")
        capital_exp = self.__user_input("monthly capital expenditure", "expense")
        prop_man = self.__user_input("monthly property management", "expense")
        mortgage = self.__user_input("monthly mortgage", "expense")
        
        self.monthly_expenses = sum([tax, insurance, electricity, water, sewer, garbage, gas, hoa,
            lawn, snow, vacancy, repairs, capital_exp, prop_man, mortgage])
        
        # calculate length of number in string form for formatting purposes
        len_e = len(str(self.monthly_expenses))
        # print monthly expenses with dashes above and below matching statement length
        print('\n' + '-'*(34 + len_e + (len_e - 1)//3) + '\nYour total monthly expenses are $' + 
            format(self.monthly_expenses, ',') + '.\n' + '-'*(34 + len_e + (len_e - 1)//3))
    
    def cash_flow(self):
        '''Calculate and print total montly/annual cash flow from income and expenses.'''

        self.monthly_cf = self.monthly_income - self.monthly_expenses
        self.annual_cf = self.monthly_cf * 12

        # calculate length of numbers in string form for formatting purposes
        len_cf = len(str(self.monthly_cf) + str(self.annual_cf))
        # print monthly/annual cash flow with dashes above and below matching statement length
        print('\n' + '-'*(64 + len_cf + (len_cf - 1)//3) + '\nYour total monthly cash flow is $' + 
            format(self.monthly_cf, ',') + ' and your annual cash flow is $' + 
            format(self.annual_cf, ",") + '.\n' + '-'*(64 + len_cf + (len_cf - 1)//3))

    def cash_on_cash(self):
        '''Ask user to input various investments. Calculate and print total investments and 
        a summary of results with cash on cash ROI.'''
        
        print('\nLet\'s look at your investments.')

        down_payment = self.__user_input("down", "payment")
        closing_cost = self.__user_input("closing", "cost")
        rehab = self.__user_input("rehab", "budget")
        misc = self.__user_input("total miscellanous", "investment")

        self.investment = sum([down_payment, closing_cost, rehab, misc])
         # calculate cash on cash ROI in percent form (no percent sign) with two decimal places 
        self.coc_roi = format(self.annual_cf / self.investment * 100, ',.2f')

        # calculate length of number in string form for formatting purposes
        len_i = len(str(self.investment))
        # print investments with dashes/stars above and below matching statement lengths
        print('\n' + '-'*(29 + len_i + (len_i - 1)//3) + '\nYour total investments are $' + 
            format(self.investment, ',') + '.\n' + '-'*(29 + len_i + (len_i - 1)//3))
        
        self.view_results()

    def view_results(self):
        '''Print income, expenses, monthly/annual cash flow, investments, and cash on cash ROI.'''
        
        inc = format(self.monthly_income, ',')
        e = format(self.monthly_expenses, ',')
        mcf = format(self.monthly_cf, ',')
        acf = format(self.annual_cf, ',')
        inv = format(self.investment, ',')

        # put dashes above/below results and right justify dollar amounts with periods before
        print('\n' + '-'*45 + '\nTotal monthly income' + '.'*(24 - len(inc)) + '$' + inc)
        print('\nTotal monthly expenses' + '.'*(22 - len(e)) + '$' + e)
        print('\nTotal monthly cash flow' + '.'*(21 - len(mcf)) + '$' + mcf)
        print('\nTotal annual cash flow' + '.'*(22 - len(acf)) + '$' + acf)
        print('\nTotal investments' + '.'*(27 - len(inv)) + '$' + inv + '\n' + '-'*45)

        # calculate length of number in string form for formatting purposes
        len_roi = len(str(self.coc_roi))
        print('\n' + '*'*(34 + len_roi) + '\n    Your cash on cash ROI is ' + self.coc_roi + 
            '%.    \n' + '*'*(34 + len_roi))
    
    def edit_input(self):
        '''Allow user to change their inputs for income, expenses, or investments and view a
        summary of updated results.'''

        choice = input('\nWhich category would you like to edit? Type "income", "expenses", or '
            '"investments".\n').lower()
        while choice not in ['income', 'expenses', 'investments']:
            choice = input('\nPlease type "income", "expenses", or "investments".\n')

        if choice == 'income':
            self.income()
            self.__recalculate()
            self.view_results()
        elif choice == 'expenses':
            self.expenses()
            self.__recalculate()
            self.view_results()
        elif choice == 'investments':
            self.cash_on_cash() 
            # view_results is in cash_on_cash, no need to recalculate other categories
    
    def __user_input(self, input_name:str, input_type:str) -> int:
        '''Ask user to input a number for input_name input_type (e.g. laundry income).
        Check that the user inputs digits. Return an integer.'''

        user_input = input(f'\nWhat is your {input_name} {input_type}?\n')
        while user_input.isdigit() != True:
            user_input = input('\nPlease enter a number in digit form greater than or equal to '
                'zero. Please exclude any currency signs, commas, or decimal points.\n')
        return int(user_input)

    def __recalculate(self):
        '''Recalculate monthly cash flow, annual cash flow, and cash on cash ROI.'''

        self.monthly_cf = self.monthly_income - self.monthly_expenses
        self.annual_cf = self.monthly_cf * 12
        self.coc_roi = '{0:.2f}'.format(self.annual_cf / self.investment * 100)

def rental_roi_calc():
    '''
    Calculate a rental property's return on investment, and other metrics, based on user inputs of 
    income, expenses, and investments. Also allow user to edit inputs, view results again, or quit.
    '''

    rental = Rental_roi()

    rental.welcome()
    rental.income()
    rental.expenses()
    rental.cash_flow()
    rental.cash_on_cash()

    while True:
        choice = input(
            '\n\t- To edit your inputs and view updated results, type "edit".'
            '\n\t- To view your results again, type "view".'
            '\n\t- To exit this program, type "exit".\n\n').lower()

        while choice not in ['view', 'edit', 'exit']:
            choice = input('\nPlease type "view", "edit", or "exit".\n\n').lower()

        if choice == 'view':
            rental.view_results()    
        
        elif choice == 'edit':
            rental.edit_input()

        elif choice == 'exit':
            break

rental_roi_calc()