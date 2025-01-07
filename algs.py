import pandas as pd
import numpy as np
from sklearn import datasets


def main():
    print("hello")
    df = pd.read_csv('combine_data_2000-2018.csv')
    print(df)


if __name__ == "__main__":
    main()