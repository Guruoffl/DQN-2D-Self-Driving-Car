import pygame
import random
import torch
import torch.nn.functional as F
from car import Car
from track import Track
from sensors import Sensors
from reward import compute_reward
from dqn import DQN
from replay_buffer import ReplayBuffer

pygame.init()

MODE = "draw"   

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Self-Driving Car")

clock = pygame.time.Clock()

track = Track()

car = Car()
car.x = 400
car.y = 300

car.angle = 45      
car.speed = 0
car.rect.center = (car.x, car.y)

sensors = Sensors(car)

STATE_SIZE = 7
ACTION_SIZE = 3

policy_net = DQN(STATE_SIZE, ACTION_SIZE)
target_net = DQN(STATE_SIZE, ACTION_SIZE)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

optimizer = torch.optim.Adam(policy_net.parameters(), lr=0.001)
memory = ReplayBuffer()

GAMMA = 0.99
BATCH_SIZE = 64
TARGET_UPDATE = 100

epsilon = 1.0
epsilon_min = 0.1
epsilon_decay = 0.995

step_count = 0
brake = 0

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                MODE = "drive"

                car.x, car.y = pygame.mouse.get_pos()

                car.angle = 45
                car.speed = 0
                car.rect.center = (car.x, car.y)

                print("🚗 Drive mode (anticlockwise start)")

            if event.key == pygame.K_c:
                track.clear()
                MODE = "draw"
                print("🎨 Draw mode")

    if MODE == "draw":
        if pygame.mouse.get_pressed()[0]:
            track.draw_brush(pygame.mouse.get_pos())

        track.draw(screen)
        pygame.display.update()
        continue

    track.draw(screen)

    sensor_vals = sensors.read(track.track_surface)
    state = sensor_vals + [car.speed, brake]
    state_tensor = torch.tensor(state, dtype=torch.float32)

    if random.random() < epsilon:
        action = random.randint(0, ACTION_SIZE - 1)
    else:
        with torch.no_grad():
            action = torch.argmax(policy_net(state_tensor)).item()

    brake = 0

    if action == 0:
        car.accelerate()
    elif action == 1:
        car.turn_left()
    elif action == 2:
        car.turn_right()   

    car.move_forward()
    car.apply_friction()

    on_road = track.on_road(car)
    done = not on_road

    next_sensor_vals = sensors.read(track.track_surface)
    next_state = next_sensor_vals + [car.speed, brake]

    reward = compute_reward(on_road, car.speed, brake, sensor_vals)
    memory.push(state, action, reward, next_state, done)

    if len(memory) >= BATCH_SIZE:
        states, actions, rewards, next_states, dones = memory.sample(BATCH_SIZE)

        states = torch.tensor(states, dtype=torch.float32)
        actions = torch.tensor(actions)
        rewards = torch.tensor(rewards, dtype=torch.float32)
        next_states = torch.tensor(next_states, dtype=torch.float32)
        dones = torch.tensor(dones, dtype=torch.float32)

        current_q = policy_net(states).gather(1, actions.unsqueeze(1)).squeeze()
        next_q = target_net(next_states).max(1)[0]
        target_q = rewards + GAMMA * next_q * (1 - dones)

        loss = F.mse_loss(current_q, target_q.detach())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    step_count += 1
    if step_count % TARGET_UPDATE == 0:
        target_net.load_state_dict(policy_net.state_dict())

    if done:
        car.x, car.y = pygame.mouse.get_pos()
        car.angle = 45      
        car.speed = 0
        car.rect.center = (car.x, car.y)
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

    car.draw(screen)
    pygame.display.update()

pygame.quit()