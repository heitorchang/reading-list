def ordenar_por_selecao(a):
    len_a = len(a)

    # só é necessário ordenar os primeiros n - 1 elementos porque
    # todo que ficar à esquerda será menor que o último elemento 
    for cur_inx in range(len_a-1):

        # localizar menor elemento do resto
        cur_min = a[cur_inx]
        cur_min_inx = cur_inx
        for i in range(cur_inx+1, len_a):
            if a[i] < cur_min:
                cur_min = a[i]
                cur_min_inx = i

        # permutar (trocar de posicao)
        a[cur_inx], a[cur_min_inx] = a[cur_min_inx], a[cur_inx]
        
