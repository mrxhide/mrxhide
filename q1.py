import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Fungsi untuk menggambar gelas 3D
def draw_glass():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Membuat data untuk gelas
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Menggambar permukaan gelas
    ax.plot_surface(x, y, z, color='c', alpha=0.7)

    # Menampilkan plot
    plt.show()

# Memanggil fungsi untuk menggambar gelas
draw_glass()
