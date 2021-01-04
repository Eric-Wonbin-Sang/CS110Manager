# William Parente
# CS-110 Final Project: Tic-Tac-Toe Game
# I pledge my honor I have abided by the Stevens honor system

"""This Program will have the user play a two-player game of Tic-Tac-Toe displayed within a graphics window"""

from graphics import *

win1 = GraphWin("Tic-Tac-Toe", 700, 700)


def init_board():               # These four commented blocks initialize the board
    p78 = Point(250, 650)
    p12 = Point(250, 50)

    vline1 = Line(p78, p12)   # Draws left-most vertical line
    vline1.draw(win1)

    p89 = Point(450, 650)
    p23 = Point(450, 50)

    vline2 = Line(p89, p23)   # Draws right-most vertical line
    vline2.draw(win1)

    p74 = Point(50, 250)
    p96 = Point(650, 250)

    hline1 = Line(p74, p96)   # Draws bottom-most horizontal line
    hline1.draw(win1)

    p41 = Point(50, 450)
    p63 = Point(650, 450)

    hline2 = Line(p41, p63)   # Draws top-most line
    hline2.draw(win1)


v1 = Point(50, 50)
v2 = Point(250, 50)
v3 = Point(450, 50)
v4 = Point(650, 50)

v5 = Point(50, 250)
v6 = Point(250, 250)
v7 = Point(450, 250)
v8 = Point(650, 250)

v9 = Point(50, 450)
v10 = Point(250, 450)
v11 = Point(450, 450)
v12 = Point(650, 450)

v13 = Point(50, 650)
v14 = Point(250, 650)
v15 = Point(450, 650)
v16 = Point(650, 650)


def buttons():                      # Defines and returns the 9 rectangles/squares to be used as buttons
    leftup = Rectangle(v1, v6)
    midup = Rectangle(v2, v7)
    rightup = Rectangle(v3, v8)

    leftmid = Rectangle(v5, v10)
    midmid = Rectangle(v6, v11)
    rightmid = Rectangle(v7, v12)

    leftlow = Rectangle(v9, v14)
    midlow = Rectangle(v10, v15)
    rightlow = Rectangle(v11, v16)

    return leftup, midup, rightup, leftmid, midmid, rightmid, leftlow, midlow, rightlow


def button_test(point, rectangle):
    lowleftcorner = rectangle.getP1()
    uprightcorner = rectangle.getP2()

    return lowleftcorner.getX() < point.getX() < uprightcorner.getX() and \
           lowleftcorner.getY() < point.getY() < uprightcorner.getY()


def win_text_x():
    text = Text(Point(350, 350), "Three Xs in a Row! \nPlayer 1 Wins!")
    text.setSize(36)
    text.draw(win1)


def win_text_y():
    text = Text(Point(350, 350), "Three Os in a Row! \nPlayer 2 Wins!")
    text.setSize(36)
    text.draw(win1)


def win_test():                                                     # Tests if any winning arrangement of moves
    if index[0] == 1 and index[1] == 1 and index[2] == 1:           # are present on the board. Any three-in-a-row of
        Line(Point(150, 150), Point(550, 150)).draw(win1)           # like symbols yield a win
        win_text_x()
    elif index[0] == 2 and index[1] == 2 and index[2] == 2:
        Line(Point(150, 150), Point(550, 150)).draw(win1)
        win_text_y()

    elif index[3] == 1 and index[4] == 1 and index[5] == 1:
        Line(Point(150, 350), Point(550, 350)).draw(win1)
        win_text_x()
    elif index[3] == 2 and index[4] == 2 and index[5] == 2:
        Line(Point(150, 350), Point(550, 350)).draw(win1)
        win_text_y()

    elif index[6] == 1 and index[7] == 1 and index[8] == 1:
        Line(Point(150, 550), Point(550, 550)).draw(win1)
        win_text_x()
    elif index[6] == 2 and index[7] == 2 and index[8] == 2:
        Line(Point(150, 550), Point(550, 550)).draw(win1)
        win_text_y()

    elif index[6] == 1 and index[3] == 1 and index[0] == 1:
        Line(Point(150, 550), Point(150, 150)).draw(win1)
        win_text_x()
    elif index[6] == 2 and index[3] == 2 and index[0] == 2:
        Line(Point(150, 550), Point(150, 150)).draw(win1)
        win_text_y()

    elif index[7] == 1 and index[4] == 1 and index[1] == 1:
        Line(Point(350, 550), Point(350, 150)).draw(win1)
        win_text_x()
    elif index[7] == 2 and index[4] == 2 and index[1] == 2:
        Line(Point(350, 550), Point(350, 150)).draw(win1)
        win_text_y()

    elif index[8] == 1 and index[5] == 1 and index[2] == 1:
        Line(Point(550, 550), Point(550, 150)).draw(win1)
        win_text_x()
    elif index[8] == 2 and index[5] == 2 and index[2] == 2:
        Line(Point(550, 550), Point(550, 150)).draw(win1)
        win_text_y()

    elif index[6] == 1 and index[4] == 1 and index[2] == 1:
        Line(Point(150, 550), Point(550, 150)).draw(win1)
        win_text_x()
    elif index[6] == 2 and index[4] == 2 and index[2] == 2:
        Line(Point(150, 550), Point(550, 150)).draw(win1)
        win_text_y()

    elif index[0] == 1 and index[4] == 1 and index[8] == 1:
        Line(Point(150, 150), Point(550, 550)).draw(win1)
        win_text_x()
    elif index[0] == 2 and index[4] == 2 and index[8] == 2:
        Line(Point(150, 150), Point(550, 550)).draw(win1)
        win_text_y()


def draw_x(topleft, botright, botleft, topright):   # Defines lines to be drawn as X's on the board
    Line(topleft, botright).draw(win1)
    Line(topright, botleft).draw(win1)


def draw_circ(center):                  # Defines circles to be drawn on the board
    Circle(center, 50).draw(win1)


init_board()

leftup, midup, rightup, leftmid, midmid, \
rightmid, leftlow, midlow, rightlow = buttons()    # Transition rectangles from local to global variables

index = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 0                                        # Initializes various variables to be used as conditions
used = 0

while True:
    clicked_point = win1.getMouse()

    if index[0] != 0:           # If the space has already been played, it will not be played again
        pass
    elif button_test(clicked_point, leftup):
        if turn == 0:
            draw_x(Point(100, 200), Point(200, 100), Point(100, 100), Point(200, 200))
            turn = 1
            index[0] = 1
        else:
            turn = 0
            draw_circ(Point(150, 150))
            index[0] = 2
        win_test()

    if index[1] != 0:
        pass
    elif button_test(clicked_point, midup):
        if turn == 0:
            draw_x(Point(300, 200), Point(400, 100), Point(300, 100), Point(400, 200))
            turn = 1
            index[1] = 1
        else:
            turn = 0
            draw_circ(Point(350, 150))
            index[1] = 2
        win_test()

    if index[2] != 0:
        pass
    elif button_test(clicked_point, rightup):
        if turn == 0:
            draw_x(Point(500, 200), Point(600, 100), Point(500, 100), Point(600, 200))
            turn = 1
            index[2] = 1
        else:
            turn = 0
            draw_circ(Point(550, 150))
            index[2] = 2
        win_test()

    if index[3] != 0:
        pass
    elif button_test(clicked_point, leftmid):
        if turn == 0:
            draw_x(Point(100, 400), Point(200, 300), Point(100, 300), Point(200, 400))
            turn = 1
            index[3] = 1
        else:
            turn = 0
            draw_circ(Point(150, 350))
            index[3] = 2
        win_test()

    if index[4] != 0:
        pass
    elif button_test(clicked_point, midmid):
        if turn == 0:
            draw_x(Point(300, 400), Point(400, 300), Point(300, 300), Point(400, 400))
            turn = 1
            index[4] = 1
        else:
            turn = 0
            draw_circ(Point(350, 350))
            index[4] = 2
        win_test()

    if index[5] != 0:
        pass
    elif button_test(clicked_point, rightmid):
        if turn == 0:
            draw_x(Point(500, 400), Point(600, 300), Point(500, 300), Point(600, 400))
            turn = 1
            index[5] = 1
        else:
            turn = 0
            draw_circ(Point(550, 350))
            index[5] = 2
        win_test()

    if index[6] != 0:
        pass
    elif button_test(clicked_point, leftlow):
        if turn == 0:
            draw_x(Point(100, 600), Point(200, 500), Point(100, 500), Point(200, 600))
            turn = 1
            index[6] = 1
        else:
            turn = 0
            draw_circ(Point(150, 550))
            index[6] = 2
        win_test()

    if index[7] != 0:
        pass
    elif button_test(clicked_point, midlow):
        if turn == 0:
            draw_x(Point(300, 600), Point(400, 500), Point(300, 500), Point(400, 600))
            turn = 1
            index[7] = 1
        else:
            turn = 0
            draw_circ(Point(350, 550))
            index[7] = 2
        win_test()

    if index[8] != 0:
        pass
    elif button_test(clicked_point, rightlow):
        if turn == 0:
            draw_x(Point(500, 600), Point(600, 500), Point(500, 500), Point(600, 600))
            turn = 1
            index[8] = 1
        else:
            turn = 0
            draw_circ(Point(550, 550))
            index[8] = 2
        win_test()

