# Gaussian Mixture Models Explained<sup>[1]</sup>

## K-means vs GMM

| K-means        | GMM        |
| -----------  | -----------  |
| Hard clustering method | Soft clustering method |
| Lack of flexibility in cluster shape (i.e. only circular boundary) | Cluster boundary could be ellpises rather than circles |
| Lack of probabilistic cluster assignment | Measure uncertainty in cluster assignment by comparing the distance of each point to **all cluster centers** |


## Definitions

- A Gaussian mixture model (GMM) attempts to find a mixture of multi-dimensional Gaussian probability distributions that best model any input dataset. 
- Let's say there are `K` clusters in the dataset. Each Gaussian (cluster) `k` in the mixture is comprised of the following parameters:
    - $\mu$ defines the center of a cluster
    - $\Sigma$ defines the `width` of the cluster
    - $\pi$ defines the probability that a point belongs to this cluster


## Expectation — Maximization (EM) algorithm

1. Choose starting guesses for the location and shape

2. Repeat until converged

    1. `E-step`: for each point, find weights encoding the probability of membership in each cluster. (Create a heuristic of the posterior distribution and the log-likelihood using the current estimate for the parameters)

    2. `M-step`: for each cluster, update its location, normalization, and shape based on all data points, making use of weights. (Compute parameters by maximizing the expected log-likelihood from the E step)


## GMM for Generating New Data<sup>[2]</sup>

1. Use GMM to model the distribution of the given dataset

2. Sample new data points from the distribution just generated

## References
[1] O. C. Carrasco, “Gaussian Mixture Models Explained,” Medium, Feb. 21, 2020. https://towardsdatascience.com/gaussian-mixture-models-explained-6986aaf5a95

[2] J. VanderPlas, “In Depth: Gaussian Mixture Models | Python Data Science Handbook,” Github.io, 2019. https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html
