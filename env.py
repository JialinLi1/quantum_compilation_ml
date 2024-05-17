import gymnasium as gym
import numpy as np
from gymnasium import spaces
from sympy import *


class GateEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}


    def __init__(self, target, precision):
        super().__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        gates = {
            0: Matrix([[1, 0], [0, exp(I*pi/4)]]),
            1: Matrix([[1/sqrt(2), 1/sqrt(2)],[1/sqrt(2),-1/sqrt(2)]])
        }
        self.current_gate = Matrix([[1, 0], [0, 1]])
        self.current_length = 0
        self.target = target
        self.precision = precision

        self.action_space = spaces.Discrete(len(gates))
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=-1.0, high=1.0,
                                            shape=(4,2), dtype=np.float64)

    def step(self, action):
        ...
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def render(self):
        ...

    def close(self):
        ...