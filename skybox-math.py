import numpy as np

def main(star_vector: np.array):
    return star_vector / np.linalg.norm(star_vector)

if __name__ == "__main__":
    print(main(np.array([1,2,3])))
    pass
