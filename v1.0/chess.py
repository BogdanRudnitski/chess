import pygame
import copy

memory=[]

ram=[]
table={1:'W',-1:'B'}
turn=1

board=[['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.']]

class piece:

    def __init__(self, name, type, team, image, virgin=True):

        self.name=name
        self.type=type
        self.team=team
        self.image=image
        self.virgin=virgin

    def __repr__(self):
        return self.name
    
Bpawn=piece('Bp', 'pawn', 'B', 'v1.0/pieces/black pawn.png')
Brook=piece('Br', 'rook', 'B', 'v1.0/pieces/black rook.png')
Bbishop=piece('Bb', 'bishop', 'B', 'v1.0/pieces/black bishop.png')
Bknight=piece('Bk', 'knight', 'B', 'v1.0/pieces/black knight.png')
Bqueen=piece('Bq', 'queen', 'B', 'v1.0/pieces/black queen.png')
Bking=piece('BK', 'king', 'B', 'v1.0/pieces/black king.png')
Wpawn=piece('Wp', 'pawn', 'W', 'v1.0/pieces/white pawn.png')
Wrook=piece('Wr', 'rook', 'W', 'v1.0/pieces/white rook.png')
Wbishop=piece('Wb', 'bishop', 'W', 'v1.0/pieces/white bishop.png')
Wknight=piece('Wk', 'knight', 'W', 'v1.0/pieces/white knight.png')
Wqueen=piece('Wq', 'queen', 'W', 'v1.0/pieces/white queen.png')
Wking=piece('WK', 'king', 'W', 'v1.0/pieces/white king.png')

empty=piece('.', '', '', '')


def board_reset():

    for n in range(8):
        board[1][n]=Bpawn
        board[6][n]=Wpawn
        for m in range(2,6):
            board[m][n]=empty

    row1=board[0]
    row1[0]=Brook
    row1[7]=Brook
    row1[1]=Bknight
    row1[6]=Bknight
    row1[2]=Bbishop
    row1[5]=Bbishop
    row1[3]=Bqueen
    row1[4]=Bking
    
    row8=board[7]
    row8[0]=Wrook
    row8[7]=Wrook
    row8[1]=Wknight
    row8[6]=Wknight
    row8[2]=Wbishop
    row8[5]=Wbishop
    row8[3]=Wqueen
    row8[4]=Wking
   
def round_switch():
    new=[]
    for row in board:
        row.reverse()
        new.append(row)
    new.reverse()
    return new

def pawn_moves(y,x):
    team=board[y][x].team
    available=[]

    if board[y][x].name=='Wp':
        if y-1>=0:
            if board[y-1][x].team=='':
                available.append([y-1,x])
        if y-1>=0 and x-1>=0:
            if board[y-1][x-1].team!=team and board[y-1][x-1].team!='':
                available.append([y-1,x-1])
        if y-1>=0 and x+1<8:
            if board[y-1][x+1].team!=team and board[y-1][x+1].team!='':
                available.append([y-1,x+1])
        if y==6 and board[5][x].team=='' and board[4][x].team=='':
            available.append([4,x])

    else:
        if y+1<8:
            if board[y+1][x].team=='':
                available.append([y+1,x])
        if y+1<8 and x-1>=0:
            if board[y+1][x-1].team!=team and board[y+1][x-1].team!='':
                available.append([y+1,x-1])
        if y+1<8 and x+1<8:
            if board[y+1][x+1].team!=team and board[y+1][x+1].team!='':
                available.append([y+1,x+1])
        if y==1 and board[2][x].team=='' and board[3][x].team=='':
            available.append([3,x])

    return available

def knight_moves(y,x):
    team=board[y][x].team
    available=[]
    if y-2>=0 and x-1>=0:
        if board[y-2][x-1].team!=team:
            available.append([y-2,x-1])
    if y-2>=0 and x+1<8:
        if board[y-2][x+1].team!=team:
            available.append([y-2,x+1])
    if y+1<8 and x+2<8:
        if board[y+1][x+2].team!=team:
            available.append([y+1,x+2])
    if y-1>=0 and x+2<8:
        if board[y-1][x+2].team!=team:
            available.append([y-1,x+2])
    if y+2<8 and x+1<8:
        if board[y+2][x+1].team!=team:
            available.append([y+2,x+1])
    if y+2<8 and x-1>=0:
        if board[y+2][x-1].team!=team:
            available.append([y+2,x-1])
    if y+1<8 and x-2>=0:
        if board[y+1][x-2].team!=team:
            available.append([y+1,x-2])
    if y-1>=0 and x-2>=0:
        if board[y-1][x-2].team!=team:
            available.append([y-1,x-2])

    return available
        
def rook_moves(y,x):
    team=board[y][x].team
    available=[]
    for n in range(1,9):
        if y+n<8:
            if board[y+n][x].team!=team:
                available.append([y+n,x])
                if board[y+n][x].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if y-n>=0:
            if board[y-n][x].team!=team:
                available.append([y-n,x])
                if board[y-n][x].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if x-n>=0:
            if board[y][x-n].team!=team:
                available.append([y,x-n])
                if board[y][x-n].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if x+n<8:
            if board[y][x+n].team!=team:
                available.append([y,x+n])
                if board[y][x+n].team!='':
                    break
            else:
                break

    return available

def bishop_moves(y,x):
    team=board[y][x].team
    available=[]
    for n in range(1,9):
        if x+n<8 and y+n<8:
            if board[y+n][x+n].team!=team:
                available.append([y+n,x+n])
                if board[y+n][x+n].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if x+n<8 and y-n>=0:
            if board[y-n][x+n].team!=team:
                available.append([y-n,x+n])
                if board[y-n][x+n].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if x-n>=0 and y-n>=0:
            if board[y-n][x-n].team!=team:
                available.append([y-n,x-n])
                if board[y-n][x-n].team!='':
                    break
            else:
                break
    for n in range(1,9):
        if x-n>=0 and y+n<8:
            if board[y+n][x-n].team!=team:
                available.append([y+n,x-n])
                if board[y+n][x-n].team!='':
                    break
            else:
                break

    return available

def king_moves(y,x):
    team=board[y][x].team
    available=[]
    if x+1<8:
        if board[y][x+1].team!=team:
            available.append([y,x+1])
    if y+1<8:
        if board[y+1][x].team!=team:
            available.append([y+1,x])
    if x+1<8 and y+1<8:
        if board[y+1][x+1].team!=team:
            available.append([y+1,x+1])
    if x-1>=0 and y+1<8:
        if board[y+1][x-1].team!=team:
            available.append([y+1,x-1])
    if x-1>=0 and y-1>=0:
        if board[y-1][x-1].team!=team:
            available.append([y-1,x-1])   
    if x+1<8 and y-1>=0:
        if board[y-1][x+1].team!=team:
            available.append([y-1,x+1])
    if x-1>=0:
        if board[y][x-1].team!=team:
            available.append([y,x-1])
    if y-1>=0:
        if board[y-1][x].team!=team:
            available.append([y-1,x])
    
    return available


def moves(y,x):
    A=[]
    if board[y][x].type=='pawn':
        A=pawn_moves(y,x)
    if board[y][x].type=='knight':
        A=knight_moves(y,x)
    if board[y][x].type=='rook':
        A=rook_moves(y,x)
    if board[y][x].type=='bishop':
        A=bishop_moves(y,x)
    if board[y][x].type=='queen':
        bishop=bishop_moves(y,x)
        rook=rook_moves(y,x)
        A=bishop+rook
    if board[y][x].type=='king':
        A=king_moves(y,x)

    return A

def pawn_to_queen():
    for x in range(8):
        if board[0][x].name=='Wp':
            board[0][x]=Wqueen
    for x in range(8):
        if board[7][x].name=='Bp':
            board[7][x]=Bqueen

def check_castling():
    coords=[]
    if board[picky][pickx].type=='king' and board[picky][pickx].virgin:
        if board[picky][5]==empty and board[picky][6]==empty:
            if board[picky][7].type=='rook' and board[picky][7].virgin:
                coords.append([picky,7])
        if board[picky][3]==empty and board[picky][2]==empty and board[picky][1]==empty:
            if board[picky][0].type=='rook' and board[picky][0].virgin:
                coords.append([picky,0]) 
    return coords
    
def check_en_passant():
    if board[newy][newx].type=='pawn':
        if abs(newy-y)==2:
            if x-1>=0:
                if board[newy][newx-1].team==table[turn*-1] and board[newy][newx-1].type=='pawn':
                    return True
            if x+1<8:
                if board[newy][newx+1].team==table[turn*-1] and board[newy][newx+1].type=='pawn':
                    return True
    return False



def print_board():
    table={1:'white',-1:'grey'}
    n=-1
    width=screen.get_width()
    height=screen.get_height()
    mouse=pygame.mouse.get_pos()
    for x in range(8):
        n*=-1
        for y in range(8):
            if x*width/8 <= mouse[0] <= (x+1)*width/8 and y*height/8 <= mouse[1] <= (y+1)*height/8:
                if pick:
                    color='orange'
                else:
                    color='yellow'
            
            elif pick:
                available=moves(picky,pickx)
                if [y,x] in available:
                    color='green'
                elif x==pickx and y==picky:
                    color='yellow'
                elif [y,x] in castling:
                    color='blue'
                elif [y,x] == passing:
                    color='blue'
                else:
                    color=table[n]
            else:
                color=table[n]
            pygame.draw.rect(screen, color, [x*width/8,y*height/8,(x+1)*width/8,(y+1)*height/8])
            n*=-1

            if board[y][x].type!='':
                display=pygame.transform.scale(pygame.image.load(board[y][x].image),(width/8,width/8))
                screen.blit(display, (x*width/8,y*height/8))

            
    


    """for i in board:
        fmt='{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}{:4s}'
        x=fmt.format(i[0].name,i[1].name,i[2].name,i[3].name,i[4].name,i[5].name,i[6].name,i[7].name)
        print(x)"""


    
board_reset()





res=(800,800)
screen=pygame.display.set_mode(res)
pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Calibri', 100)
checkmate_mess=my_font.render('CHECKMATE',False,'red')
check_mess=my_font.render('CHECK',False,'blue')



if __name__ == "__main__":

    check=False
    checkmate=False
    pick=False
    running=True
    castling=[]
    passing=[]
    en_passant_opportunity=False

    while running:
        
        print_board()
        if checkmate:
            screen.blit(checkmate_mess, (90,345))
        elif check:
            screen.blit(check_mess, (230,345))
        pygame.display.update()
        
    

        for ev in pygame.event.get():

            if ev.type==pygame.QUIT:
                pygame.quit()
                running=False

            if ev.type==pygame.KEYDOWN:
                if ev.key==pygame.K_z:
                    if memory:
                        print('HEY')
                        board=memory.pop()
                        turn*=-1
                    else:
                        print('ALREADY AT BEGGINING')
                        memory.append(copy.deepcopy(board))

            if ev.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                
                if not pick:
                    y=mouse[1]//100
                    x=mouse[0]//100
                    pickx,picky=x,y

                    castling=check_castling()

                    if en_passant_opportunity:
                        if board[picky][pickx].type=='pawn' and picky==epy and abs(pickx-epx)==1:
                            if board[picky][pickx].team=='B':
                                passing=[picky+1,epx]
                            if board[picky][pickx].team=='W':
                                passing=[picky-1,epx]
                
                    if board[y][x].team!=table[turn]:
                        print('Select a valid piece')
                        continue
                    pick=True
                    continue

                if mouse[1]//100==y and mouse[0]//100==x:
                    pick=False
                    continue
                
            
                newy=mouse[1]//100
                newx=mouse[0]//100
                move=[newy,newx]
                    
                available=moves(y,x)

                if move in castling:
                    if move[1]==7:
                        board[picky][7].virgin=False
                        board[picky][6]=board[picky][4]
                        board[picky][5]=board[picky][7]
                        board[picky][7]=empty
                    if move[1]==0:
                        board[picky][0].virgin=False
                        board[picky][2]=board[picky][4]
                        board[picky][3]=board[picky][0]
                        board[picky][0]=empty

                    board[picky][4].virgin=False
                    board[picky][4]=empty
                    
                    pick=False
                    turn*=-1

                if move == passing:
                    board[newy][newx]=board[y][x]
                    board[y][x]=empty
                    board[y][newx]=empty
                    pick=False
                    turn*=-1

                elif move in available:

                    memory.append(copy.deepcopy(board))
                    
                    #check if creates check for own team/doesnt break check
                    ram.append(board[newy][newx])

                    '''if board[y][x].type=='pawn':
                        if abs(newy-y)==2:
                            two_step_pawn==True'''

                    board[newy][newx]=board[y][x]
                    board[y][x]=empty
                    danger=[]
                    for ay in range(8):
                        for ax in range(8):
                            if board[ay][ax].team==table[turn*-1]:
                                available=moves(ay,ax)
                                danger+=available
                            if board[ay][ax].type=='king':
                                if board[ay][ax].team==table[turn]:
                                    kingy=ay
                                    kingx=ax
                    print(danger)
                    
                    if [kingy,kingx] in danger:
                        board[y][x]=board[newy][newx]
                        board[newy][newx]=ram.pop()
                        memory.pop()
                        if check:
                            print('\nCannot move there. King is still checked\n')
                        else:
                            print('\nCannot move there. King will be checked\n')
                        continue
                    
                    board[newy][newx].virgin=False

                    

                    pawn_to_queen()

                    danger=[]
                    if check:
                        check=False
                    
                    pick=False ####
                    

                    #CHECK?
                    for c in range(8):
                        for d in range(8):
                            if board[c][d].team==table[turn]:
                                available=moves(c,d)
                                danger+=available
                            if board[c][d].type=='king':
                                if board[c][d].team!=table[turn]:
                                    kingy=c
                                    kingx=d
                    if [kingy,kingx] in danger:
                        check=True
                        if danger.count([kingy,kingx])>1:
                            if not moves(kingy,kingx):
                                checkmate=True
                                break
                        
                    checkmate=True
                    for move in moves(kingy,kingx):
                        if move not in danger:
                            checkmate=False
        
                    for e in range(8):
                        for f in range(8):
                            danger=[]
                            if board[e][f].team==table[turn*-1] and board[e][f].type!='king':
                                for move in moves(e,f):
                                    danger=[]
                                    tryy,tryx=move[0],move[1]

                                    ram.append(board[tryy][tryx])
                                    board[tryy][tryx]=board[e][f]
                                    board[e][f]=empty

                                    for a in range(8):
                                        for b in range(8):
                                            if board[a][b].team==table[turn]:
                                                available=moves(a,b)
                                                danger+=available

                                    board[e][f]=board[tryy][tryx]
                                    board[tryy][tryx]=ram.pop()

                                    if [kingy,kingx] in danger:
                                        continue

                                    checkmate=False      

                        

                    if checkmate:
                        break


                    #board=round_switch() ######
                    
                    en_passant_opportunity=False
                    en_passant_opportunity=check_en_passant()
                    if en_passant_opportunity:
                        epy=newy
                        epx=newx

                    turn*=-1
                    
                

                else:
                    print('Cannot move there')
                    continue

                castling_right=[]  
                
            

        



    



   

"""
while True:

    pick=input('Choose a square: ')
    if pick=='e':
        break
    if len(pick)==2:
        if 0<int(pick[0])<9:
            if 0<int(pick[1])<9:
                y=int(pick[1])-1
                x=int(pick[0])-1
                memoryy=y
                memoryx=x
                if board[y][x].team!=table[turn]:
                    print('Select a valid piece')
                    continue
                while True:
                    y=memoryy
                    x=memoryx
                    choice=input('Choose a square to move to: ')
                    if choice=='z':
                        break
                    newx=int(choice[0])-1
                    newy=int(choice[1])-1
                    move=[newy,newx]
                    
                    available=moves()

                    if move in available:
                        
                        #check if move creates/keeps check
                        ramy,ramx=y,x
                        board[newy][newx]=board[y][x]
                        board[y][x]=empty
                        danger=[]
                        board=round_switch()
                        turn*=-1
                        for y in range(8):
                            for x in range(8):
                                if board[y][x].team==table[turn]:
                                    available=moves()
                                    danger+=available
                                if board[y][x].type=='king':
                                    if board[y][x].team!=table[turn]:
                                        kingy=y
                                        kingx=x
                        if [kingy,kingx] in danger:
                            if danger.count([kingy,kingx])>1:
                                checkmate=True
                                break
                            y,x=kingy,kingx
                            turn*=-1
                            available=king_moves()
                            turn*=-1
                            checkmate=True
                            for move in available:
                                if move not in danger:
                                    checkmate=False
                            if checkmate:
                                break
                            board=round_switch()
                            turn*=-1
                            board[ramy][ramx]=board[newy][newx]
                            board[newy][newx]=empty
                            if check:
                                print('\nCannot move there. King is still checked\n')
                            else:
                                print('\nCannot move there. King will be checked\n')
                            continue
                        board=round_switch()
                        turn*=-1
                        danger=[]
                        if check:
                            check=False
                        
                        #check if checked
                        for y in range(8):
                            for x in range(8):
                                if board[y][x].team==table[turn]:
                                    available=moves()
                                    danger+=available
                                if board[y][x].type=='king':
                                    if board[y][x].team!=table[turn]:
                                        kingy=y
                                        kingx=x
                        if [kingy,kingx] in danger:
                            if danger.count([kingy,kingx])>1:
                                checkmate=True
                                break
                            y,x=kingy,kingx
                            turn*=-1
                            available=king_moves()
                            turn*=-1
                            checkmate=True
                            for move in available:
                                if move not in danger:
                                    checkmate=False
                            if checkmate:
                                break
                            check=True
                            print('\nCHECK\n')
                        break

                    else:
                        print('Cannot move there')
                        continue

                    
                        
                if checkmate:
                    print_board()
                    print('\nCHECKMATE\n')
                    break

                if choice=='z':
                    continue
                
                
            else:
                print('Out of range')
                continue
        else:
            print('Out of range')
            continue
    else:
        print('Incorrect format')
        continue

    

    board=round_switch()
    turn*=-1
    print_board()
"""
    
    
