class employee:
    def __init__(self,employee_name,employee_id,contact): #using constructor to initialize some attributes for class employee
         self.employee_name=employee_name
         self.employee_id=employee_id
         self.contact=contact  
    
    def get_employeedetail(self):
     
        print("\nEmployee full name:",self.employee_name)
        print("Emploee ID:",self.employee_id)
        print("Contact info:",self.contact)
      


class customer:
    def __init__(self,customer_name,customer_contact,customer_address): #same as line 2
        self.customer_name=customer_name
        self.customer_contact=customer_contact
        self.customer_address=customer_address

    def get_customerdetails(self):
        print("\nCustomer full name:",self.customer_name)
        print("Customer contact info:",self.customer_contact)
        print("Customer address:",self.customer_address)
       
    def get_customername(self):
        return self.customer_name

    
    def __repr__(self): #this is used here because I couldnt print the class objects. This allowed be to represent the class objects as a string.
        return self.customer_name  

  


class property:
   def __init__(self,property_type,property_address): #same as line 37
     self.property_type=property_type
     self.property_address=property_address
    
   def get_propertydetails(self):
       print("\nProperty type:",self.property_type)
       print("\nProperty address:",self.property_address)
        
   def get_propertyaddress(self):
       return self.property_address
   
   def __repr__(self):
       return self.property_address

#Below a function to ask the user for input to supply into the attributes of the classes.
#
#to add new employees   
def set_employee():
    employee_name=input("Enter the full name of the employee:") 
    employee_id=int(input("Enter the ID of the employee:"))
    contact=int(input("Enter the employee's phone number:"))
    employees=employee(employee_name,employee_id,contact)
    return employees

#to add new customers
def set_customer():
    customer_name=input("Enter the full name of the customer:")
    customer_name.lower() #I have converted the input to lower cases because later in the program, uppercase case wont be recognised in the list. It didn't seem to work
    customer_contact=int(input("Enter the phone number of the customer:"))
    customer_address=input("Enter customer's address:")
    customers=customer(customer_name,customer_contact,customer_address)
    return customers 

#to add new property
def set_property():
    property_type=input("What type of property is it? (Apartment,House,Unit and so on):")
    property_address=input("Enter the address for the property:").lower()  #same reason as 53
    properties=property(property_type,property_address)
    return properties

#creating a list for each of the employee, customer and property class. here we can add object for each classes with thier initialized attributes using a constructor
list_properties=[]
list_employees=[]
list_customers=[]



    

class inspection_booking: #here we haven't initialized attributes for the class as it was not necessary
   customer_bookings=[]
   property_bookings=[]
   list_datetime=[]
   def add_booking(self):
       num_booking=int(input("How many bookings do you want to add?:"))
#initially I have checked if the booking has been already done.
       for i in (0,num_booking):  #I do not know why it is looping twice even though i gave "1" as input for num_booking 
             print("\nBooking",i+1) 
             name_check=input("Enter the name of the customer you want to add to this booking:") #we ask who the user wants to assign the booking to
             property_check=input("Enter the address of the property:")
             date_time=input("Please enter date and time for the booking in this format (YYYY-MM-DD, HH:MM):")
             if (name_check in self.customer_bookings) and (property_check in self.property_bookings):
                 
                 if (x.date_time==date_time for x in self.list_datetime):
                     print("This booking has already been created")
#this will check if two customers are trying to book inspection of same property and the same time   
             elif (property_check in self.property_bookings) and (x.date_time==date_time for x in self.list_datetime)  :
                 print("Booking time not available")
             
             
#it is important to write the date and time exactly as mentioned in the output. It may lead to various errors but thats all i could manage.
#For example: 2021-02-05, 21:44 will be recognised as "already booked" by the program if you try to add a new booking with same customer name and property addresss with the same date and time of2021-02-05, 21:44.             
             elif any(x.customer_name==name_check for x in list_customers): 
                 #here I have used any(), which is a built in function.
                 #I found about it in the internet and it really is useful in this scenario.
                 #any() will return a TRUE if it finds any element we are looking for in the list of objects.
                 if any(x.property_address for x in list_properties):
                     
                     self.customer_bookings.append(name_check)
                     self.property_bookings.append(property_check)
                     date_time=input("Please enter date and time for the booking in this format (YYYY-MM-DD, HH:MM):")
                     self.list_datetime.append(date_time)
                 else: 
                     print("Property with the given address couldn't be found")
             else:
                 print("Customer name not found in the database")
#in the above elif statement, I have checked if the name of the customer and address of the property is in the database.
#If not found in the database, relevent output will be displayed.           
                         
             
             
      
   
   def get_booking_details(self): #this fucntion will print the bookings list
           
           print("BOOKING LIST IS EMPTY")
           print("%-30s %-30s %s"%("\nCustomer info","Property Address","Date and Time"))
           print("%-30s %-30s %s"%("_____________","________________","______________"))
           for a,b,c in zip(self.customer_bookings,self.property_bookings,self.list_datetime): #here I have made a zipping list to print outputs of two in two columns
               print("%-30s %-30s %s"%(a,b,c))
#in this for loop I have zipped the three lists to make each appear on a column.
#%-30s means a gap equal to the length of 30 strings will be achieved.

#MAIN FUNCTION
bookings=inspection_booking() #I have created an object named bookings for the class inspection_booking
while True:  #while loop to create a menu for the users.
       
    print("\nEnter 1 to add employees\t Enter 2 to display the list of employees \nEnter 3 to add customers\t Enter 4 to display the list of customers \nEnter 5 to add property\t     Enter 6 to display the list of properties\nEnter 7 to add bookings\t     Enter 8 to display the list of inspection bboking\nEnter 9 to end the program")
    print("Note: Please enter all data in lowercases. Thanks") 
    what=int(input("Your choice?:"))
    if what==1:
            n=int(input("How many employees would you like to add?:"))
            for i in range(0,n):
                print("\nEmployee",i+1)
                list_employees.append(set_employee()) #this will extract values from the set_employees function and add it to the list
            ask_employee=input("Do you want to print the list of employees?(y/n)):" )
            if ask_employee=='y':
                for employeee in list_employees:
                    employeee.get_employeedetail()
    elif what==2:
        if len(list_employees)==0:
            print("Employees list is empty")
        else:
            for employeee in list_employees:
                    employeee.get_employeedetail()  #calling function from classemployee
                    
    elif what==3:    
            n=int(input("How many customers would you like to add?:"))
            for i in range(0,n):
                print("\nCustomer",i+1)
                list_customers.append(set_customer()) #similar reason as of 149
            ask_customer=input("Do you want to print the list of customers?(y/n)):" )
            if ask_customer=='y':    
                for customerr in list_customers:
                    customerr.get_customerdetails()
    elif what==4:
        if len(list_customers)==0:
            print("Customer list is empty")
        else:    
            for customerr in list_customers:
                    customerr.get_customerdetails()
    
    elif what==5:
                n=int(input("How many properties would you like to add:"))
                for i in range(0,n):
                    print("\nProperty",i+1)
                    list_properties.append(set_property())
                ask_property=input("Do you want to print the list of properties? (y/n):")
                if ask_property=='y':
                    for propertyy in list_properties:
                        propertyy.get_propertydetails()
    elif what==6:
        if len(list_properties)==0: #checking if the list is empty
            print("Property list is empty")
        else:
            for propertyy in list_properties:
                propertyy.get_propertydetails()
        
    elif what==7:
            
            bookings.add_booking()
            ask_booking=input("Do you want to display a list of inspection bookings?(y/n):")
            if ask_booking=='y':
                bookings.get_booking_details()
    elif what==8:
            bookings.get_booking_details()
        
    elif what==9:
            print("THANK YOU FOR USING BUILD BOLD SYSTEM")
            print("\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.")
            print("The system is exiting......Done.")
            
            break` #to break the while loop.








