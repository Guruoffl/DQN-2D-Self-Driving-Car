 2D Self-Driving Car using Deep Q-Learning (DQN)

   A 2D autonomous driving simulator built with Python, Pygame, and Deep Reinforcement Learning, where an AI-controlled Formula-1-style car learns to drive on user-drawn tracks using Deep Q-Learning (DQN).

   This project focuses on perception, learning, and adaptability, rather than hard-coded rules.


 => Key Features
	•	User-Drawn Tracks
	•	Draw custom race tracks using a painter brush
	•	Train and test the agent on unseen tracks
	•	Deep Q-Network (DQN)
	•	Reinforcement learning–based decision making
	•	Experience replay & target network for stability
	•	Multi-Sensor Perception
	•	5 invisible distance sensors (far-left → far-right)
	•	Sensor-based awareness of track boundaries
	•	Realistic Car Dynamics
	•	Acceleration, steering, friction, speed limits
	•	Continuous movement and rotation
	•	Two-Mode System
	•	Draw Mode → create tracks interactively
	•	Drive Mode → autonomous driving by AI
	•	Reward Shaping
	•	Encourages staying on track
	•	Penalizes edge proximity and crashes
	•	Promotes smooth, centered driving


=> Tech Stack
	•	Language: Python 3
	•	Simulation & Rendering: Pygame
	•	AI / ML: PyTorch
	•	Learning Algorithm: Deep Q-Learning (DQN)
	•	Version Control: Git & GitHub

=> PROCESS TO RUN

 install dependencies - pip install pygame torch
 run the simulator - python3 main.py

=> Controls

 Draw Mode (default on start)
	•	Left Mouse Button → Draw the track
	•	C → Clear the canvas
	•	ENTER → Switch to Drive Mode

 Drive Mode
	•	The AI takes control and starts driving autonomously
	•	The car respawns automatically if it goes off-track

=> Reinforcement Learning Details

 State Space
  [far_left, left, center, right, far_right, speed, brake]

 Action Space
  0 → Accelerate
  1 → Turn Left
  2 → Turn Right

=> Innovations & Highlights
	•	User-defined environments (human-in-the-loop design)
	•	Learning-based control instead of rule-based logic
	•	Track generalization using drawn layouts
	•	Invisible sensor perception for realism
	•	Anticlockwise-biased initial orientation (configurable)