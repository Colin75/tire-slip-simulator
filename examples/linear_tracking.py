from simulator import generator as gen

# Vehicle position breakpoints
freq = 1  # Number of measure / second
n_points_interval = 10  # Number of points between two breakpoints
# fmt: off
v_vehicle_breaks = (10, 10, 110, 20, 40, 40, 100, 70, 10, 110, 50, 5, 5, 60, 100, 100,
                    130, 130, 60, 70, 0, 0, 75, 10, 10, 10, 10, 110, 20, 40, 40, 100,
                    70, 10, 110, 50, 5, 5,60, 100, 100, 130, 130, 60, 70, 0, 0, 75, 10,
                    10)

a = gen.seq_generator_tracking(v_vehicle_breaks,
                               n_seq=10,
                               func_interp=gen.linear_interp,
                               freq=1.,
                               n_points_interval=10,
                               xp_rand=True)
