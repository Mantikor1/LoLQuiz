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

fontQuestionText = pygame.font.SysFont('arial', 24)

pygame.display.set_caption('League of Legends Quiz')

window_icon = pygame.image.load('resources/Aurelion_Sol_Thumbnail.png')

pygame.display.set_icon(window_icon)


class Button():
    def __init__(self, x_pos, y_pos, text, color = None, borderColor = None, 
                 hoverColor = None, textColor = None, height = None, width = None):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__height = height or 50
        self.__width = width or 100
        self.__colorOriginal = color or (149, 0, 179)
        self.__color = self.__colorOriginal
        self.__borderColor = borderColor or (255, 255, 255)
        self.__text = text
        self.__hoverEnable = True
        self.__hoverColor = hoverColor or (184, 38, 214)
        self.__textColor = textColor or (255, 255, 255)
      
        
    def draw(self, surface):
        
        #draw button with border
        pygame.draw.rect(surface, self.__borderColor, (self.__x_pos -2, self.__y_pos -2, self.__width + 4, self.__height + 4))
        pygame.draw.rect(surface, self.__color, (self.__x_pos, self.__y_pos, self.__width, self.__height))
        
        #write text on button (centered)
        write_text = fontMenuText.render(self.__text, True, self.__textColor)
        text_rect = write_text.get_rect(center=(self.__x_pos + self.__width/2, self.__y_pos + 22))
        screen.blit(write_text, text_rect)
        
        if not self.__hoverEnable:
            pygame.draw.line(surface, (205, 190, 145), 
                (self.__x_pos, self.__y_pos + 50), (self.__x_pos + 100, self.__y_pos), width = 3)
    
    def onHover(self, hovered):
        if self.__hoverEnable:
            if hovered:
                self.__color = self.__hoverColor
            else:
                self.__color = self.__colorOriginal
            
            
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
          
        self.__answer1 = Button(370, 280, str(self.__answers[0]), (33, 60, 57), (136, 115, 50), (71, 170, 159), (205, 190, 145))
        self.__answer2 = Button(490, 280, str(self.__answers[1]), (33, 60, 57), (136, 115, 50), (71, 170, 159), (205, 190, 145))
        self.__answer3 = Button(370, 350, str(self.__answers[2]), (33, 60, 57), (136, 115, 50), (71, 170, 159), (205, 190, 145))
        self.__answer4 = Button(490, 350, str(self.__answers[3]), (33, 60, 57), (136, 115, 50), (71, 170, 159), (205, 190, 145))


    def getButtons(self):
        return [self.__answer1, self.__answer2, self.__answer3, self.__answer4]

        
    def draw(self, surface):
        global width, height
        
        #draw the name of the item
        write_text = fontMenuText.render(self.__name, True, (193, 186, 170))
        text_rect = write_text.get_rect(center=(width/2, 95))
        screen.blit(write_text, text_rect)
        
        #draw the question text
        write_text = fontQuestionText.render("How much gold does this", True, (193, 186, 170))
        text_rect = write_text.get_rect(center=(width/2, 215))
        screen.blit(write_text, text_rect)
        
        write_text = fontQuestionText.render("item cost in total?", True, (193, 186, 170))
        text_rect = write_text.get_rect(center=(width/2, 245))
        screen.blit(write_text, text_rect)
        
        pygame.draw.rect(surface, (85, 85, 87), (445, 126, 70, 70))
        screen.blit(self.__image, (448, 129))
        
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


def redrawMenuWindow(surface, gameOver, scoreValue, gameWon, moneyBagImage):
    global width, height, screen
    surface.fill((0, 0, 0))
    screen.blit(menuBackground, (0, 0))
    
    #border rectangle background main menu
    rect1 = pygame.Rect(0, 0, 326, 406)
    rect1.center = (width/2, height/2)
    pygame.draw.rect(screen, (136, 115, 50), rect1)
    
    #rectangle background main menu
    rect2 = pygame.Rect(0, 0, 320, 400)
    rect2.center = (width/2, height/2)
    pygame.draw.rect(screen, (13, 23, 24), rect2)
    
    playButton.draw(surface)
    playButton2.draw(surface)
    quitButton.draw(surface)
    
    screen.blit(moneyBagImage, (595, 153))
    
    #drawing message when game is over or won
    if gameOver:
        write_text = fontMenuText.render("Game over!", True, (193, 186, 170))        
        text_rect = write_text.get_rect(center=(width/2, 60))
        screen.blit(write_text, text_rect)
        write_text = fontMenuText.render("Your Score: {}".format(scoreValue), True, (193, 186, 170))        
        text_rect = write_text.get_rect(center=(width/2, 100))
        screen.blit(write_text, text_rect)
    elif gameWon:
        write_text = fontMenuText.render("You won!", True, (193, 186, 170))
        text_rect = write_text.get_rect(center=(width/2, 60))
        screen.blit(write_text, text_rect)
        write_text = fontMenuText.render("Your Score: {}".format(scoreValue), True, (193, 186, 170))
        text_rect = write_text.get_rect(center=(width/2, 100))
        screen.blit(write_text, text_rect)
   
 
def redrawGameWindow(surface, background, item, scoreValue, lifeValue, 
                     countdown, heartImage, heartDepletedImage, hourglassImage):
    global width, height, screen
    
    surface.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    menuButton.draw(surface)
    
    #border rectangle background question
    #rect = pygame.Rect(0, 0, 406, 406)
    #rect.center = (width/2, 270)
    #pygame.draw.rect(screen, (136, 115, 50), rect)  
    pygame.draw.rect(screen, (136, 115, 50), (252, 67, 456, 366))
    
    #rectangle background question
    #rect = pygame.Rect(0, 0, 400, 400)
    #rect.center = (width/2, 270)
    #pygame.draw.rect(screen, (13, 23, 24), rect)    
    pygame.draw.rect(screen, (13, 23, 24), (255, 70, 450, 360))
    
    #rectangle border score background
    pygame.draw.rect(screen, (136, 115, 50), (547, 0, width - 547, 58))
    
    #rectangle score background
    pygame.draw.rect(screen, (13, 23, 24), (550, 0, width - 550, 55))
    
    #draw the item, lifes, score and countdown
    item.draw(surface)
    displayScore(scoreValue)
    displayLifes(lifeValue, heartImage, heartDepletedImage)
    displayCountdown(countdown)
    screen.blit(hourglassImage, (895, 12))

   
def menu(scoreValue, gameOver, gameWon, moneyBagImage):
    global screen, running, playButton, quitButton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonType = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            if mouseButtonType[0]:
                
                #Mouse x-position
                if 330 <= mousePos[0] <= 630:
                    
                    #Mouse y-position
                   
                    #on click "Play"-Button
                    if 140 <= mousePos[1] <= 190:
                        return False
                    
                    #on click "Quit"-Button
                    if 280 <= mousePos[1] <= 330:
                        running = False
         
                    
        #hovering menu buttons
        mousePos = pygame.mouse.get_pos()
        if 330 <= mousePos[0] <= 630 and 140 <= mousePos[1] <= 190:
            playButton.onHover(True)
        else:
            playButton.onHover(False)
        if 330 <= mousePos[0] <= 630 and 210 <= mousePos[1] <= 260:
            playButton2.onHover(True)
        else:
            playButton2.onHover(False)
        if 330 <= mousePos[0] <= 630 and 280 <= mousePos[1] <= 330:
            quitButton.onHover(True)
        else:
            quitButton.onHover(False)
                
    redrawMenuWindow(screen, gameOver, scoreValue, gameWon, moneyBagImage)
    
    return True
    

def displayScore(scoreValue):
    write_text = fontMenuText.render("Score: {}".format(scoreValue), True, (193, 186, 170))
    screen.blit(write_text, (720, 2))


def displayLifes(lifeValue, heartImage, heartDepletedImage):
    for i in range(lifeValue):       
        screen.blit(heartImage, (560 + i*50, 8))
    for i in range(3 - lifeValue):        
        screen.blit(heartDepletedImage, (660 - i*50, 8))
    
    
def displayCountdown(countdown):
    global width, height
    write_text = fontMenuText.render(str(countdown), True, (193, 186, 170))
    screen.blit(write_text, (925, 2))


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
    elixirOfIronImage = pygame.image.load("resources/Elixir_of_Iron.png").convert_alpha()
    elixirOfSorceryImage = pygame.image.load("resources/Elixir_of_Sorcery.png").convert_alpha()
    elixirOfWrathImage = pygame.image.load("resources/Elixir_of_Wrath.png").convert_alpha()
    healthPotionImage = pygame.image.load("resources/Health_Potion.png").convert_alpha()
    refillablePotionImage = pygame.image.load("resources/Refillable_Potion.png").convert_alpha()
    berserkersImage = pygame.image.load("resources/Berserker's_Greaves.png").convert_alpha()
    bootsImage = pygame.image.load("resources/Boots.png").convert_alpha()
    bootsOfSwiftnessImage = pygame.image.load("resources/Boots_of_Swiftness.png").convert_alpha()
    ionianBootsImage = pygame.image.load("resources/Ionian_Boots_of_Lucidity.png").convert_alpha()
    mercurysImage = pygame.image.load("resources/Mercury's_Treads.png").convert_alpha()
    mobilityBootsImage = pygame.image.load("resources/Mobility_Boots.png").convert_alpha()
    platedSteelcapsImage = pygame.image.load("resources/Plated_Steelcaps.png").convert_alpha()
    sorcerersShoesImage = pygame.image.load("resources/Sorcerer's_Shoes.png").convert_alpha()
    amplifyingTomeImage = pygame.image.load("resources/Amplifying_Tome.png").convert_alpha()
    bfSwordImage = pygame.image.load("resources/B_F_Sword.png").convert_alpha()
    blastingWandImage = pygame.image.load("resources/Blasting_Wand.png").convert_alpha()
    cloakOfAgilityImage = pygame.image.load("resources/Cloak_of_Agility.png").convert_alpha()
    clothArmorImage = pygame.image.load("resources/Cloth_Armor.png").convert_alpha()
    daggerImage = pygame.image.load("resources/Dagger.png").convert_alpha()
    faerieCharmImage = pygame.image.load("resources/Faerie_Charm.png").convert_alpha()
    longSwordImage = pygame.image.load("resources/Long_Sword.png").convert_alpha()
    largeRodImage = pygame.image.load("resources/Needlessly_Large_Rod.png").convert_alpha()
    
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
    elixir_of_iron = Question("Elixir of Iron", elixirOfIronImage, [500, 1000, 700, 400])
    elixir_of_sorcery = Question("Elixir of Sorcery", elixirOfSorceryImage, [500, 1000, 800, 600])
    elixir_of_wrath = Question("Elixir of Wrath", elixirOfWrathImage, [500, 800, 400, 550])
    health_potion = Question("Health Potion", healthPotionImage, [50, 100, 75, 40])
    refillable_potion = Question("Refillable Potion", refillablePotionImage, [150, 50, 500, 250])
    berserkers_greaves = Question("Berserker's Greaves", berserkersImage, [1100, 750, 900, 1000])
    boots = Question("Boots", bootsImage, [300, 500, 550, 700])
    boots_of_swiftness = Question("Boots of Swiftness", bootsOfSwiftnessImage, [900, 1000, 1100, 850])
    ionian_boots_of_lucidity = Question("Ionian Boots of Lucidity", ionianBootsImage, [950, 900, 1000, 1100])
    mercurys_treads = Question("Mercury's Treads", mercurysImage, [1100, 950, 1000, 900])
    mobility_boots = Question("Mobility Boots", mobilityBootsImage, [1000, 950, 1000, 900])
    plated_steelcaps = Question("Plated Steelcaps", platedSteelcapsImage, [1100, 1000, 950, 900])
    sorcerers_shoes = Question("Sorcerer's Shoes", sorcerersShoesImage, [1100, 1000, 950, 900])
    amplifying_tome = Question("Amplifying Tome", amplifyingTomeImage, [435, 375, 500, 465])
    b_f_sword = Question("B. F. Sword", bfSwordImage, [1300, 1000, 875, 1500])
    blasting_wand = Question("Blasting Wand", blastingWandImage, [850, 950, 1075, 1200])
    cloak_of_agility = Question("Cloak of Agility", cloakOfAgilityImage, [600, 750, 550, 875])
    cloth_armor = Question("Cloth Armor", clothArmorImage, [300, 400, 275, 500])
    dagger = Question("Dagger", daggerImage, [300, 310, 400, 385])
    faerie_charm = Question("Faerie Charm", faerieCharmImage, [250, 275, 300, 225])
    long_sword = Question("Long Sword", longSwordImage, [350, 400, 500, 450])
    needlessly_large_rod = Question("Needlessly Large Rod", largeRodImage, [1250, 1500, 1100, 1275])
   
    #Shorter list for playtesting
    #itemList = [elixir_of_iron]
      
    #Full list
    
    itemList = [liandrys_anguish, morellonomicon, crown_of_the_shattered_queen,
                divine_sunderer, duskblade_of_draktharr, eclipse, evenshroud,
                everfrost, frostfire_gauntlet, galeforce, cull, dark_seal, 
                dorans_blade, dorans_ring, dorans_shield, emberknife, hailblade,
                relic, spectral, spellthiefs, steel_shoulderguards, 
                tear_of_the_goddess, control_ward, corrupting_potion,
                elixir_of_iron, elixir_of_sorcery, elixir_of_wrath,
                health_potion, refillable_potion, berserkers_greaves, boots,
                boots_of_swiftness, ionian_boots_of_lucidity, mercurys_treads,
                mobility_boots, plated_steelcaps, sorcerers_shoes,
                amplifying_tome, b_f_sword, blasting_wand, cloak_of_agility,
                cloth_armor, dagger, faerie_charm, long_sword,
                needlessly_large_rod]
    
    return itemList  


def hovering(mousePos, menuButton, questionButtons):
    
    #checking if menu button or one of the question buttons is being hovered
    if 0 <= mousePos[0] <= 100 and 0 <= mousePos[1] <= 50:
        menuButton.onHover(True)
    else:
        menuButton.onHover(False)
    if 370 <= mousePos[0] <= 470 and 280 <= mousePos[1] <= 330:
        questionButtons[0].onHover(True)
    else:
        questionButtons[0].onHover(False)
    if 490 <= mousePos[0] <= 590 and 280 <= mousePos[1] <= 330:
        questionButtons[1].onHover(True)
    else:
        questionButtons[1].onHover(False)
    if 370 <= mousePos[0] <= 470 and 350 <= mousePos[1] <= 400:
        questionButtons[2].onHover(True)
    else:
        questionButtons[2].onHover(False)
    if 490 <= mousePos[0] <= 590 and 350 <= mousePos[1] <= 400:
        questionButtons[3].onHover(True)
    else:
        questionButtons[3].onHover(False)
    
       
def main():
    global width, height, playButton, playButton2, screen, quitButton, running, menuButton, background, menuBackground
    running = True
    
    #setting screen-size
    width = 960
    height = 478
    screen = pygame.display.set_mode((width, height))
    
    #load background images
    background = pygame.image.load('resources/backgroundResized.png').convert_alpha()
    menuBackground = pygame.image.load('resources/menuBackgroundResized.png').convert_alpha()
    
    #load heart images
    heartImage = pygame.image.load("resources/heart.png").convert_alpha()
    heartImage = pygame.transform.scale(heartImage, (40, 40))
    heartDepletedImage = pygame.image.load("resources/heartDepleted.png").convert_alpha()
    heartDepletedImage = pygame.transform.scale(heartDepletedImage, (40, 40))
    
    #load and resize money image
    moneyBagImage = pygame.image.load("resources/money-bag.png").convert_alpha()
    moneyBagImage = pygame.transform.scale(moneyBagImage, (26, 26))
    
    #load and resize clock image
    hourglassImage = pygame.image.load("resources/hourglass.png").convert_alpha()
    hourglassImage = pygame.transform.scale(hourglassImage, (26, 26))
    
    #menu buttons
    buttonX = 330
    buttonWidth = 300 
    
    #play gold quiz button  
    playButton = Button(buttonX, 140, 'Play Gold Quiz', (33, 60, 57), (136, 115, 50), (71, 170, 159), (127, 118, 87), 50, buttonWidth)
    
    #play build quiz button
    playButton2 = Button(buttonX, 210, 'Play Build Quiz', (33, 60, 57), (136, 115, 50), (71, 170, 159), (127, 118, 87), 50, buttonWidth)
   
    #quitButton
    quitButton = Button(buttonX, 280, 'Quit', (33, 60, 57), (136, 115, 50), (71, 170, 159), (127, 118, 87), 50, buttonWidth)
    
    menuButton = Button(0, 0, 'Menu', (33, 60, 57), (136, 115, 50), (71, 170, 159), (127, 118, 87))
    
    #loading items and setting default values
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
            menuOpen = menu(scoreValue, gameOver, gameWon, moneyBagImage)
            if not menuOpen:
                scoreValue = 0
                lifeValue = 3
                gameOver = False
                gameWon = False
                countdown = 5
                
                #timer can be disabled for testing purposes
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
                        
            redrawGameWindow(screen, background, randomItem, scoreValue, 
                             lifeValue, countdown, heartImage, 
                             heartDepletedImage, hourglassImage)
                       
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
                        if 370 <= mousePos[0] <= 470 and 280 <= mousePos[1] <= 330:
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
                                
                        if 490 <= mousePos[0] <= 590 and 280 <= mousePos[1] <= 330:
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
                                
                        if 370 <= mousePos[0] <= 470 and 350 <= mousePos[1] <= 400:
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
                                
                        if 490 <= mousePos[0] <= 590 and 350 <= mousePos[1] <= 400:
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