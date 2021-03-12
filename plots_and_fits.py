from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def do_boxplot_save(dat):
    """ Does the boxplots, saves results for the given data."""
    
    return


def do_scatterplot_save(dat):
    """ Does the scatterplots, saves results for the given data."""
    return


def main():

    cloud_df = read_csv("clouds.csv")

    do_boxplot_save()
    do_scatterplot_save()

    # Linear regression fit
    lin_model = LinearRegression().fit(X,y)
    lin_model.coef_
    lin_model.intercept_
    LinearRegression().score(X,y)
    
    return


if __name__ == "__main__":
    main()
