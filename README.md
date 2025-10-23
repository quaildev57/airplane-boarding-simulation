# ✈️ Airplane Boarding Simulation Environment

Welcome to the **Airplane Boarding Environment**, a fully custom OpenAI Gymnasium-compatible simulation designed to explore and optimize the airplane boarding process using Reinforcement Learning (RL). This environment mimics real-world passenger dynamics, complete with aisle congestion, luggage stowing behavior, and decision-making regarding who boards next.

---

## 🚀 Motivation

What if boarding a plane didn’t feel like herding through chaos?

Every airline has tried—from boarding by rows to loading windows first—but somehow, it still takes forever. This project flips that problem on its head. Instead of guessing, it lets an AI agent learn the smartest way to get passengers seated—by experimenting, adapting, and discovering patterns that humans might never see.

Through reinforcement learning, the system runs virtual boarding simulations, measuring how small changes ripple through the crowd. Over time, it figures out how to turn that slow shuffle down the aisle into a smooth, optimized flow.

It’s not just about beating the line—it’s about showing how machines can rethink everyday inefficiencies and turn data into real-world convenience.


---

## 🛠️ Features

* **Custom Gymnasium Environment**: Handcrafted environment that simulates airplane boarding using real-life constraints.
* **Maskable Actions**: Invalid actions (e.g., choosing empty rows) are automatically masked using `MaskablePPO` from `sb3-contrib`.
* **Passenger Behavior Modeling**: Passengers have realistic states: `MOVING`, `STALLED`, `STOWING`, and `SEATED`.
* **Aisle Movement Logic**: Simulates real delays caused by blocked paths and stowing luggage.
* **Configurable Layout**: Easily adjust the number of rows and seats per row.
* **Terminal Rendering**: Visualize the seating, aisle, and boarding line step-by-step.
* **Vectorized Training Support**: Uses `SubprocVecEnv` for efficient parallel training.

---

## 📂 Repository Structure

```
.
├── agent.py                # RL training and evaluation logic using MaskablePPO
├── airplane_boarding.py    # Main Gymnasium environment definition
├── main.py                 # Script to manually run and test environment
├── new.py                  # Alternate implementation of environment (legacy/test)
├── README.md               # You're reading it!
```

---

## 🧠 Environment Design

### Environment Overview:

* Each simulation represents an airplane boarding session.
* The airplane is represented by a grid of seats divided into rows.
* Passengers start in a lobby organized by row.
* The agent must select a row to send a passenger from the lobby into the boarding aisle.

### Passenger Flow:

1. Passenger enters the aisle.
2. They move forward step-by-step.
3. If blocked, they stall.
4. When at their seat row, they must first stow luggage, then sit.
5. Once seated, they are removed from the aisle.

### Action Space:

* A discrete value representing the row from which to board the next passenger.
* Only rows with waiting passengers are valid (enforced by action masking).

### Observation Space:

* A flat NumPy array of shape `(2 * num_seats,)`, encoding for each position in the aisle:

  * Passenger's seat number
  * Passenger's current status (encoded as an integer enum)

### Passenger States:

* `MOVING` (0): Walking forward
* `STALLED` (1): Blocked by someone ahead
* `STOWING` (2): Placing luggage before sitting
* `SEATED` (3): Reached and seated at destination

---

## 🦜 Training the Agent

The agent is trained using **MaskablePPO**, which prevents selecting invalid actions (like boarding from an empty row).

### Training Script

```bash
python agent.py
```

* Models saved under: `models/MaskablePPO/`
* TensorBoard logs: `logs/`

### Inside `agent.py`:

* Uses `SubprocVecEnv` to parallelize 12 environments.
* Reward shaping is done by penalizing stalls.
* Evaluation callback tracks the best model.

### Example Callback Configuration:

```python
MaskableEvalCallback(
    env,
    eval_freq=10000,
    best_model_save_path='models/MaskablePPO',
    verbose=1,
)
```

### Testing the Agent

In `agent.py`, run:

```python
test("best_model")
```

This loads the best checkpoint and simulates a test run in render mode.

---

## 🎮 Manual Environment Execution

For manual interaction with the environment (no learning), simply run:

```bash
python main.py
```

This visualizes a boarding sequence using random actions. It's useful for debugging and observing how the logic plays out.

---

## 📊 Reward Function Design

### Base Reward:

```python
reward = - num_passengers_stalled()
```

The reward penalizes stalls in the aisle, encouraging smooth movement. There is also a commented-out optional term:

```python
+ num_passengers_moving()
```

This can be added to slightly boost rewards when passengers are moving forward.

---

## 📚 Dependencies

Install the necessary packages with:

```bash
pip install gymnasium numpy stable-baselines3 sb3-contrib
```

> Optional: Use a virtual environment or Conda for cleaner dependency management.

---

## 📈 Potential Improvements

* ✅ More realistic airplane layouts (e.g., window vs aisle vs middle seat)
* ✅ Overhead bin capacity constraints
* ✅ Noise in passenger behavior (e.g., random delays)
* ✅ Integration with real airline boarding strategies (e.g., Southwest, WilMA, Back-to-Front)
* ✅ 3D visual rendering or animation

---

## 🙌 Contributing

Pull requests are welcome! Here's how you can help:

* Tune the reward function
* Add new boarding policies
* Improve the rendering logic
* Refactor and modularize code further
* Add metrics to benchmark policies

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 📝 Author Notes

This environment was built with thoughtful logic, real-world inspiration, and curiosity about how machine learning can optimize everyday human systems. Whether you're a reinforcement learning researcher or just an aviation geek, we hope this project adds value to your experiments and inspires further innovation.

Happy Simulating!

— *AirplaneEnv Devs*
