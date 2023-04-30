peso = float(input())
idade = int(input())
if idade == 17 or idade ==16:
    Documentodeautorização = input()    
boasaude = input()
usodedrogas = input()
primeiradoa = input()
if primeiradoa == "N":
    mesesultdoacao = int(input())
    doacoesnosultimosdozemeses = int(input())
sexobio = input()
if sexobio == "F":
    gravidez = input()
    amamentando = input()
    if amamentando == "S":
        idadebb = int(input())
erro = 0
print(f"Peso: {peso}")
print(f"Idade: {idade}")
if idade <18 and idade >=16:
    print(f"Documento de autorizacao: {Documentodeautorização}")     
print(f"Boa saude: {boasaude}")
print(f"Uso de drogas injetaveis: {usodedrogas}")
print(f"Primeira doacao: {primeiradoa}")
if primeiradoa == "N":
    print(f"Meses desde ultima doacao: {mesesultdoacao}")
    print(f"Doacoes nos ultimos 12 meses: {doacoesnosultimosdozemeses}")
print(f"Sexo biologico: {sexobio}")
if sexobio == "F":
    print(f"Gravidez: {gravidez}") 
    print(f"Amamentando: {amamentando}")
    if amamentando == "S":
        print(f"Meses bebe: {idadebb}")
if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    erro = 1    
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    erro = 1
if idade == 17 or idade ==16:
    if Documentodeautorização == "N":
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
        erro = 1
if idade > 60 and primeiradoa == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    erro = 1
if idade > 69:
    print("Impedimento: maior de 69 anos.")
    erro = 1
if boasaude == "N":
    print("Impedimento: nao esta em boa saude.")
    erro = 1
if usodedrogas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    erro = 1
if primeiradoa == "N" and sexobio == "M":
    if mesesultdoacao < 2:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        erro = 1
    if doacoesnosultimosdozemeses >= 4:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        erro = 1      
elif sexobio == "F"and primeiradoa == "N":
    if   mesesultdoacao < 3:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        erro = 1
    if  doacoesnosultimosdozemeses >= 3:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        erro = 1
if sexobio == "F" and gravidez == "S":
        print("Impedimento: gravidez.")
        erro = 1
if sexobio == "F" and amamentando == "S":
    if idadebb <12:
        print("Impedimento: amamentacao.")
        erro = 1
if erro == 0:
    print("Procure um hemocentro.")

