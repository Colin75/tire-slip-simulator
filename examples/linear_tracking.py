from simulator import generator as gen
from simulator.generator import to_csv
from simulator.viz import subplots_dataset_tracking

freq = 1  # Number of measure / second
n_points_interval = 20  # Number of points between two breakpoints
n_seq = 1000
# fmt: off
positions = (10, 10, 30, 50, 80, 90, 110, 100, 110, 80, 65, 50, 55, 70, 100, 90, 70, 30,
             10, 15, 25, 60, 70, 55, 45, 40, 35, 5, 5, 30, 35, 40, 60, 100, 100, 130,
             130, 110, 60, 70, 65, 45, 10, 0, 0, 10, 45, 50, 70, 30, 10, 10, 10, 40,
             110, 100, 130, 90, 100, 70, 40, 20, 10, 40, 10, 30, 10, 50, 80, 70, 65, 50,
             60, 100, 100, 130, 130, 85, 65, 55)

dataset = gen.seq_generator_tracking(positions,
                                     n_seq=1000,
                                     func_interp=gen.linear_interp,
                                     freq=1.,
                                     n_points_interval=n_points_interval,
                                     xp_rand=True)

to_csv(dataset, f'./dataset/tracking_seq_{n_seq}_points_{n_points_interval*(len(positions)-1)}.csv')

subplots_dataset_tracking(
    f"./dataset/tracking_seq_{n_seq}_points_{n_points_interval*(len(positions)-1)}.csv",
    n_rows=2,
    n_cols=2,
)
