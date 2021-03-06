import os.path

from ..constants import ANALYSIS_DIR

MIN_MEASUREMENTS_NORMALIZED = 5
SEPARATION_VALUES_NORMALIZED = [1./365., 1, 1, [0, 25, 50, 85, 120, 170, 220, 290, 360, 455, 550, 670, 790, 935, 1080, 1250, 1420, 1615, 1810, 2030, 2250, 2495, 2740, 3010, 3280, 3575, 3870, 4190, 4510, 6755, 9000]]
MEASUREMENTS_NORMALIZED_DICT_FILE = os.path.join(ANALYSIS_DIR, 'measurement_normalized_dict.ppy')


CORRELOGRAM_DIRNAME = 'correlogram'
CORRELOGRAM_JOB_OUTPUT_DIRNAME_PREFIX = 'direction_'
CORRELOGRAM_JOB_DIRECTION_FILENAME = 'direction.npy'
CORRELOGRAM_JOB_CORRELOGRAM_FILENAME = 'correlogram.npy'

CORRELATION_JOB_DIRECTION = (1/52., 0.5, 0.5, 20)
CORRELATION_JOB_OUTPUT_DIRNAME_PREFIX = 'correlation/t_factor_'
CORRELATION_JOB_MIN_MEASUREMENTS = 100
CORRELATION_JOB_CORRELATION_FILENAME = 'correlation.npy'

SAME_BOUNDS = (1/(365.0 * 8), 0.1, 0.1, 10)
DIM_RANGES = ((1920, 2015), (-180, 180), (-90, 90), (0, 9000))


from measurements.constants import BASE_DIR
PYTHON_DIR = os.path.join(BASE_DIR, 'python')


# ## old stuff
#
#
# T_RANGE = (0, 1)
# X_RANGE = (-180, 180)
#
#
# SEPARATION_VALUES = (1/(365.0*2.0),)
#
# SEPARATION_VALUES_DISCARD_YEAR = (1/(365.0*8.0),)
# SAME_BOUNDS_DISCARD_YEAR = (1/(365.0*2.0), 0.2, 0.2, 10)
# DIM_RANGES_DISCARD_YEAR = ((0, 1), (-180, 180), (-90, 90), (0, 9000))
#
# CORRELOGRAM_DIRNAME = 'correlogram'
# CORRELOGRAM_JOB_OUTPUT_DIRNAME_PREFIX = 'direction_'
# CORRELOGRAM_JOB_DIRECTION_FILENAME = 'direction.npy'
# CORRELOGRAM_JOB_CORRELOGRAM_FILENAME = 'correlogram.npy'
#
# CORRELATION_JOB_DIRECTION = (1/52., 0.5, 0.5, 20)
# CORRELATION_JOB_OUTPUT_DIRNAME_PREFIX = 'correlation/t_factor_'
# CORRELATION_JOB_MIN_MEASUREMENTS = 100
# CORRELATION_JOB_CORRELATION_FILENAME = 'correlation.npy'





# P1_OPT = [0.31370216, 0.73684415, 0.77861289, 0.9937939]
# P1E_OPT = [0.08886658, 0.22455463, 0.39680138, 0.97862766, 0.39641933]
# P2_OPT = [1.47978141, 0.47940142, 0.34635459, 0.00937349]
# P2E_OPT = [3.60201342, 2.62436568, 1.23911104, 0.03378583, 0.37666791]
# P22_OPT = [1.47978141, 0.47940142, 0.34635459, 0.00937349, 0, 0, 0, 0]
# P22E_OPT = [3.60201342, 2.62436568, 1.23911104, 0.03378583, 0, 0, 0, 0, 0.37666791]
# P3_OPT = [9.15750079e-01, 8.00021898e-03, 1.25993544e-02, 4.03705505e-04]
# P3E_OPT = [5.62891846e+01, 4.91756224e-01, 7.74455168e-01, 2.48149077e-02, 9.83731332e-01]
# P_1_2_OPT =  [1., 1., 1., 1., 1.47978139, 0.47940143, 0.3463546, 0.00937349]
# P_1E_2E_OPT = [6.01230014e-01, 6.48987031e-01, 7.72822921e-01, 9.85380860e-01, 3.52985614e-01, 1.07493121e+03, 1.35453975e+04, 5.52384948e+00, 1.89169056e-04, 7.73659598e-01]
# P_1E_2E_E_OPT = [6.01230014e-01, 6.48987031e-01, 7.72822921e-01, 9.85380860e-01, 3.52985614e-01, 1.07493121e+03, 1.35453975e+04, 5.52384948e+00, 1.89169056e-04, 7.73659598e-01, 0]
# P_1_3_OPT =  [0.31370216, 0.73684415, 0.77861289, 0.9937939, 0, 0, 0, 0]
# P_1E_3E_OPT = [9.14224170e+00, 2.37754190e+01, 2.92737995e+00, 7.49105905e-02, 5.49624665e-01, 0.00000000e+00, 5.68506062e-01, 1.03955749e+00, 2.18176774e-02, 9.88532818e-01]
# P_2_3_OPT =  [1.47978141, 0.47940142, 0.34635459, 0.00937349, 0, 0, 0, 0]
# P_2E_3E_OPT = [1.0e-08, 1.0e-08, 6.45314364e-02, 9.27795445e-01, 6.68034494e-01,   0, 7.55962350e-01, 1.34565816e+00, 3.19713187e-02, 9.90460830e-01]

# P1E_OPT = [0.95083429, 0.64123166, 0.73152487, 0.98556788, 0.45747902, 0.43047404]
# P2E_OPT = [0.05819369, 0.55155303, 0.3305381 , 0.01903545, 0.85978221, 0.37650682]