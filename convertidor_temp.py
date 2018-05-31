temperatura=input("transformar de fac o caf:")

if temperatura=="caf":
    grados_c = int(input("grados C:"))
    grados=((grados_c * 9 / 5) + 32)
    print("{} grados F".format(grados))

elif temperatura=="fac":
    grados_f = int(input("grados F:"))
    grados=(grados_f-32)/(9/5)
    print("{} grados C".format(grados))