x = float (input ("Cantidad de dinero:"))
e = (4/100) #(El 4% de intereses a decimales)
p1 = ((x*e)+x) #(cantidad de ahorros primer año)
a = round (p1, 2)
p2 = ((p1*e)+p1) #(cantidad de ahorros segundo año)
b = round (p2, 2)
p3 = ((p2*e)+p2) #(cantidad de ahorros tercer año)
c = round (p3, 2)
print ("primer año:", a
      ,"segundo año:", b
      ,"tercer año:", c )
