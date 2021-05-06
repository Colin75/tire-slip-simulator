from simulator import generator as gen
from simulator.generator import to_csv
from simulator.utils import subplots_dataset

freq = 1  # Number of measure / second
n_points_interval = 20  # Number of points between two breakpoints
n_seq = 1000
# fmt: off
positions = (10, 10, 110, 20, 40, 40, 100, 70, 10, 110, 50, 5, 5, 60, 100, 100,
             130, 130, 60, 70, 0, 0, 75, 10, 10, 10, 10, 110, 20, 40, 40, 100,
             70, 10, 110, 50, 5, 5, 60, 100, 100, 130, 130, 60, 70, 0, 0, 75, 10,
             10, 10)

dataset = gen.seq_generator_tracking(positions,
                                     n_seq=1000,
                                     func_interp=gen.linear_interp,
                                     freq=1.,
                                     n_points_interval=n_points_interval,
                                     xp_rand=True)

to_csv(dataset, f'./dataset/tracking_seq_{n_seq}_points_{n_points_interval*(len(positions)-1)}.csv')

# subplots_dataset(
#     f"./test.csv",
#     nrows=3,
#     ncols=3,
# )
