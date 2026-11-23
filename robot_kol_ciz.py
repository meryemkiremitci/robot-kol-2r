import math
import matplotlib.pyplot as plt
from robot_kol import L1, L2, ileri, ters


def ciz(ax, t1, t2, hedef, baslik):
    dirsek, uc = ileri(t1, t2)

    # Ulaşılabilir halka: dış çember L1+L2, iç çember |L1-L2|
    ax.add_patch(plt.Circle((0, 0), L1 + L2, fill=False, ls="--", color="gray"))
    ax.add_patch(plt.Circle((0, 0), abs(L1 - L2), fill=False, ls="--", color="gray"))

    # Kol: taban -> dirsek -> uç nokta
    ax.plot([0, dirsek[0]], [0, dirsek[1]], "-", lw=6, color="tab:blue")
    ax.plot([dirsek[0], uc[0]], [dirsek[1], uc[1]], "-", lw=5, color="tab:purple")
    ax.plot([0, dirsek[0], uc[0]], [0, dirsek[1], uc[1]], "ko", ms=7)

    # Hedef
    ax.plot(*hedef, "rx", ms=12, mew=3)

    ax.set_title(baslik)
    ax.set_aspect("equal")
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.8, 0.8)
    ax.grid(True, alpha=0.3)


hedef = (0.4, 0.3)
cozumler = ters(*hedef)

if not cozumler:
    print("Hedefe ulaşılamıyor.")
else:
    fig, eksenler = plt.subplots(1, len(cozumler), figsize=(5 * len(cozumler), 5))
    for i, (ax, (t1, t2)) in enumerate(zip(eksenler, cozumler), start=1):
        baslik = f"{i}. çözüm: θ1={math.degrees(t1):.2f}°, θ2={math.degrees(t2):.2f}°"
        ciz(ax, t1, t2, hedef, baslik)
    plt.tight_layout()
    plt.savefig("kol.png", dpi=120)
    plt.show()
