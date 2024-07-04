from settings import *
from textRenderer import renderText

class Button():
    def __init__(self, action) -> None:
        self.action = action
        self.state = "active"
        #self.rect = pygame.Rect(pos[0]-size[0]/2, pos[1]-size[1]/2, size[0], size[1])
    
    def _checkState(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()): self.state = "hover"
        else: self.state = "active"
    
    def updateDraw(self, window, pos:list, size:list, rotated = False):
        self.rect = pygame.Rect(pos[0]-size[0]/2, pos[1]-size[1]/2, size[0], size[1])
        self._checkState()
        if self.state == "hover": colour = BUTTON_HOVER_COL
        elif self.state == "active": colour = BUTTON_ACTIVE_COL
        
        pygame.draw.rect(window, colour, self.rect, 0, 10)
        pygame.draw.rect(window, BLACK, self.rect, 1, 10)
        
        renderText(window, self.rect.center, BUTTON_ACTIONS[self.action], int(self.rect.height*0.6))