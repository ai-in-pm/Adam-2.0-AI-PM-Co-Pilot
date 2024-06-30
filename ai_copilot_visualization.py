import math
import random
import pygame

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Project Manager Co-Pilot Visualization")

# Colors
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
RED = (255, 69, 0)
BLACK = (0, 0, 0)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)
        self.color = ORANGE
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

def main():
    clock = pygame.time.Clock()
    center_x, center_y = width // 2, height // 2
    particles = [Particle(center_x, center_y) for _ in range(100)]
    is_responding = False
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_responding = not is_responding

        screen.fill(BLACK)

        # Draw outer circles
        for i in range(3):
            pygame.draw.circle(screen, ORANGE, (center_x, center_y), 200 - i * 30, 1)

        # Draw radiating lines
        num_lines = 12
        for i in range(num_lines):
            angle = (i / num_lines) * math.pi * 2
            x = center_x + math.cos(angle) * 200
            y = center_y + math.sin(angle) * 200
            pygame.draw.line(screen, ORANGE, (center_x, center_y), (x, y), 1)

        # Draw pulsating inner circle
        pulse_radius = 50 + math.sin(pygame.time.get_ticks() / 200) * 10
        pygame.draw.circle(screen, GOLD, (center_x, center_y), int(pulse_radius), 1)

        # Add more animation when responding
        if is_responding:
            responding_circle_radius = 100 + math.sin(pygame.time.get_ticks() / 150) * 20
            pygame.draw.circle(screen, RED, (center_x, center_y), int(responding_circle_radius), 1)

        # Update and draw particles
        for particle in particles:
            particle.move()
            particle.draw(screen)
            if (particle.x - center_x)**2 + (particle.y - center_y)**2 > 200**2:
                particles.remove(particle)
                particles.append(Particle(center_x, center_y))

        # Draw text
        text = font.render("Adam the AI PM Co-Pilot" if not is_responding else "Adam the AI PM Co-Pilot (Responding...)", True, GOLD)
        text_rect = text.get_rect(center=(width // 2, height - 50))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()