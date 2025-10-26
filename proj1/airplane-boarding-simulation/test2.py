# test.py
import airplane_boarding
import gymnasium as gym


env = gym.make('airplane-boarding-v0', num_of_rows=10, seats_per_row=5, render_mode='human')

observation, _ = env.reset()
terminated = False
total_reward = 0
step_count = 0

while not terminated:
    masks = env.unwrapped.action_masks()
    valid_actions = [i for i, mask in enumerate(masks) if mask]
    if not valid_actions:
        break
    import numpy as np
    action = np.random.choice(valid_actions)
    observation, reward, terminated, _, _ = env.step(action)
    total_reward += reward
    step_count += 1

    print(f"Step {step_count} Action: {action}")
    print(f"Observation: {observation}")
    print(f"Reward: {reward}\n")

env.close()
print(f"Total Reward: {total_reward}")
