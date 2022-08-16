def subida_c(quantidade_andares):

    tempo = [0]
    velocidade_variavel = 0.3333333333333333
    
    if quantidade_andares == 0:
        print('NOTA: Com a velocidade zero, a vovó está no térreo e não se desloca para nenhum outro andar. Portanto, o tempo é igual a 0 🙂')
    else:
        andares_total = []
        for andar in range(quantidade_andares):
            andares_total.append(andar)

        def get_andares_especiais(a_e):

            andares_e = []
            for each in range(a_e[0], a_e[-1], 7):
                andares_e.append(each+1)

            return andares_e

        andares_especiais = get_andares_especiais(andares_total)

        for andar in andares_total:
            if andar in set(andares_especiais) and andar != 0:
                velocidade_variavel = velocidade_variavel / 2
                tempo.append(andar/velocidade_variavel)
            else:
                tempo.append(andar/velocidade_variavel)

        tempo = sum(tempo)

        tempo_formatado = int(tempo)
        horas = tempo_formatado // 60
        minutos = tempo_formatado % 60

        return print('🕒 TEMPO: {} hora(s) e {} minuto(s)!'.format(horas, minutos))
      
subida_c(21)
