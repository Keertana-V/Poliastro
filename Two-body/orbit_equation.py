import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 500)
p = 1.0

eccentricities = [0, 0.3, 0.7, 1.0, 1.5]

plt.figure(figsize=(7, 7))
for e in eccentricities:
    r = p / (1 + e * np.cos(theta))
    r = np.where((r > 0) & (r < 10), r, np.nan)  # also cut off huge near-singularity spikes
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y, label=f"e = {e}")

plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.gca().set_aspect("equal")
plt.xlim(-6, 4)
plt.ylim(-5, 5)
plt.legend()
plt.title("Orbit shapes for varying eccentricity")
plt.show()