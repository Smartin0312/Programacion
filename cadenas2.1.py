

# #ejercicio1
# def hacer_acronimo(palabra):
#     acronimo=""
#     for i in palabra:
#         if i == i.upper()  and not i==" ":
#             acronimo= acronimo+i
#     return acronimo
# print(hacer_acronimo("Hola Mundo"))
#assert(hacer_acronimo("HolaMundoMAC")=="HMMAC")
#assert(hacer_acronimo("Hola       Mundo   M A C")=="HMMAC")
#assert(hacer_acronimo("HolaMundoM A C")=="HMMAC")


#ejercicio2
# def quitarespacios(cadena):
#     cadenatotal=""
#     mayuscyulas=False
#     for i in cadena:
#         if i==" " :
#             cadenatotal=cadenatotal
#             mayuscyulas=True
#         elif mayuscyulas==True:
#             cadenatotal+=i.upper()
#             mayuscyulas=False
#         else:
#             cadenatotal+=i
#     return cadenatotal
# assert(quitarespacios("holaa               s")=="holaas")
# assert(quitarespacios("holaas")=="holaas")
# assert(quitarespacios("ho    laa               s")=="holaas")


#ejercicio3


# def calcular_numeros(cadena):
#     suma=0
#     guardar=""
#     for i in cadena:
#         if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"  :
#             guardar+=i
#          else:
#             suma+=int(guardar)
#     return suma
# print(calcular_numeros("hola34gg2"))
# assert(calcular_numeros("hola34gg2")==9)
# assert(calcular_numeros("1hola34gg2")==10)
# assert(calcular_numeros("hola34gg-2")==9)




#ejercicio4
# def rotar(numero_veces,cadena):
#     cadenaguardada=""
#     cadenaguardada+=(cadena[-numero_veces:]+(cadena[:-numero_veces]))
#     return cadenaguardada


# print(rotar(4 ,"holamuybuenas"))
#assert(rotar(6,"que tal buenas")=="buenasque tal ")
#assert(rotar(1,"que tal buenas")=="sque tal buena")


#ejercicio5
# def contar_caracteres(caracter.upper(),cadena.upper()):
#     contador=0
#     for i in cadena:
#         if i == caracter:
#             contador+=1
#     return contador
# print(contar_caracteres("a","holaa"))
# #ejercicio6
# def lowCaseInString(caracter,cadena):
#     for i in cadena:
#         if i == caracter.lower():
#              contador+=1
#     return contador
# # print(contar_caracteres("a","holaA"))
#ejerccio7
# def numberOfCharacter(cadena):
#     numeros=0
#     for i in cadena:
#         if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"  :
#             numeros+=1
#     return numeros
#
# # ejercicio8
# def palindromo(cadena):
#     cadenatotal=""
#     for i in cadena:
#         if i==" " :
#             cadenatotal=cadenatotal
#         else:
#             cadenatotal+=i


#     cadenaalreves=cadenatotal[::-1]
 
#     return cadenaalreves==cadenatotal




# print(palindromo("hola mundo "))
# assert(palindromo("reconocer"))
# assert(palindromo("hola mundo"))




#ejercicio9
# def buscarPalabra(busqueda,cadena):
#     verdadero=False
#     numeroverdaderos=0
#     encontrada=False
#     for i in  busqueda:
#         for a in cadena:
#             if i ==a:
#                 verdadero=True
#         if  verdadero==True:
#             numeroverdaderos+=1
#             verdadero=False
#     if numeroverdaderos==len(busqueda):
#         encontrada=True
#     return encontrada


# assert(buscarPalabra("hola", "hppppppopppppplpppppa")== True)
# assert(buscarPalabra("hola", "hppppppopppppplppppp")== False)
# assert(buscarPalabra("holaa", "hppppppopppppplpppppa")== False)




#ejercicio10
def verificar_anstrom(numero):
   sumatorio=0
   for i in range (len(numero)):
       sumatorio+=numero[i]**len(numero)
   return sumatorio==int(numero)


# """Ejercicio11"""    
# def calcular_Amstrong(numero):
#     cantidad=0
#     resultado=""
#     for i in range(len(numero)):
#         if numero[i].isdigit():
#             cantidad+=int(numero[i])**len(numero)
#     if cantidad==int(numero):
#         resultado=numero
#     return resultado

# def Amstrong_Numbrer_0_999():
#     cadena=""
#     for i in range(0,999):
#         if calcular_Amstrong(str(i)) != "":
#             print (cadena)

# Amstrong_Numbrer_0_999()


# """Ejercicio12"""    
# def  calcular_Amstrong(numero):
#     cantidad=0
#     resultado=""
#     for i in range(len(numero)):
#         if numero[i].isdigit():
#             cantidad+=int(numero[i])**len(numero)
#     if cantidad==int(numero):
#         resultado=numero
#     return resultado



# """Ejercicio13"""
# def remplazar(frase,contenido,remplazo):
#     mensaje=f"No existe |{contenido}| en |{frase}|"
#     if contenido.upper() in frase.upper():
#         mensaje=frase[:frase.upper().find(contenido.upper())]+remplazo+frase[frase.upper().find(contenido.upper())+len(contenido):]
#     return mensaje




#"""Ejercicio14 TERMINAR"""
#def remplazar(frase,contenido,remplazo):
#    numero_sustituciones=0
#    mensaje=f"No existe |{contenido}| en |{frase}|"
#    mensaje=frase
#    auxiliar=""
#    letraActual=0
#    while contenido.upper() in frase.upper()[letraActual:]:

#    return mensaje




# """Ejercicio15"""
# def contar_vocales(cadena):
#     contador=0
#     for i in range(len("AEIOU")):
#         if "AEIOU"[i] in cadena.upper(): contador+=1
#     return contador

# assert (contar_vocales("hola")==2)
# assert (contar_vocales("holaa")==3)
# assert (contar_vocales("quetalla")==4)
# assert (contar_vocales("qwrrrc")==0)

# """Ejercicio16"""
# def contar_vocales(cadena):
#     contador=0
#     letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#     for i in range(len(letras)):
#         if letras[i] in cadena.upper(): contador+=1
#     return contador


# """Ejercicio17"""
# def reconstruir_cadena(input):
#     vocales="AEIOU"
#     consonantes="BCDFGHJKLMNÑPQRSTVWXYZ"
#     frase_consonantes=""
#     frase_vocales=""
#     for i in input:
#         if i.upper() in consonantes: frase_consonantes+=i
#         elif i.upper() in vocales: frase_vocales+=i
#     return frase_consonantes+frase_vocales

# assert(reconstruir_cadena("ejercicicos de programacion")=="jrccsdprgrmcioneaeioai")
# assert(reconstruir_cadena("un raton valcilom")=="nrtvclmuaoaio")



# """Ejercicio 18"""
# def contar_palabras(input):
#     contador=0
#     inicio_palabra=False
#     for i in range(len(input)):
#         if input[i] !=" " and inicio_palabra==False : inicio_palabra=True
#         elif input[i] ==" " and inicio_palabra==True : 
#             inicio_palabra=False
#             contador+=1
#     if inicio_palabra==True : contador+=1
#     return contador

# assert(contar_palabras("hola buenas tardes")==3)
# assert(contar_palabras("hola")==1)
