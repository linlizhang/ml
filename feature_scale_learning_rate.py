import numpy as np
import matplotlib.pyplot as plt
from sympy import true

from lab_utils_multi import load_house_data, run_gradient_descent
from lab_utils_multi import norm_plot, plt_equal_scale,plot_cost_i_w
from lab_utils_common import dlc
np.set_printoptions(precision=2)

X_train, y_train = load_house_data()
X_features = ['size(sqft)','bedrooms','floors','age']

fig, ax = plt.subplots(1, 4, figsize=(12, 3), sharey=true)
for i in range(len(ax)):
    ax[i].scatter(X_train[:, i], y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("Price(1000's)")
# plt.show()

_, _, hist = run_gradient_descent(X_train, y_train, 1000, 9.9e-7, )
# plot_cost_i_w(X_train, y_train, hist)

def zscore_normalize_features(X):
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)

    X_norm = (X - mu) /sigma

    return (X_norm, mu, sigma)

X_norm, X_mu, X_sigma = zscore_normalize_features(X_train)

w_norm, b_norm, hist = run_gradient_descent(X_norm, y_train, 1000, 1.0e-1, )
