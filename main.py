from turtle import *

'''' sprite class ''''
class Sprite(Turtle):
    def __init__(self, x, y, shape, color, step):
        super().__init__()
        self.speed(100)
        self.penup()
        self.goto(x,y)
        self.shape(shape)
        self.color(color)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def set_direction(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        angle = self.towards(x_end, y_end)
        self.setheading(angle)

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_direction(self.x_start, self.y_start, self.x_end, self.y_end)


'''' objects ''''
player = Sprite(0, -100, 'circle', 'orange', 5)

enemy1 = Sprite(-100, 0, 'square', 'red', 5)
enemy1.set_direction(x_start = -200 , y_start = -30, x_end = 200, y_end = -30)

enemy2 = Sprite(100, 0, 'square', 'red', 5)
enemy2.set_direction(x_start = 200, y_start = 30, x_end = -200, y_end = 30)

goal = Sprite(0, 100, 'triangle', 'green', 5)


'''' event controller ''''
screen = player.getscreen()
screen.listen()

screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')
screen.onkey(player.move_left, 'left')
screen.onkey(player.move_right, 'right')


'''' variables '''
total_score = 0

'''' game loop '''
while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()

    if player.is_collide(goal):
        player.goto(0, -100)
        total_score += 1
        print(total_score)
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        break

enemy1.hideturtle()
enemy2.hideturtle()

