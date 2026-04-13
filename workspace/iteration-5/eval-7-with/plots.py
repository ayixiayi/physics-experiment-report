import numpy as np
import matplotlib.pyplot as plt
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

# ===== Data: 3 configurations =====

# Config 1: 80 cm, 4 series, 0°
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
P1 = U1 * I1  # mW

# Config 2: 60 cm, 4 parallel, 0°
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

# Config 3: 60 cm, 4 series, 30°
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

# Pm points
idx1 = np.argmax(P1)
idx2 = np.argmax(P2)
idx3 = np.argmax(P3)

print(f"Config 1 Pm = {P1[idx1]:.1f} mW at U = {U1[idx1]:.1f} V")
print(f"Config 2 Pm = {P2[idx2]:.1f} mW at U = {U2[idx2]:.1f} V")
print(f"Config 3 Pm = {P3[idx3]:.1f} mW at U = {U3[idx3]:.1f} V")

# ===== Plot 1: I-V curves =====
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(
    U1,
    I1,
    "o-",
    color="#1f77b4",
    markersize=4,
    linewidth=1.5,
    label="配置1: 80cm 串联 0°",
)
ax.plot(
    U2,
    I2,
    "s-",
    color="#ff7f0e",
    markersize=4,
    linewidth=1.5,
    label="配置2: 60cm 并联 0°",
)
ax.plot(
    U3,
    I3,
    "^-",
    color="#2ca02c",
    markersize=4,
    linewidth=1.5,
    label="配置3: 60cm 串联 30°",
)

# Mark key points
ax.annotate(
    f"Isc={I1[0]:.1f}mA",
    xy=(U1[0], I1[0]),
    xytext=(1.5, I1[0] + 1),
    fontsize=8,
    color="#1f77b4",
    arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=0.8),
)
ax.annotate(
    f"Uoc={U1[-1]:.1f}V",
    xy=(U1[-1], I1[-1]),
    xytext=(U1[-1] - 2.5, I1[-1] + 3),
    fontsize=8,
    color="#1f77b4",
    arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=0.8),
)

ax.set_xlabel("电压 U (V)", fontsize=12)
ax.set_ylabel("电流 I (mA)", fontsize=12)
ax.set_title("太阳电池 I-V 特性曲线", fontsize=14)
ax.legend(fontsize=10, loc="best")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "solar_IV_curves.png"), dpi=300, bbox_inches="tight"
)
print("Saved solar_IV_curves.png")
plt.close()

# ===== Plot 2: P-V curves with Pm marked =====
fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(
    U1,
    P1,
    "o-",
    color="#1f77b4",
    markersize=4,
    linewidth=1.5,
    label="配置1: 80cm 串联 0°",
)
ax.plot(
    U2,
    P2,
    "s-",
    color="#ff7f0e",
    markersize=4,
    linewidth=1.5,
    label="配置2: 60cm 并联 0°",
)
ax.plot(
    U3,
    P3,
    "^-",
    color="#2ca02c",
    markersize=4,
    linewidth=1.5,
    label="配置3: 60cm 串联 30°",
)

# Mark Pm points
for idx, U, P, color, label in [
    (idx1, U1, P1, "#1f77b4", "配置1"),
    (idx2, U2, P2, "#ff7f0e", "配置2"),
    (idx3, U3, P3, "#2ca02c", "配置3"),
]:
    ax.plot(U[idx], P[idx], "*", color=color, markersize=14, zorder=5)
    ax.annotate(
        f"Pm={P[idx]:.1f}mW\n({U[idx]:.1f}V)",
        xy=(U[idx], P[idx]),
        xytext=(U[idx] + 0.5, P[idx] + 15),
        fontsize=8,
        color=color,
        arrowprops=dict(arrowstyle="->", color=color, lw=0.8),
    )

ax.set_xlabel("电压 U (V)", fontsize=12)
ax.set_ylabel("功率 P (mW)", fontsize=12)
ax.set_title("太阳电池 P-V 特性曲线", fontsize=14)
ax.legend(fontsize=10, loc="best")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "solar_PV_curves.png"), dpi=300, bbox_inches="tight"
)
print("Saved solar_PV_curves.png")
plt.close()

print("\nAll figures generated successfully.")
