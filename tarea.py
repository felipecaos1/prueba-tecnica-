class matrix():

    def dimension(self, mat):
        self.aux=mat[0]
        self.x=0
        self.con=0
        while self.x==0:#se utiliza un ciclo para repetir la accion de
            try:# intentar acceder en cada iteracion a una capa mas propunda de la matriz 
                self.a=len(self.aux)
                self.con=self.con+1    #con este contador sabremos a cuantas capas pudo acceder 
                self.aux=self.aux[0]
            except:
                self.x=1
        return self.con+1

    def straight(self, mat): #este metodo esta diseñado par las dimensiones 1,2,3 por practicidad 
        self.dime=o.dimension(mat) #hacemos uso del metodo para calcular la dimension 
        self.estado=""
        self.con=0
        if self.dime==1: #si es un vector, suponemos que esta bien escrito y por tanto es simetrico
            self.estado=True
        if self.dime==2: #para una matriz
            for i in range(len(mat)):
                if len(mat[0])==len(mat[i]): #comparamos el tamaño de la pocision [0] con todas las demas 
                    self.con+=1
                else:
                    pass
            
            if self.con==len(mat): 
                self.estado=True
            else:
                self.estado=False

        if self.dime==3: #dimension 3
           for i in range(len(mat)):
                 for j in range(len(mat[i])):
                        if len(mat[0][0])==len(mat[i][j]):#comparamos la posicion [0][0] con todas las demas 
                           self.con+=1
                           self.estado=True
                        else: #si en algun momento el tamaño no coincide se rompera el ciclo 
                            self.estado=False
                            break
        return self.estado           

    def compute(self, mat): #este metodo esta diseñado para dimension 1,2 y 3 
        self.dime=o.dimension(mat) #hacemos uso del metodo dimension 
        self.total=0
        if self.dime==1:
            self.total=sum(mat)#utilizamos el metodo sum()
        if self.dime==2:
            for i in range(len(mat)):
                self.total=self.total+sum(mat[i])
        if self.dime==3:
           for i in range(len(mat)):
                 for j in range(len(mat[i])):
                        self.total=self.total+sum(mat[i][j])
        
        
        return self.total



o=matrix()

c = [[1,2],[2,4],[2,4],[1,2,3]]
#print(o.straight(c))
#print(o.dimension(c))
f = [[[1, 2, 6], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]
#print(o.straight(f))
e = [[[1, 2, 3]], [[5, 6, 7],[5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
a=[[[[1,2,2],[1,2,3]]]]
d = [[[3,4],[6,5]]]
#print(o.dimension(d))
print(o.straight(d))
a=[1,2,3]
#o.suma(c)
#c = [[1,2],[2,4],[2,4]]
#o.suma(c)
#d = [[[3,4],[6,5]]]
#o.dimension(d)
#e = [[[1, 2, 3]], [[5, 6, 7],[5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
#o.suma(e)

