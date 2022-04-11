# Prompt the customer to enter their name and pounds of food they ate
Customer =  (input("Please enter name:"))
Pounds =  float (input("Please enter the amount of food consumed:"))
Tax_rate = 0.0715


#calculate the total for the amount of food eaten
if Pounds <= 3 :
    Cost = 12.99
    Subtotal = Cost
    Tax = Subtotal * Tax_rate
    Total_due = Subtotal + Tax
    
    print("Customer:", Customer)
    print("Pounds:", Pounds)
    print("Subtotal:", Subtotal)
    print("Tax:","{:.2f}".format( Tax))
    print("Total due:","{:.2f}".format( Total_due))
elif Pounds <= 4.2:
    Cost_2 = 22.99
    Subtotal_2 = Cost_2
    Tax_2 = Subtotal_2 * Tax_rate
    Total_due_2 = Subtotal_2 + Tax_2
    print("Customer:", Customer)
    print("Pounds:", Pounds)
    print("Subtotal:", Subtotal_2)
    print("Tax:", "{:.2f}".format(Tax_2))
    print("Total due:", "{:.2f}".format(Total_due_2))         
elif Pounds <= 6.0:
    Cost_3 = 28.99
    Subtotal_3 = Cost_3
    Tax_3 = Subtotal_3 *Tax_rate
    Total_due_3 = Subtotal_3 + Tax_3
    print("Customer:", Customer)
    print("Pounds:", Pounds)
    print("Subtotal:", Subtotal_3)
    print("Tax:", "{:.2f}".format(Tax_3))
    print("Total due:", "{:.2f}".format(Total_due_3))    

else:
    Pounds > 6.0
    Cost_4 = 34.99
    Subtotal_4 = Cost_4
    Tax_4 = Subtotal_4 *Tax_rate
    Total_due_4 = Subtotal_4 + Tax_4
    print("Customer:", Customer)
    print("Pounds:", Pounds)
    print("Subtotal:", Subtotal_4)
    print("Tax:", "{:.2f}".format(Tax_4))
    print ("Total due:", "{:.2f}".format(Total_due_4))   
    
       
     
    
    
    
    
            

 
            
    
    

    
    


