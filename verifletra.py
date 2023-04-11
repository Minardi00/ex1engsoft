while True:
    entrada = input("Digite um caracter: ")

    if entrada == 'a' or entrada == 'e' or entrada == 'i' or entrada == 'o' or entrada == 'u' or entrada =='A' or entrada =='E' or entrada =='I' or entrada =='O' or entrada == 'U':
        print (entrada, " é uma vogal")

    else:
        print(entrada, " é uma consoante") 

    resposta = input("Deseja verificar novamente? (s/n) ")
    
    if resposta.lower() != 's': 
        break
      
    
