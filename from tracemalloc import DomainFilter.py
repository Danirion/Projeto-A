from tracemalloc import DomainFilter


nome="Daniel"
nota1=7
nota2=8
nfalta=3
soma=nota1+nota2
media=soma/2
 
if (media < 7) and (nfalta > 3):
    print(nome, " Reprovado")
else:
    print(nome, " Aprovado")

