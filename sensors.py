import math
import pygame

class Sensors:
    def __init__(self, car):
        self.car = car
        self.angles = [-75, -35, 0, 35, 75]
        self.max_distance = 150

    def read(self, track_surface):
        readings = []

        for angle in self.angles:
            ray_angle = math.radians(self.car.angle + angle)

            hit_distance = self.max_distance
            for dist in range(0, self.max_distance, 5):
                x = int(self.car.x + math.cos(ray_angle) * dist)
                y = int(self.car.y - math.sin(ray_angle) * dist)

                if x < 0 or x >= 800 or y < 0 or y >= 600:
                    hit_distance = dist
                    break

                if track_surface.get_at((x, y))[0] == 0:
                    hit_distance = dist
                    break

            readings.append(hit_distance / self.max_distance)

        return readings

    def draw(self, screen):
        pass