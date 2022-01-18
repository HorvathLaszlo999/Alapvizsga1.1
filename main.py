'''
Nagyobb szám.
A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
--------------
Adj meg egy számot! 1
Adj meg egy másik számot! 17
A nagyobb érték 17
--------------
Adj meg egy számot! 28
Adj meg egy másik számot! -2
A nagyobb érték: 28
---------------
Adj meg egy számot! 999
Adj meg egy másik számot! 999
A két szám egyenlő
------------------
'''


szam1 = int(input("kérek egy számot!"))
szam2 = int (input("Kérek egy másik számot!"))

if szam1 < szam2:
  print(f"A nagyobb érték {szam2}")
elif szam1 > szam2:
  print(f"A nagyobb érték {szam2}")
else:
  print("A két szám egyenlő")