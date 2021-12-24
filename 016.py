def main():
    name=input()
    height=int(input())
    weight=int(input())


    Bmi=float('%.6f'%(weight/(height/100)**2))
    if Bmi>24:
        print('Hi {Name}, Your BMI: {BMI} too HIGH.'.format(Name=name,BMI=Bmi))
    elif Bmi<18.5:
        print('Hi {Name}, Your BMI: {BMI} too LOW.'.format(Name=name,BMI=Bmi))
    else:
        print('Hi {Name}, Your BMI: {BMI}.'.format(Name=name,BMI=Bmi))
main()

