print("""
====================================
        A ILHA DO CÓDIGO PERDIDO
====================================

Você acorda em uma pequena ilha misteriosa.
Ao seu lado há uma mochila velha, uma trilha na floresta e uma praia deserta.

O que você faz?

1. Abrir a mochila
2. Seguir pela trilha da floresta
3. Caminhar pela praia
""")

escolha = input("> ")

if escolha == "1":
    print("""
Você abre a mochila e encontra três objetos:

1. Uma lanterna
2. Um mapa antigo
3. Uma garrafa de água

Qual objeto você pega primeiro?
""")

    objeto = input("> ")

    if objeto == "1":
        print("""
Você pega a lanterna e percebe que ela ainda funciona.
Ao iluminar algumas pedras próximas, encontra uma entrada escondida para uma caverna.

O que você faz?

1. Entrar na caverna
2. Voltar para a praia
""")

        acao = input("> ")

        if acao == "1":
            print("""
Você entra na caverna com cuidado.
Lá dentro, encontra uma porta de pedra com um símbolo de computador.

Na parede está escrito:
"Para sair da ilha, escolha a lógica correta."

1. if
2. talvez
3. qualquer coisa
""")

            resposta = input("> ")

            if resposta == "1":
                print("""
A porta se abre lentamente.
Dentro dela há um rádio antigo funcionando.

Você chama por ajuda e consegue sair da ilha.

Parabéns! Você venceu usando lógica condicional.
""")
            elif resposta == "2":
                print("""
A porta não abre.
A palavra "talvez" não é uma estrutura condicional válida em Python.

Você volta para estudar mais um pouco e tenta novamente depois.
""")
            else:
                print("""
Nada acontece.
A porta parece exigir uma resposta mais lógica.

Fim de jogo.
""")

        elif acao == "2":
            print("""
Você decide voltar para a praia.
No caminho, acaba se perdendo porque deixou o mapa na mochila.

Fim de jogo.
""")
        else:
            print("""
Você ficou parado pensando demais.
A noite chegou e ficou difícil continuar explorando.

Fim de jogo.
""")

    elif objeto == "2":
        print("""
Você pega o mapa antigo.
Ele mostra três lugares importantes da ilha:

1. Caverna do Norte
2. Torre Abandonada
3. Lago Azul

Para onde você vai?
""")

        lugar = input("> ")

        if lugar == "1":
            print("""
Você chega até a Caverna do Norte.
Na entrada há uma placa dizendo:

"Somente quem entende decisões pode entrar."

Você percebe que precisa de uma lanterna, mas não pegou uma.

Fim de jogo.
""")

        elif lugar == "2":
            print("""
Você chega até a Torre Abandonada.
Lá em cima, encontra um sinalizador antigo.

O que você faz?

1. Acender o sinalizador
2. Guardar o sinalizador
""")

            sinal = input("> ")

            if sinal == "1":
                print("""
O sinalizador ilumina o céu.
Um barco distante vê o sinal e vem até a ilha.

Parabéns! Você conseguiu escapar.
""")
            elif sinal == "2":
                print("""
Você guarda o sinalizador, mas ninguém consegue ver você na ilha.

Fim de jogo.
""")
            else:
                print("""
Você não escolheu uma ação válida.
O vento aumenta e você precisa sair da torre.

Fim de jogo.
""")

        elif lugar == "3":
            print("""
Você chega ao Lago Azul.
A água é limpa, mas não há nenhum caminho de saída por ali.

Você descansa um pouco, mas continua preso na ilha.

Fim de jogo.
""")

        else:
            print("""
Esse lugar não existe no mapa.
Você se perde na ilha.

Fim de jogo.
""")

    elif objeto == "3":
        print("""
Você pega a garrafa de água.
Isso ajuda bastante, mas você ainda precisa encontrar uma forma de sair da ilha.

Depois de caminhar, você encontra uma bifurcação:

1. Caminho com pegadas
2. Caminho com pedras brilhantes
""")

        caminho = input("> ")

        if caminho == "1":
            print("""
Você segue as pegadas e encontra uma pequena cabana.
Dentro dela há um rádio, mas está sem bateria.

Fim de jogo.
""")

        elif caminho == "2":
            print("""
Você segue as pedras brilhantes e encontra uma torre.
Lá em cima, existe um sinalizador.

Você acende o sinalizador e consegue chamar ajuda.

Parabéns! Você escapou da ilha.
""")

        else:
            print("""
Você escolheu um caminho desconhecido.
A aventura termina aqui.

Fim de jogo.
""")

    else:
        print("""
Você não pegou nenhum objeto útil.
Sem equipamento, fica difícil explorar a ilha.

Fim de jogo.
""")

elif escolha == "2":
    print("""
Você segue pela trilha da floresta.
Depois de alguns minutos, encontra uma ponte de madeira e um caminho escuro.

O que você faz?

1. Atravessar a ponte
2. Seguir pelo caminho escuro
""")

    floresta = input("> ")

    if floresta == "1":
        print("""
Você atravessa a ponte com cuidado.
Do outro lado, encontra uma torre abandonada.

Dentro da torre há dois itens:

1. Um sinalizador
2. Um livro velho
""")

        item = input("> ")

        if item == "1":
            print("""
Você pega o sinalizador e sobe até o topo da torre.
Ao acendê-lo, um barco vê o sinal.

Parabéns! Você conseguiu sair da ilha.
""")

        elif item == "2":
            print("""
Você abre o livro velho.
Ele fala sobre programação, mas não ajuda muito a sair da ilha agora.

Fim de jogo.
""")

        else:
            print("""
Você não escolheu nenhum item válido.
A chance de sair da ilha passou.

Fim de jogo.
""")

    elif floresta == "2":
        print("""
Você segue pelo caminho escuro.
Sem lanterna, fica difícil enxergar.

Você decide voltar, mas já está perdido.

Fim de jogo.
""")

    else:
        print("""
Você não escolheu um caminho válido.
A floresta ficou silenciosa demais e você voltou para o início.

Fim de jogo.
""")

elif escolha == "3":
    print("""
Você caminha pela praia.
Depois de algum tempo, encontra uma garrafa com uma mensagem dentro.

A mensagem diz:
"Procure a torre ou a caverna."

O que você faz?

1. Procurar a torre
2. Procurar a caverna
3. Ignorar a mensagem
""")

    praia = input("> ")

    if praia == "1":
        print("""
Você procura a torre e encontra uma construção antiga.
No topo dela há um sinalizador.

O que você faz?

1. Acender o sinalizador
2. Descer da torre
""")

        torre = input("> ")

        if torre == "1":
            print("""
O sinalizador chama a atenção de um barco próximo.
Você é resgatado.

Parabéns! Você venceu o jogo.
""")

        elif torre == "2":
            print("""
Você desce da torre sem usar o sinalizador.
A oportunidade de pedir ajuda passou.

Fim de jogo.
""")

        else:
            print("""
Você não tomou uma decisão clara.
O sinalizador para de funcionar.

Fim de jogo.
""")

    elif praia == "2":
        print("""
Você procura a caverna.
Na entrada, há uma porta com três palavras:

1. Python
2. Banana
3. Pedra

Qual palavra você escolhe?
""")

        palavra = input("> ")

        if palavra == "1":
            print("""
A porta da caverna se abre.
Dentro dela há um rádio funcionando.

Você chama ajuda e consegue sair da ilha.

Parabéns! Você venceu.
""")

        elif palavra == "2":
            print("""
Nada acontece.
A caverna parece não gostar de bananas.

Fim de jogo.
""")

        elif palavra == "3":
            print("""
A porta continua fechada.
Pedra não era a resposta.

Fim de jogo.
""")

        else:
            print("""
Você digitou algo que a porta não reconhece.

Fim de jogo.
""")

    elif praia == "3":
        print("""
Você ignora a mensagem e continua andando pela praia.
Depois de horas caminhando, volta para o mesmo lugar.

Fim de jogo.
""")

    else:
        print("""
Você não escolheu uma opção válida.

Fim de jogo.
""")

else:
    print("""
Você ficou parado sem decidir o que fazer.
Em jogos de aventura, escolher é muito importante.

Fim de jogo.
""")