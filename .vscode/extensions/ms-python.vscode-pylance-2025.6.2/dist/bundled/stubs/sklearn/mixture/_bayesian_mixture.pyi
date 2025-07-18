from typing import ClassVar, Literal

from numpy import ndarray
from numpy.random import RandomState

from .._typing import ArrayLike, Float, Int
from ._base import BaseMixture

# Author: Wei Xue <xuewei4d@gmail.com>
#         Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

class BayesianGaussianMixture(BaseMixture):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    covariance_prior_: float | ArrayLike = ...
    degrees_of_freedom_: ArrayLike = ...
    degrees_of_freedom_prior_: float = ...
    mean_prior_: ArrayLike = ...
    mean_precision_: ArrayLike = ...
    mean_precision_prior_: float = ...
    weight_concentration_: ArrayLike = ...
    weight_concentration_prior_: float | tuple = ...
    lower_bound_: float = ...
    n_iter_: int = ...
    converged_: bool = ...
    precisions_cholesky_: ArrayLike = ...
    precisions_: ArrayLike = ...
    covariances_: ArrayLike = ...
    means_: ArrayLike = ...
    weights_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_components: Int = 1,
        covariance_type: Literal["full", "tied", "diag", "spherical"] = "full",
        tol: Float = 1e-3,
        reg_covar: Float = 1e-6,
        max_iter: Int = 100,
        n_init: Int = 1,
        init_params: Literal["kmeans", "k-means++", "random", "random_from_data"] = "kmeans",
        weight_concentration_prior_type: Literal["dirichlet_process", "dirichlet_distribution"] = "dirichlet_process",
        weight_concentration_prior: None | Float = None,
        mean_precision_prior: None | Float = None,
        mean_prior: None | ArrayLike = None,
        degrees_of_freedom_prior: None | Float = None,
        covariance_prior: float | None | ArrayLike = None,
        random_state: RandomState | None | Int = None,
        warm_start: bool = False,
        verbose: Int = 0,
        verbose_interval: Int = 10,
    ) -> None: ...
