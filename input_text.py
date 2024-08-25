from settings import *

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font("Hack-Regular.ttf", 32)


class InputBox:

    def __init__(self, player):
        self.color = COLOR_INACTIVE
        self.text = ""
        self.active = False
        self.player = player

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text == "":
                        self.text = '0'
                    else:
                        self.player.provisionalBet = int(self.text)
                    #self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isdigit():
                        if len(self.text) < 6:
                            self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self, screen, pos, w, h):
        # Resize the box if the text is too long.
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = pos
        self.draw(screen)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)