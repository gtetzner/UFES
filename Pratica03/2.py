produto = int(input("Escolha seu produto: "))
print("-"*35)
if produto ==101:
    print("101 - Batata List          - R$4.50")
elif produto ==305:
    print("305 - Suco Py              - R$2.00")
elif produto == 248:
    print("248 - Suco Interpretado    - R$4.25")
elif produto == 389:
    print("389 - Guaraná Lambda       - R$3.50")
elif produto == 145:
    print("145 - Sanduiche Integral   - R$9.00")
elif produto == 567:
    print("567 - Cerveja Derivada     - R$8.50")
elif produto ==673:    
    print("673 - Vitamina Compilada   - R$7.80")
else:
    print("ERRO")    
print("-"*35)


#Complete o código
#O objetivo é verificar se o código do produto lido é válido e, caso seja, 
# imprimir o produto escolhido e o seu preço. Caso seja escolhido 
# um produto inválido, exibir uma mensagem de erro.