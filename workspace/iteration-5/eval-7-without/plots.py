import numpy as np
import matplotlib.pyplot as plt
import os

output_dir = os.path.dirname(os.path.abspath(__file__))

# Config 1: 80 cm, Series, 0 deg
U1 = np.array(
    [
        0,
        2.0,
        4.0,
        6.0,
        7.0,
        8.0,
        9.0,
        9.5,
        10.0,
        10.5,
        11.0,
        11.5,
        12.0,
        12.5,
        13.0,
        13.5,
    ]
)
I1 = np.array(
    [
        27.2,
        27.2,
        27.0,
        26.8,
        26.4,
        26.1,
        25.3,
        24.2,
        23.2,
        21.8,
        19.5,
        16.6,
        12.5,
        7.5,
        2.3,
        0,
    ]
)
P1 = U1 * I1

# Config 2: 60 cm, Parallel, 0 deg
U2 = np.array(
    [0, 0.2, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.36]
)
I2 = np.array(
    [
        181.8,
        181.6,
        181.0,
        180.0,
        179.2,
        177.6,
        174.5,
        170.0,
        165.0,
        157.0,
        143.0,
        120.0,
        88.0,
        50.0,
        13.2,
        0,
    ]
)
P2 = U2 * I2

# Config 3: 60 cm, Series, 30 deg
U3 = np.array(
    [
        0,
        2.0,
        4.0,
        6.0,
        7.0,
        8.0,
        9.0,
        9.5,
        10.0,
        10.5,
        11.0,
        11.5,
        12.0,
        12.5,
        13.0,
        13.46,
    ]
)
I3 = np.array(
    [
        38.7,
        38.5,
        38.3,
        37.8,
        37.4,
        36.9,
        35.8,
        34.8,
        33.5,
        31.3,
        28.0,
        23.4,
        17.2,
        9.8,
        2.3,
        0,
    ]
)
P3 = U3 * I3

idx1 = np.argmax(P1)
idx2 = np.argmax(P2)
idx3 = np.argmax(P3)

# I-V curves
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(U1, I1, "o-", markersize=4, label="Config 1: 80cm Series 0°")
ax.plot(U2, I2, "s-", markersize=4, label="Config 2: 60cm Parallel 0°")
ax.plot(U3, I3, "^-", markersize=4, label="Config 3: 60cm Series 30°")
ax.set_xlabel("Voltage U (V)", fontsize=12)
ax.set_ylabel("Current I (mA)", fontsize=12)
ax.set_title("Solar Cell I-V Characteristics", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "solar_IV_curves.png"), dpi=300, bbox_inches="tight"
)
print("Saved solar_IV_curves.png")
plt.close()

# P-V curves
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(U1, P1, "o-", markersize=4, label="Config 1: 80cm Series 0°")
ax.plot(U2, P2, "s-", markersize=4, label="Config 2: 60cm Parallel 0°")
ax.plot(U3, P3, "^-", markersize=4, label="Config 3: 60cm Series 30°")

for idx, U, P, lbl in [(idx1, U1, P1, "1"), (idx2, U2, P2, "2"), (idx3, U3, P3, "3")]:
    ax.plot(U[idx], P[idx], "*", markersize=12, zorder=5)
    ax.annotate(
        f"Pm={P[idx]:.1f}mW",
        xy=(U[idx], P[idx]),
        xytext=(U[idx] + 0.3, P[idx] + 10),
        fontsize=8,
        arrowprops=dict(arrowstyle="->", lw=0.7),
    )

ax.set_xlabel("Voltage U (V)", fontsize=12)
ax.set_ylabel("Power P (mW)", fontsize=12)
ax.set_title("Solar Cell P-V Characteristics", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "solar_PV_curves.png"), dpi=300, bbox_inches="tight"
)
print("Saved solar_PV_curves.png")
plt.close()

print("All figures generated.")
