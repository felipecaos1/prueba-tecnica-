class texto():

    def operation(self, entrada):
        self.estado=True
        self.lista="0123456789+-/*()" #caracteres que indican que es una operacion matematica 
        self.con1=0
        self.con2=0
        for i in entrada:
            if i in self.lista:
                if i=="(":
                    self.con1 += 1
                else:
                    pass 
                if i== ")":
                    self.con2 +=1
                else:
                    pass
            else: #si hay algun caracter diferente a los establecidos se descarta que sea una operacion matematica 
                self.estado=False
                break

        if self.con1==self.con2: #si el numero y el sentido de los parentesis coincide se asume que esta correctamente escrita 
            pass
        else:
            self.estado=False
            
        return self.estado

    def compute(self, entrada):# funcion solo diseñada para operar dos numeros mediante una sola operacion matematica (+,-,*,/)
        self.estado=s.operation(entrada)
        if self.estado==False:
            return False
        else:
            if "+" in entrada:
                self.separada=entrada.split("+")
                return int(self.separada[0])+int(self.separada[1])

            if "-" in entrada:
                self.separada=entrada.split("-")
                return int(self.separada[0])-int(self.separada[1])
            
            if "*" in entrada:
                self.separada=entrada.split("*")
                return int(self.separada[0])*int(self.separada[1]) 
            if "/" in entrada:
                self.separada=entrada.split("/")
                return int(self.separada[0])/int(self.separada[1])


            

s=texto()

print(s.operation("2*3")) 
print(s.compute("2*3")) 

