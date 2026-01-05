import numpy as np

def simulate_pdn(stages, load_func, Vin=1.0, dt=1e-9, t_end=5e-6):
    time = np.arange(0, t_end, dt)
    Vout = []

    for t in time:
        Iload = load_func(t)
        Vin_stage = Vin

        for i, stage in enumerate(stages):
            # Load only applies to last stage
            I_L_out = Iload if i == len(stages) - 1 else 0.0

            # Differential equations
            dIl = (Vin_stage - stage.Vc - stage.Il * stage.R) / stage.L
            dVc = (stage.Il - I_L_out) / stage.C

            # Euler integration
            stage.Il += dIl * dt
            stage.Vc += dVc * dt

            Vin_stage = stage.Vc  # feed next stage

        Vout.append(stages[-1].Vc)

    return time, np.array(Vout)
