# Farm OpenAI Project

## Overview
This project is designed to train gpt-3.5-turbo to detect phishing emails.

## Installation
To set up the project environment:
```bash
git clone https://github.com/WoodyTheOriginal/farm_openai.git
cd farm_openai
pip install -r requirements.txt
```

## Usage
To run the project:
```bash
python analysis.py
```

## How does it work?
The project makes API calls with gpt-3.5-turbo to detect phsihing emails.
To improve performance, we chose to use multi-threading to make multiple API calls at once.
Therefore we can generate as much threads as needed to make parallel API calls.
All those threads are stored in a list called a generation.
After all those threads have analyzed as many emails as wanted, wa can store the results in MongoDB.
The results are as follows:
- Accuracy
- Error
- True Positives
- False Positives
- True Negatives
- False Negatives
We then choose a champion between all the threads based on the one that has the highest accuracy combined with the lowest False Negatives. So the champion will have the highest accuracy between all the threads and betweend all of them that have the same accuracy, the one with the lowest False Negatives will be chosen.
We then store the champion in MongoDB and we can start a new generation of threads.
At the beginning of each generation we make API calls to improve the prompt of each thread. 
To select the prompt to improve we compare the champion with the previous one and use the prompt from the best one of them.