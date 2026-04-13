import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams["font.sans-serif"] = [
    "SimHei",
    "WenQuanYi Micro Hei",
    "Noto Sans CJK SC",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False

output_dir = os.path.dirname(os.path.abspath(__file__))


def deg_min_to_decimal(deg, minute):
    return deg + minute / 60.0


# ===== Reflection Method =====
theta1 = [
    deg_min_to_decimal(20, 2),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 2),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 2),
]
theta1_p = [
    deg_min_to_decimal(200, 1),
    deg_min_to_decimal(200, 0),
    deg_min_to_decimal(200, 1),
    deg_min_to_decimal(200, 1),
    deg_min_to_decimal(200, 0),
    deg_min_to_decimal(200, 1),
]
theta2 = [
    deg_min_to_decimal(260, 3),
    deg_min_to_decimal(260, 2),
    deg_min_to_decimal(260, 3),
    deg_min_to_decimal(260, 2),
    deg_min_to_decimal(260, 2),
    deg_min_to_decimal(260, 3),
]
theta2_p = [
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 1),
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 1),
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 3),
]

# α = ½ × [(360° - (θ₂ - θ₁)) + (360° - (θ₂′ adjusted))]
# Simpler: φ_A = θ₂ - θ₁ (mod 360), if > 180 take 360 - φ_A to get 2α
alpha_reflection = []
for i in range(6):
    phi_A = theta2[i] - theta1[i]
    if phi_A < 0:
        phi_A += 360
    two_alpha_A = 360 - phi_A if phi_A > 180 else phi_A

    phi_B = theta2_p[i] - theta1_p[i]
    if phi_B < 0:
        phi_B += 360
    two_alpha_B = 360 - phi_B if phi_B > 180 else phi_B

    alpha_i = 0.5 * (two_alpha_A + two_alpha_B) / 2
    # Actually: each vernier gives 2α, average the two verniers, then /2
    # Correct: α = average of (two_alpha_A/2, two_alpha_B/2)
    alpha_i = 0.5 * (two_alpha_A / 2 + two_alpha_B / 2)
    alpha_reflection.append(alpha_i)

alpha_ref_arr = np.array(alpha_reflection)
mean_ref = np.mean(alpha_ref_arr)
std_ref = np.std(alpha_ref_arr, ddof=1)

print("=== 反射法 ===")
for i, a in enumerate(alpha_ref_arr):
    d = int(a)
    m = (a - d) * 60
    print(f"  第{i + 1}次: α = {d}°{m:.1f}'")
d = int(mean_ref)
m = (mean_ref - d) * 60
print(f"  平均: α = {d}°{m:.1f}' ± {std_ref * 60:.2f}' (1σ)")

# ===== Autocollimation Method =====
t1 = [
    deg_min_to_decimal(18, 45),
    deg_min_to_decimal(18, 44),
    deg_min_to_decimal(18, 47),
    deg_min_to_decimal(18, 46),
    deg_min_to_decimal(18, 45),
    deg_min_to_decimal(18, 46),
]
t1_p = [
    deg_min_to_decimal(198, 45),
    deg_min_to_decimal(198, 44),
    deg_min_to_decimal(198, 48),
    deg_min_to_decimal(198, 46),
    deg_min_to_decimal(198, 45),
    deg_min_to_decimal(198, 47),
]
t2 = [
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
]
t2_p = [
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
]

alpha_auto = []
for i in range(6):
    diff_A = t2[i] - t1[i]
    if diff_A < 0:
        diff_A += 360
    alpha_A = 180 - diff_A / 2

    diff_B = t2_p[i] - t1_p[i]
    if diff_B < 0:
        diff_B += 360
    alpha_B = 180 - diff_B / 2

    alpha_i = 0.5 * (alpha_A + alpha_B)
    alpha_auto.append(alpha_i)

alpha_auto_arr = np.array(alpha_auto)
mean_auto = np.mean(alpha_auto_arr)
std_auto = np.std(alpha_auto_arr, ddof=1)

print("\n=== 自准法 ===")
for i, a in enumerate(alpha_auto_arr):
    d = int(a)
    m = (a - d) * 60
    print(f"  第{i + 1}次: α = {d}°{m:.1f}'")
d = int(mean_auto)
m = (mean_auto - d) * 60
print(f"  平均: α = {d}°{m:.1f}' ± {std_auto * 60:.2f}' (1σ)")

Er_ref = abs(mean_ref - 60) / 60 * 100
Er_auto = abs(mean_auto - 60) / 60 * 100
print(f"\n反射法 Er = {Er_ref:.4f}%")
print(f"自准法 Er = {Er_auto:.4f}%")

# ===== Plot 1: Reflection method results =====
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

measurements = np.arange(1, 7)
alpha_ref_min = (alpha_ref_arr - 59) * 60  # offset from 59° in arcminutes

axes[0].bar(measurements, alpha_ref_min, color="#4C72B0", alpha=0.8, width=0.6)
axes[0].axhline(
    y=(mean_ref - 59) * 60,
    color="red",
    linestyle="--",
    linewidth=1.5,
    label=f"平均值: {int(mean_ref)}°{(mean_ref - int(mean_ref)) * 60:.1f}'",
)
axes[0].axhline(
    y=60, color="green", linestyle=":", linewidth=1.5, label="标称值: 60°0'"
)
axes[0].set_xlabel("测量次数", fontsize=12)
axes[0].set_ylabel("α - 59° (角分)", fontsize=12)
axes[0].set_title("反射法测量结果", fontsize=14)
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3, axis="y")
axes[0].set_xticks(measurements)

alpha_auto_min = (alpha_auto_arr - 59) * 60

axes[1].bar(measurements, alpha_auto_min, color="#55A868", alpha=0.8, width=0.6)
axes[1].axhline(
    y=(mean_auto - 59) * 60,
    color="red",
    linestyle="--",
    linewidth=1.5,
    label=f"平均值: {int(mean_auto)}°{(mean_auto - int(mean_auto)) * 60:.1f}'",
)
axes[1].axhline(
    y=60, color="green", linestyle=":", linewidth=1.5, label="标称值: 60°0'"
)
axes[1].set_xlabel("测量次数", fontsize=12)
axes[1].set_ylabel("α - 59° (角分)", fontsize=12)
axes[1].set_title("自准法测量结果", fontsize=14)
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3, axis="y")
axes[1].set_xticks(measurements)

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "reflection_method.png"), dpi=300, bbox_inches="tight"
)
print("\nSaved reflection_method.png")
plt.close()

# ===== Plot 2: Method comparison =====
fig, ax = plt.subplots(figsize=(8, 5))

methods = ["反射法", "自准法"]
means_min = [(mean_ref - 59) * 60, (mean_auto - 59) * 60]
errs_min = [std_ref / np.sqrt(6) * 60 * 2, std_auto / np.sqrt(6) * 60 * 2]  # 2σ

bars = ax.bar(
    methods,
    means_min,
    yerr=errs_min,
    capsize=8,
    color=["#4C72B0", "#55A868"],
    alpha=0.8,
    width=0.5,
    edgecolor="black",
    linewidth=0.5,
)
ax.axhline(y=60, color="red", linestyle="--", linewidth=1.5, label="标称值 60°0'")
ax.set_ylabel("α - 59° (角分)", fontsize=12)
ax.set_title("两种方法测量结果对比 (误差棒为 2σ)", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis="y")

for bar, mean_val, err_val in zip(bars, means_min, errs_min):
    total_deg = 59 + mean_val / 60
    d = int(total_deg)
    m = (total_deg - d) * 60
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + err_val + 0.02,
        f"{d}°{m:.1f}' ± {err_val:.1f}'",
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "autocollimation_method.png"), dpi=300, bbox_inches="tight"
)
print("Saved autocollimation_method.png")
plt.close()

print("\nAll figures generated successfully.")
