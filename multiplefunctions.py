class MultiFunctions:

#print the subfields of AI
    def sub_ai():
        subfields=['Machine Learning','Neural Networks','Vision','Robotics',
                   'Speech Processing','Natural Language Processing']
        print ("Subfields in AI are:")
        for temp in subfields:
            print (temp)

#Check if the given number is Odd or Even
    def OddEven():
        num=int(input("Enter the number"))
        if num%2==0:
            print(num," is an Even number")
        else:
            print(num," is an Odd number")

#Eligibility Check for marriage
    def Elig_Mar():
        age=int(input("Enter your age:"))
        gen=input("Enter your gender(male or female):")

        if age >= 25 and gen=='male':
            print("You are eligible for marriage")
        elif age >=21 and gen=='female':
            print("You are eligible for marriage")
        else:
            print("You are not eligible for marriage")

#Check the percentage of marks 
    def calc_percent():
        Sub1=int(input("Enter the marks for Subject1:"))
        Sub2=int(input("Enter the marks for Subject2:"))
        Sub3=int(input("Enter the marks for Subject3:"))
        Sub4=int(input("Enter the marks for Subject4:"))
        Sub5=int(input("Enter the marks for Subject5:"))

        sum=Sub1+Sub2+Sub3+Sub4+Sub5
        Quo=sum/5
        print("Your percentage is:",Quo)
        return Quo    

#calculate the perimetre of a triangle
    def tri_peri():
        side1=int(input("Enter the value of side1:"))
        side2=int(input("Enter the value of side2:"))
        side3=int(input("Enter the value of side3:"))

        peri=side1+side2+side3
        print("The perimetre of the triangle is:",peri)
        return peri

#calculate the area of a triangle
    def tri_area():
        breadth=int(input("Enter the breadth:"))
        height=int(input("Enter the height:"))

        ar=breadth*height
        area=ar/2
        print("The area of the given triangle is:",area)
        return area