def run():
 name=input("What is your name human? ")
 age=input("What is your age?(in years) ")
 height=float(input("How tall are you?( in meters)"))
 weight=float(input("How much do you weight(in kilograms)"))
 bmi=weight/(height/100)**2
 print(name,"you are "+str(age),"and","your BMI is "+str(bmi))

 run()
