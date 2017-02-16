counter = 1

while counter != 0:

    choice1 = int(input("Do you want calculator [1] \nDo you want a Formula Calculator [2]"))

    if choice1 == 1:

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        choice = input("Enter choice(1/2/3/4):")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        if choice == '1':
           print(num1+num2)

        elif choice == '2':
           print(num1-num2)

        elif choice == '3':
           print(num1*num2)

        elif choice == '4':
           print(num1/num2)
           
        else:
           print("Invalid input")


    else:
        print("Select operation.")
        print("1.Pythagorus")
        print("2.Area")
        print("3.Volume")
        print("4.Surface Area")

        choice3 = int(input("Enter choice(1/2/3/4):"))

        if choice3 == 1:
            num3 = int(input("Enter 1st side: "))
            num4 = int(input("Enter 2nd side: "))

            answer = int(num3 * num3 + num4*num4)
            hypo = (answer ** (0.5))
            print(hypo)

        elif choice3 == 2:
            print("Select option.")
            print("1.Square")
            print("2.Triangle")
            print("3.Circle")
            print("4.Trapizium")

            choice4 = int(input("Enter choice(1/2/3/4):"))

            if choice4 == 1:
                num5 = float(input("Enter height: "))
                num6 = float(input("Enter length: "))
                print(num5*num6)

            elif choice4 == 2:
                num7 = float(input("Enter first height: "))
                num8 = float(input("Enter first length: "))
                one = (num7*num8)
                tri = (one/2)

            elif choice4 == 3:
                num9 = float(input("Enter Radius: "))
                a = 3.142*(num9*num9)
                print(a)

            elif choice4 == 4:
                num10 = float(input("Enter Top base: "))
                num11 = float(input("Enter Bottom base: "))
                num12 = float(input("Enter Height: "))
                ab = float(num10+num11)
                ab2 = float(ab/2)
                abh = float(ab2*num12)
                print(abh)

        elif choice3 == 3:
            print("Select option.")
            print("1.Cube")
            print("2.Box")
            print("3.Sphere")
            print("4.Cylinder")

            choice5 = int(input("Enter choice(1/2/3/4):"))

            if choice5 == 1:
                numb1 =float(input("Enter one side"))
                nu1 = float(numb1*numb1*numb1)
                print(nu1)

            elif choice5 == 2:
                numb2 = float(input("Enter 1st Side: "))
                numb3 = float(input("Enter 2nd Side: "))
                numb4 = float(input("Enter 3rd Side: "))
                print(numb2*numb3*numb4)

            elif choice5 == 3:
                numb5 = float(input("Enter Radius: "))
                nu2 = (4/3)*3.142*(numb5*numb5*numb5)
                print(nu2)

            elif choice5 == 4:

                
                numb6 = float(input("Enter Radius: "))
                numb7 = float(input("Enter Height: "))
                nu3 = 3.142*(numb6*numb6)*numb7
                print(nu3)

        elif choice3 == 4:
            print("Select option.")
            print("1.Cube")
            print("2.Rectangular Prism")
            print("3.Sphere")
            print("4.Cylinder")

            choice6 = int(input("Enter choice(1/2/3/4):"))

            if choice6 == 1:
                n1 = float(input("Enter one side: "))
                n2 = n1*n1
                n3 = n2*6
                print(n3)

            elif choice6 == 2:
                n4 = float(input("Enter width: "))
                n5 = float(input("Enter length: "))
                n6 = float(input("Enter height: "))

                q1 = (n4*n6)*2

                q2 = (n6*n5)*2
                q3 = (n4*n5)*2
                q4 = q1+q2+q3
                print(q4)

            elif choice6 == 3:
                n7 = float(input("Enter Radius: "))

                q5 = n7*n7
                q6 = q5*3.142
                q7 = q6*4
                print(q7)

            elif choice6 == 4:
                n8 = float(input("Enter Radius: "))
                n9 = float(input("Enter Height: "))

                q8 = n8*n8
                q9 = q8*3.142
                q10 = q9*2
                w1 = n8*n9
                w2 = w1*3.142
                w3 = w2*2
                w4 = q10+w3
                
                print(w4)

                
                
                
                
            
                
                

            
            

            
                
                


                
            

            
            
                
                
                
                
                
                

                
            
            

        







        
