import matplotlib.pyplot as plt
import numpy as np
def plot_rangeAng(Xcube, rng_grid, agl_grid):
    Xpow = np.abs(Xcube)
    Xpow = np.squeeze(np.sum(Xpow, axis=2) / Xpow.shape[2])

    Xsnr = Xpow

    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(yvalue, xvalue, np.transpose(Xsnr), cmap='jet')
    agl_grid2,rng_grid2 = np.meshgrid(agl_grid,rng_grid)
    ax.plot_surface(agl_grid2,rng_grid2, Xsnr, cmap='jet')
    # ax.view_init(90, 0)
    # ax.set_xlim(-60, 60)
    # ax.set_ylim(2, 25)
    ax.set_xlabel('Angle of arrival (degrees)')
    ax.set_ylabel('Range (meters)')
    ax.set_zlabel('Amplitude')
    ax.set_title('Range-Angle heatmap')
    plt.savefig('RF_image1.png')
    plt.close(fig)


    index = []
    index_amount = 20
    tick = (agl_grid.size-1) / index_amount
    for i in range(index_amount+1):
        index.append(round(tick*i))

    plt.figure()
    plt.imshow(Xsnr[::-1], cmap='jet')
    plt.xticks(index, agl_grid[index].round().astype('int'), rotation=90);
    plt.yticks(index, rng_grid[index[::-1]].round().astype('int'), rotation=0);
    plt.xlabel('Angle of arrival (degrees)')
    plt.ylabel('Range (meters)')
    plt.title('Range-Angle heatmap')
    plt.savefig('RF_image2.png')
    plt.close()