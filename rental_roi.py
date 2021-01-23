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
        print('\nTo calculate the return on investment (ROI) for your rental property, let\'s '
            'first look at your sources of income.'
            '\n\nPlease exclude any currency signs, commas, or decimal points in your inputs.')

    def income(self):
        '''Ask for sources of income and calculate total income.'''

        rental = self.__user_prompt("monthly rental", "income")
        other_income = input('\nDo you have any income from laundry, storage, or miscellaneous sources? Type '
            '\'yes\' or \'no\'.\n').lower()
        while other_income not in ['yes','no']:
            other_income = input('\nPlease type "yes" or "no".\n').lower()
        if other_income == 'yes':
            laundry = self.__user_prompt("monthly laundry", "income")
            storage = self.__user_prompt("monthly storage", "income")
            miscellaneous = self.__user_prompt("monthly miscellaneous", "income")
        elif other_income == 'no':
            laundry, storage, miscellaneous = 0, 0, 0
        
        self.monthly_income = sum([rental, laundry, storage, miscellaneous])
        
        print('\n' + '-'*36 + f'\nYour total monthly income is ${self.monthly_income}.\n' + 
            '-'*36)

    def expenses(self):
        '''Ask for expenses and calculate total expenses.'''
        
        print('\nLet\'s look at your expenses.')

        tax = self.__user_prompt('monthly tax', 'expense')
        insurance = self.__user_prompt('monthly insurance', 'expense')
        
        utilities = input('\nDo you have any utility expenses? Type "yes" or "no".\n').lower()
        while utilities not in ['yes','no']:
            utilities = input('\nPlease type "yes" or "no".\n').lower()
        if utilities == 'yes':
            electricity = self.__user_prompt("monthly electricity", "expense")
            water = self.__user_prompt("monthly water", "expense")
            sewer = self.__user_prompt("monthly sewer", "expense")
            garbage = self.__user_prompt("monthly garbage", "expense")
            gas = self.__user_prompt("monthly gas", "expense")
        elif utilities == 'no':
            electricity, water, sewer, garbage, gas = 0, 0, 0, 0, 0
        
        hoa = self.__user_prompt("monthly homeowner's association", "expense")
        
        lawn_snow = input('\nDo you have any lawncare or snow expenses? Type "yes" or ' 
            '"no".\n').lower()
        while lawn_snow not in ['yes','no']:
            lawn_snow = input('\nPlease type "yes" or "no".\n').lower()
        if lawn_snow == 'yes':  
            lawn = self.__user_prompt("monthly lawncare", "expense")
            snow = self.__user_prompt("monthly snow", "expense")
        elif lawn_snow == 'no':
            lawn, snow = 0, 0
        
        vacancy = self.__user_prompt("monthly vacancy", "expense")
        repairs = self.__user_prompt("monthly repairs", "expense")
        capital_exp = self.__user_prompt("monthly capital expenditure", "expense")
        prop_man = self.__user_prompt("monthly property management", "expense")
        mortgage = self.__user_prompt("monthly mortgage", "expense")
        
        self.monthly_expenses = sum([tax, insurance, electricity, water, sewer, garbage, gas, hoa,
            lawn, snow, vacancy, repairs, capital_exp, prop_man, mortgage])
        
        print('\n' + '-'*39 + f'\nYour total monthly expenses are ${self.monthly_expenses}.\n' + 
            '-'*39)
    
    def cash_flow(self):
        '''Calculate total montly cash flow from monthly income and expenses.'''

        self.monthly_cf = self.monthly_income - self.monthly_expenses
        self.annual_cf = self.monthly_cf * 12
        
        print('\n' + '-'*75 + f'\nYour total monthly cash flow is ${self.monthly_cf} and your annual cash flow is '
            f'${self.annual_cf}.' + '\n' + '-'*75)

    def cash_on_cash(self):
        '''Ask for investments, calculate total investments, and calculate cash on cash ROI.'''
        
        print('\nLet\'s look at your investments.')

        down_payment = self.__user_prompt("down", "payment")
        closing_cost = self.__user_prompt("closing", "cost")
        rehab = self.__user_prompt("rehab", "budget")
        misc = self.__user_prompt("total miscellanous", "investment")

        self.investment = sum([down_payment, closing_cost, rehab, misc])
        # calculate cash on cash ROI in percent form (no percent sign) with two decimal places 
        self.coc_roi = '{0:.2f}'.format(self.annual_cf / self.investment * 100)

        print('\n' + '-'*35 + f'\nYour total investments are ${self.investment}.' '\n' + '-'*35)
        print('\n' + '*'*41 + f'\n    Your cash on cash ROI is {self.coc_roi}%.     \n' + '*'*41)

    def view_results(self):
        '''View income, expenses, cash flow, ivestments, and cash on cash ROI.'''

        print('\n' + '-'*41 + f'\n- Your total monthly income is ${self.monthly_income}.')
        print(f'\n- Your total monthly expenses are ${self.monthly_expenses}.')
        print(f'\n- Your total monthly cash flow is ${self.monthly_cf}.')
        print(f'\n- Your annual cash flow is ${self.annual_cf}.')
        print(f'\n- Your total investments are ${self.investment}.' + '\n' + '-'*41)
        print('\n' + '*'*41 + f'\n    Your cash on cash ROI is {self.coc_roi}%.     \n' + '*'*41)
    
    def edit_input(self):
        '''Allow user to change their inputs in income, expenses, investments (in cash on cash).'''

        choice = input('\nWhich category would you like to edit? Type "income", "expenses", or '
            '"investments".\n').lower()
        while choice not in ['income', 'expenses', 'investments']:
            choice = input('\nPlease type "income", "expenses", or "investments".\n')

        if choice == 'income':
            self.income()
            self.__recalculate()
        elif choice == 'expenses':
            self.expenses()
            self.__recalculate()
        elif choice == 'investments':
            self.cash_on_cash()
            self.__recalculate()
    
    def __user_prompt(self, input_name:str, input_type:str) -> int:
        '''
        Insert input_name and input_type into an input question that asks for a number.
        Check that the user inputs digits.
        Output an integer.
        Example input_name: "laundry", "tax", "miscellaneous".
        Example input_type: "income", "expenses", "expense total".
        '''
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
            '\n\t- To edit your inputs, type "edit".'
            '\n\t- To view your recalculated results or to view your results again, type "view".'
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