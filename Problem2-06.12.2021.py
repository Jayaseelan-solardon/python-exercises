
COUNTRYNAME=str(input("Enter your Country Name: "))
AGE=int(input("Enter your Age: "))
AMOUNT=40
FREDERICKAMOUNT=35
Countryname="Frederick"
if AGE >0 and AGE<110 and AGE>=65 and COUNTRYNAME.lower()==Countryname.lower():
       CURRENCY=FREDERICKAMOUNT/2
       TicketPriceforSeniorCitizen="${:,.2F}".format(CURRENCY)
       print("Ticket Prize: {}".format(TicketPriceforSeniorCitizen))
elif(AGE >0 and AGE<110 and AGE>=65):
       CURRENCY=AMOUNT/2
       TicketPriceforSeniorCitizen="${:,.2F}".format(CURRENCY)
       print("Ticket Prize: {}".format(TicketPriceforSeniorCitizen))  
elif(AGE >0 and AGE<110 and AGE>5 and AGE<65 and COUNTRYNAME.lower()==Countryname.lower()):
        TicketPrice="${:,.2F}".format(FREDERICKAMOUNT)
        print("Ticket Prize: {}".format(TicketPrice))            
elif(AGE >0 and AGE<110 and AGE>5 and AGE<65):
        TicketPrice="${:,.2F}".format(AMOUNT)
        print("Ticket Prize: {}".format(TicketPrice))  
elif(AGE >0 and AGE<110 and AGE<6):
        Currency1=0
        TicketPriceforchildren="${:,.2F}".format(Currency1)
        print("Ticket Prize: {}".format(TicketPriceforchildren))  
else:
    print("Enter valid information")  
