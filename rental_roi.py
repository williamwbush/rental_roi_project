
class Rental_roi():

    def __init__(self, monthly_income=0, monthly_expenses=0, monthly_cf=0, annual_cf=0, 
                investment=0, coc_roi=0):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.monthly_cf = monthly_cf 
        self.annual_cf = annual_cf
        self.investment = investment
        self.coc_roi = coc_roi

    def income(self):
        print('\nThank you for using this rental ROI calculator.')
        print('\nFirst, let\'s calculate your monthly income.')

        rental_income = int(input('\nWhat is your monthly rental income?\n'))
        laundry = int(input('\nWhat is your laundry income?\n'))
        storage = int(input('\nWhat is your storage income?\n'))
        miscellaneous = int(input('\nWhat is your total miscellaneous income?\n'))
        
        self.monthly_income = sum([rental_income, laundry, storage, miscellaneous])
        
        print(f'\nYour total monthly income is ${self.monthly_income}.\n')

    def expenses(self):
        print('Now, let\'s calculate your monthly expenses.')

        tax = int(input('\nWhat is your monthly tax expense?\n'))
        insurance = int(input('\nWhat is your monthly insurance expense?\n'))
        utilities = input('\nDo you have any utility expenses? Type \'yes\' or \'no\'.\n')
        if utilities.lower() == 'yes':
            electricity = int(input('\nWhat is your monthly electricity expense?\n'))
            water = int(input('\nWhat is your monthly water expense?\n'))
            sewer = int(input('\nWhat is your monthly sewer expense?\n'))
            garbage = int(input('\nWhat is your monthly garbage expense?\n'))
            gas = int(input('\nWhat is your monthly gas expense?\n'))
        else:
            electricity, water, sewer, garbage, gas = 0, 0, 0, 0, 0
        hoa = int(input('\nWhat is your monthly homeowner\'s association expense?\n'))
        lawn = int(input('\nWhat is your monthly lawncare expense?\n'))
        snow = int(input('\nWhat is your monthly snow expense?\n'))
        vacancy = int(input('\nWhat is your monthly vacancy expense?\n'))
        repairs = int(input('\nWhat is your monthly repair expense?\n'))
        capital_exp = int(input('\nWhat is your monthly capital expenditure expense?\n'))
        prop_man = int(input('\nWhat is your monthly property management expense?\n'))
        mortgage = int(input('\nWhat is your monthly mortgage expense?\n'))
        
        self.monthly_expenses = sum([tax, insurance, electricity, water, sewer, garbage, gas, hoa,
            lawn, snow, vacancy, repairs, capital_exp, prop_man, mortgage])
        
        print(f'\nYour total monthly expenses are ${self.monthly_expenses}.\n')
    
    def cash_flow(self):
        self.monthly_cf = self.monthly_income - self.monthly_expenses
        self.annual_cf = self.monthly_cf * 12
        
        print(f'\nYour total monthly cash flow is ${self.monthly_cf} and your yearly cash flow is '
            f'${self.annual_cf}.')

    def cash_on_cash(self):
        print('\nFinally, let\'s calculate your cash on cash return on investment (ROI).')
        print('\nFirst, input your investments.')

        down_payment = int(input('\nWhat is your down payment?\n'))
        closing_costs = int(input('\nWhat are your closing costs?\n'))
        rehab = int(input('\nWhat is your rehab budget?\n'))
        misc = int(input('\nWhat are your miscellaneous expenses?\n'))

        self.investment = sum([down_payment, closing_costs, rehab, misc])
        print(f'\nYour total investments are ${self.investment}.')
        self.coc_roi = self.annual_cf / self.investment * 100 
        print(f'\nYour cash on cash ROI is {int(self.coc_roi) + round(self.coc_roi % 1, 2)}%.\n')

def rental_roi_calc():

    rental_prop = Rental_roi()

    rental_prop.income()
    rental_prop.expenses()
    rental_prop.cash_flow()
    rental_prop.cash_on_cash()

rental_roi_calc()




# Income
    # input
        # rental income
        # laundry
        # storage
        # miscellaneous
    # output
        # total monthly income

# Expenses
    # input
        # tax
        # insurance
        # utilities
            #electricity, water, sewer, garbage, gas
        # HOA (Home Owners' Association)
        # lawn, snow
        # vacancy
        # repairs
        # capital expenses
        # property management
        # mortgage
    # output
        # total monthly expenses

# Cash Flow
    # output
        # total monthly cash flow (income - expenses)
        # total annual cash flow

# Cash on Cash ROI
    # input (investments)
        # down payment
        # closing costs
        # rehab budget
        # miscellaneous other
    # output
        # total investment (sum of investments)
        # cash on cash ROI (annual cash flow/total investment) as %