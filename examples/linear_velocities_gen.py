from simulator.generator import linear_interp, seq_generator
from simulator.model import magic_formula
from simulator.utils import subplots_dataset

# System character
m = 300  # mass
g = 9.81  # gravity constant
p = m * g  # weight

# Vehicle velocities breakpoints
freq = 1  # Number of measure / second
step_breakpoint = 10  # DT between two v_vehicle breakpoint
# fmt: off
v_vehicle_breaks = (10, 10, 110, 20, 40, 40, 100, 70, 10, 110, 50, 5, 5, 60, 100, 100,
                    130, 130, 60, 70, 0, 0, 75, 10, 10, 10, 10, 110, 20, 40, 40, 100,
                    70, 10, 110, 50, 5, 5,60, 100, 100, 130, 130, 60, 70, 0, 0, 75, 10,
                    10)
# fmt: on
F_long, alpha = magic_formula(p)

n_train_seq = 1000
seq_generator(
    v_vehicle_breaks,
    n_seq=n_train_seq,
    xp_rand=True,
    func_interp=linear_interp,
    m=m,
    freq=freq,
    step_breakpoint=step_breakpoint,
    F_long=F_long,
    alpha=alpha,
    filename=f"linear_n_seq_{n_train_seq}_step_{step_breakpoint}_freq_{freq}",
    data_dir="../dataset",
)

n_test_seq = 300
seq_generator(
    v_vehicle_breaks,
    n_seq=n_test_seq,
    xp_rand=True,
    func_interp=linear_interp,
    m=m,
    freq=freq,
    step_breakpoint=step_breakpoint,
    F_long=F_long,
    alpha=alpha,
    filename=f"linear_n_seq_{n_test_seq}_step_{step_breakpoint}_freq_{freq}_TEST",
    data_dir="../dataset",
)

subplots_dataset(
    f"../dataset/linear_n_seq_{n_train_seq}_step_{step_breakpoint}_freq_{freq}.csv",
    nrows=4,
    ncols=4,
)
