# Trend Detection Service

# Overview
The Trend Detection Service is responsible for analyzing social media posts and identifying trending topics in real time. It reads data from a shared storage file (sample_post.json) and processes the content to extract hashtags and detect trends. This service is part of our distributed microservices architecture for the CSC258 project.

# Why This Service Was Created
In a distributed system, different services handle different responsibilities. While the producer service collects data from social media, there needs to be a separate component that processes this data and extracts useful insights.

# This service was created to:
Analyze incoming social media data
Identify trending topics based on hashtag frequency
Simulate real-time stream processing
Act as a foundation for a future consumer service (e.g., Kafka-based processing). It helps demonstrate key distributed systems concepts such as separation of concerns, scalability, and real-time data processing.

# How It Works

# The service reads posts from:
storage/data/sample_post.json

# For each post:
The text is cleaned (lowercased, punctuation removed)
Hashtags are extracted

# A sliding window (recent posts only) is used to:
Focus on current trends instead of all historical data

# The system counts hashtag frequency and outputs:
Top trending topics. The process repeats every few seconds to simulate real-time updates.

# How It Was Implemented
Built using Python

# Used built-in libraries:
json → for reading data
re → for text cleaning
collections → for counting trends
deque → for sliding window logic
pathlib → for reliable file paths

# Steps followed:
Created a new microservice folder inside services/
Designed a trend detection algorithm using hashtag frequency
Implemented sliding window logic for real-time simulation
Connected the service to shared storage (sample_post.json)
Tested the service with sample data

# How to Run

# From the project root:
python services/trend_service/src/trend_detector.py

# Dependencies
No external dependencies are required for this version.
All modules used are part of Python’s standard library.

# Future Improvements
Connect to Kafka for real-time streaming
Add API endpoints using Flask
Improve trend detection using NLP techniques
Integrate with dashboard for visualization

# Resources
Python Documentation: https://docs.python.org/3/
Collections Module (Counter, deque)
Regular Expressions (re module)
Course materials and lecture notes (CSC258 Distributed Systems)