import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split

def main():
    #Pre-processing
    iris = load_iris()
    print (iris)


if __name__ == "__main__":
    main()