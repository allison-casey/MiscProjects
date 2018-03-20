import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys;


def plot_text(x, y, z, text, ax, spacing):
    ax.text(x + spacing, y + spacing, z + spacing, text, None)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.view_init(elev=17, azim=-37)

x = [ 1, 0, 1, 1, 1, 0 ]
y = [ 1, 0, 0, 1, 0, 1 ]
z = [ 1, 0, 0, 1, 0, 1 ]

plot_text(1, 1, 1, 'D1, D4', ax, 0.025)
plot_text(0, 0, 0, 'D2', ax, 0.025)
plot_text(1, 0, 0, 'D3, D5', ax, 0.025)
plot_text(0, 1, 1, 'Query', ax, 0.025)

ax.scatter(x, y, z, s=50)
ax.plot([0, 1], [ 1, 1 ], [ 1, 1 ])
ax.plot([0, 0], [ 1, 0 ], [ 1, 0 ])
ax.plot([0, 1], [ 1, 0 ], [ 1, 0 ])

ax.set_xlim3d(1, 0)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

ax.set_xlabel('Recipes')
ax.set_ylabel('Baking')
ax.set_zlabel('Bread')

#  plt.show()
fig.savefig('baking_bread.png', dpi=300)


