book1=int(input("How many Introduction to Python books are required: "))
book2=int(input("How many  Python Libraries Cookbooks are required: "))
book3=int(input("How many Data Science in Python books are required: "))
bp1=499.00
bp2=855.00
bp3= 645.00
gst=0.12
delivary_charges=250
print("Cost of book1: ",bp1,"Cost of book2: ",bp2,"Cost of book3: ",bp3,sep="\n")
total=book1*bp1+book2*bp2+book3*bp3
tax=total*gst
total_amount=total+tax+delivary_charges
print("The total amount is: ",total_amount)
