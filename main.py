def deriv():
  #Dont need to add the x in it!
  #Uses power rule 
    coef=eval(input("Enter the coefficient : "))
    ex=eval(input("Enter the exponent of the coefficient: "))
    if coef<0 and ex<0:
        print("The derivative is:", abs(coef*ex),"/(x^", abs((ex-1)),")")
  
    elif ex==1:
        print("The derivative is:",coef)
    elif ex>1:
        print("The derivative is:", coef*ex,"x^", ex-1)
    
    elif coef<0:
        print("The derivative is:", coef*ex,"x^", ex-1)
    elif ex==0:
        print("The derivative is: 0, obv smh")
    
    elif ex<0:
        print("The derivative is:",coef*ex,"/(x^",abs(ex-1),")")
deriv()
#ak is cool cool