import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Chinese font support
plt.rcParams["font.sans-serif"] = [
    "SimHei",
    "WenQuanYi Micro Hei",
    "Noto Sans CJK SC",
    "Arial Unicode MS",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False

output_dir = os.path.dirname(os.path.abspath(__file__))

# ===== Experiment 1: K measurement (U vs B linear fit) =====
Im_mA = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450])
U_mV = np.array([0, 22.15, 44.20, 66.30, 88.44, 110.30, 132.25, 154.24, 176.47, 198.50])

# Solenoid parameters
mu0 = 4 * np.pi * 1e-7  # T·m/A
N = 3000
L = 0.260  # m

# Calculate B for each Im
Im_A = Im_mA * 1e-3
B_T = mu0 * N * Im_A / L
B_mT = B_T * 1e3  # mT

# Linear fit: U(mV) vs B(mT) -> slope = K in mV/mT = V/T
slope, intercept, r_value, p_value, std_err = stats.linregress(B_mT, U_mV)
R2 = r_value**2
K_exp = slope  # V/T (since mV/mT = V/T)

print(f"Linear fit: U = {slope:.4f} * B + ({intercept:.4f})")
print(f"R² = {R2:.6f}")
print(f"K_exp = {K_exp:.2f} V/T")
print(f"Er = {abs(K_exp - 31.25) / 31.25 * 100:.1f}%")

# Plot 1: U vs B linear fit
fig, ax = plt.subplots(figsize=(8, 6))
B_fit = np.linspace(0, B_mT.max() * 1.05, 200)
U_fit = slope * B_fit + intercept

ax.scatter(B_mT, U_mV, c="blue", s=50, zorder=5, label="实验数据")
ax.plot(
    B_fit,
    U_fit,
    "r-",
    linewidth=1.5,
    label=f"线性拟合: U = {slope:.2f}B + ({intercept:.2f})\n$R^2$ = {R2:.6f}",
)
ax.set_xlabel("磁感应强度 B (mT)", fontsize=12)
ax.set_ylabel("霍尔电压 U (mV)", fontsize=12)
ax.set_title(f"霍尔传感器灵敏度测量 (K = {K_exp:.2f} V/T)", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "hall_UB_fit.png"), dpi=300, bbox_inches="tight")
print(f"Saved hall_UB_fit.png")
plt.close()

# ===== Experiment 2: B(x) distribution =====
x_cm = np.arange(-14, 15)  # -14 to +14
U0 = 2.514  # V (zero-field offset)
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

# Convert to B using K_exp
delta_U_V = U_x - U0  # in V
B_exp_mT = delta_U_V / K_exp * 1000  # convert V/(V/T) = T -> mT

# Theoretical B(x) for finite solenoid
Im_exp2 = 0.20  # A
x_m = x_cm * 1e-2  # convert to meters
L_half = L / 2  # half length of solenoid
R_sol = 0.035 / 2  # radius of solenoid (D=35mm)

# B(x) = (mu0 * N * I) / (2L) * [cos(theta1) + cos(theta2)]
# theta1 = angle from x to left end, theta2 = angle from x to right end
# cos(theta) = (L/2 + x) / sqrt((L/2 + x)^2 + R^2) for left end
# cos(theta) = (L/2 - x) / sqrt((L/2 - x)^2 + R^2) for right end
x_theory = np.linspace(-0.14, 0.14, 500)
cos_theta1 = (L_half + x_theory) / np.sqrt((L_half + x_theory) ** 2 + R_sol**2)
cos_theta2 = (L_half - x_theory) / np.sqrt((L_half - x_theory) ** 2 + R_sol**2)
B_theory = mu0 * N * Im_exp2 / (2 * L) * (cos_theta1 + cos_theta2) * 1000  # mT

# Scale theoretical curve to match experiment (account for K calibration)
# Actually, let's compute theoretical B at center for comparison
B_theory_center = (
    mu0 * N * Im_exp2 / (2 * L) * 2 * L_half / np.sqrt(L_half**2 + R_sol**2) * 1000
)
B_exp_center = B_exp_mT[14]  # x=0 is index 14
print(f"\nB(x=0) experimental: {B_exp_center:.3f} mT")
print(f"B(x=0) theoretical (finite solenoid): {B_theory_center:.3f} mT")

# Plot 2: B(x) distribution
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x_cm, B_exp_mT, c="blue", s=30, zorder=5, label="实验测量值")
ax.plot(
    x_theory * 100,
    B_theory,
    "r-",
    linewidth=1.5,
    alpha=0.8,
    label="有限长螺线管理论曲线",
)

# Mark solenoid boundaries
ax.axvline(x=-13, color="gray", linestyle="--", alpha=0.5, label="螺线管端面 (±13 cm)")
ax.axvline(x=13, color="gray", linestyle="--", alpha=0.5)

ax.set_xlabel("轴线位置 x (cm)", fontsize=12)
ax.set_ylabel("磁感应强度 B (mT)", fontsize=12)
ax.set_title("螺线管轴线磁场分布 ($I_m$ = 0.20 A)", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "hall_Bx_distribution.png"), dpi=300, bbox_inches="tight"
)
print(f"Saved hall_Bx_distribution.png")
plt.close()

print("\nAll figures generated successfully.")
