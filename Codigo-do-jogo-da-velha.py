tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
ganhar = False
jogadorX = "X"
jogadorO = "O"

def jogar():
    print('O jogador X começa!')
    while(True):
        inserirLinhaColuna(jogadorX)

        if(checarSeGanhou(jogadorX) == True):
            break
            
        mostrarTabuleiro()
        inserirLinhaColuna(jogadorO)

        if(checarSeGanhou(jogadorO) == True):
            break
        mostrarTabuleiro()

def checarSeGanhou(jogador):
    velha = darVelha()
    linha =ganharEmLinha()
    coluna = ganharEmColuna()
    diagonal = ganharEmDiagonal()

    if(velha == True or linha == True or coluna == True or diagonal == True):
        mostrarTabuleiro()
        return True

def mostrarTabuleiro():
    for i in range(0,3):
        print()
        print(tabuleiro[i][0],'|', tabuleiro[i][1],'|', tabuleiro[i][2])
    print()

def inserirLinhaColuna(jogador):
    linha1 = int(input('JOGADOR '+ jogador+' | Coloque a linha: '))
    coluna1 = int (input('JOGADOR '+ jogador+' | Coloque a coluna: '))
    print()

    tabuleiro[linha1 - 1][coluna1 - 1] = jogador

def ganharEmLinha():
    for a in range (0,3):
        if tabuleiro[a][0] == 'X' and tabuleiro[a][1] == 'X' and tabuleiro[a][2] == 'X':
            print('Jogador X Ganhou!')
            return True
            
        if tabuleiro[a][0] == 'O' and tabuleiro[a][1] == 'O' and tabuleiro[a][2]== 'O':
            print('Jogador O Ganhou!')
            return True
        
    return False

def ganharEmColuna():
    for k in range (0,3):
        if tabuleiro[0][k] == 'X' and tabuleiro[1][k] == 'X' and tabuleiro[2][k] == 'X' :
            print('Jogador X Ganhou!')
            return True
                  
        if tabuleiro[0][k] == 'O' and tabuleiro[1][k] == 'O' and tabuleiro[2][k] == 'O' :
            print('Jogador O Ganhou!')        
            return True
    return False

def ganharEmDiagonal():
    if tabuleiro[0][0]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][2] == 'X':
        print ('Jogador X Ganhou!')
        return True
          
    if tabuleiro[0][2]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][0] == 'X':
        print ('Jogador X Ganhou!')
        return True
                  
    if tabuleiro[0][0]== 'O' and tabuleiro[1][1]== 'O' and tabuleiro[2][2] == "O":
        print ('Jogador O Ganhou!')
        return True
          
    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('Jogador O Ganhou!')
        return True

    return False

def darVelha():
    if (tabuleiro[0][0] != '_' and tabuleiro[0][1] != '_'and tabuleiro[0][2] != '_'):
        if(tabuleiro[1][0] != '_' and tabuleiro[1][1] != '_' and tabuleiro[1][2] != '_'):
            if (tabuleiro[2][0] != '_' and tabuleiro[2][1] != '_' and tabuleiro[2][2] != '_'):
                if (ganharEmLinha() == False and ganharEmColuna() == False and ganharEmDiagonal() == False):
                    print ("# Deu velha #")
                    return True
    return False


jogar()