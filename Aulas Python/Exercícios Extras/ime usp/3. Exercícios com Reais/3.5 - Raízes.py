a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
if b*b - 4*a*c == 0:
    x = -b/(2*a)
    print("Possuí raíz %.1f"%(x))
elif b*b - 4*a*c > 0:
    x1 = (-b + (b*b -4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b*b -4*a*c)**(1/2))/(2*a)
    print ("A raíz 1 é %.1f, e a raíz 2, %.1f"%(x1, x2))
else:
    x1_r = -b/(2*a)
    x1_i = ((-(b*b) + 4*a*c)**(1/2))/(2*a)
    x2_i = - ((-(b*b) + 4*a*c)**(1/2))/(2*a)
    print("A parte real é %.1f e a imaginário 1 é %.1f, e 2 é %.1f"%(x1_r, x1_i, x2_i))
    
