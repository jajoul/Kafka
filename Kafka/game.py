import turtle
import time
import sounds
from images import random_image
import cohere
from tkinter import messagebox,Button
import os
#from images import Image
PLAYER_SIZE=1
SCREEN_WIDTH=500
SCREEN_HEIGHT=500
ENEMY_SIZE=0.5
COLLISION_THRESHOLD = PLAYER_SIZE + ENEMY_SIZE
NEAR_THRESHOLD=30
import random
class Game:
    def __init__(self):
        turtle.tracer(0)
        #Screen
        self.screen=turtle.Screen()
        self.screen.setup(width=1.0,height=1.0)
        turtle.title(titlestring='Kafka')
        turtle.bgcolor('black')
        #Player
        self.player=turtle.Turtle()
        self.player.hideturtle()
        self.player.shape(name='square')
        
        self.player.shapesize(stretch_len=PLAYER_SIZE,stretch_wid=PLAYER_SIZE,outline=0)
        self.player.penup()
        self.player.color('white')
        self.player.goto(
            x=-(SCREEN_WIDTH/2)+(PLAYER_SIZE*10),
            y=(SCREEN_HEIGHT/2)-(PLAYER_SIZE*10)
            )
        self.player.showturtle()
        #Border
        self.border=turtle.Turtle()
        self.border.color('white')
        self.border.hideturtle()
        self.border.penup()
        self.border.goto(x=-(SCREEN_WIDTH/2),y=SCREEN_HEIGHT/2)
        self.border.pendown()
        self.border.goto(x=SCREEN_WIDTH//2,y=SCREEN_HEIGHT//2)
        self.border.goto(x=SCREEN_WIDTH//2,y=-SCREEN_HEIGHT//2)
        self.border.goto(x=-SCREEN_WIDTH//2,y=-SCREEN_HEIGHT//2)
        self.border.goto(x=-(SCREEN_WIDTH/2),y=SCREEN_HEIGHT/2)
        #ai api
        self.co=cohere.ClientV2(api_key=os.environ['COHERE_API'])
        #hint button
        """ self.hint_btn=turtle.Turtle()
        self.hint_btn.color('red')
        self.hint_btn.penup()
        self.hint_btn.goto(x=-400,y=100)
        self.hint_btn.write("Hint from AI",move=True,font=('Arial',12,'bold'))
        self.hint_btn.onclick(fun=self.ai_hint) """
        canvas=self.screen.getcanvas()
        self.hint_btn=Button(canvas.master,text='Hint from AI',command=self.ai_hint)
        self.hint_btn.pack()
        self.hint_btn.place(x=10,y=10)
        

        #Enemy
        self.enemies=[]
        for enemy in range(25):
            enemy=turtle.Turtle()
            enemy.shape(name='square')
            enemy.shapesize(stretch_wid=ENEMY_SIZE,stretch_len=ENEMY_SIZE,outline=0)
            enemy.penup()
            enemy.goto(x=random.randint(-(SCREEN_WIDTH//2),(SCREEN_WIDTH//2)),y=random.randint(-(SCREEN_HEIGHT//2),SCREEN_HEIGHT//2))
            enemy.color('red')
            enemy.hideturtle()
            self.enemies.append(enemy)
        """ self.rand_img=random_image()
        self.screen.addshape(self.rand_img)
        self.jumpscare_image=turtle.Turtle()
        self.jumpscare_image.shape(self.rand_img)
        self.jumpscare_image.penup()
        self.jumpscare_image.hideturtle() """
        self.screen.update()
        print('done')

    def move_right(self):
        self.player.setheading(0)
        self.player.forward(5)
        self.check_collision()
        self.screen.update()
    def move_up(self):
        self.player.setheading(90)
        self.player.forward(5)
        self.check_collision()
        self.screen.update()
    def move_down(self):
        self.player.setheading(270)
        self.player.forward(5)
        self.check_collision()
        
        self.screen.update()
    def move_left(self):
        self.player.setheading(180)
        self.player.forward(5)
        self.check_collision()
        self.screen.update()
    def check_collision(self):
        self.is_visible=False
        for enemy in self.enemies:
            if self.player.distance(enemy) < COLLISION_THRESHOLD * 10:
                print('Hit')
                sounds.scream_sound()
                enemy.showturtle()
                self.is_visible=True
                random_image()
                
                self.screen.update()
            elif self.player.distance(enemy)< NEAR_THRESHOLD and self.is_visible==False:
                sounds.door_sound()
                
    def ai_hint(self):
        enemy_positions=[]
        for pos in self.enemies:
            enemy_positions.append(pos.pos())
        system_message=f'player will give you his position and enemies pos are {enemy_positions}. guide the player.be helpful and summerize the soloution in one sentense.the playground is 500 * 500.'
        response=self.co.chat(
            model='command-r-plus-08-2024',
            messages=[
                {
                    "role":"system","content":system_message
                },
                {
                    'role':'user',
                    'content':f'Player position is in {self.player.pos()} give me hints to avoid enemies'
                }

            ]
        )       
        #print(response)
        text=response.message.content[0].text
        print(text)
        messagebox.showinfo('Hint from AI:',text)

                 
    def run(self):
        
        sounds.background_sound()
        sounds.whisper_sound()
        
        self.screen.onkeypress(fun=self.move_right,key='Right')
        self.screen.onkeypress(fun=self.move_down,key='Down')
        self.screen.onkeypress(fun=self.move_up,key='Up')
        self.screen.onkeypress(fun=self.move_left,key='Left')
        


        self.screen.listen()
        turtle.done()