a = float(input('informe a primeira nota: '))
b = float(input('informe a segunda nota: '))
c = float(input('informe a terceira nota: '))

if 10>= a >=0:
    if 10>= b >=0:
        if 10>= c >=0:        
                mc = float(input('agora informe o metodo de calculo de media entre (1)aritimetico ou (2)ponterada: '))


                if mc == 1:
                    mg = (a + b + c)/3
                    print('a media aritimetica é: ', mg)

                elif mc == 2:
                    i = float(input('informe o peso da primeira nota: '))
                    o = float(input('informe o peso da segunda nota: '))
                    p = float(input('informe o peso da terceira nota: '))

                    mg = ((a*i) + (b*o) + (c*p))/(i+o+p)
                    print('a media ponterada é: ', mg)

                else:
                    print('opção invalida')
        else:
            print('Terceira nota invalida: "', c,'"')
    else:
        print('Segunda nota invalida: "', b,'"')
else:
   print('Primeira nota invalida: "', a,'"')