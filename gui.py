import pygame, sys
from threading import Thread

class Window():
    def __init__(self, CPU):
        self.win = pygame.display.set_mode((1000, 1000))
        self.cpu = CPU


    def Start(self):
        self.Loop()

    def Decode_Click(self, pos):
        # Temp
        self.cpu.Interupt = True

    def Loop(self):
        # Setup
        GUI_Image = pygame.transform.scale2x(pygame.image.load("gui/gui.png"))

        # Loop
        while True:
            self.win.blit(GUI_Image, (0,-150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("EXIT")
                    sys.exit("Closed GUI")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Mouse_Position = pygame.mouse.get_pos()
                    self.Decode_Click(Mouse_Position)


            pygame.display.flip()

def Boot(CPU):
    print("Loading gui")
    Win = Window(CPU)
    x = Thread(target=Win.Loop)
    x.daemon = True
    x.start()


if __name__ == "__main__":
    def t(): pass
    Boot(t)