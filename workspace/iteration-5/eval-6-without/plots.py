"""Goniometer experiment data processing - without skill guidance."""

import numpy as np
import matplotlib.pyplot as plt


def deg_min_to_decimal(deg, minute):
    """Convert degree-minute to decimal degrees."""
    return deg + minute / 60.0


# Reflection method data
theta1 = [
    deg_min_to_decimal(20, 2),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 2),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 1),
    deg_min_to_decimal(20, 2),
]
theta1p = [
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
theta2p = [
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 1),
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 1),
    deg_min_to_decimal(80, 2),
    deg_min_to_decimal(80, 3),
]

# Reflection method: alpha = (360 - (theta2 - theta1))/2 averaged with other vernier
alpha_ref = []
for i in range(6):
    d1 = theta2[i] - theta1[i]
    phi1 = 360.0 - d1
    a1 = phi1 / 2.0

    d2 = theta2p[i] - theta1p[i]
    if d2 < 0:
        d2 += 360.0
    phi2 = 360.0 - d2
    a2 = phi2 / 2.0

    alpha_ref.append((a1 + a2) / 2.0)

# Autocollimation method data
t1_ac = [
    deg_min_to_decimal(18, 45),
    deg_min_to_decimal(18, 44),
    deg_min_to_decimal(18, 47),
    deg_min_to_decimal(18, 46),
    deg_min_to_decimal(18, 45),
    deg_min_to_decimal(18, 46),
]
t1p_ac = [
    deg_min_to_decimal(198, 45),
    deg_min_to_decimal(198, 44),
    deg_min_to_decimal(198, 48),
    deg_min_to_decimal(198, 46),
    deg_min_to_decimal(198, 45),
    deg_min_to_decimal(198, 47),
]
t2_ac = [
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
    deg_min_to_decimal(258, 46),
    deg_min_to_decimal(258, 45),
]
t2p_ac = [
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
    deg_min_to_decimal(78, 45),
    deg_min_to_decimal(78, 44),
]

alpha_ac = []
for i in range(6):
    d1 = t2_ac[i] - t1_ac[i]
    d2 = t2p_ac[i] - t1p_ac[i]
    if d2 < 0:
        d2 += 360.0
    a1 = 180.0 - d1 / 2.0
    a2 = 180.0 - d2 / 2.0
    alpha_ac.append((a1 + a2) / 2.0)

# Print results
print("Reflection method alpha values (degrees):")
for i, a in enumerate(alpha_ref):
    deg = int(a)
    minute = (a - deg) * 60
    print(f"  #{i + 1}: {deg}°{minute:.1f}'")
print(
    f"  Mean: {np.mean(alpha_ref):.6f}° = {int(np.mean(alpha_ref))}°{(np.mean(alpha_ref) - int(np.mean(alpha_ref))) * 60:.1f}'"
)

print("\nAutocollimation method alpha values (degrees):")
for i, a in enumerate(alpha_ac):
    deg = int(a)
    minute = (a - deg) * 60
    print(f"  #{i + 1}: {deg}°{minute:.1f}'")
print(
    f"  Mean: {np.mean(alpha_ac):.6f}° = {int(np.mean(alpha_ac))}°{(np.mean(alpha_ac) - int(np.mean(alpha_ac))) * 60:.1f}'"
)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

measurements = np.arange(1, 7)

# Reflection
axes[0].plot(measurements, alpha_ref, "bo-", markersize=8, label="Measured")
axes[0].axhline(y=60.0, color="r", linestyle="--", label="Nominal 60°")
axes[0].set_xlabel("Measurement #")
axes[0].set_ylabel("Alpha (degrees)")
axes[0].set_title("Reflection Method")
axes[0].legend()
axes[0].set_ylim(59.95, 60.05)
axes[0].grid(True, alpha=0.3)

# Autocollimation
axes[1].plot(measurements, alpha_ac, "rs-", markersize=8, label="Measured")
axes[1].axhline(y=60.0, color="b", linestyle="--", label="Nominal 60°")
axes[1].set_xlabel("Measurement #")
axes[1].set_ylabel("Alpha (degrees)")
axes[1].set_title("Autocollimation Method")
axes[1].legend()
axes[1].set_ylim(59.95, 60.05)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("goniometer_results.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nSaved: goniometer_results.png")
