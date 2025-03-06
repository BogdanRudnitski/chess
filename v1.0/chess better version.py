#need to check if en passant threatens king


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
Brook1=piece('Br', 'rook', 'B', 'v1.0/pieces/black rook.png')
Brook2=piece('Br', 'rook', 'B', 'v1.0/pieces/black rook.png')
Bbishop=piece('Bb', 'bishop', 'B', 'v1.0/pieces/black bishop.png')
Bknight=piece('Bk', 'knight', 'B', 'v1.0/pieces/black knight.png')
Bqueen=piece('Bq', 'queen', 'B', 'v1.0/pieces/black queen.png')
Bking=piece('BK', 'king', 'B', 'v1.0/pieces/black king.png')
Wpawn=piece('Wp', 'pawn', 'W', 'v1.0/pieces/white pawn.png')
Wrook1=piece('Wr', 'rook', 'W', 'v1.0/pieces/white rook.png')
Wrook2=piece('Wr', 'rook', 'W', 'v1.0/pieces/white rook.png')
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
    row1[0]=Brook1
    row1[7]=Brook2
    row1[1]=Bknight
    row1[6]=Bknight
    row1[2]=Bbishop
    row1[5]=Bbishop
    row1[3]=Bqueen
    row1[4]=Bking
    
    row8=board[7]
    row8[0]=Wrook1
    row8[7]=Wrook2
    row8[1]=Wknight
    row8[6]=Wknight
    row8[2]=Wbishop
    row8[5]=Wbishop
    row8[3]=Wqueen
    row8[4]=Wking
   
def within_bounds(available,team,y,x):
    if 0<=y<8 and 0<=x<8:
        if board[y][x].team!=team:
            available.append([y,x])
            if board[y][x].team!='':
                return False
            return True,y,x


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
    coeff={'W':-1,'B':1}
    c=coeff[team]
    v=3.5-2.5*c

    if 0<=y+c<8:
        if board[y+c][x].team=='':
            available.append([y+c,x])
    if 0<=y+c<8 and x-1>=0:
        if board[y+c][x-1].team!=team and board[y+c][x-1].team!='':
            available.append([y+c,x-1])
    if 0<=y+c<8 and x+1<8:
        if board[y+c][x+1].team!=team and board[y+c][x+1].team!='':
            available.append([y+c,x+1])
    if y==v and board[y+c][x].team=='' and board[y+2*c][x].team=='':
        available.append([y+2*c,x])

    return available


def knight_moves(y,x):
    team=board[y][x].team
    available=[]
    coeff=[-1,1]
    for c1 in coeff:
        for c2 in coeff:
            within_bounds(available, team, y+c1*2,x+c2*1)  
            within_bounds(available, team, y+c1*1,x+c2*2)
    return available
        

def rook_moves(y,x):
    team=board[y][x].team
    available=[]
    coeff=[-1,1]
    
    for c in coeff:
        a,b=y,x
        while within_bounds(available, team, a+c,x):
            a+=c
        while within_bounds(available, team, y,b+c):
            b+=c

    return available


def bishop_moves(y,x):
    team=board[y][x].team
    available=[]
    coeff=[-1,1]

    for c1 in coeff:
        for c2 in coeff:
            a,b=y,x
            while within_bounds(available, team, a+c1,b+c2):
                a+=c1
                b+=c2

    return available


def king_moves(y,x):
    team=board[y][x].team
    available=[]
    coeff=[-1,1]
    
    for c in coeff:
        a,b=y,x
        if within_bounds(available, team, a+c,x):
            a+=c
        if within_bounds(available, team, y,b+c):
            b+=c
    
    for c1 in coeff:
        for c2 in coeff:
            a,b=y,x
            if within_bounds(available, team, a+c1,b+c2):
                a+=c1
                b+=c2
    
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
        if board[7][x].name=='Bp':
            board[7][x]=Bqueen

def check_castling():
    coords=[]
    threat=get_threat(opp)
    if board[picky][pickx].type=='king' and board[picky][pickx].virgin:
        if board[picky][5].type=='' and board[picky][6].type=='':
            if board[picky][7].type=='rook' and board[picky][7].virgin:
                if [picky,5] not in threat and [picky,6] not in threat:
                    coords.append([picky,7])
        if board[picky][3].type=='' and board[picky][2].type=='' and board[picky][1].type=='':
            if board[picky][0].type=='rook' and board[picky][0].virgin:
                if [picky,3] not in threat and [picky,2] not in threat and [picky,1] not in threat:
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


def draw_menu():
    screen.blit(see_through, (0,0))
    menu_BG=(0,0,0,100)
    pygame.draw.rect(see_through, menu_BG, [0,0,800,800])

def print_board():
    table={1:'white',-1:'grey'}
    n=-1
    width=screen.get_width()
    height=screen.get_height()
    mouse=get_mouse()
    
    
    for x in range(8):
        n*=-1
        for y in range(8):
            
            if x*width/8 <= mouse[0] <= (x+1)*width/8 and y*height/8 <= mouse[1] <= (y+1)*height/8:
                if pick:
                    color='orange'
                else:
                    color='yellow'
        
            elif pick:

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

    if menu:
        draw_menu()



def get_threat(team):

    danger=[]
    for y in range(8):
        for x in range(8):
            if board[y][x].team==team:
                available=moves(y,x)
                danger+=available

    return danger
    

def verify_check(team,opp):

    danger=[]
    for y in range(8):
        for x in range(8):
            if board[y][x].team==team:
                available=moves(y,x)
                danger+=available
            if board[y][x].type=='king' and board[y][x].team==opp:
                kingy,kingx=y,x

    if [kingy,kingx] in danger:
        return True, kingy,kingx

    return False, kingy,kingx


def verify_checkmate():

    for move in moves(kingy,kingx):
        if move not in get_threat(team):
            return False

    for y in range(8):
        for x in range(8):
            danger=[]
            if board[y][x].team==opp and board[y][x].type!='king':

                
                for move in moves(y,x):
                    danger=[]
                    tryy,tryx=move[0],move[1]

                    ram.append(board[tryy][tryx])
                    board[tryy][tryx]=board[y][x]
                    board[y][x]=empty

                    nope=verify_check(team,opp)

                    board[y][x]=board[tryy][tryx]
                    board[tryy][tryx]=ram.pop()

                    if nope[0]:
                        continue

                    return False

    return True

def filtered_available(y,x):
    
    available=moves(y,x)
    cannot=[]

    for potential in available:
        checky=potential[0]
        checkx=potential[1]

        ram.append(board[checky][checkx])

        board[checky][checkx]=board[y][x]
        board[y][x]=empty
        
        
        if verify_check(opp,team)[0]:
            cannot.append(potential)
        
        
        board[y][x]=board[checky][checkx]
        board[checky][checkx]=ram.pop()

    for possible in cannot:
        available.remove(possible)

    return available


def get_mouse():
    mouse=pygame.mouse.get_pos()
    if menu or checkmate:
        return [-1000,-1000]
    return mouse
    
    
board_reset()





res=(800,800)
screen=pygame.display.set_mode(res)
see_through=pygame.Surface((800,800), pygame.SRCALPHA)
pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Calibri', 100)
checkmate_mess=my_font.render('CHECKMATE',False,'red')
check_mess=my_font.render('CHECK',False,'blue')



if __name__ == "__main__":

    
    
    
    menu=False
    available=[]
    checked=False
    check=False
    checkmate=False
    pick=False
    running=True
    castling=[]
    passing=[]
    en_passant_opportunity=False
    

    while running:
        
        team=table[turn]
        opp=table[turn*-1]
        
        print_board()
        if checkmate:
            screen.blit(checkmate_mess, (90,345))
        elif check:
            screen.blit(check_mess, (230,345))
        pygame.display.flip()
        
        if pick:
            if not checked:
                available=filtered_available(y,x)
                checked=True

        for ev in pygame.event.get():

            if ev.type==pygame.QUIT:
                pygame.quit()
                running=False

            if ev.type==pygame.KEYDOWN:
                if ev.key==pygame.K_z and not pick:
                    if memory:
                        print('HEY')
                        z=memory.pop()
                        board=z[0]
                        en_passant_opportunity=z[1]
                        checkmate,check=False,False
                        turn*=-1
                    else:
                        print('ALREADY AT BEGGINING')

                if ev.key==pygame.K_ESCAPE:
                    if menu:
                        menu=False
                    else:
                        menu=True

            if ev.type==pygame.MOUSEBUTTONDOWN and (not menu and not checkmate):
                mouse=get_mouse()
                
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
                    checked=False
                    available=[]
                    passing=[]
                    continue
                
            
                
                    
                

                newy=mouse[1]//100
                newx=mouse[0]//100
                move=[newy,newx]    

                if move in castling:
                    memory.append([copy.deepcopy(board), bool(en_passant_opportunity)])
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
                    
                    available=[]
                    pick=False
                    turn*=-1

                if move == passing:
                    memory.append([copy.deepcopy(board), bool(en_passant_opportunity)])
                    board[newy][newx]=board[y][x]
                    board[y][x]=empty
                    board[y][newx]=empty
                    available=[]
                    pick=False
                    turn*=-1

                if move in available:

                    memory.append([copy.deepcopy(board), bool(en_passant_opportunity)])
                    
                   
                    board[newy][newx]=board[y][x]
                    board[y][x]=empty
                    
                    
                    board[newy][newx].virgin=False

                    

                    

                    pawn_to_queen()

                    danger=[]
                    if check:
                        check=False
                    
                    pick=False ####
                    

                    data=verify_check(team,opp)        #CHECK
                    check,kingy,kingx= data[0],data[1],data[2]
                    if check:   
                        checkmate=verify_checkmate()


                    #board=round_switch() ######
                    
                    en_passant_opportunity=False
                    en_passant_opportunity=check_en_passant()
                    if en_passant_opportunity:
                        epy=newy
                        epx=newx

                    
                    available=[]
                    turn*=-1
                    
                

                else:
                    print('Cannot move there')
                    
                checked=False
                castling=[]
                passing=[]
