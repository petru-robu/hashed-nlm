import matplotlib.pyplot as plt
from helpers import *
from hashnlm import *


def standard_comparison(img_path, output_path, sigma=0.07, num_features=4, beta=0.88):
    # noise std
    original_image = load_image(path=img_path)
    original_image = convert_to_grayscale(original_image)
    noisy_image = add_noise(original_image, sigma)

    # denoising
    denoised_image = denoise_hashnlm(noisy_image, sigma, num_features, beta)

    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.imshow(original_image, cmap='gray')
    plt.title("Original (Clean)")
    plt.subplot(132)
    plt.imshow(noisy_image, cmap='gray')
    plt.title(
        f"Noisy (sigma={sigma}) MSE = {mse(original_image, noisy_image):.4f}")
    plt.subplot(133)
    plt.imshow(denoised_image, cmap='gray')
    plt.title(
        f"Denoised MSE = {mse(original_image, denoised_image):.4f}")

    plt.suptitle(
        f"Hashed NLM sigma={sigma}, beta={beta}, #features={num_features}")

    # plt.tight_layout()
    plt.savefig(output_path)
