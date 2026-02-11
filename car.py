import pygame
import math

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.speed = 0

        self.max_speed = 3.5
        self.acc = 0.12
        self.turn_speed = 2.5
        self.friction = 0.03

        original = pygame.image.load(
            "assets/f1_car.png"
        ).convert_alpha()

        target_width = 45
        scale = target_width / original.get_width()
        target_height = int(original.get_height() * scale)

        self.original_image = pygame.transform.scale(
            original,
            (target_width, target_height)
        )

        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def accelerate(self):
        self.speed = min(self.speed + self.acc, self.max_speed)

    def slow_accelerate(self):
        self.speed = min(self.speed + self.acc * 0.5, self.max_speed * 0.6)

    def turn_left(self):
        self.angle += self.turn_speed

    def turn_right(self):
        self.angle -= self.turn_speed

    def move_forward(self):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y -= math.sin(rad) * self.speed
        self.rect.center = (self.x, self.y)

    def apply_friction(self):
        self.speed -= self.friction
        if self.speed < 0:
            self.speed = 0

    def stop(self):
        self.speed = 0

    def draw(self, screen):
        self.image = pygame.transform.rotate(
            self.original_image, self.angle
        )
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)