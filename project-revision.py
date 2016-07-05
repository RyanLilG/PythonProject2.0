from tkinter import *
from random import choice as rc

root = Tk()
root.title("Blackjack")

canvas = Canvas(root,width=1100, height=843)
canvas.grid()

import tkinter as tk

photo1 = PhotoImage(file="pictures/fond_projet.png")
photo2 = PhotoImage(file="pictures/blackjack_logo.png")
photo5 = PhotoImage(file="pictures/signature.png")
photo7 = PhotoImage(file="pictures/back.png")
photo8 = PhotoImage(file="pictures/back.png")
photo9 = PhotoImage(file="pictures/jeton1.png")
photo10 = PhotoImage(file="pictures/jeton5.png")
photo11 = PhotoImage(file="pictures/jeton25.png")
photo12 = PhotoImage(file="pictures/jeton50.png")
photo13 = PhotoImage(file="pictures/jeton100.png")
photo14 = PhotoImage(file="pictures/jeton500.png")
photo15 = PhotoImage(file="pictures/jeton1000.png")
photo16 = PhotoImage(file="pictures/jeton5000.png")
photo17 = PhotoImage(file="pictures/jeton10000.png")
photo18 = PhotoImage(file="pictures/double.png")
photo19 = PhotoImage(file="pictures/hit.png")
photo20 = PhotoImage(file="pictures/stand.png")
photo21 = PhotoImage(file="pictures/highscore.png")
photo22 = PhotoImage(file="pictures/croix.png")
photo23 = PhotoImage(file="pictures/doscarte.png")
photo24 = PhotoImage(file="pictures/yourmoney.png")
photo25 = PhotoImage(file="pictures/blackjack_logo_play.png")
photo29 = PhotoImage(file="pictures/play_card.png")
photo30 = PhotoImage(file="pictures/you_lose.png")
photo31 = PhotoImage(file="pictures/you_win.png")




tr_A = PhotoImage(file="pictures/A_tr.png")
tr_2 = PhotoImage(file="pictures/2_tr.png")
tr_3 = PhotoImage(file="pictures/3_tr.png")
tr_4 = PhotoImage(file="pictures/4_tr.png")
tr_5 = PhotoImage(file="pictures/5_tr.png")
tr_6 = PhotoImage(file="pictures/6_tr.png")
tr_7 = PhotoImage(file="pictures/7_tr.png")
tr_8 = PhotoImage(file="pictures/8_tr.png")
tr_9 = PhotoImage(file="pictures/9_tr.png")
tr_10 = PhotoImage(file="pictures/10_tr.png")
tr_J = PhotoImage(file="pictures/J_tr.png")
tr_Q = PhotoImage(file="pictures/Q_tr.png")
tr_K = PhotoImage(file="pictures/K_tr.png")

pi_A = PhotoImage(file="pictures/A_pi.png")
pi_2 = PhotoImage(file="pictures/2_pi.png")
pi_3 = PhotoImage(file="pictures/3_pi.png")
pi_4 = PhotoImage(file="pictures/4_pi.png")
pi_5 = PhotoImage(file="pictures/5_pi.png")
pi_6 = PhotoImage(file="pictures/6_pi.png")
pi_7 = PhotoImage(file="pictures/7_pi.png")
pi_8 = PhotoImage(file="pictures/8_pi.png")
pi_9 = PhotoImage(file="pictures/9_pi.png")
pi_10 = PhotoImage(file="pictures/10_pi.png")
pi_J = PhotoImage(file="pictures/J_pi.png")
pi_Q = PhotoImage(file="pictures/Q_pi.png")
pi_K = PhotoImage(file="pictures/K_pi.png")

co_A = PhotoImage(file="pictures/A_co.png")
co_2 = PhotoImage(file="pictures/2_co.png")
co_3 = PhotoImage(file="pictures/3_co.png")
co_4 = PhotoImage(file="pictures/4_co.png")
co_5 = PhotoImage(file="pictures/5_co.png")
co_6 = PhotoImage(file="pictures/6_co.png")
co_7 = PhotoImage(file="pictures/7_co.png")
co_8 = PhotoImage(file="pictures/8_co.png")
co_9 = PhotoImage(file="pictures/9_co.png")
co_10 = PhotoImage(file="pictures/10_co.png")
co_J = PhotoImage(file="pictures/J_co.png")
co_Q = PhotoImage(file="pictures/Q_co.png")
co_K = PhotoImage(file="pictures/K_co.png")

ca_A = PhotoImage(file="pictures/A_ca.png")
ca_2 = PhotoImage(file="pictures/2_ca.png")
ca_3 = PhotoImage(file="pictures/3_ca.png")
ca_4 = PhotoImage(file="pictures/4_ca.png")
ca_5 = PhotoImage(file="pictures/5_ca.png")
ca_6 = PhotoImage(file="pictures/6_ca.png")
ca_7 = PhotoImage(file="pictures/7_ca.png")
ca_8 = PhotoImage(file="pictures/8_ca.png")
ca_9 = PhotoImage(file="pictures/9_ca.png")
ca_10 = PhotoImage(file="pictures/10_ca.png")
ca_J = PhotoImage(file="pictures/J_ca.png")
ca_Q = PhotoImage(file="pictures/Q_ca.png")
ca_K = PhotoImage(file="pictures/K_ca.png")







def total(hand):
    # how many aces in the hand
    aces = hand.count(11)
    # to complicate things a little the ace can be 11 or 1
    # this little while loop figures it out for you
    t = sum(hand)
    # you have gone over 21 but there is an ace
    if t > 21 and aces > 0:
        while aces > 0 and t > 21:
            # this will switch the ace from 11 to 1
            t -= 10
            aces -= 1
    return t

def hsupdate(money, highscore):  # updates the highscore
    if money > highscore:
        highscore = money
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))
    return highscore

# a suit of cards in blackjack assume the following values
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# there are 4 suits per deck and usually several decks
# this way you can assume the cards list to be an unlimited pool
cwin = 0  # computer win counter
pwin = 0  # player win counter







with open("highscore.txt", "r") as file:
    highscore = int(file.readline())  # highscore contains the highscore

with open("save.txt", "r") as file:
    money = int(file.readline())  # money contains the score

with open("bet.txt", "r") as file:
    bet = int(file.readline())


highscore = hsupdate(money, highscore)



bet_done = False
in_game = False
stop_color=False
pbust = False
bjp = False
already_doubled = False
already_stood = False








def print_game():
    canvas.delete("all")

    with open("save.txt", "r") as file:
        money = int(file.readline())

    id1 = canvas.create_image(0, 0, anchor=NW, image=photo1)
    id9 = canvas.create_image(0,763, anchor=NW, image=photo9)
    id10 = canvas.create_image(80,763, anchor=NW, image=photo10)
    id11 = canvas.create_image(160,763, anchor=NW, image=photo11)
    id12 = canvas.create_image(240,763, anchor=NW, image=photo12)
    id13 = canvas.create_image(320,763, anchor=NW, image=photo13)
    id14 = canvas.create_image(400,763, anchor=NW, image=photo14)
    id15 = canvas.create_image(0,683, anchor=NW, image=photo15)
    id16 = canvas.create_image(80,683, anchor=NW, image=photo16)
    id17 = canvas.create_image(160,683, anchor=NW, image=photo17)
    id18 = canvas.create_image(50,600, anchor=NW, image=photo18)
    id19 = canvas.create_image(920,600, anchor=NW, image=photo19)
    id20 = canvas.create_image(920,670, anchor=NW, image=photo20)
    id21 = canvas.create_image(920,20, anchor=NW, image=photo21)
    id22 = canvas.create_image(75,368, anchor=NW, image=photo22)
    id24 = canvas.create_image(600,800, anchor=NW, image=photo24)
    id25 = canvas.create_image(-50,-50, anchor=NW, image=photo25)
    id26 = canvas.create_text(1000, 65, text="$"+str(highscore), font=("Bookman Old Style",18,'bold'), fill="yellow")




print_game()


id23_1 = canvas.create_image(450,50, anchor=NW, image=photo23)
id23_2 = canvas.create_image(490,50, anchor=NW, image=photo23)
id23_3 = canvas.create_image(450,500, anchor=NW, image=photo23)
id23_4 = canvas.create_image(490,500, anchor=NW, image=photo23)

id27 = canvas.create_text(950, 400, text="$"+str(bet), font=("Bookman Old Style",30,'bold','italic'), fill="yellow")
id28 = canvas.create_text(930, 810, text="$"+str(money), font=("Bookman Old Style",20,'bold','italic'), fill="yellow")
id29 = canvas.create_image(500, 390, anchor=NW, image=photo29)

player = []
# draw 2 cards for the player to start
player.append(rc(cards))
player.append(rc(cards))
# draw 2 cards for the computer to start
comp = []
comp.append(rc(cards))










def on_click(event):

    x = event.x
    y = event.y




    global id27, id28, id23_1, id23_2,id23_3,id23_4
    global bet_done, in_game, stop_color, pbust, bjp, already_doubled, already_stood
    global A_tr, A_pi, A_co, A_ca
    global player, comp


    tp = total(player)
    tc = total(comp)

    lose = False
    win = False

    with open("bet.txt", "r") as file:
        bet = int(file.readline())
    with open("save.txt", "r") as file:
        money = int(file.readline())



    if not bet_done:

        if money >=0 :
            canvas.delete(id27)
            canvas.delete(id28)

        if money >= 1:
            if x >= 0 and x <= 80 and y >= 763 and y <= 843:#jeton1

                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 1

                with open("bet.txt", "w") as file:
                    file.write(str(bet))

                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 1

                with open("save.txt", "w") as file:
                    file.write(str(money))

                canvas.delete(id28)

        if money >= 5:
            if x >= 81 and x <= 160 and y >= 763 and y <= 843:#jeton5
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 5
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 5
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)

        if money >= 25:
            if x >= 161 and x <= 240 and y >= 763 and y <= 843:#jeton25
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 25
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 25
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 50:
            if x >= 241 and x <= 320 and y >= 763 and y <= 843:#jeton50
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 50
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 50
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 100:
            if x >= 321 and x <= 400 and y >= 763 and y <= 843:#jeton100
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 100
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 100
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 500:
            if x >= 401 and x <= 480 and y >= 763 and y <= 843:#jeton500
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 500
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 500
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 1000:
            if x >= 0 and x <= 80 and y >= 682 and y <= 762:#jeton1000
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 1000
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 1000
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 5000:

            if x >= 81 and x <= 160 and y >= 682 and y <= 762:#jeton5000
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 5000
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 5000
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)


        if money >= 10000:
            if x >= 161 and x <= 240 and y >= 682 and y <= 762:#jeton10000
                with open("bet.txt", "r") as file:
                    bet = int(file.readline())
                bet += 10000
                with open("bet.txt", "w") as file:
                    file.write(str(bet))
                canvas.delete(id27)

                with open("save.txt", "r") as file:
                    money = int(file.readline())
                money -= 10000
                with open("save.txt", "w") as file:
                    file.write(str(money))
                canvas.delete(id28)

        if x >= 75 and x <= 145 and y >= 370 and y <= 440:#cross to delete
            money += bet
            bet=0

            with open("bet.txt", "w") as file:
                file.write(str(bet))
            canvas.delete(id27)

            with open("save.txt", "w") as file:
                file.write(str(money))
            canvas.delete(id28)


    if not in_game:

        player = []
        # draw 2 cards for the player to start
        player.append(rc(cards))
        player.append(rc(cards))
        # draw 2 cards for the computer to start
        comp = []
        comp.append(rc(cards))
        pbust = False  # player busted flag
        cbust = False  # computer busted flag



    if bet > 0:
        if x >= 500 and x <= 650 and y >= 390 and y <= 460:
            bet_done = True
            in_game = True
            canvas.delete(id29)




    if bet_done:
        print(player)
        print(comp)
        canvas.delete(id23_3, id23_4)
        if not stop_color:
            for i in range(len(player)):
                if player[i] == 11:
                    card = rc([tr_A, pi_A, co_A, ca_A])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 2:
                    card = rc([tr_2, pi_2, co_2, ca_2])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 3:
                    card = rc([tr_3, pi_3, co_3, ca_3])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 4:
                    card = rc([tr_4, pi_4, co_4, ca_4])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 5:
                    card = rc([tr_5, pi_5, co_5, ca_5])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 6:
                    card = rc([tr_6, pi_6, co_6, ca_6])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 7:
                    card = rc([tr_7, pi_7, co_7, ca_7])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 8:
                    card = rc([tr_8, pi_8, co_8, ca_8])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 9:
                    card = rc([tr_9, pi_9, co_9, ca_9])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                elif player[i] == 10:
                    card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                    canvas.create_image(450+40*(i), 500, anchor=NW, image=card)

                canvas.delete(id23_1)
                for i in range(len(comp)):
                    if comp[i] == 11:
                        card = rc([tr_A, pi_A, co_A, ca_A])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 2:
                        card = rc([tr_2, pi_2, co_2, ca_2])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 3:
                        card = rc([tr_3, pi_3, co_3, ca_3])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 4:
                        card = rc([tr_4, pi_4, co_4, ca_4])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 5:
                        card = rc([tr_5, pi_5, co_5, ca_5])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 6:
                        card = rc([tr_6, pi_6, co_6, ca_6])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 7:
                        card = rc([tr_7, pi_7, co_7, ca_7])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 8:
                        card = rc([tr_8, pi_8, co_8, ca_8])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 9:
                        card = rc([tr_9, pi_9, co_9, ca_9])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                    elif comp[i] == 10:
                        card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                        canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
            stop_color = True

        if tp == 21:
            win = True

            id31 = canvas.create_image(430,380, anchor=NW, image=photo31)
            money = money + 2*bet
            bet = 0

            with open("bet.txt", "w") as file:
                file.write(str(bet))


            with open("save.txt", "w") as file:
                file.write(str(money))








        if tp < 21:
            if not (already_stood or already_doubled) :
                if x >= 935 and x <= 1010 and y >= 600 and y <= 650:#hit
                    player.append(rc(cards))
                    print(player)

                    for i in range(2,len(player)):
                        if player[i] == 11:
                            card = rc([tr_A, pi_A, co_A, ca_A])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 2:
                            card = rc([tr_2, pi_2, co_2, ca_2])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 3:
                            card = rc([tr_3, pi_3, co_3, ca_3])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 4:
                            card = rc([tr_4, pi_4, co_4, ca_4])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 5:
                            card = rc([tr_5, pi_5, co_5, ca_5])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 6:
                            card = rc([tr_6, pi_6, co_6, ca_6])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 7:
                            card = rc([tr_7, pi_7, co_7, ca_7])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 8:
                            card = rc([tr_8, pi_8, co_8, ca_8])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 9:
                            card = rc([tr_9, pi_9, co_9, ca_9])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 10:
                            card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)

        else:
            lose = True



        if not (already_doubled or already_stood):
            if x >= 50 and x <= 250 and y >= 600 and y <= 650: #double
                if money >= bet:

                    money -= bet
                    bet *= 2

                    with open("bet.txt", "w") as file:
                        file.write(str(bet))
                    canvas.delete(id27)

                    with open("save.txt", "w") as file:
                        file.write(str(money))
                    canvas.delete(id28)

                    print(bet)

                    player.append(rc(cards))
                    for i in range(2,len(player)):
                        if player[i] == 11:
                            card = rc([tr_A, pi_A, co_A, ca_A])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 2:
                            card = rc([tr_2, pi_2, co_2, ca_2])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 3:
                            card = rc([tr_3, pi_3, co_3, ca_3])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 4:
                            card = rc([tr_4, pi_4, co_4, ca_4])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 5:
                            card = rc([tr_5, pi_5, co_5, ca_5])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 6:
                            card = rc([tr_6, pi_6, co_6, ca_6])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 7:
                            card = rc([tr_7, pi_7, co_7, ca_7])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 8:
                            card = rc([tr_8, pi_8, co_8, ca_8])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 9:
                            card = rc([tr_9, pi_9, co_9, ca_9])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)
                        elif player[i] == 10:
                            card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                            canvas.create_image(450+40*(i), 500, anchor=NW, image=card)

                    already_doubled = True

                    canvas.delete(id23_2)
                    while tc<=16 :

                        comp.append(rc(cards))
                        tc = total(comp)
                        for i in range(1,len(comp)):
                            if comp[i] == 11:
                                card = rc([tr_A, pi_A, co_A, ca_A])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 2:
                                card = rc([tr_2, pi_2, co_2, ca_2])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 3:
                                card = rc([tr_3, pi_3, co_3, ca_3])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 4:
                                card = rc([tr_4, pi_4, co_4, ca_4])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 5:
                                card = rc([tr_5, pi_5, co_5, ca_5])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 6:
                                card = rc([tr_6, pi_6, co_6, ca_6])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 7:
                                card = rc([tr_7, pi_7, co_7, ca_7])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 8:
                                card = rc([tr_8, pi_8, co_8, ca_8])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 9:
                                card = rc([tr_9, pi_9, co_9, ca_9])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                            elif comp[i] == 10:
                                card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                                canvas.create_image(450+40*(i), 50, anchor=NW, image=card)



        if not (already_stood or lose) :
            if x >= 935 and x <= 1085 and y >= 675 and y <= 725:#stand

                print(comp)
                canvas.delete(id23_2)
                while tc<=16 :

                    comp.append(rc(cards))
                    tc = total(comp)
                    for i in range(1,len(comp)):
                        if comp[i] == 11:
                            card = rc([tr_A, pi_A, co_A, ca_A])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 2:
                            card = rc([tr_2, pi_2, co_2, ca_2])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 3:
                            card = rc([tr_3, pi_3, co_3, ca_3])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 4:
                            card = rc([tr_4, pi_4, co_4, ca_4])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 5:
                            card = rc([tr_5, pi_5, co_5, ca_5])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 6:
                            card = rc([tr_6, pi_6, co_6, ca_6])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 7:
                            card = rc([tr_7, pi_7, co_7, ca_7])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 8:
                            card = rc([tr_8, pi_8, co_8, ca_8])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 9:
                            card = rc([tr_9, pi_9, co_9, ca_9])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)
                        elif comp[i] == 10:
                            card = rc([tr_10, pi_10, co_10, ca_10, tr_J, pi_J, co_J, ca_J, tr_Q, pi_Q, co_Q, ca_Q, tr_K, pi_K, co_K, ca_K])
                            canvas.create_image(450+40*(i), 50, anchor=NW, image=card)

                    already_stood = True





    id27 = canvas.create_text(950, 400, text="$"+str(bet), font=("Bookman Old Style",30,'bold','italic'), fill="yellow")
    id28 = canvas.create_text(930, 810, text="$"+str(money), font=("Bookman Old Style",20,'bold','italic'), fill="yellow")



    if already_stood or already_doubled:
        tp = total(player)
        tc = total(comp)
        if tp >= tc:
            win = True
        elif (tc > 21 and tp<21) :
            win = True
        elif (tp>21):
            lose = True
        elif (tp<21 and tc>tp and tc<21):
            lose=True

    if lose:
        bet = 0
        with open("bet.txt", "w") as file:
            file.write(str(bet))
        canvas.delete(id27)
        id30 = canvas.create_image(415,380, anchor=NW, image=photo30)


    if win:
        id31 = canvas.create_image(430,380, anchor=NW, image=photo31)
        money = money + 2*bet
        bet = 0

        with open("bet.txt", "w") as file:
            file.write(str(bet))
        canvas.delete(id27)

        with open("save.txt", "w") as file:
            file.write(str(money))
        canvas.delete(id28)






canvas.bind("<Button-1>", on_click)

root.mainloop()