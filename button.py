from settings import *

class Button():
    def __init__(self, pos, size, action) -> None:
        self.action = action
        self.state = "active"
        self.rect = pygame.Rect(pos[0]-size[0]/2, pos[1]-size[1]/2, size[0], size[1])
    
    def _checkState(self):
        if not self.state == "active":
            pass
        else:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                print("Colliding")
                self.rect.inflate_ip(5, 5)
                self.state = "hover"
                print("Hover")
            else:
                self.state = "active"
    
    def update(self, window):
        self._checkState()
        if self.state == "inactive": colour = BUTTON_INACTIVE_COL
        elif self.state == "hover": colour = BUTTON_HOVER_COL
        elif self.state == "active": colour = BUTTON_ACTIVE_COL
        
        pygame.draw.rect(window, colour, self.rect, 0, 10)
        pygame.draw.rect(window, BLACK, self.rect, 1, 10)
        
        #renderText(window, self.rect.center, self.functionLabel, int(self.rect.height*0.6), BLACK)