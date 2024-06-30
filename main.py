import math
import random
import os
import pygame
import openai
from dotenv import load_dotenv

# load_dotenv() # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Project Manager Co-Pilot")

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

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in ChatGPT API call: {e}")
        return "Error: Could not get response from ChatGPT"

def main():
    clock = pygame.time.Clock()
    center_x, center_y = width // 2, height // 2
    particles = [Particle(center_x, center_y) for _ in range(100)]
    is_responding = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_responding = not is_responding
                    if is_responding:
                        prompt = "Give me a brief project management tip."
                        response = get_chatgpt_response(prompt)
                        print(f"ChatGPT response: {response}")

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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()