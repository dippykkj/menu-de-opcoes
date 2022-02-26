print('Olá, caro cliente! Aqui está o cardápio: \n[1] = pizza \n[2] = hamburguer \n[3] = batata frita \n[4] = sorvete \n[5] = pastel')

resposta = input('faça sua escolha: ')
if resposta == 1:
    print('Pagamento efetuado! Você comprou uma pizza por R$40,00!')
elif resposta == 2:
    print('Pagamento efetuado! Você comprou um hamburguer por R$20,00!')
elif resposta == 3:
    print('Pagamento efetuado! Você comprou uma batata frita por R$15,00!')
elif resposta == 4:
    print('Pagamento efetuado! Você comprou um sorvete por R$5,00!')
elif resposta == 5:
    print('Pagamento efetuado! Você comprou um pastel por R$6,00!')
elif resposta.isnumeric() == False:
  print('Use somente números!')
else:
    print('Ops! Algo deu errado... Verifique se este número existe no menu!')
    
#Peço perdão em casos de erros, ainda estou começando na linguagem!
