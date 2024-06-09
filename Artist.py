import pygame 
from AnimatedText import AnimatedText

class Artist:
    def __init__(self, Global):
        self.Global = Global
        self.player1_points = None
        self.player2_points = None
        self.player1_health = None
        self.player2_health = None
        self.mid_text = None
        self.background_image = pygame.image.load("images/background.png")
        self.poll_text = None
        self.poll_values = None
        self.poll_active = False
        self.prev_values = [0,0]
    
    def draw_mid_text(self, text, color):
        self.mid_text = self.draw_text(text, (255, 255, 255), self.Global.SCREEN_WIDTH//2 - 200, self.Global.SCREEN_HEIGHT//2, 0,72)
        self.mid_text.animate(color)
        

    def enable_poll(self):
        self.poll_active = True
        self.poll_text = self.draw_text("Poll Active", (255, 255, 255), self.Global.SCREEN_WIDTH//2 - 150, self.Global.SCREEN_HEIGHT//2-100, 0,72)
        self.poll_text.animate((0,255,0))

        self.poll_values = [
            self.draw_text("0", (255, 255, 255), self.Global.SCREEN_WIDTH//2 + 90, self.Global.SCREEN_HEIGHT//2, 0,60),
            self.draw_text("0", (255, 255, 255), self.Global.SCREEN_WIDTH//2 - 250, self.Global.SCREEN_HEIGHT//2, 0,60)
        ]
        self.poll_values[0].animate((50,255,50))
        self.poll_values[1].animate((50,255,50))


    def update_poll(self,poller):
        votes = poller.votes
        if(self.Global.POLLING):
            self.poll_text.update()
            self.poll_text.draw(self.Global.screen)

            self.poll_values[0].update(f"votes: {votes[0]}")
            self.poll_values[0].draw(self.Global.screen)
            self.poll_values[1].update(f"votes: {votes[1]}")
            self.poll_values[1].draw(self.Global.screen)
            if(votes[0] != self.prev_values[0]):
                self.poll_values[0].animate()
            if(votes[1] != self.prev_values[1]):
                self.poll_values[1].animate()


            self.prev_values = votes



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
            
        if(not self.Global.GAMEOVER):
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


        if(self.mid_text is not None):
            self.mid_text.update()
            self.mid_text.draw(self.Global.screen)


        flipped_screen = pygame.transform.flip(self.Global.screen, True, True)
        self.Global.screen.blit(flipped_screen, (0, 0))



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

    def draw_text(self,text,color, x, y, rotation, font_size = 42):
        animated_text = AnimatedText(text, (x,y),font_size,color, rotation)
        animated_text.update()
        animated_text.draw(self.Global.screen)
        return animated_text
