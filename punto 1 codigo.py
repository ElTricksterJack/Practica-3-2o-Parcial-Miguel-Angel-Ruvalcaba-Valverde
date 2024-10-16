print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------PUNTO 1---------------")#Mr.Ink: aqui bamos de nuevo , 13:si quieŕes yo me encaŕgo ,Mr.Ink: si grasias 13 nesito un descanso
M = {#13:pŕimeŕo agamos un diccionaŕio, donde se podŕan los siengientes valoŕes
    'Euro':'€', 
    'Dolar':'$', 
    'Yen':'¥'
}
def error():#13:ahoŕa paŕa el mensaje de eŕŕoŕ hay que haseŕ una funsion que diga el eŕŕoŕ
    print("\n            -X_X-ERROR-X_X-ERROR-X_X-ERROR-X_X-")
    print("ERROR valor no reconosido, porfavor contacatar con el desarollador")
    print("a espera no puedes hasi que aguantate")
    print("             -X_X-ERROR-X_X-ERROR-X_X-ERROR-X_X-")
    exit()

print("1.Euro---2.Dolar---3.Yen")
x = int(input("Porfabr elige uno: "))#13: ahoŕa te daŕemos libeŕtad, o elecion como quieŕas desiŕlo
match x:#con esto puedes elegiŕ una opcion de todas
    case 1:
        print("--€-Euro-€--")#titulo
        d = int(input("Cuantos Euros tienes?: "))#caputrar valor: caturalos a todos, son 150 o mas que ver, po ke mon. pokemon capturalos a todos
        print("Euro: 1 = Peso: 21.46")#se muestra la equibalensa a pesos segun la mmoneda elegida
        print("*-------*")#separador
        e = d*21.46#operacion
        print("Euros propios:",d,M["Euro"])#mostrar la moneda
        print("Equibalensia a pesos:",e,M["Euro"])#mostrar el equibalente a ppesos
#ahora puedes repetir el proseso multiples beses
#13:mmm gŕasias vos que no conosco? peŕo tiene ŕason hasi que no explicaŕe los otŕos 2 es OVIO
    case 2:
        print("--$-Dolar-$--")
        d = int(input("Cuantos Dolares tienes?: "))
        print("Dolar: 1 = Peso: 19.70")
        print("*-------*")
        e = d*19.70
        print("Euros propios:",d,M["Dolar"])
        print("Equibalensia a pesos:",e,M["Dolar"])

    case 3:
        print("--¥-Yen-¥--")
        d = int(input("Cuantos Yenes tienes?: "))
        print("Yen: 1 = Peso: 0.13")
        print("*-------*")
        e = d*0.13
        print("Euros propios:",d,M["Yen"])
        print("Equibalensia a pesos:",e,M["Yen"])
    case _:#13: esta es la opcion de eŕŕoŕ
        error()

print("-------------------------------------")#resultado, balla no los esperaba
print("Objetivo: Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, \nEl usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.")
print("Resultado: Se logro vel el simbolo escojido conectandolo con el dicionario que era el punto prinsipal,\n tambien se bio el mensaje de error pedido y como extra se calculo el equibalente a pesos\n")
