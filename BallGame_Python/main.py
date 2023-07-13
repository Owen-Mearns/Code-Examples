#Author: Owen Mearns
#Purpose: Make a simple game in Pygames with a ball and a block.


import pygame
from text import Text
from ball import Ball
from block import Block

def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('CS 172 Game')
    fpsclock = pygame.time.Clock()


    gameSurfaceWidth = 600
    gameSurfaceHeight = 600
    gameSurfaceColor = (240, 240, 240)
    gameSurface = pygame.display.set_mode((gameSurfaceWidth, gameSurfaceHeight))


    groundHeight = 500


    ballSize = 12
    xPos = 30
    yPos = groundHeight-ballSize
    xv = 0 
    yv = 0 
    ball = Ball(xPos, yPos, ballSize, (255, 0, 0))
    ballIsMoving = False


    numBlocks = 9 
    blockColor = (20, 20, 255)
    blockSize = 30
    blocks = []

    for r in range(0, 3):
        for c in range(1, 4):
            blocks.append(Block(400 + r * blockSize, groundHeight - c * blockSize, blockSize, blockColor))
    
    score = 0
    scoreString = 'Score: {}'
    scoreText = Text(0, 0, scoreString.format(score))
    hiScore = 0
    hiScoreString = 'High Score: {}'
    hiScoreText = Text(350, 0, hiScoreString.format(hiScore))


    dt = .1
    g = 6.67
    R = .7
    eta = .5


    gameOver = False
    waitingForNewGame = False

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()

        if not gameOver:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDownPos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            
            mouseUpPos = pygame.mouse.get_pos()

            xv = mouseUpPos[0] - mouseDownPos[0]
            yv = mouseUpPos[1] - mouseDownPos[1]
            ballIsMoving = True
            gameOver = True

        if waitingForNewGame:
            if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_y):


                score = 0


                gameOver = False
                waitingForNewGame = False


                ballIsMoving = False
                ball.setPosition((30, groundHeight - ballSize))
                xPos, yPos = ball.getPosition()


                for block in blocks:
                    block.setVisible(True)

            elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_n:
                pygame.quit()
                exit()

    if ballIsMoving:

        if yPos > groundHeight-(ballSize): 
            yv = -R * yv
            xv = eta * xv
            yPos = groundHeight-(ballSize) 
            xPos += dt * xv

        else:
            yv = yv + g * dt
            yPos += dt * yv
            xPos += dt * xv


        if yv < 0.0001 and xv < 0.0001:
            ballIsMoving = False

        if (not (0 < xPos < gameSurfaceWidth)) or (not (0 < yPos < gameSurfaceHeight)):
            ballIsMoving = False


        ball.setPosition((int(xPos), int(yPos)))


    for block in blocks:
        if intersect(block.getRect(), ball.getRect()):
            if block.getVisible():
                score += 1
                if score >= hiScore:
                    hiScore = score
            block.setVisible(False)



    gameSurface.fill(gameSurfaceColor)
    ground_Line = pygame.draw.line(gameSurface, (0, 0, 0), (0, groundHeight), (gameSurfaceWidth, groundHeight), 3)
    ball.draw(gameSurface)


    for block in blocks:
        block.draw(gameSurface)


    scoreText.setMessage(scoreString.format(score))
    scoreText.draw(gameSurface)

    hiScoreText.setMessage(hiScoreString.format(hiScore))
    hiScoreText.draw(gameSurface)

    if not ballIsMoving and gameOver:
        new_game_string = 'New Game? Press [Y] or [N]'
        new_game_text = Text(90, 150, new_game_string)
        new_game_text.draw(gameSurface)
        waitingForNewGame = True

    pygame.display.update()
    fpsclock.tick(30)