__author__ = '80726'

#Analiza palabra impar y terminda en "s"
def imp_y_S(pal):
    var = False
    le = len(pal)-1
    imp = len(pal) % 2
    if (pal[le]=="s")& imp == 1:
        var = True
    else:
        var = False
    return var

#verifico la oracion
def oracion_imp(ora):
    cont = 0
    palabra = ""
    for i in (ora):
        if ( i != " ")& (i != "."):
            palabra += i
        else:
            if imp_y_S(palabra):
                print (palabra, " ")
                cont += 1
                palabra = ""
            else:
                palabra = ""
    print ("La palabras impares y terminadas con letra s, mostrada/s arriba son: ",cont)

def con_NyE(pla):
    var = False
    largo = len(pla)
    if largo >= 3:
        if (pla[2]=="n"):
            for i in (pla):
                if i == "e":
                    var = True
        else:
            var = False
    return var

def prom_n_e(ora):
    prom = 0
    cant = 0
    palabra = ""
    for i in (ora):
        if ( i != " ")& (i != "."):
            palabra += i
        else:
            if con_NyE(palabra):
                cant += len(palabra)
                palabra = ""
            else:
                palabra = ""
    print ("Promedio de letras por palabra con N en 3 y E: ",cant/2)

def cant_vi(pal):
    var = False
    largo = len(pla)
    if largo >= 4:
        for i in (largo):
            if pal[0,1]=="vi":
                var = True
            else:
                var = False
    return var

def cant_vi(ora):
    cant = 0
    palabra = ""
    for i in (ora):
        if ( i != " ")& (i != "."):
            palabra += i
        else:
            if cant_vi(palabra):
                cant += 1
                palabra = ""
            else:
                palabra = ""
   # print ("Cantidad de palabras con vi: ",cant)

print ("La oracion termina con . ")
a = input("Ingrese una oracion: ")

oracion_imp(a)
prom_n_e(a)
cant_vi(a)

