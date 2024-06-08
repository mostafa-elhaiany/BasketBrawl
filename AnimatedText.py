import pygame

class AnimatedText:
    def __init__(self, text, position, font_size=48, color=(255, 255, 255), rotation=0,animation_color=(255, 0, 0), animation_duration=1000):
        self.text = text
        self.position = position
        self.original_font_size = font_size
        self.color = color
        self.rotation = rotation
        self.animation_color = animation_color
        self.animation_duration = animation_duration
        self.font = pygame.font.SysFont(None, self.original_font_size)
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_surface = pygame.transform.rotate(self.text_surface, rotation)
        self.animation_start_time = None
        self.animating = False
        self.grow_phase = True

    def animate(self, color=None):
        if(color is not None):
            self.animation_color = color
        self.animating = True
        self.animation_start_time = pygame.time.get_ticks()
        self.grow_phase = True

    def update(self, new_text = None):
        if(new_text is not None):
            self.text = new_text
        if self.animating:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.animation_start_time
            if self.grow_phase:
                progress = elapsed_time / (self.animation_duration / 2)
                if progress >= 1.0:
                    progress = 1.0
                    self.grow_phase = False
                    self.animation_start_time = current_time  # Reset start time for shrinking phase
                eased_progress = progress
            else:
                progress = elapsed_time / (self.animation_duration / 2)
                if progress >= 1.0:
                    progress = 1.0
                    self.animating = False  # End of animation
                eased_progress = 1 - progress

            animated_font_size = int(self.original_font_size * (1 + 0.5 * eased_progress))
            self.font = pygame.font.SysFont(None, animated_font_size)

            # Interpolate color between the original color and animation color
            r = int(self.color[0] + (self.animation_color[0] - self.color[0]) * eased_progress)
            g = int(self.color[1] + (self.animation_color[1] - self.color[1]) * eased_progress)
            b = int(self.color[2] + (self.animation_color[2] - self.color[2]) * eased_progress)
            animated_color = (r, g, b)

            self.text_surface = self.font.render(self.text, True, animated_color)
            self.text_surface = pygame.transform.rotate(self.text_surface, self.rotation)

        else:
            self.font = pygame.font.SysFont(None, self.original_font_size)
            self.text_surface = self.font.render(self.text, True, self.color)
            self.text_surface = pygame.transform.rotate(self.text_surface, self.rotation)


    def draw(self, surface):
        text_rect = self.text_surface.get_rect(center=self.position)
        text_rect.topleft = self.position
        surface.blit(self.text_surface, text_rect)