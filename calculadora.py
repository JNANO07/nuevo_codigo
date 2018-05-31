operacion=input("elige la operacion deseada (multi/divi/suma/resta/poten):")

primer_digito=int(input("escribe el primer digito:"))
segundo_digito=int(input("escribe el segundo digito:"))

if operacion==("multi"):
    print("el resuntado es:{}".format(primer_digito * segundo_digito))

elif operacion==("divi"):
    print("el resuntado es:{}".format(primer_digito / segundo_digito))
elif operacion==("suma"):
    print("el resuntado es:{}".format(primer_digito + segundo_digito))

elif operacion==("resta"):
    print("el resuntado es:{}".format(primer_digito-segundo_digito))

elif operacion==("poten"):
    print("el resuntado es:{}".format(primer_digito**segundo_digito))


