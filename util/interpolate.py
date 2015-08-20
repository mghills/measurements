import bisect

import numpy as np

import util.math.spherical
import util.math.interpolate

import util.logging
logger = util.logging.logger






# class Time_Periodic_Interpolator(util.math.interpolate.Interpolator):
#
#     def __init__(self, data_points, data_values, t_len, wrap_around_amount=0, number_of_linear_interpolators=1, total_overlapping_linear_interpolators=0, t_scaling=1, copy_arrays=True, parallel=False):
#
#         logger.debug('Initiating time periodic interpolator with {} data points, time len {}, wrap around amount {}, {} linear interpolators with total overlapping of {}.'.format(len(data_points), t_len, wrap_around_amount, number_of_linear_interpolators, total_overlapping_linear_interpolators))
#
#         self._t_len = t_len
#         self._wrap_around_amount = wrap_around_amount
#
#         super().__init__(data_points, data_values, number_of_linear_interpolators=number_of_linear_interpolators, total_overlapping_linear_interpolators=total_overlapping_linear_interpolators, scaling_values=(t_scaling, 1, 1, 1), copy_arrays=copy_arrays, parallel=parallel)
#
#         assert len(self._data_points) == len(self._data_values) == len(self._data_indices)
#
#
#     def _prepare_data_values(self, data_values):
#         logger.debug('Wrapping around data values.')
#
#         data_values = data_values[self._data_indices]
#         data_values = super()._prepare_data_values(data_values)
#
#         return data_values
#
#
#     def _modify_points(self, points, is_data_points):
#         ## discard time for periodicity
#         t_len = self._t_len
#         logger.debug('Discarding time of points which is a multiple of {}.'.format(t_len))
#         points[:,0] = points[:,0] % t_len
#
#         ## if data points, wrap around t
#         if is_data_points:
#             points, indices = util.math.interpolate.wrap_around(points, 0, t_len, amount=self._wrap_around_amount, return_also_indices=True)
#             self._data_indices = indices
#
#         return points
#
#
#     def _modify_interpolation_points(self, points):
#         points = self._modify_points(points, False)
#         points = super()._modify_interpolation_points(points)
#         return points
#
#
#     def _modify_data_points(self, points):
#         points = self._modify_points(points, True)
#         points = super()._modify_data_points(points)
#         return points
#
#
#
#
#
#
#
#
#
# class Time_Periodic_Non_Cartesian_Interpolator(Time_Periodic_Interpolator):
#
#     def __init__(self, data_points, data_values, t_len, x_len, t_scale=True, wrap_around_amount=0, number_of_linear_interpolators=1, total_overlapping_linear_interpolators=0, parallel=False):
#
#         logger.debug('Initiating time periodic non spherical interpolator with {} data points, time len {}, x len {}, time scale {}, wrap around amount {} and {} linear interpolators with total overlapping of {}.'.format(len(data_points), t_len, x_len, t_scale, wrap_around_amount, number_of_linear_interpolators, total_overlapping_linear_interpolators))
#
#         assert np.max(data_points[:,0]) - np.min(data_points[:,0]) <= t_len
#         assert np.max(data_points[:,1]) - np.min(data_points[:,1]) <= x_len
#
# #         ## wrap around x
# #         data_points, data_indices = util.math.interpolate.wrap_around(data_points, 1, x_len, amount=wrap_around_amount, return_also_indices=True)
# #         data_values = data_values[data_indices]
# #
# #         ## call super constructor
#
#         self._x_len = x_len
#         if t_scale:
#             t_scaling = x_len / t_len
#         else:
#             t_scaling = 1
#
#         super().__init__(data_points, data_values, t_len, wrap_around_amount=wrap_around_amount, number_of_linear_interpolators=number_of_linear_interpolators, total_overlapping_linear_interpolators=total_overlapping_linear_interpolators, t_scaling=t_scaling, parallel=parallel)
#
# #         ## set indices with x wrap around
# #         self._data_indices = data_indices[self._data_indices]
#
#         assert len(self._data_points) == len(self._data_values) == len(self._data_indices)
#
#
#
#     def _modify_points(self, points, is_data_points):
#         points = super()._modify_points(points, is_data_points)
#
#         ## if data points, wrap around x
#         x_len = self._x_len
#         if is_data_points:
#             points, indices = util.math.interpolate.wrap_around(points, 1, x_len, amount=self._wrap_around_amount, return_also_indices=True)
#             self._data_indices = self._data_indices[indices]
#
#         return points
#



#
# class Time_Periodic_Earth_Interpolator(Time_Periodic_Interpolator):

class Time_Periodic_Earth_Interpolator(util.math.interpolate.Periodic_Interpolator):


    def __init__(self, data_points, data_values, t_len, wrap_around_amount=0, number_of_linear_interpolators=1, total_overlapping_linear_interpolators=0, parallel=False):
        from measurements.constants import EARTH_RADIUS

        logger.debug('Initiating time periodic earth interpolator with {} data points, time len {}, wrap around amount {} and {} linear interpolators with total overlapping of {}.'.format(len(data_points), t_len, wrap_around_amount, number_of_linear_interpolators, total_overlapping_linear_interpolators))

        ## call super constructor
        self.order = number_of_linear_interpolators

        t_scaling = 2 * EARTH_RADIUS / t_len

#         super().__init__(data_points, data_values, t_len, wrap_around_amount=wrap_around_amount, number_of_linear_interpolators=number_of_linear_interpolators, total_overlapping_linear_interpolators=total_overlapping_linear_interpolators, t_scaling=t_scaling, parallel=parallel)

        super().__init__(data_points, data_values, point_range_size=(t_len, None, None, None), wrap_around_amount=(wrap_around_amount, 0, 0, 0),  scaling_values=(t_scaling, None, None, None), number_of_linear_interpolators=number_of_linear_interpolators, total_overlapping_linear_interpolators=total_overlapping_linear_interpolators, parallel=parallel)

#         ## set indices with depth shift
#         self._data_indices = data_indices[self._data_indices]

        assert len(self._data_points) == len(self._data_values) == len(self._data_indices)



    def _modify_points(self, points, is_data_points):
        from measurements.constants import EARTH_RADIUS, MAX_SEA_DEPTH

        points = super()._modify_points(points, is_data_points)

        ## if data points, append values for lower and upper bound of depth
        if self.order > 0 and is_data_points:
            lower_depth = 0
            lower_depth_bound = np.min(points[:,3])
            upper_depth = MAX_SEA_DEPTH
            upper_depth_bound = np.max(points[:,3])

            logger.debug('Lower depth is {}, upper depth is {}.'.format(lower_depth, upper_depth))

            assert lower_depth_bound >= lower_depth and upper_depth_bound <= upper_depth

            if lower_depth_bound > lower_depth:
                # lower_depth_bound_indices = np.where(points[:,3] == lower_depth_bound)[0]
                lower_depth_bound_indices = np.where(np.isclose(points[:,3], lower_depth_bound))[0]
                lower_depth_bound_points = points[lower_depth_bound_indices]
                lower_depth_bound_points[:,3] = lower_depth
                logger.debug('{} values appended for lower bound {}.'.format(len(lower_depth_bound_indices), lower_depth))
            else:
                lower_depth_bound_indices = np.array([])
                lower_depth_bound_points = np.array([])
                logger.debug('No values appended for lower bound {}.'.format(lower_depth))
            if upper_depth_bound < upper_depth:
                # upper_depth_bound_indices = np.where(points[:,3] == lower_depth_bound)[0]
                upper_depth_bound_indices = np.where(np.isclose(points[:,3], lower_depth_bound))[0]
                upper_depth_bound_points = points[upper_depth_bound_indices]
                upper_depth_bound_points[:,3] = upper_depth
                logger.debug('{} values appended for upper bound {}.'.format(len(upper_depth_bound_indices), upper_depth))
            else:
                upper_depth_bound_indices= np.array([])
                upper_depth_bound_points = np.array([])
                logger.debug('No values appended for upper bound {}.'.format(upper_depth))

            indices = np.concatenate((lower_depth_bound_indices, np.arange(len(points)), upper_depth_bound_indices), axis=0)
            points = np.concatenate((lower_depth_bound_points, points, upper_depth_bound_points), axis=0)
            self._data_indices = self._data_indices[indices]

        ## convert to cartesian
        points[:,1:] =  util.math.spherical.to_cartesian(points[:,1:], surface_radius=EARTH_RADIUS)

        return points



## convert coordinates

# #TODO: Remove? -> lsm
# def convert_coordinates_to_map_index(coordinates, map_shape, coordinates_t_len=1):
#
#     result_ndim = coordinates.ndim
#     if coordinates.ndim == 1:
#         coordinates = coordinates[np.newaxis]
#
#     logger.debug('Transforming {} coordinates to indices for map with shape {}'.format(len(coordinates), map_shape))
#     t_dim, x_dim, y_dim, z_values_centered = map_shape
#
#     transformed_coordinates = np.empty(coordinates.shape)
#
#     ## transform each point
#     for i in range(len(coordinates)):
#         t = (coordinates[i, 0] % coordinates_t_len) / coordinates_t_len * t_dim
#
#         x = (coordinates[i, 1] % 360) / 360 * x_dim - 0.5    # center of the box
#
#         ## y
#         # consider lowmost and topmost box (no wrap around)
#         y = (coordinates[i, 2] + 90) / 180 * y_dim  - 0.5    # center of the box
#         if y < 0:
#             y = 0
#         if y > y_dim - 1:
#             y = y_dim - 1
#
#         ## z
#         z = bisect.bisect_left(z_values_centered, coordinates[i, 3])
#         if z > 0:
#             if z < len(z_values_centered):
#                 z += (coordinates[i, 3] - z_values_centered[z-1]) / (z_values_centered[z] - z_values_centered[z-1])   # center of the box
#             z -= 1
#
#         transformed_coordinates[i] = (t, x, y, z)
#
#     if result_ndim == 1:
#         transformed_coordinates = transformed_coordinates[0]
#
#     return transformed_coordinates



## interpolate

def periodic_with_coordinates(data, interpolation_points, lsm_base, interpolator_setup=(0.1, 1, 0.0, 0)):
    assert data.shape[1] == 5

    ## split in points and values
    data_points = data[:, :-1]
    data_values = data[:, -1]

    ## convert point to box indices
#     data_points = convert_coordinates_to_map_index(data_points, (lsm.t_dim, lsm.x_dim, lsm.y_dim, lsm.z_centered))
#     interpolation_points = convert_coordinates_to_map_index(interpolation_points, (lsm.t_dim, lsm.x_dim, lsm.y_dim, lsm.z_centered))
#     def convert_points_to_box_indices(points):
#         points = lsm_base.coordinates_to_map_indices(points)
#         for i in range(len(points)):
#             if points[i, 2] < 0:
#                 points[i, 2] = 0
#             if points[i, 2] < lsm_base.y_dim - 1:
#                 points[i, 2] = 0
#
#         points[points[:, 2] < 0 == 0
    data_points = lsm_base.coordinates_to_map_indices(data_points)
    interpolation_points = lsm_base.coordinates_to_map_indices(interpolation_points)

    ## for y and z set interpolations points to min and max of data
    for k in (2, 3):
        data_points_min = data_points[:,k].min()
        data_points_max = data_points[:,k].max()
        for i in range(len(interpolation_points)):
            if interpolation_points[i,k] < data_points_min:
                interpolation_points[i,k] = data_points_min
            if interpolation_points[i,k] > data_points_max:
                interpolation_points[i,k] = data_points_max


    ## prepare wrap_around_amount
    wrap_around_amount=interpolator_setup[0]
    try:
        wrap_around_amount = tuple(wrap_around_amount)
    except TypeError:
        wrap_around_amount = (wrap_around_amount,)
    if len(wrap_around_amount) == 1:
        ## use same wrap around for t and x
        wrap_around_amount = wrap_around_amount * 2
    if len(wrap_around_amount) == 2:
        ## append wrap around for y and z if missing
        wrap_around_amount = wrap_around_amount + (0,0)

    ## create interpolator
    interpolator = util.math.interpolate.Periodic_Interpolator(data_points, data_values, point_range_size=(lsm_base.t_dim, lsm_base.x_dim, lsm_base.y_dim, lsm_base.z_dim), scaling_values=(lsm_base.x_dim/lsm_base.t_dim, None, None, None), wrap_around_amount=wrap_around_amount, number_of_linear_interpolators=interpolator_setup[1], total_overlapping_linear_interpolators=interpolator_setup[2], parallel=bool(interpolator_setup[3]))

    ## interpolating
    interpolation_data = interpolator.interpolate(interpolation_points)
    return interpolation_data

