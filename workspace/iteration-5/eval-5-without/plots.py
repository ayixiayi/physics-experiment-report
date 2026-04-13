import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

plt.rcParams["font.sans-serif"] = [
    "SimHei",
    "WenQuanYi Micro Hei",
    "Noto Sans CJK SC",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False

output_dir = os.path.dirname(os.path.abspath(__file__))

# Data
Im_mA = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450])
U_mV = np.array([0, 22.15, 44.20, 66.30, 88.44, 110.30, 132.25, 154.24, 176.47, 198.50])

mu0 = 4 * np.pi * 1e-7
N = 3000
L = 0.260
B_mT = mu0 * N * (Im_mA * 1e-3) / L * 1e3

slope, intercept, r_value, _, _ = stats.linregress(B_mT, U_mV)
K = slope
print(f"K = {K:.2f} V/T, R² = {r_value**2:.6f}")

# Plot 1: U vs B
fig, ax = plt.subplots(figsize=(8, 6))
B_fit = np.linspace(0, B_mT.max() * 1.05, 100)
ax.scatter(B_mT, U_mV, c="blue", label="data")
ax.plot(B_fit, slope * B_fit + intercept, "r-", label=f"fit: K={K:.2f} V/T")
ax.set_xlabel("B (mT)")
ax.set_ylabel("U (mV)")
ax.set_title("Hall Sensor Sensitivity")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "hall_fit.png"), dpi=200)
plt.close()

# Plot 2: B(x)
x_cm = np.arange(-14, 15)
U0 = 2.514
U_x = np.array(
    [
        2.534,
        2.538,
        2.545,
        2.558,
        2.575,
        2.598,
        2.622,
        2.642,
        2.654,
        2.659,
        2.660,
        2.660,
        2.660,
        2.660,
        2.660,
        2.659,
        2.658,
        2.654,
        2.644,
        2.625,
        2.600,
        2.577,
        2.560,
        2.545,
        2.536,
        2.528,
        2.522,
        2.518,
        2.516,
    ]
)
B_x = (U_x - U0) / K * 1000

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x_cm, B_x, "bo-", markersize=4, label="B(x) measured")
ax.set_xlabel("x (cm)")
ax.set_ylabel("B (mT)")
ax.set_title("Solenoid B(x) Distribution")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "bx_distribution.png"), dpi=200)
plt.close()

print("Done.")
