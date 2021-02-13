import re
print("CALCULATOR")
print("type exit to close the caculator")
previous_result=0      #this value is created to store previous equation result
run=True              # this variable is created for calculator exit purpose
def do_sum():
    global run         #here run and previous_result are set to gloal because of variable issues.
    global previous_result
    equation=''   #initially equation remain empty
    if previous_result==0:
        equation = input("Enter the equation:")
    else:
        equation=input(str(previous_result))  #after first execution of equation this will be performed because then previous value will exit.

    if equation=='exit':
        run=False
        print("Good bye, See you again !")
    else:
     equation=re.sub('[a-zA-Z,<>!?$#@^()|}{]','',equation) #using build in function re with in [] elements will be replaced by blank space, so [] exlements will not show to the users
     if previous_result == 0:
        previous_result=eval(equation) #build in fun eval(evaluate) is used for performing math operations.
     else:
        previous_result=eval(str(previous_result)+equation) #previous equation result will be converted to string then new written equation will be added and it will be stored at previous_result variable.
while run:    #initially run is true hence it will execute the functon do_sum():
        do_sum()