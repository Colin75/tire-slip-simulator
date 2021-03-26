from simulator.generator import polyn_interp, seq_generator
from simulator.model import magic_formula
from simulator.utils import subplots_dataset

# Model parameters
m = 300  # mass
g = 9.81  # gravity constant
p = m * g  # weight

# wheel velocity breakpoints
freq = 1  # Number of measure per second
step_breakpoint = 20  # DT between two v_vehicle_break
# fmt: off
yp = (10, 10, 90, 30, 30, 120, 100, 80, 10, 80, 50, 70)
# fmt: on
F_long, alpha = magic_formula(p)

seq_generator(
    yp,
    n_seq=1500,
    xp_rand=True,
    func_interp=polyn_interp,
    m=m,
    freq=freq,
    point_per_step=step_breakpoint,
    F_long=F_long,
    alpha=alpha,
    filename=f"dataset_poly_step_{step_breakpoint}_freq_{freq}",
    data_dir="../dataset",
)

seq_generator(
    yp,
    n_seq=500,
    xp_rand=True,
    func_interp=polyn_interp,
    m=m,
    freq=freq,
    point_per_step=step_breakpoint,
    F_long=F_long,
    alpha=alpha,
    filename=f"dataset_poly_step_{step_breakpoint}_freq_{freq}_TEST",
    data_dir="../dataset",
)

subplots_dataset("./dataset/dataset_poly_step_20_freq_1.csv", nrows=4, ncols=4)
