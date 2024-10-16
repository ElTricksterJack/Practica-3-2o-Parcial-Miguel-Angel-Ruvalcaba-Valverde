print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------PUNTO 3---------------")
fruteria = {#hay que haser una diccionaro o matriz como quieran llamarlo
    "manzana":12,
    "uva":140,
    "platano":34.90,
    "piña":70.60,
    "fresa":40,
    "kIwi":92,
    "averrhoa carambola":61.01,
    "papaya":50,
    "aguacate":66.33,
    "chile":99,
    "zarzamora":119,
    "naranja":20,
    "pitahaya":40,
    "mandarina":20,
    "sandia":30,
    "melon":30,
    "granada":16.73,
    "limon":25,
    "lichi":130.49,
    "rambutan":168.86,
}
#capturemos valores.
#en este momento estaba viendo jujutsu kaisen en la parque en la que mekamaru dise sus ultimas palabras a miwa y me rompio el corazon.
fru = input("allade una fruta:").lower()#este truco lo aprnedi en la Practica 2 2o Parcial
kil = float(input("cuantos kilos quieres comprar:"))
if fru in fruteria:#este if te permite ver si el valor caputrado es valido.
    total = fruteria[fru] * kil#aqui se hase una operasion rapida, sacando el presio de la fruta del dicionario
    print("Fruta:",fru)#y aqui se muestran los valores para saber cual es
    print("Presio por kilo:",fruteria[fru])
    print("------------------")
    print("Kilos pedidos:",kil)
    print("Total:",total)
else:#este es el promedio de error
    print("No tenemos esa fruta.")
print("-------------------------------------")
print("Objetivo: Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta, un número de kilos mostrar el precio de ese número de kilos de fruta.")
print("Resultado: todo funsiono tal y como se pide.\n")
