import pygame 
from AnimatedText import AnimatedText

class Artist:
    def __init__(self, Global):
        self.Global = Global
        self.player1_points = None
        self.player2_points = None
        self.player1_health = None
        self.player2_health = None
        

    def draw_screen(self):
        self.Global.screen.fill((0, 0, 0))

        if(self.player1_points is None):
            self.player1_points = self.draw_text(f'Points: {self.Global.player1.points}', (255, 255, 255), 20, 20, -90)
            self.player1_health = self.draw_text(f'Health: {self.Global.player1.health}', (255, 255, 255), 20, 500, -90)

            self.player2_points = self.draw_text(f'Points: {self.Global.player2.points}', (255, 255, 255), 1040, 20, 90)
            self.player2_health = self.draw_text(f'Health: {self.Global.player2.health}', (255, 255, 255), 1040, 500, 90)

            self.Global.player1_texts = [self.player1_points,self.player1_health]
            self.Global.player2_texts = [self.player2_points,self.player2_health]
        else:
            self.player1_points.update()
            self.player1_points.draw(self.Global.screen)
            self.player2_points.update()
            self.player2_points.draw(self.Global.screen)
            

            # self.player1_points.update()
            # self.player1_points.draw(self.Global.screen)
            # self.player2_points.update()
            # self.player2_points.draw(self.Global.screen)
            
            # self.Global.player1_texts = [self.player1_points,self.player1_health]
            # self.Global.player2_texts = [self.player2_points,self.player2_health]
        # Draw player 1 hand
        if(len(self.Global.player1.hand)!=0):
            y_offset = 20
            for card in self.Global.player1.hand:
                self.draw_card(card, 45, y_offset, self.Global.card_width, self.Global.card_height, -90)
                y_offset += self.Global.card_offset
        else:
            self.Global.player1.add_draws()

        # Draw player 2 hand
        if(len(self.Global.player2.hand)!=0):
            y_offset = 20
            for card in self.Global.player2.hand:
                self.draw_card(card, 840, y_offset, self.Global.card_width, self.Global.card_height, 90)
                y_offset += self.Global.card_offset
        else:
            self.Global.player2.add_draws()



            # flipped_screen = pygame.transform.flip(Global.screen, True, True)
            # Global.screen.blit(flipped_screen, (0, 0))



    # Function to draw cards as rectangles
    def draw_card(self,card, x, y, w, h, rotation):
        card_rect = pygame.Rect(x, y, w, h)
        if not card.played:
            image = pygame.transform.rotate(card.image, rotation)
            image = pygame.transform.scale(image, (w,h))
            self.Global.screen.blit(image, card_rect)

    def draw_text(self,text, color, x, y, rotation):
        
        animated_text = AnimatedText(text, (x,y),32,color, rotation)
        animated_text.update()
        animated_text.draw(self.Global.screen)
        return animated_text
        # textobj = font.render(text, True, color)
        # textobj = pygame.transform.rotate(textobj, rotation)
        # textrect = textobj.get_rect()
        # textrect.topleft = (x, y)
        # surface.blit(textobj, textrect)
