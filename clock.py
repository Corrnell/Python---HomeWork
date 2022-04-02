import turtle as t

hours   = 10
minutes = 56
seconds = 0
def printTime():


    print( f"{hours:02}:{minutes:02}:{seconds:02}" )
def drawing():
    # Alignment
    t.pensize(2)
    t.circle(100)
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    # -----------------

    # Hour Alignment
    t.right(hours * 30)
    t.pensize(4)
    t.forward(65)
    # ----------------

    # Reseting to default position
    t.left(180)
    t.penup()
    t.forward(65)
    t.right(180-hours * 30)
    t.pendown()
    # ----------------------

    # Minute Alignment
    t.right(minutes * 6)
    t.pensize(3)
    t.forward(75)
    # ---------------------

    # Reseting to default position
    t.left(180)
    t.penup()
    t.forward(75)
    t.right(180-minutes * 6)
    t.pendown()
    # ----------------------

    # Seconds Alignment
    t.right(seconds * 6)
    t.pensize(2)
    t.forward(90)
    # --------------------

    # Reseting to default position
    t.left(180)
    t.penup()
    t.forward(90)
    t.right(180-seconds * 6)
    t.pendown()
    t.pensize(1)
    # ----------------------