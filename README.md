# airplane-boarding-simulation
 # ✈️ Airplane Boarding Simulation Environment

Welcome to the Airplane Boarding Environment — a custom-built reinforcement learning simulation designed to explore efficient passenger boarding strategies using the Gymnasium interface and `MaskablePPO` from `sb3-contrib`.

This project simulates the boarding process inside an airplane, complete with passengers, seats, stalling, and luggage stowing behavior. It's an ideal playground for testing intelligent policies aimed at reducing total boarding time and congestion.

---

## 🚀 Project Motivation

Ever wondered why boarding a flight takes so long even when people board in order? This simulation models that process and allows an agent to learn better boarding strategies. Whether it’s window-to-aisle, back-to-front, or something in between, this environment gives RL the power to find out what actually works.

---

## 🛠 Features

- **Fully Custom OpenAI Gym Environment** – built from scratch to model real-world passenger dynamics.
- **Supports Action Masking** – integrates with `MaskablePPO` to prevent invalid boarding actions.
- **Detailed Passenger States** – passengers can move, stall, stow luggage, or be seated.
- **Custom Rendering** – get a full terminal view of what's happening inside the aircraft aisle.
- **Multi-Process Training Support** – thanks to `SubprocVecEnv`, you can train across multiple parallel environments.

---

## 📂 Repository Structure

```plaintext
.
├── agent.py                # Training & evaluation loop using MaskablePPO
├── airplane_boarding.py    # Core custom Gymnasium environment
├── main.py                 # Run the environment manually (for testing)
├── new.py                  # Variant of environment (not used in agent.py)
├── README.md               # You are here!
```

---

## 🧠 How the Environment Works

- The airplane consists of **rows** and **seats per row**.
- Each passenger has a target seat and starts in the **lobby**.
- Actions correspond to selecting a **row** from which to send a passenger to the aisle.
- The agent learns to minimize **stalls** and **boarding time** by selecting which passengers board when.
- The observation space is a flat array representing the state of all passengers in the boarding line.

### Passenger States:
- `MOVING` – actively walking through the aisle
- `STALLED` – blocked by another passenger
- `STOWING` – putting away luggage before sitting
- `SEATED` – sitting at their assigned seat

---

## 🧪 Training the Agent

The agent is trained using `MaskablePPO`, which avoids choosing invalid actions (e.g., trying to board a row that's already empty).

### To train:
```bash
python agent.py
```

> Model checkpoints and logs will be saved to the `models/` and `logs/` directories respectively.

### To test a trained model:
```python
test("best_model")  # In agent.py
```

---

## 🎮 Manual Testing (No RL)

You can run the environment interactively without training:
```bash
python main.py
```

This allows you to visualize how the environment works using randomly sampled actions, and understand how rewards are computed.

---

## 🧩 Dependencies

Make sure you have the following Python packages installed:

```bash
pip install gymnasium numpy stable-baselines3 sb3-contrib
```

We recommend using a virtual environment for managing dependencies.

---

## 🏁 Reward Function

The reward at each step is designed to encourage:
- Minimizing the number of **stalled** passengers
- Maximizing **efficiency** in seating passengers

```python
reward = - num_passengers_stalled
```

Optional improvement (commented in code):
```python
+ num_passengers_moving
```

---

## 📈 Future Ideas

- Add realistic airplane layouts (aisle/window seat dynamics)
- Include luggage bin capacity constraints
- Test with real-world boarding strategies (e.g. Southwest, Reverse Pyramid)

---

## 🙌 Contributing

Feel free to fork, experiment, and open a PR! Whether you're optimizing the reward function or experimenting with new policies, this environment is made to be extended.

---

## 📃 License

This project is open source and available under the MIT License.

---

## ✍️ Author Notes

Built with a lot of logic, coffee ☕, and curiosity about why airplanes don’t board faster than they do.
