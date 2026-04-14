texto = input("Digite um texto:")
vogais = "aeiouAEIOU"
contador = 0
 
for letra in texto:
     if letra in vogais:
        contador += 1
        print(f"0 texto contém {contador} vogais.")