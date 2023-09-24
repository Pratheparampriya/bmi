height=int(input("enter your height in cm"))
weight=int(input("enter your weight"))
height=height/100
bmi=weight/(height*height)
print("your body mass index is",bmi)
if(bmi>0):
    if(bmi<=16):
        print("under weight")
    elif(bmi>25):
        print("obisity")
    elif(bmi<=25):
        print("healty")
    else:
        print("severe over weight")