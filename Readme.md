 # project no.1 Chatty: The Terminal Chatbot

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

# project no.2 Data classification model
This project demonstrates the fundamental pipeline of teaching a machine to recognize patterns in data and categorize new information.

 Using the K-Nearest Neighbors (KNN) algorithm , the model classifies samples from the Iris benchmark dataset.  

 The Pipeline (IPO Framework) 

 Input: Loading the balanced Iris dataset, which consists of 150 samples across 4 dimensions. The data is shuffled and split into an 80% training set and a 20% validation test set. Feature scaling is applied using StandardScaler (setting the mean to $0$ and variance to $1$) to ensure the distance-based algorithm isn't biased by raw data dimensions. 

Process: The K-Nearest Neighbors classifier is instantiated with K=5 (the optimal "elbow" value to prevent noise/overfitting and generic underfitting). The model is then fitted to the scaled training data to map the decision boundaries.  

Output: The model applies its derived logic to predict classes for the unseen test data. Future iterations of this pipeline will implement a Confusion Matrix and F1 Score calculations to validate trustworthiness and sensitivity, avoiding the "Accuracy Mirage" common in imbalanced data.  

Tech StackPythonScikit-Learn (KNeighborsClassifier, StandardScaler, train_test_split)  
 How to Run:
 Clone this repository to your local machine.
 Ensure you have the required libraries installed.
Execute the script:model.py

Author: Belal Abdelsalam