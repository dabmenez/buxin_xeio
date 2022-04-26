from time import gmtime
from PPlay.sprite import Sprite
from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import Mouse
from game import Game
import modos


class Options1(object):
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.easy1 = Sprite("Buttons/EASY1.png")
        self.easy2 = Sprite("Buttons/EASY2.png")
        self.medium1 = Sprite("Buttons/MEDIUM1.png")
        self.medium2 = Sprite("Buttons/MEDIUM2.png")
        self.hard1 = Sprite("Buttons/HARD1.png")
        self.hard2 = Sprite("Buttons/HARD2.png")
        self.fundo2 = Sprite("Imagens/fundo2.jpg")
        self.mouse = Mouse()

    def set_pos(self):
        self.easy1.set_position(self.janela.width/2 - 45, self.janela.height/2 - 160)
        self.easy2.set_position(self.janela.width/2 - 45, self.janela.height/2 - 160)
        self.medium1.set_position(self.janela.width/2 - self.medium1.width/2 + 25, self.janela.height/2 - 10)
        self.medium2.set_position(self.janela.width/2 - self.medium1.width/2 + 25, self.janela.height/2 - 10)
        self.hard1.set_position(self.janela.width/2 - 45, self.janela.height/2 + self.easy1.height + self.medium1.height + 55)
        self.hard2.set_position(self.janela.width/2 - 45, self.janela.height/2 + self.easy1.height + self.medium1.height + 55)

    def _draw(self):
        self.fundo2.draw()
        self.easy1.draw()
        self.medium1.draw() 
        self.hard1.draw()       

    def Dificuldade(self):
        dificuldade = 0
        if(self.mouse.is_over_object(self.easy2)):
            if(self.mouse.is_button_pressed(1)):
                dificuldade = 1
        elif(self.mouse.is_over_object(self.medium2)):
            if(self.mouse.is_button_pressed(1)):
                dificuldade = 2
        elif(self.mouse.is_over_object(self.hard2)):
            if(self.mouse.is_button_pressed(1)):
                dificuldade = 3
        
        return dificuldade

    
    def run(self):
        self._draw()
        self.set_pos()
        modos.dificuldade = self.Dificuldade()
        if modos.dificuldade == 1:
            modos.modo = 1
            modos.texto = 'Easy'
        if modos.dificuldade == 2:
            modos.modo = 1 
            modos.texto = 'Medium' 
        if modos.dificuldade == 3:
            modos.modo = 1
            modos.texto = 'Hard'
        
        if(self.mouse.is_over_object(self.easy1)):
            self.easy2.draw() 
            
        if(self.mouse.is_over_object(self.medium1)):
            self.medium2.draw() 
                
        if(self.mouse.is_over_object(self.hard1)):
            self.hard2.draw()
            
        if(self.teclado.key_pressed("ESC")):
            modos.modo = 0
