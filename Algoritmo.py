#Primero definimos el conjunto minimal
def minimal(E):
    n = len(E)
    i = 0
    while i < n:
        arista_1 = E[i]
        j = 0
        gate = True
        while j < n and gate:
            arista_2 = E[j]
            if arista_2.issubset(arista_1) and (arista_1!=arista_2):
                E.pop(i)
                i -=1
                n -= 1
                gate = False
            else:
                j += 1
        i += 1
    return E


print('Ejemplo del minimal con [{2,3},{3}]: \n', minimal([{2,3},{3}]), '\n')

#defino la union
def union(A,B):
    return [a.union(b) for a in A for b in B]

#print('Ejemplo de unión con [{2,3},{3}],[{1},{2}]: \n',union([{2,3},{3}],[{1},{2}]),'\n')

#defino el transversal de un conjunto con un sólo elemento
def transveral_un_elemento(A):
    return [{elemento} for a in A for elemento in a]

#print('Ejemplo de transversal con [{3,2}]: \n',transveral_un_elemento([{3,2}]),'\n')

def algoritmo(E,menor=True):
    minimal_sets = minimal(E)
    last_Tr = []
    for k in range(1,len(minimal_sets)+1):
        e = minimal_sets.pop()
        if k == 1:
            Tr_A = transveral_un_elemento([e])
        else:
            Tr_A = minimal(union(last_Tr,transveral_un_elemento([e])))
        last_Tr = Tr_A
    if (menor==True):
        minimo = 0
        for transv in last_Tr:
            if (len(transv) >= minimo):
                if (minimo==0):
                    minimo = len(transv)
                    transv_minimo = transv
            else:
                minimo = len(transv)
                transv_minimo = transv
        return transv_minimo
    else:
        return(Tr_A)

Ejemplo = [{3,2},{4}]
print("Conjunto de aristas: ", Ejemplo)
print("Transversal mínimo: ", algoritmo(Ejemplo),'\n')

Ejemplo = [{1,2,3}, {2,3}, {3,5,6}, {4}]
print("Conjunto de aristas: ", Ejemplo)
print("Transversal mínimo: ", algoritmo(Ejemplo),'\n')

#Crear el tablero de ajedrez
def tablero(n):
    conjunto_aristas = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            arista = {(i,j)}
            for m in range(1,n+1):
                if (i,m) not in arista:
                    arista.add((i,m))
                if (m,j) not in arista:
                    arista.add((m,j))
                for k in range(1,n+1):
                    if (m-j == k-i) or (m-j == -(k-i)):
                        if (k,m) not in arista:
                            arista.add((k,m))
            conjunto_aristas.append(arista)
    return conjunto_aristas 

#print('Tablero 4x4')
#print("Transversal mínimo: ",algoritmo(tablero(4),True), '\n')

#print('Tablero 5x5')
#print("Transversal mínimo: ",algoritmo(tablero(5),True), '\n')

def tablero_alternativo(n):
    conjunto_aristas = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            celda = (j-1)*n+i
            arista = {celda}
            k = min(n-i,n-j)+1
            q = min (n-i,j-1)+1
            l = min(n-j,i-1)+1
            p = min(j-1,i-1)+1
            if i!=n and j!=n:
                for m in range(1,k):
                    arista.add(celda+(n+1)*m)
            if i!=1 and j!=1:
                for m in range(1,p):
                    arista.add(celda-(n+1)*m)
            if i!=1 and j!=n:
                for k in range(1,l):
                    arista.add(celda+(n-1)*k)
            if j!=1 and i!=n:
                for k in range(1,q):
                    arista.add(celda-(n-1)*k)
            for t in range(0,n):
                arista.add(t*n+i)
            for r in range(1,n+1):
                arista.add((j-1)*n+r)
            conjunto_aristas.append(arista)
    return conjunto_aristas

#Aún definiendo de dos formas el tablero se llega a errores, estimo yo que es por la cantidad
#de operaciones que se tiene que hacer
#print(algoritmo(tablero_alternativo(5)))

Ejemplo = [{1,2,3}, {2,5}, {3,4}, {1,2,4,6}, {5,6}, {6}]
print("Conjunto de aristas: ", Ejemplo)
print("Transversal mínimo: ", algoritmo(Ejemplo),'\n')