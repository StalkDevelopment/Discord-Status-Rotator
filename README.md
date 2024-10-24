# Discord Status Rotator

## Description

This project is a Discord user account status rotator using the latest version of `discord.py-self`. The purpose of this project is to automatically rotate the status of a Discord user account at regular intervals. The project is designed to be readable, maintainable, and modularized, following principles such as DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid), SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), YAGNI (You Aren't Gonna Need It), and SoC (Separation of Concerns).

## Setup and Running

1. Clone the repository:
   ```sh
   git clone https://github.com/StalkDevelopment/Discord-Status-Rotator.git
   cd Discord-Status-Rotator
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure the bot by editing the `src/config.py` file with your Discord token and desired status rotation interval.

4. Run the bot:
   ```sh
   python src/main.py
   ```

## Principles Followed

### DRY (Don't Repeat Yourself)
The code is designed to minimize repetition by using functions and classes to encapsulate reusable logic.

### KISS (Keep It Simple, Stupid)
The implementation is kept as simple as possible, avoiding unnecessary complexity.

### SOLID
- **Single Responsibility Principle**: Each class and function has a single responsibility.
- **Open/Closed Principle**: The code is open for extension but closed for modification.
- **Liskov Substitution Principle**: Subclasses can be substituted for their base classes without affecting the correctness of the program.
- **Interface Segregation Principle**: Interfaces are designed to be small and specific to the needs of the client.
- **Dependency Inversion Principle**: High-level modules do not depend on low-level modules; both depend on abstractions.

### YAGNI (You Aren't Gonna Need It)
The code includes only the functionality that is necessary for the current requirements, avoiding over-engineering.

### SoC (Separation of Concerns)
The code is organized into modules, each responsible for a specific aspect of the functionality, making it easier to understand and maintain.
