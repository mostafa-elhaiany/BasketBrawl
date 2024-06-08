import pygame 
from AnimatedText import AnimatedText

class Artist:
    def __init__(self, Global):
        self.Global = Global
        self.player1_points = None
        self.player2_points = None
        self.player1_health = None
        self.player2_health = None
        self.background_image = pygame.image.load("images/background.png")

        

    def draw_screen(self):
        self.Global.screen.fill((0, 0, 0))

        bg_rect = pygame.Rect(0, 0, self.Global.SCREEN_WIDTH, self.Global.SCREEN_HEIGHT)
        # image = pygame.transform.rotate(card.image, rotation)
        bg_image = pygame.transform.scale(self.background_image, (self.Global.SCREEN_WIDTH, self.Global.SCREEN_HEIGHT))
        self.Global.screen.blit(bg_image, bg_rect)

        if(self.player1_points is None):
            self.player1_points = self.draw_text(f'Points: {self.Global.player1.points}', (255, 255, 255), 20, 20, -90)
            self.player1_health = self.draw_text(f'Health: {self.Global.player1.health}', (255, 255, 255), 20, 450, -90)

            self.player2_points = self.draw_text(f'Points: {self.Global.player2.points}', (255, 255, 255), 1040, 20, 90)
            self.player2_health = self.draw_text(f'Health: {self.Global.player2.health}', (255, 255, 255), 1040, 450, 90)

            self.Global.player1_texts = [self.player1_points,self.player1_health]
            self.Global.player1.animate_point_function = self.player1_points.animate
            self.Global.player1.animate_health_function = self.player1_health.animate

            self.Global.player2_texts = [self.player2_points,self.player2_health]
            self.Global.player2.animate_point_function = self.player2_points.animate
            self.Global.player2.animate_health_function = self.player2_health.animate
            
        else:
            self.player1_points.update(f'Points: {self.Global.player1.points}')
            self.player1_points.draw(self.Global.screen)
            self.player2_points.update(f'Points: {self.Global.player2.points}')
            self.player2_points.draw(self.Global.screen)
            

            self.player1_health.update(f'Health: {self.Global.player1.health}')
            self.player1_health.draw(self.Global.screen)
            self.player2_health.update(f'Health: {self.Global.player2.health}')
            self.player2_health.draw(self.Global.screen)
            
        # Draw player 1 hand
        if(len(self.Global.player1.hand)!=0):
            y_offset = 20
            for card in self.Global.player1.hand:
                self.draw_card(card, self.Global.p1_card_x, y_offset, self.Global.card_width, self.Global.card_height, -90)
                y_offset += self.Global.card_offset
        else:
            self.Global.player1.add_draws()

        # Draw player 2 hand
        if(len(self.Global.player2.hand)!=0):
            y_offset = 20
            for card in self.Global.player2.hand:
                self.draw_card(card, self.Global.p2_card_x, y_offset, self.Global.card_width, self.Global.card_height, 90)
                y_offset += self.Global.card_offset
        else:
            self.Global.player2.add_draws()



            # flipped_screen = pygame.transform.flip(Global.screen, True, True)
            # Global.screen.blit(flipped_screen, (0, 0))



    # Function to draw cards as rectangles
    def draw_card(self,card, x, y, w, h, rotation):
        card_rect = pygame.Rect(x, y, w, h)
        if not card.played:
            if(card.image is not None):
                image = pygame.transform.rotate(card.image, rotation)
                image = pygame.transform.scale(image, (w,h))
                self.Global.screen.blit(image, card_rect)
            else:
                pygame.draw.rect(self.Global.screen, (255, 255, 255), card_rect)
                self.draw_text(card.name, (0, 0, 0), x + 10, y + 10, 0)

    def draw_text(self,text, color, x, y, rotation):
        
        animated_text = AnimatedText(text, (x,y),42,color, rotation)
        animated_text.update()
        animated_text.draw(self.Global.screen)
        return animated_text
        # textobj = font.render(text, True, color)
        # textobj = pygame.transform.rotate(textobj, rotation)
        # textrect = textobj.get_rect()
        # textrect.topleft = (x, y)
        # surface.blit(textobj, textrect)
