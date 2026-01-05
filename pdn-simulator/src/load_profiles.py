import numpy as np
#Step_load  causes worst-case voltage droop 
def step_load(t, I_idle=5.0, I_load=80.0, t_step=1e-6):
    return I_idle if t < t_step else I_load


def burst_load(t, base=20.0, amplitude=40.0, freq=1e6):
    return base + amplitude * np.sin(2 * np.pi * freq * t)
