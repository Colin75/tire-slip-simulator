from numpy import arange, asarray, interp, loadtxt, polyfit, polyval, savetxt, zeros
from numpy.random import randint

from simulator.model import slip_velocities


def negative_value_thresholder(velocity):
    """
    Force all negative velocities to zero value.
    """
    velocity[velocity < 0] = 0
    return velocity


def linear_interp(xp, yp):
    x = arange(0.0, xp[-1])
    velocities = interp(x, xp, yp)
    velocities = negative_value_thresholder(velocities)
    return velocities


def polyn_interp(xp, yp):
    x = arange(0.0, xp[-1])
    p = polyfit(xp, yp, deg=int(len(yp) * 0.7))
    velocities = polyval(p, x)
    velocities = negative_value_thresholder(velocities)
    return velocities


def breakpoints_randomize(
    x_breakpoints, y_breakpoints, n_seq, y_delta=30, xp_rand=True, x_delta=5
):
    xp = asarray(x_breakpoints)
    yp = asarray(y_breakpoints)
    sets = zeros([n_seq, 2, len(yp)])
    for i in range(n_seq):
        yp_rand = yp.copy()
        yp_rand[2:-2] += randint(
            -y_delta, y_delta, len(yp) - 4
        )  # Avoid randomization of the two first and last values
        if xp_rand is True:
            xp_rand = xp.copy()
            xp_rand[2:-2] += randint(-x_delta, x_delta, len(xp) - 4)  # Idem
            sets[i] = [xp_rand, negative_value_thresholder(yp_rand)]
        else:
            sets[i] = [xp, negative_value_thresholder(yp_rand)]

    return sets


def wheel_velocities_computer(velocities_vehicle, func_interp, m, freq, F, k):
    velocities_set = zeros(
        [2 * velocities_vehicle.shape[0], int(velocities_vehicle[0][0][-1])]
    )

    for i, set in enumerate(velocities_vehicle):
        velocities_set[i * 2] = func_interp(set[0], set[1])
        velocities_set[(i * 2 + 1)], *_ = slip_velocities(
            velocities_set[i * 2], m, freq, F, k, verbose=False
        )

    return velocities_set


def to_csv(X, filename, **kwargs):
    savetxt(filename, X, delimiter=";", **kwargs)


def read_dataset(filename):
    return loadtxt(filename, delimiter=";")


def batch_dataset(filename, batch_size, seq_size=None):
    if seq_size is None:
        seq_size = -1
    dataset = loadtxt(filename, delimiter=";")
    dataset = dataset[:, :seq_size].reshape(batch_size, 2, seq_size)
    return dataset


def seq_generator(
    y_breakpoints,
    n_seq,
    xp_rand,
    func_interp,
    m,
    freq,
    step_breakpoint,
    F_long,
    alpha,
    filename,
    data_dir="./dataset",
):
    seq_end = int(len(y_breakpoints) * step_breakpoint / freq)
    step = int(step_breakpoint / freq)
    x_breakpoints = [x for x in range(0, seq_end, step)]
    v_vehicle = breakpoints_randomize(
        x_breakpoints, y_breakpoints, n_seq, xp_rand=xp_rand, x_delta=5
    )
    velocities = wheel_velocities_computer(
        v_vehicle, func_interp, m, freq, F_long, alpha
    )
    # TODO : Transfer save csv to other function
    filename = f"{data_dir}/{filename}.csv"
    to_csv(velocities, filename)
