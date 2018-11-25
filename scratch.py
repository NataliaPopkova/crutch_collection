# -*- coding: utf-8 -*-
import random
board = list(range(1,10))
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
def take_input(player_token, player_answer):
    if (str(board[player_answer-1]) not in "XO"):
        board[player_answer-1] = player_token
        return True
    else:
        return False
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    print("Чем хотите играть, Х или О ?")
    while True:
        my_symbol = input()
        if (my_symbol in "XO"):
            break
        else:
            print("Вы можете ввести только Х и О, попробуйте еще раз")
    enemy_symbol = "X"
    if (my_symbol == "X"):
        enemy_symbol = "O"
    while not win:
        draw_board(board)
        while True:
            try:
                player_answer = int(input("Куда поставим " + my_symbol+"? "))
                if player_answer >= 1 and player_answer <= 9:
                    take_input(my_symbol, player_answer)
                    break
                else:
                    print("вы не то написали")
            except:
                print("вы не то написали")

        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break

        while True:
            player_answer = random.randint(1, 9)
            if player_answer >= 1 and player_answer <= 9:
                take_input(enemy_symbol, player_answer)
                break

        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)