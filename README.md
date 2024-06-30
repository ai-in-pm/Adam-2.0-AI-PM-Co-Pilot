![image](https://github.com/ai-in-pm/Adam-2.0-GUI-AI-PM-Co-Pilot/assets/36999549/9c386a23-3674-44f5-a4e5-fd54514a954d)

# Adam 2.0 - Artificial Intelligence Project Manager Co-Pilot

Welcome to the Adam 2.0 repository! This project aims to create a user-friendly Project Manager Co-Pilot, an advanced AI chatbot designed to assist with project management tasks.

## Table of Contents
- [About Adam 2.0](#about-adam-20)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Next Steps](#next-steps---phase-2)
- [Contributing](#contributing)

## About Adam 2.0
Adam 2.0 is an AI-powered chatbot designed to help project managers streamline their tasks and improve efficiency. It leverages advanced natural language processing and machine learning techniques to provide intelligent responses and project management insights. Adam can be trained using Synthetic data.

## Features
- Intuitive GUI: A user-friendly interface to interact with Adam 2.0.
- Real-time Communication: Seamless chat interface for real-time interaction.
- Project Management Tools: Integration with popular project management tools.
- Customizable Settings: Options to customize the chatbot's behavior and responses.
- Analytics and Reporting: Generate reports and analytics to monitor project progress.
- Large Language Model Integration: Powered by GPT-4 for advanced natural language understanding and generation.

## Installation
To get started with the Adam 2.0 GUI, follow these steps:

1. Clone the Repository:
   ```
   git clone https://github.com/yourusername/adam-2.0-gui.git
   ```
2. Navigate to the Project Directory:
   ```
   cd adam-2.0-ai-pm-co-pilot
   ```
3. Create a virtual environment (recommended):
     ```
     Python 
     Create a new directory and make cwd
     create the virtual directory I use: python -m venv 'Virtual project name'
     You can activate virtual environment inside of VSCode:
     
     -On your keyboard click Ctrl/Shift/P all at the same time
     -click on select interpreter 
     -choose your newly created virtual environment (will be remembered, for all code in project)
     -when using python from command line, start virtual environment as follows:
     -Set cwd to top directory of project
     -Issue command (Linux) . ./venv/bin/activate

     OR

     Conda
   # [optional to create conda environment]
   # conda create -n Adam-2.0-AI-PM-Co-Pilot python=3.11
   # conda activate Adam-2.0-AI-PM-Co-Pilot
     
     ```

5. Install Dependencies:

   Make sure you have following Python libraries installed.

   You can install them using pip: (pygame, flask, ollama, dotenv, python-dotenv, openai).

   You can run the code in your CLI: 
   
   ```
   pip install -r requirements.txt
   ```
6. Set up OpenAI API Key:
   Copy the .envsample.txt file and rename it to `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
To run the GUI with the provided visualization code and LLM integration, follow these steps:

1. Create a Python File: Create a file named `main.py` and copy the following code into it:

```python
import math
import random
import os
import pygame
import openai
from dotenv import load_dotenv

load_dotenv()
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
    font = pygame.font.Font(None, 36)

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
                        print(f"Adam's response: {response}")

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

2. Run the Application: Execute the Python script to run the visualization:
   ```
   python main.py
   ```

## PHASE 2 Completed 
- Improving the User Interface: Enhancing the GUI to display Adam's responses directly in the application window.

  -Implemented Large Language Models - ChatGPT and Ollama onto the source code located on main.py
  
## Next Steps

PHASE 3 - Add Voice-to-Voice
- Incorporate Eleven Labs: Adding functionalities from Eleven Labs for improved speech synthesis and recognition to make Adam more interactive and user-friendly.

PHASE 4 - Synthetic Dataset

   Add open source code called "llm-data-creation" developed by Microsoft.  This will be used to train Adam based on Synthetic Datasets.

-GitHub Repository to llm-data-creation:  https://github.com/microsoft/llm-data-creation

Stay tuned for updates and contributions to these exciting developments!
## Contributing
We welcome contributions from the community! To contribute to the project, follow these steps:

1. Fork the Repository: Click the "Fork" button on the top right of this page.
2. Clone Your Fork:
   ```
   git clone https://github.com/yourusername/adam2.0-gui.git
   ```
3. Create a Branch:
   ```
   git checkout -b feature/your-feature-name
   ```
4. Commit Your Changes:
   ```
   git commit -m 'Add some feature'
   ```
5. Push to the Branch:
   ```
   git push origin feature/your-feature-name
   ```
6. Open a Pull Request: Go to the repository on GitHub and open a pull request.
