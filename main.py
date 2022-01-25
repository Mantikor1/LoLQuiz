# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:40:36 2022

@author: Jonas Töns
"""

import pygame
import random

pygame.init()


#Resources
fontMenuText = pygame.font.SysFont('arial', 32)

pygame.display.set_caption('League of Legends Quizz')

window_icon = pygame.image.load('resources/Aurelion_Sol_Thumbnail.png')

pygame.display.set_icon(window_icon)


class Button():
    def __init__(self, x_pos, y_pos, text, color = (149, 0, 179), borderColor = (255, 255, 255), hoverEnable = True):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__color = color
        self.__borderColor = borderColor
        self.__text = text
        self.__hoverEnable = hoverEnable
      
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.__borderColor, (self.__x_pos -2, self.__y_pos -2, 104, 54))
        pygame.draw.rect(surface, self.__color, (self.__x_pos, self.__y_pos, 100, 50))
        write_text = fontMenuText.render(self.__text, True, (255, 255, 255))
        screen.blit(write_text, (self.__x_pos + 10, self.__y_pos))
        if not self.__hoverEnable:
            pygame.draw.line(surface, (255, 255, 255), (self.__x_pos, self.__y_pos + 50), (self.__x_pos + 100, self.__y_pos), width = 3)
    
    def onHover(self, hovered):
        if self.__hoverEnable:
            if hovered:
                self.__color = (184, 38, 214)
            else:
                self.__color = (149, 0, 179)
            
            
    def onWrongAnswer(self):
        self.__color = (206, 51, 0)
        self.__hoverEnable = False 

    
    def onCorrectAnswer(self):
        self.__color = (149, 0, 179)
        self.__hoverEnable = True
 
        
    def getText(self):
        return self.__text


class Question():
    def __init__(self, name, image, answers):
        super()
        self.__name = name
        self.__image = image        
        self.__cost = answers[0]
        self.__wrongAnswers = answers[1:]
        self.__answers = random.sample(answers, len(answers))
        
        
        self.__answer1 = Button(330, 250, str(self.__answers[0]))
        self.__answer2 = Button(530, 250, str(self.__answers[1]))
        self.__answer3 = Button(330, 350, str(self.__answers[2]))
        self.__answer4 = Button(530, 350, str(self.__answers[3]))


    def getButtons(self):
        return [self.__answer1, self.__answer2, self.__answer3, self.__answer4]

        
    def draw(self, surface):
        global width, height
        write_text = fontMenuText.render(self.__name, True, (255, 255, 255))
        text_rect = write_text.get_rect(center=(width/2, 70))
        screen.blit(write_text, text_rect)
        write_text = fontMenuText.render("How much gold does this item cost in total?", True, (255, 255, 255))
        text_rect = write_text.get_rect(center=(width/2, 190))
        screen.blit(write_text, text_rect)
        screen.blit(self.__image, (448, 100))
        self.__answer1.draw(surface)
        self.__answer2.draw(surface)
        self.__answer3.draw(surface)
        self.__answer4.draw(surface)


    def answer1clicked(self):
        if self.__answer1.getText() == str(self.__cost):
            return True
        else:
            return False
        
    
    def answer2clicked(self):
        if self.__answer2.getText() == str(self.__cost):
            return True
        else:
            return False
    
    
    def answer3clicked(self):
        if self.__answer3.getText() == str(self.__cost):
            return True
        else:
            return False
    
    
    def answer4clicked(self):
        if self.__answer4.getText() == str(self.__cost):
            return True
        else:
            return False
  
      
def redrawMenuWindow(surface, gameOver, scoreValue, gameWon):
    global width, height, screen
    surface.fill((0, 0, 0))
    screen.blit(menuBackground, (0, 0))
    playButton.draw(surface)
    quitButton.draw(surface)
    if gameOver:
        write_text = fontMenuText.render("Game over!", True, (255, 255, 255))
        screen.blit(write_text, (395, 15))
        write_text = fontMenuText.render("Your highscore was: {}".format(scoreValue), True, (255, 255, 255))
        screen.blit(write_text, (330, 55))
    elif gameWon:
        write_text = fontMenuText.render("You won!", True, (255, 255, 255))
        screen.blit(write_text, (415, 15))
        write_text = fontMenuText.render("Your highscore was: {}".format(scoreValue), True, (255, 255, 255))
        screen.blit(write_text, (330, 55))
   
 
def redrawGameWindow(surface, background, item, scoreValue, lifeValue, countdown, heartImage, heartDepletedImage):
    global width, height, screen
    surface.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    menuButton.draw(surface)
    item.draw(surface)
    displayScore(scoreValue)
    displayLifes(lifeValue, heartImage, heartDepletedImage)
    displayCountdown(countdown)

   
def menu(scoreValue, gameOver, gameWon):
    global screen, running, playButton, quitButton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonType = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            if mouseButtonType[0]:
                
                #Mouse x-position
                if 430 <= mousePos[0] <= 530:
                    
                    #Mouse y-position
                    #"Quit"-Button
                    if 230 <= mousePos[1] <= 280:
                        running = False
                    #"Play"-Button
                    if 130 <= mousePos[1] <= 180:
                        return False
                        
        mousePos = pygame.mouse.get_pos()
        if 430 <= mousePos[0] <= 530 and 130 <= mousePos[1] <= 180:
            playButton.onHover(True)
        else:
            playButton.onHover(False)
        if 430 <= mousePos[0] <= 530 and 230 <= mousePos[1] <= 280:
            quitButton.onHover(True)
        else:
            quitButton.onHover(False)
                
    redrawMenuWindow(screen, gameOver, scoreValue, gameWon)
    return True
    

def displayScore(scoreValue):
    write_text = fontMenuText.render("Score: {}".format(scoreValue), True, (255, 255, 255))
    screen.blit(write_text, (770, 10))


def displayLifes(lifeValue, heartImage, heartDepletedImage):
    #write_text = fontMenuText.render("Lifes: {}".format(lifeValue), True, (255, 255, 255))
    #screen.blit(write_text, (650, 10))
    for i in range(lifeValue):       
        screen.blit(heartImage, (610 + i*50, 13))
    for i in range(3 - lifeValue):        
        screen.blit(heartDepletedImage, (710 - i*50, 13))
    
    
def displayCountdown(countdown):
    global width, height
    write_text = fontMenuText.render(str(countdown), True, (255, 255, 255))
    text_rect = write_text.get_rect(center=(width/2, 325))
    screen.blit(write_text, text_rect)


def loadItems():
    
    #Loading objects
   
    liandrysImage = pygame.image.load("resources/Liandry's_Anguish.png").convert_alpha()
    morellonomiconImage = pygame.image.load("resources/Morellonomicon.png").convert_alpha()
    crownImage = pygame.image.load("resources/Crown.png").convert_alpha()
    divineImage = pygame.image.load("resources/Divine_Sunderer.png").convert_alpha()
    duskbladeImage = pygame.image.load("resources/Duskblade_of_Draktharr.png").convert_alpha()
    eclipseImage = pygame.image.load("resources/Eclipse.png").convert_alpha()
    evenshroudImage = pygame.image.load("resources/Evenshroud.png").convert_alpha()
    everfrostImage = pygame.image.load("resources/Everfrost.png").convert_alpha()
    frostfireImage = pygame.image.load("resources/Frostfire_Gauntlet.png").convert_alpha()
    galeforceImage = pygame.image.load("resources/Galeforce.png").convert_alpha()
    cullImage = pygame.image.load("resources/Cull.png").convert_alpha()
    darkImage = pygame.image.load("resources/Dark_Seal.png").convert_alpha()
    doransBladeImage = pygame.image.load("resources/Doran's_Blade.png").convert_alpha()
    doransRingImage = pygame.image.load("resources/Doran's_Ring.png").convert_alpha()
    doransShieldImage = pygame.image.load("resources/Doran's_Shield.png").convert_alpha()
    emberknifeImage = pygame.image.load("resources/Emberknife.png").convert_alpha()
    hailbladeImage = pygame.image.load("resources/Hailblade.png").convert_alpha()
    relicImage = pygame.image.load("resources/Relic_Shield.png").convert_alpha()
    spectralImage = pygame.image.load("resources/Spectral_Sickle.png").convert_alpha()
    spellthiefsImage = pygame.image.load("resources/Spellthief's_Edge.png").convert_alpha()
    steel_shoulderguardsImage = pygame.image.load("resources/Steel_Shoulderguards.png").convert_alpha()
    tearImage = pygame.image.load("resources/Tear_of_the_Goddess.png").convert_alpha()
    control_wardImage = pygame.image.load("resources/Control_Ward.png").convert_alpha()
    corruptingImage = pygame.image.load("resources/Corrupting_Potion.png").convert_alpha()

    
    liandrys_anguish = Question("Liandry's Anguish", liandrysImage, [3200, 3100, 3400, 3050])
    morellonomicon = Question("Morellonomicon", morellonomiconImage, [2500, 2600, 2700, 2550])
    crown_of_the_shattered_queen = Question("Crown of the Shattered Queen", crownImage, [2800, 2750, 2500, 3000])
    divine_sunderer = Question("Divine Sunderer", divineImage, [3300, 3100, 2800, 3200])
    duskblade_of_draktharr = Question("Duskblade of Draktharr", duskbladeImage, [3100, 3300, 2500, 2700])
    eclipse = Question("Eclipse", eclipseImage, [3100, 3200, 2900, 3050])
    evenshroud = Question("Evenshroud", evenshroudImage, [2500, 3100, 2600, 3000])
    everfrost = Question("Everfrost", everfrostImage, [2800, 3300, 2900, 3200])
    frostfire_gauntlet = Question("Frostfire Gauntlet", frostfireImage, [2800, 2500, 3000, 2600])
    galeforce = Question("Galeforce", galeforceImage, [3400, 3100, 2800, 3200])
    cull = Question("Cull", cullImage, [450, 350, 400, 300])
    dark_seal = Question("Dark Seal", darkImage, [350, 450, 300, 400])
    dorans_blade = Question("Doran's Blade", doransBladeImage, [450, 400, 350, 300])
    dorans_ring = Question("Doran's Ring", doransRingImage, [400, 450, 350, 300])
    dorans_shield = Question("Doran's Shield", doransShieldImage, [450, 350, 400, 300])
    emberknife = Question("Emberknife", emberknifeImage, [350, 400, 450, 300])
    hailblade = Question("Hailblade", hailbladeImage, [350, 300, 400, 450])
    relic = Question("Relic Shield", relicImage, [400, 450, 350, 300])
    spectral = Question("Spectral Sickl", spectralImage, [400, 450, 350, 300])
    spellthiefs = Question("Spellthief's Edge", spellthiefsImage, [400, 450, 350, 300])
    steel_shoulderguards = Question("Steel Shoulderguards", steel_shoulderguardsImage, [400, 450, 350, 300])
    tear_of_the_goddess = Question("Tear of the Goddess", tearImage, [400, 450, 350, 300])
    control_ward = Question("Control Ward", control_wardImage, [75, 50, 25, 100])
    corrupting_potion = Question("Corrupting Potion", corruptingImage, [500, 250, 450, 400])

   
    #Shorter list for playtesting
    #itemList = [liandrys_anguish, morellonomicon]
      
    #Full list
    itemList = [liandrys_anguish, morellonomicon, crown_of_the_shattered_queen,
                divine_sunderer, duskblade_of_draktharr, eclipse, evenshroud,
                everfrost, frostfire_gauntlet, galeforce, cull, dark_seal, 
                dorans_blade, dorans_ring, dorans_shield, emberknife, hailblade,
                relic, spectral, spellthiefs, steel_shoulderguards, 
                tear_of_the_goddess, control_ward, corrupting_potion]
    
    return itemList  


def hovering(mousePos, menuButton, questionButtons):
    if 0 <= mousePos[0] <= 100 and 0 <= mousePos[1] <= 50:
        menuButton.onHover(True)
    else:
        menuButton.onHover(False)
    if 330 <= mousePos[0] <= 430 and 250 <= mousePos[1] <= 300:
        questionButtons[0].onHover(True)
    else:
        questionButtons[0].onHover(False)
    if 530 <= mousePos[0] <= 630 and 250 <= mousePos[1] <= 300:
        questionButtons[1].onHover(True)
    else:
        questionButtons[1].onHover(False)
    if 330 <= mousePos[0] <= 430 and 350 <= mousePos[1] <= 400:
        questionButtons[2].onHover(True)
    else:
        questionButtons[2].onHover(False)
    if 530 <= mousePos[0] <= 630 and 350 <= mousePos[1] <= 400:
        questionButtons[3].onHover(True)
    else:
        questionButtons[3].onHover(False)
    
       
def main():
    global width, height, playButton, screen, quitButton, running, menuButton, background, menuBackground
    running = True
    width = 960
    height = 478
    screen = pygame.display.set_mode((width, height))
    
    background = pygame.image.load('resources/backgroundResized.png').convert_alpha()
    menuBackground = pygame.image.load('resources/menuBackgroundResized.png').convert_alpha()
    
    heartImage = pygame.image.load("resources/heart.png").convert_alpha()
    heartImage = pygame.transform.scale(heartImage, (40, 40))
    heartDepletedImage = pygame.image.load("resources/heartDepleted.png").convert_alpha()
    heartDepletedImage = pygame.transform.scale(heartDepletedImage, (40, 40))
    
    playButton = Button(430, 130, 'Play')
    quitButton = Button(430, 230, 'Quit')
    menuButton = Button(0, 0, 'Menu')
    
    itemList = loadItems()
    newItem = True
    scoreValue = 0
    lifeValue = 3
    gameOver = False
    gameWon = False
    countdown = 5
    
    #Menu open
    menuOpen = True
    
    FPS_CLOCK = pygame.time.Clock()
    
    while running: 
        FPS_CLOCK.tick(30)
        
        if menuOpen or lifeValue < 0 or gameWon or countdown <= 0:
            if lifeValue < 0 or countdown <= 0:
                gameOver = True
            menuOpen = menu(scoreValue, gameOver, gameWon)
            if not menuOpen:
                scoreValue = 0
                lifeValue = 3
                gameOver = False
                gameWon = False
                countdown = 5
                pygame.time.set_timer(pygame.USEREVENT, 1000, loops = 5) 
                itemList = loadItems()
                newItem = True
            
        #Main game loop
        else:
            if newItem and itemList:
                randomItem = random.choice((itemList))
                itemList.remove(randomItem)
                newItem = False
            elif newItem and not itemList:
                gameWon = True
                        
            redrawGameWindow(screen, background, randomItem, scoreValue, lifeValue, countdown, heartImage, heartDepletedImage)
                       
            for event in pygame.event.get():
                questionButtons = randomItem.getButtons()
                
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseButtonType = pygame.mouse.get_pressed()
                    mousePos = pygame.mouse.get_pos()
                    
                    if mouseButtonType[0]:
                        if 0 <= mousePos[0] <= 100 and 0 <= mousePos[1] <= 50:
                            menuOpen = True
                            scoreValue += 10
                        if 330 <= mousePos[0] <= 430 and 250 <= mousePos[1] <= 300:
                            if randomItem.answer1clicked():
                                newItem = True
                                scoreValue += 10
                                countdown = 5
                                pygame.time.set_timer(pygame.USEREVENT, 1000, loops = 5)
                                for i in range(4):
                                    questionButtons[i].onCorrectAnswer()
                            else:
                                lifeValue -= 1
                                questionButtons[0].onWrongAnswer()
                                
                        if 530 <= mousePos[0] <= 630 and 250 <= mousePos[1] <= 300:
                            if randomItem.answer2clicked():
                                newItem = True
                                scoreValue += 10
                                countdown = 5
                                pygame.time.set_timer(pygame.USEREVENT, 1000, loops = 5)
                                for i in range(4):
                                    questionButtons[i].onCorrectAnswer()
                            else:
                                lifeValue -= 1
                                questionButtons[1].onWrongAnswer()
                                
                        if 330 <= mousePos[0] <= 430 and 350 <= mousePos[1] <= 400:
                            if randomItem.answer3clicked():
                                newItem = True
                                scoreValue += 10
                                countdown = 5
                                pygame.time.set_timer(pygame.USEREVENT, 1000, loops = 5)
                                for i in range(4):
                                    questionButtons[i].onCorrectAnswer()
                            else:
                                lifeValue -= 1
                                questionButtons[2].onWrongAnswer()
                                
                        if 530 <= mousePos[0] <= 630 and 350 <= mousePos[1] <= 400:
                            if randomItem.answer4clicked():
                                newItem = True
                                scoreValue += 10
                                countdown = 5
                                pygame.time.set_timer(pygame.USEREVENT, 1000, loops = 5)
                                for i in range(4):
                                    questionButtons[i].onCorrectAnswer()
                            else:
                                lifeValue -= 1 
                                questionButtons[3].onWrongAnswer()
                                
                if event.type == pygame.USEREVENT:
                    countdown -= 1
                
                mousePos = pygame.mouse.get_pos()
                
                hovering(mousePos, menuButton, questionButtons)
 
        pygame.display.update()
        
        
main()
pygame.quit()