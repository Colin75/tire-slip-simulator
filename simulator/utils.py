from matplotlib.pyplot import subplots
from numpy import loadtxt, ndarray
from numpy.random import choice


def subplots_dataset(filename, nrows=4, ncols=4):
    # TODO : adapt x-axis tick
    fig, axes = subplots(nrows, ncols, figsize=(5 * nrows, 5 * ncols))
    if isinstance(filename, str):
        dataset = loadtxt(filename, delimiter=";")
        dataset = dataset.reshape((-1, 2, dataset.shape[1]))
    elif isinstance(filename, ndarray):
        dataset = filename
    else:
        raise TypeError("Input type is not recognize.")

    nsets = dataset.shape[0]
    naxes = min(nrows * ncols, nsets)

    for i in range(naxes):
        i_random = choice(range(0, nsets - 1, 2))
        v_vehicle = dataset[i_random, 0]
        v_wheel = dataset[i_random, 1]

        ax = axes[i // nrows, i % ncols]
        ax.plot(v_vehicle, "g-", label="v_vehicle")
        ax.plot(v_wheel, "m--", label="v_wheel")
        ax.set(xlabel="t [s]", ylabel="v [km/s]")
        ax_twin = ax.twinx()
        ax_twin.plot(v_vehicle - v_wheel, "r:", label="Δv")
        # Add both axes's label on same box (stackoverflow.com/a/10129461)
        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax_twin.get_legend_handles_labels()
        ax_twin.legend(lines + lines2, labels + labels2, loc=0)
    fig.show()
