# Grade Calculator

print("Welcome to Grade Calculator!")

lst = []

def final_grade(grade_number):
    total_percent = 0
    Final_Grade = 0
    
    while total_percent < 100:
        Grade = input("Place Grade 1 % Here: ")
        Worth = input("Place Worth of Grade 1 Here: ")   
        total_percent += float(Worth)
        Final_Grade += float(Grade) * float(Worth)/100
         
    lst.append(Final_Grade) 
    print("Your Final Grade for " + str(grade_number) + "is " + str(Final_Grade))

stop = False

while stop == False:
    final_grade("Final_Grade1")
    another = input("Type 'yes' to calculate another class or 'no' to stop calculating: ")
    
    if another == "yes":   
        print("Thank you for continuing...")
    else:
        stop = True
          
print("Very Well have a great day. Here are you're grades:")   
print(lst)
