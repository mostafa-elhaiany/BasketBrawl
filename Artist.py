import pygame 

def draw_screen(Global):
        Global.screen.fill((0, 0, 0))

        draw_text(f'{Global.player1.name} Points: {Global.player1.points}', Global.font, (255, 255, 255), Global.screen, 20, 20, -90)
        draw_text(f'Health: {Global.player1.health}', Global.font, (255, 255, 255), Global.screen, 20, 500, -90)

        draw_text(f'{Global.player2.name} Points: {Global.player2.points}', Global.font, (255, 255, 255), Global.screen, 1040, 20, 90)
        draw_text(f'Health: {Global.player2.health}', Global.font, (255, 255, 255), Global.screen, 1040, 500, 90)

        # Draw player 1 hand
        if(len(Global.player1.hand)!=0):
            y_offset = 20
            for card in Global.player1.hand:
                draw_card(Global.screen, Global.font, card, 100, y_offset, Global.card_width, Global.card_height, -90)
                y_offset += Global.card_offset
        else:
             Global.player1.add_draws()

        # Draw player 2 hand
        if(len(Global.player2.hand)!=0):
            y_offset = 20
            for card in Global.player2.hand:
                draw_card(Global.screen, Global.font, card, 850, y_offset, Global.card_width, Global.card_height, 90)
                y_offset += Global.card_offset
        else:
             Global.player2.add_draws()



        # flipped_screen = pygame.transform.flip(Global.screen, True, True)
        # Global.screen.blit(flipped_screen, (0, 0))



# Function to draw cards as rectangles
def draw_card(screen, font, card, x, y, w, h, rotation):
    card_rect = pygame.Rect(x, y, w, h)
    if not card.played:
        image = pygame.transform.rotate(card.image, rotation)
        image = pygame.transform.scale(image, (w,h))
        screen.blit(image, card_rect)

def draw_text(text, font, color, surface, x, y, rotation=0):
    textobj = font.render(text, True, color)
    textobj = pygame.transform.rotate(textobj, rotation)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
