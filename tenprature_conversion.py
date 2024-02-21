choice=input("what do you want to convert celsius or fahrenheit " )
if (choice=="celsius"):
    value=int(input('enter the celsius value here:'))
    fahr= value*9/5+32
    print(fahr)
elif(choice=="fahrenheit"):
    value=int(input('enter value of farenheit'))
    cel=(value-32)*5/9
    print(cel)
