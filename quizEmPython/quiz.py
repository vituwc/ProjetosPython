print('Quiz em Python')
print('Olá, Seja Bem-Vindo.')
answer_user = input("Você deseja começar o quiz? (S/N): ")

if answer_user.upper() != "S":
    quit()

score = 0

print('Começando o Quiz...')

print('1. Cultura Geral\nQual é a capital do Canadá?\na) Toronto\nb) Ottawa\nc) Vancouver\nd) Montreal')
resposta1 = input('Resposta: ')

if resposta1.lower() == "b":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('2. Cultura Geral\nQuem foi o autor de "Dom Quixote"?\na) William Shakespeare\nb) Miguel de Cervantes\nc) Gabriel García Márquez\nd) Federico García Lorca')
resposta2 = input('Resposta: ')

if resposta2.lower() == "b":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('3. Ciências\nQual é o maior planeta do Sistema Solar?\na) Terra\nb) Marte\nc) Júpiter\nd) Saturno')
resposta3 = input('Resposta: ')

if resposta3.lower() == "c":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('4. Ciências\nQual é a fórmula química da água?\na) H2O\nb) CO2\nc) O2\nd) NaCl')
resposta4 = input('Resposta: ')

if resposta4.lower() == "a":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('5. Matemática\nQual é o resultado de 8 x 7?\na) 48\nb) 56\nc) 64\nd) 72')
resposta5 = input('Resposta: ')

if resposta5.lower() == "b":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('6. Matemática\nSe um triângulo tem dois lados de 3 cm e um de 5 cm, qual é o nome desse tipo de triângulo?\na) Equilátero\nb) Isósceles\nc) Escaleno\nd) Retângulo')
resposta6 = input('Resposta: ')

if resposta6.lower() == "b":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('7. História\nEm que ano o Brasil declarou sua independência de Portugal?\na) 1492\nb) 1808\nc) 1822\nd) 1889')
resposta7 = input('Resposta: ')

if resposta7.lower() == "c":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('8. História\nQuem foi o líder do movimento dos Direitos Civis nos EUA e fez o famoso discurso "Eu Tenho um Sonho"?\na) Malcolm X\nb) Nelson Mandela\nc) Martin Luther King Jr.\nd) Abraham Lincoln')
resposta8 = input('Resposta: ')

if resposta8.lower() == "c":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('9. Tecnologia\nQual dessas linguagens é principalmente usada para desenvolvimento de páginas web?\na) Python\nb) C++\nc) HTML\nd) SQL')
resposta9 = input('Resposta: ')

if resposta9.lower() == "c":
    print("Correto! Vamos para a próxima pergunta.")
    score += 1
else:
    print("Incorreto! Vamos para a próxima pergunta.")
    score -= 1

print('10. Tecnologia\nO que significa a sigla CPU?\na) Central Processing Unit\nb) Control Processing Unit\nc) Computer Power Unit\nd) Central Power Unit')
resposta10 = input('Resposta: ')

if resposta10.lower() == "a":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")
    score -= 1

print(f'Quiz finalizado! Sua pontuação final é: {score}/10')


