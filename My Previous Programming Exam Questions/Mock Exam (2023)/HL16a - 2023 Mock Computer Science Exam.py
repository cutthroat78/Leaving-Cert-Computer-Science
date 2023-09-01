#Question 16(a)
#Write your name here:

wages = int(input("Please enter your annual wages: ")) # Get the user to input their gross wages

cutoff = 36800 # variable "cutoff" has the value of 36800
tax_credits = 1700 # variable "tax_credits" has the value of 1700

def income_tax(wages): # define a function called "income_tax" and give the input as the wages variable
    print("Welcome to my income tax calculator\nNet income = Gross wages - total tax\nTotal tax = (€36800 x 20%) + ((Gross wages - €36800) x 40%) - Tax Credits")
    
    if wages == cutoff or wages > cutoff:
        print("You will have to pay income tax")
        forty_precent = wages - 36800
        
        cutoff_tax = cutoff * 20 / 100
        
        forty_tax = forty_precent * 40 / 100
        
        tax_bill = cutoff_tax + forty_tax - tax_credits
        
        print("Your income tax bill is: €" + str(tax_bill))
        
        tax_percentage = tax_bill / wages * 100
        
        rounded_tax_percentage = round(tax_percentage,2)
        
        print("The percentage you lost to tax was: " + str(rounded_tax_percentage) + "%")
        
    elif wages < cutoff:
        print ("You pay no income tax")
    

income_tax(wages)
