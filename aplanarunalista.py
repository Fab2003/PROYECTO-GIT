Ejemplo = [[3, 8, 2], [(1), 7], [(5, 9), 6], [4], [0, 10, 6, 7],8]
#Firts we define the function
def aplanar_list(lista):
    alamacen = []
    for elemento in lista: #we utilze the bucle "for" for detec every elements is are int,str,list or tuple 
        if type(elemento) in (int,str): 
            alamacen.append(elemento)
        elif type(elemento) == tuple:
            alamacen.extend(aplanar_list(elemento))
        else:
            alamacen.extend(aplanar_list(elemento))
    return alamacen

print(aplanar_list(Ejemplo))




