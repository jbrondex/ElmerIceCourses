
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Parameters
# ----------------------------------------------------------------------
DATA_FILE = "GlacierOut/ARG_Transient_1C.dat"
LABEL = r"T = +1$^{\circ}$C"
OUT_FILE = "GlacierOut/ARG_Transient_1C.png"

# column indexes
COL_TIME = 0
COL_VOLUME = 1
COL_DVDT = 2       # "Volume Change"
COL_AREA = 3
COL_SMB = 6        # "SMB Total"
COL_ZSRESIDU = 9 # Residual of Free Surface Solver
COL_FRONT = 46     # "Front Distance"

# ----------------------------------------------------------------------
# Read data
# ----------------------------------------------------------------------
data = np.loadtxt(DATA_FILE)

t = data[:, COL_TIME] - data[0, COL_TIME]   # time in year from start of simu
volume = data[:, COL_VOLUME]
dvdt = data[:, COL_DVDT]
area = data[:, COL_AREA]
smb = data[:, COL_SMB]
Zsloads = data[:, COL_ZSRESIDU]
front = data[:, COL_FRONT]


# ----------------------------------------------------------------------
# Style
# ----------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans" ,
    "font.size": 12,
    "axes.formatter.use_mathtext": True,
})

fig, axs = plt.subplots(2, 2, figsize=(14.4, 8))
ax_area, ax_vol = axs[0]
ax_front, ax_dv = axs[1]

# --- Area -------------------------------------------------------------
ax_area.plot(t, area, "k-", label=LABEL)
ax_area.set_xlabel("time [a]")
ax_area.set_ylabel(r"area [m$^2$]")
ax_area.legend(loc="lower right")

# --- Volume -----------------------------------------------------------
ax_vol.plot(t, volume, "k-", label=LABEL)
ax_vol.set_xlabel("time [a]")
ax_vol.set_ylabel(r"volume [m$^3$]")
ax_vol.legend(loc="lower right")

# --- Front position ------------------------------------------------
ax_front.plot(t, front, "k-", label=LABEL)
ax_front.set_xlabel("time [a]")
ax_front.set_ylabel("front position [m]")
ax_front.legend(loc="lower right")

# --- dV/dt and SMB -----------------------------------------------------
ax_dv.plot(t, dvdt - Zsloads, "k-", label="dV/dt-Zs load")
ax_dv.plot(t, smb, "r-", label="smb")
ax_dv.set_xlabel("time [a]")
ax_dv.set_ylabel(r"dv/dt [m$^3$/a]")
ax_dv.legend(loc="lower right")

# set scientific notation
for ax in (ax_area, ax_vol, ax_dv):
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

# set margins
for ax in axs.flat:
    ax.margins(x=0.04)

fig.tight_layout()
fig.savefig(OUT_FILE, dpi=150)
plt.show()
