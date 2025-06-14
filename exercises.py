nome = input("Olá, qual é o seu nome? ")
print(f"Certo {nome}, vamos falar um pouco sobre seus aniversários!")

ano_de_nascimento = int(input("Qual é o ano de seu nascimento? "))
print(f"Ok, então em {ano_de_nascimento} você chegou ao mundo!")

for ano in range(ano_de_nascimento, 2026):
     idade = ano - ano_de_nascimento
     if ano == 2025:
         print(f"Em 2025, você completará {idade} anos")
     else:
         print(f"No ano {ano}, você tinha {idade} anos de idade")
