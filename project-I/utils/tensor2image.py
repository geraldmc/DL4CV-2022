import numpy as np
from PIL import Image
from torchvision import transforms
import matplotlib.patches as patches
import matplotlib.pyplot as plt


def imshow(img, title=None):
    """Imshow for Tensor."""
    img = img.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img = std * img + mean
    img = np.clip(img, 0, 1)
    plt.imshow(img)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated
    
def imshow_frame(img, img_frame, tensor=False):
    fig, ax = plt.subplots(1)
    if tensor:
        ax.imshow(img.permute(1, 2, 0))
    else:
        ax.imshow(img)
    rect = patches.Rectangle((img_frame[0],img_frame[1]),
                             img_frame[2]-img_frame[0],
                             img_frame[3]-img_frame[1],
                             linewidth=1, edgecolor='#00ff00',facecolor='none')
    ax.add_patch(rect)
    plt.show()