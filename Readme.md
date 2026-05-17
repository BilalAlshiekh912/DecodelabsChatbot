 # Chatty: The Terminal Chatbot

A lightweight, interactive Python terminal chatbot built to demonstrate clean control flow and engaging terminal UI effects. 

Instead of relying on long, hard-to-read `if-elif-else` chains, this project utilizes **Dictionary Dispatching** for efficient and scalable intent matching. It also features a custom **Typewriter Animation** to make the bot feel more human and alive.

## Features

* **Typewriter Animation Effect:** The bot responds character-by-character with slight random delays, simulating a real human typing.
* **Dictionary Dispatch Architecture:** Maps user intents (trigger phrases) directly to handler functions using dictionaries, making the codebase highly modular and easy to expand.
* **Basic Conversational Intents:**
  * Greetings & Well-being
  * Introductions (Asking for the bot's name)
  * Graceful Exits

## Prerequisites

This project uses standard Python libraries, so no external dependencies are required.
* **Python 3.x**

## How to Run

1. Clone or download this repository.
2. Ensure you have the main python file (e.g., `chatbot.py`) in your directory.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the file.
5. Run the script using Python:
   ```bash
   python chatbot.py