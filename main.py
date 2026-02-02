from plots import *

if __name__ == '__main__':
    # standard_comparison("img/clock.tiff", "output/clock_4f.pdf", sigma=0.1, num_features=4)
    # standard_comparison("img/clock.tiff", "output/clock_6fspatial.pdf", sigma=0.1, num_features=6)
    standard_comparison("img/man.tiff", "output/man_4f.pdf", sigma=0.2, num_features=4)

    # standard_comparison("img/clock.tiff", "output/clock_4beta.pdf", sigma=0.1, num_features=4, beta=0.70)
    # standard_comparison("img/clock.tiff", "output/clock_4beta2.pdf", sigma=0.1, num_features=4, beta=0.40)