import math

L1, L2 = 0.4, 0.3


def ileri(t1, t2):
    """Açılar (radyan) -> dirsek ve uç nokta koordinatları."""
    dx, dy = L1 * math.cos(t1), L1 * math.sin(t1)
    ux = dx + L2 * math.cos(t1 + t2)   # toplam açı: t1 + t2
    uy = dy + L2 * math.sin(t1 + t2)
    return (dx, dy), (ux, uy)


def ters(x, y, tol=1e-9):
    """Hedef (x, y) -> [(t1, t2), ...] iki çözüm; ulaşılamıyorsa boş liste."""
    c2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(c2) > 1 + tol:                 # önce ulaşılabilirlik
        return []
    c2 = max(-1.0, min(1.0, c2))          # sonra küçük yuvarlama hatasını kırp
    cozumler = []
    for s2 in (+math.sqrt(1 - c2**2), -math.sqrt(1 - c2**2)):
        t2 = math.atan2(s2, c2)
        phi = math.atan2(y, x)
        beta = math.atan2(L2 * s2, L1 + L2 * c2)
        cozumler.append((phi - beta, t2))
    return cozumler


if __name__ == "__main__":
    for hedef in [(0.4, 0.3), (0.8, 0.0)]:
        print("Hedef:", hedef)
        cozumler = ters(*hedef)
        if not cozumler:
            print("  Ulaşılamaz\n")
            continue
        for t1, t2 in cozumler:
            _, uc = ileri(t1, t2)
            print(f"  t1={math.degrees(t1):7.2f}  t2={math.degrees(t2):7.2f}"
                  f"  -> uç nokta ({uc[0]:.3f}, {uc[1]:.3f})")
        print()
