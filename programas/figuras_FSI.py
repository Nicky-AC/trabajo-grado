"""Figuras del capitulo 3 a partir de las salidas de FSI_Particionado.edp.

Uso: python figuras.py <carpeta_datos> <prefijo> <carpeta_salida>
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

datos, pref, salida = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
salida.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif", "font.size": 10, "axes.titlesize": 10,
    "axes.edgecolor": "#555555", "axes.linewidth": 0.6,
    "xtick.color": "#555555", "ytick.color": "#555555",
})


def leer_msh(ruta):
    tok = ruta.read_text().split()
    nv, nt = int(tok[0]), int(tok[1])
    i = 3
    xy = np.array(tok[i:i + 3 * nv], float).reshape(nv, 3)[:, :2]
    i += 3 * nv
    tri = np.array(tok[i:i + 4 * nt], int).reshape(nt, 4)[:, :3] - 1
    return mtri.Triangulation(xy[:, 0], xy[:, 1], tri)


tf = leer_msh(datos / f"{pref}_fluido.msh")
u1, u2, p = np.loadtxt(datos / f"{pref}_fluido_campos.txt").T
ts = leer_msh(datos / f"{pref}_solido.msh")
d1, d2 = np.loadtxt(datos / f"{pref}_solido_campos.txt").T

# --- Figura 1: velocidad (vectores) y presion (mapa de color) -------------
# La presion es singular en las esquinas de la pared impulsora; la escala de
# color se recorta a los percentiles 2-98 para que el interior sea legible.
lim = np.percentile(np.abs(p), 98)
fig, ax = plt.subplots(figsize=(5.6, 5.0))
cf = ax.tricontourf(tf, np.clip(p, -lim, lim), levels=np.linspace(-lim, lim, 25),
                    cmap="RdBu_r", extend="both")
xg, yg = np.meshgrid(np.linspace(0.25, 9.75, 20), np.linspace(-9.75, -0.4, 20))
interp1 = mtri.LinearTriInterpolator(tf, u1)
interp2 = mtri.LinearTriInterpolator(tf, u2)
ug, vg = interp1(xg, yg), interp2(xg, yg)
ax.quiver(xg, yg, ug, vg, color="#222222", scale=12, width=0.0028)
ax.set_aspect("equal")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
cb = fig.colorbar(cf, ax=ax, shrink=0.85)
cb.set_label("Presión $p$ (media cero)")
fig.tight_layout()
fig.savefig(salida / "FSI_velocidad_presion.png", dpi=220)
plt.close(fig)

# --- Figura 2: desplazamiento vertical de la viga --------------------------
amp = 5.0
tsd = mtri.Triangulation(ts.x + amp * d1, ts.y + amp * d2, ts.triangles)
fig, ax = plt.subplots(figsize=(6.4, 2.4))
cf = ax.tripcolor(tsd, np.abs(d2), shading="gouraud", cmap="Blues")
ax.plot([0, 10, 10, 0, 0], [0, 0, 2, 2, 0], color="#888888", lw=0.8, ls="--")
ax.set_aspect("equal")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
cb = fig.colorbar(cf, ax=ax, shrink=0.9)
cb.set_label("$|d_y|$")
fig.tight_layout()
fig.savefig(salida / "FSI_desplazamiento_viga.png", dpi=220)
plt.close(fig)

# --- Figura 3: malla deformada cerca de la interfaz ------------------------
fig, ax = plt.subplots(figsize=(6.4, 3.0))
ax.triplot(tf, color="#3a5f8a", lw=0.35)
ax.set_xlim(0, 10); ax.set_ylim(-3.0, 0.2)
ax.set_aspect("equal")
ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
fig.tight_layout()
fig.savefig(salida / "FSI_malla_deformada.png", dpi=220)
plt.close(fig)

print("min d_y =", d2.min(), " en x =", ts.x[np.argmin(d2)])
print("p rango:", p.min(), p.max(), " recorte +-", lim)
