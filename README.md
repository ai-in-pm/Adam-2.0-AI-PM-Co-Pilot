![image](https://github.com/ai-in-pm/Adam-2.0-GUI-AI-PM-Co-Pilot/assets/36999549/9c386a23-3674-44f5-a4e5-fd54514a954d)

# Adam 2.0 - Artificial Intelligence Project Manager CO-Pilot

Welcome to the Adam 2.0 repository! This project aims to create a user-friendly Project Manager Co-Pilot, an advanced AI chatbot designed to assist with project management tasks.

## Table of Contents

- [About Adam 2.0](#about-adam-20)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps)
- [Contributing](#contributing)

## About Adam 2.0

Adam 2.0 is an AI-powered chatbot designed to help project managers streamline their tasks and improve efficiency. It leverages advanced natural language processing and machine learning techniques to provide intelligent responses and project management insights.

## Features

- **Intuitive GUI**: A user-friendly interface to interact with Adam 2.0.
- **Real-time Communication**: Seamless chat interface for real-time interaction.
- **Project Management Tools**: Integration with popular project management tools.
- **Customizable Settings**: Options to customize the chatbot's behavior and responses.
- **Analytics and Reporting**: Generate reports and analytics to monitor project progress.

PAHSE 1:  Develop a GUI

## Installation

To get started with the Adam 2.0 GUI, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/adam2.0-gui.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd adam2.0-gui
    ```
3. **Install Dependencies**:
    Make sure you have Python and Pygame installed. You can install Pygame using pip:
    ```bash
    pip install pygame
    ```

## Usage

To run the GUI with the provided visualization code, follow these steps:

1. **Create a Python File**:
    Create a file named `main.py` and copy the following code into it:

    ```python
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
    ```

2. **Run the Application**:
    Execute the Python script to run the visualization:
    ```bash
    python main.py
    ```

## Next Steps - PHASE 2

This is the first phase of developing Adam 2.0. The next steps involve:

1. **Integrating a Large Language Model**: Implementing a sophisticated language model to enhance Adam's natural language understanding and generation capabilities.
2. **Incorporating Eleven Labs**: Adding functionalities from Eleven Labs for improved speech synthesis and recognition to make Adam more interactive and user-friendly.

Stay tuned for updates and contributions to these exciting developments!

## Contributing

I welcome contributions from the community! To contribute to the project, follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of this page.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/yourusername/adam2.0-gui.git
    ```
3. **Create a Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
4. **Commit Your Changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
5. **Push to the Branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Open a Pull Request**: Go to the repository on GitHub and open a pull request.
