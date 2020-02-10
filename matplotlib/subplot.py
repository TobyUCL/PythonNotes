"""
Create a subplot
"""
# If only plotting in 1 dimension
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, sharex=True, sharey=True)
axes[0].imshow(image_1)
axes[1].imshow(image_2)
axes[2].imshow(image_3)
plt.show()

# If plotting in 2
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
axes[0,0].imshow(image_1a)
axes[1,0].imshow(image_2a)
axes[0,1].imshow(image_1b)
axes[1,1].imshow(image_2b)
plt.show()


# plot 3 gray images to the same scale with colourbar and no axis and labels 
fig, axes = plt.subplots(1, 3, sharex=True, sharey=True)
plot_min = 0
plot_max = 1
plot_colours = 'gray'

im = axes[0].imshow(image_1, vmin = plot_min, vmin = plot_max, cmap = plot_colours)
axes[0].axis('off')
axes[0].title.set_text("image 1")

axes[1].imshow(image_15[0], vmin = plot_min, vmin = plot_max, cmap = plot_colours)
axes[1].axis('off')
axes[1].title.set_text("image 2")

axes[2].imshow(np.abs(diff_image[0]), vmin = plot_min, vmin = plot_max, cmap = plot_colours)
axes[2].axis('off')
axes[2].title.set_text("image 3")

fig.colorbar(im, ax=axes.ravel().tolist())

plt.show()

