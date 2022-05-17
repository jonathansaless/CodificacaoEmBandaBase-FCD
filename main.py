import clock as clk
import non_return_zero as nrz
import pseudoternary as pst
import b8zs
import manchester as mct
import mostrar_grafico as mg

def main():
    seq = input("DIGITE UMA SEQUENCIA DE BITS:")
    lista_string = list(seq)                #transforma a sequencia em uma lista de string
    lista = list(map(int, lista_string))      #transforma a lista de string em uma lista de inteiro para que seja mais simples a manipulação dos dados com a funçaõ step, dado que essa função só receber lista de inteiros
    #mostrar_grafico(data, data, "SEQUENCIA DE BITS", "orange")
    #CLOCK
    clk.CLOCK(lista)
    #NRZ
    nrz_ = nrz.NRZ(lista)
    mg.mostrar_grafico(lista, nrz_, "NRZ", "green")
    #PSEUDOTERNARY
    pseudoternary = pst.PSEUDOTERNARY(lista)
    mg.mostrar_grafico(lista, pseudoternary, "PSEUDOTERNARY", "blue")
    #B8ZS
    b8zs_ = b8zs.B8ZS(lista)
    mg.mostrar_grafico(lista, b8zs_, "B8ZS", "gold")
    #MANCHESTER
    manchester = mct.MANCHESTER(lista)
    mg.mostrar_grafico(lista, manchester, "MANCHESTER", "red")
    
    
if __name__ == '__main__':
    main()