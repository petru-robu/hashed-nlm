import numpy as np
from scipy import ndimage
import cv2


def load_image(path, fallback_size=(100, 100)):
    """
    Load an image from the specified path.
    """
    img = cv2.imread(path, 0)
    if img is None:
        img = np.zeros(fallback_size)
        cv2.circle(img, (50, 50), 30, 1, -1)
    return img.astype(np.float64) / 255.0


def convert_to_grayscale(img):
    """
    Converts an RGB image to grayscale using the luminosity method.
    """
    if len(img.shape) < 3:
        return img

    weights = np.array([0.2989, 0.5870, 0.1140])
    return np.dot(img[..., :3], weights)


def add_noise(normalized_img, sigma):
    """
    Add Gaussian noise of sigma deviation to the normalized img.
    """
    noise = np.random.normal(0, sigma, normalized_img.shape)
    noisy_img = normalized_img + noise
    return np.clip(noisy_img, 0, 1)


def mse(imgA, imgB):
    """
    Computes the Mean Squared Error between two images.
    """
    err = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
    err /= float(imgA.shape[0] * imgA.shape[1])
    return err
