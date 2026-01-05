from dataclasses import dataclass

@dataclass
class PDNStage:
    R: float    # Ohms
    L: float    # Henries
    C: float    # Farads
    Vc: float = 0.0   # Capacitor voltage (state)
    Il: float = 0.0   # Inductor current (state)
