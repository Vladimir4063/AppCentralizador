def string_to_integerList(argumento):
    
    Arreglo=argumento.split(",") #queda como array ["1","2","3"]
    for i in range(len(Arreglo)): #3 0,1,2
        Arreglo[i]=int(Arreglo[i]) #0,1,2 [1,2,3]
        
        
    return Arreglo