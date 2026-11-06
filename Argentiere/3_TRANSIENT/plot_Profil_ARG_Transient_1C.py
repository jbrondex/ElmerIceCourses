
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Paramètres
# ----------------------------------------------------------------------
DATA_FILE = "GlacierOut/Profil_ARG_Transient_1C.dat"
TIMESTEP = None        # which timestep do we want to plot (1..100) ; None = last timestep
OUT_FILE = "GlacierOut/Profil_ARG_Transient_1C.png"

# ----------------------------------------------------------------------
# Read data and select proper timestep
# ----------------------------------------------------------------------
data = np.loadtxt(DATA_FILE)
steps = data[:, 0]
if TIMESTEP is None:
    TIMESTEP = int(steps.max())
prof = data[steps == TIMESTEP]

z = prof[:, 6]                                  # altitude (coordinate 3)
depth = z - z.max()                             # depth : 0 at the surface, <0 towards bed
u = np.hypot(prof[:, 7], prof[:, 8])            # norm of horizontal velocity [m/a]

# ----------------------------------------------------------------------
# Figure
# ----------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.formatter.use_mathtext": True,
})

fig, ax = plt.subplots(figsize=(8.3, 5))
ax.plot(u, depth, "k-", label="u")
ax.set_xlabel("u [m/a]")
ax.set_ylabel("depth [m]")
ax.legend(loc="lower right")

fig.tight_layout()
fig.savefig(OUT_FILE, dpi=150)
plt.show()
