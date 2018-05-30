quieres_helado = input("quieres helado? (SI/NO):").upper()
tienes_dinero = input("tienes dinero?(SI/NO):").upper()
papi_te_invita = input("tu papi te invita?(SI/NO)").upper()
if (quieres_helado=="SI") and ((tienes_dinero =="SI") or (papi_te_invita=="SI"))==True:
    cuanto_dinero_tienes = int(input("cuanto dinero tienes?:"))
    print("este es tu cambio ${}".format(cuanto_dinero_tienes - 30))
else:
    print("lo siento no puedes comer helado")
