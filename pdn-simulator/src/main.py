from components import PDNStage
from solver import simulate_pdn
from load_profiles import step_load
from plots import plot_voltage

# PDN stages (example values)
stages = [
    PDNStage(R=1e-3, L=5e-9, C=100e-6),   # Bulk caps
    PDNStage(R=5e-4, L=1e-9, C=10e-6),    # Package caps
    PDNStage(R=1e-4, L=2e-10, C=1e-6)     # On-die caps
]

time, voltage = simulate_pdn(
    stages,
    load_func=lambda t: step_load(t, t_step=1e-6),
    Vin=1.0,
    dt=1e-9,
    t_end=5e-6
)

plot_voltage(time, voltage)
