import pgzrun
import time
WIDTH = 600
HEIGHT = 450



welcome = Rect(90,5,485,50)
question = Rect(20,60,470,50)
answers1 = Rect(20,125,250,130)
answers2 = Rect(320,125,250,130)
answers3 = Rect(20,270,250,130)
answers4 = Rect(320,270,250,130)
timer = Rect(500,65,45,40)
skip = Rect(550,65,45,40)
score = 0
G_over = False
game_over_time = False
gameover = False

time_limit = 10
questions = []

answers = [answers1,answers2,answers3,answers4]

def draw():
    screen.draw.filled_rect(welcome,"black")
    screen.draw.filled_rect(question,"white")
    i = 1
    for ans in answers:
       screen.draw.filled_rect(ans,"light blue")
       screen.draw.textbox(readnext1[i],ans,color = "dark blue")
       i = i + 1
    screen.draw.filled_rect(skip,"lime green")
    screen.draw.filled_rect(timer,"blue")
    screen.draw.textbox("Welcome to our Quiz!",welcome,color = "light blue")
    screen.draw.textbox(readnext1[0],question,color = "green")
    screen.draw.textbox("SKIP",skip,color = "black")
    screen.draw.textbox(str(time_limit),timer,color = "white")

def read():
    global add
    global summm
    global questions
    questionsss = open("Quiz Game/Questions.txt", "r")
    for que in questionsss:
        questions.append(que)
    questionsss.close()
    print(questions)

def welcome_left():
    welcome.x = welcome.x - 3
    if welcome.x < -485:
        welcome.x = 590


read()
def on_mouse_down(pos):
    global time_limit
    global readnext1
    box = 1
    for ans in answers:
        if ans.collidepoint(pos):
                if gameover == False and game_over_time == False and G_over == False:
                  if box == int(readnext1[5]):
                      correct()
                  else:
                      wrong()
        box = box + 1
    if skip.collidepoint(pos):
        if questions:
          readnext1 = readnext()
          time_limit = 10
        else:
            finish()



def correct():
    global readnext1
    global time_limit
    global score
    score = score + 1
    if questions:
       readnext1 = readnext()
       time_limit = 10
    else:
        finish()
def finish():
    global gameover
    global score
    global readnext1 
    gameover = True
    readnext1 = ["You Finished!","Your score:",str(score),"-","-","afs"]

def wrong():
   global G_over
   global readnext1
   global time_limit
   G_over = True
   readnext1 = ["Incorrect!","Your score:",str(score),"-","-","afs"]
   time_limit = 0

def timesup():
   global game_over_time
   global readnext1
   game_over_time = True
   if G_over == False:
      readnext1 = ["Time's up!","Your score:",str(score),"-","-","afs"]    

def timeleft():
    global time_limit
    if questions:
      if time_limit:
        time_limit = time_limit -1
      if time_limit == 0:
          timesup()

def update():
      if gameover == False and game_over_time == False and G_over == False:       
        welcome_left()

    

clock.schedule_interval(timeleft,1)
 
def readnext():
    return questions.pop(0).split(",")
readnext1 = readnext()
print(readnext1)


    



pgzrun.go()