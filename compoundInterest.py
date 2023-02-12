def calculateCompoundInterest():
    client_one_principal = int(input("Principle (amount): "))
    client_one_time = int(input("Time:               "))
    client_one_rate = float(input("Rate:               "))

    amnt = client_one_principal*(1+client_one_rate/100)**client_one_time
    compoundinterest = amnt - client_one_principal

    print("Compound Interest:",round(compoundinterest,2))
 
#A = P( 1 + R/100)^T
#CI = A - P

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
    calculateCompoundInterest() 
    calculateCompoundInterest()  
