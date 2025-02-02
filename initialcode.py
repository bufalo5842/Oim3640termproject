Investments = {
    "VOO": 10,
    "QQQ": 13,
    "VTI": 9.79,
    "SPY": 10
    }

def compound_int(P, r, n, t):
    """
    Function that calculates compound interest.
    """
    value = P * (pow((1 + (r/n)), n * t))
    interest = value - P
    print("Compounded interest is", interest)
    print("Initial investment was", P)
    print("Final value will be", value)

def compound_int_prompts():
    
    try:
        principle = int(input('Enter how much you would like to invest: '))
        #rate = (float(input("Enter expected interest rate (%) ")))/100
        # What if the input chose the name of the stock one wants to invest in and based on the choice, the rate for that stick is used when
        # the code runs
        r_input = (input('From the following options, enter which stock you would like to invest in: VOO, QQQ, VTI,or SPY: ')) 
        if r_input == 'VOO' or 'voo':
            rate = 10/100
        elif r_input == 'QQQ' or 'qqq':
            rate = 13/100
        elif r_input == 'VTI' or 'vti':
            rate = 9.79/100
        elif r_input == 'SPY' or 'spy':
            rate = 10/100
        n_input = (input('Enter your desired compounding period: Daily, monthly, or annually: '))
        if n_input == 'annually' or 'Annually' or 'ANNUALLY':
            frequency = 1 
        elif n_input == 'monthly' or 'Monthly' or 'MONTHLY':
            frequency = 12
        elif n_input == 'daily' or 'Daily' or 'MONTHLY':
            frequency = 365
        time = float(input('Enter years of investment: '))

    except ValueError:
        print("Please follow the instructions and enter the correct value.")

    return(principle, rate, frequency, time)

def main():
    compound_int_prompts()

if __name__ == '__main__':
    main()










