import pygame

class Track:
    def __init__(self):
        self.bg_color = (0, 150, 0)      # off-track
        self.road_color = (80, 80, 80)   # road
        self.brush_radius = 18

        self.track_surface = pygame.Surface((800, 600))
        self.clear()

    def clear(self):
        self.track_surface.fill(self.bg_color)

    def draw_brush(self, position):
        pygame.draw.circle(
            self.track_surface,
            self.road_color,
            position,
            self.brush_radius
        )

    def draw(self, screen):
        screen.blit(self.track_surface, (0, 0))

    def on_road(self, car):
        x, y = int(car.x), int(car.y)

        if x < 0 or y < 0 or x >= 800 or y >= 600:
            return False

        return self.track_surface.get_at((x, y)) == self.road_color