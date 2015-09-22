if __name__ == "__main__":
    import argparse
    import multiprocessing
    import socket
    
    import measurements.all.pw_nearest.correlation
    import measurements.util.correlation
    
    import util.logging
    logger = util.logging.logger

    ## configure arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min_values', type=int)
    parser.add_argument('-y', '--max_year_diff', type=int, default=-1)
    parser.add_argument('-l', '--max_land_boxes', type=int, default=0)
    parser.add_argument('-r', '--reorder', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true', help='Print debug infos.')
    args = parser.parse_args()

    ## run
    with util.logging.Logger(disp_stdout=args.debug):
        logger.debug('Running on {}.'.format(socket.gethostname()))

        if args.max_year_diff < 0:
            args.max_year_diff = float('inf')

        correlation_model = measurements.all.pw_nearest.correlation.CorrelationMatrix(min_values=args.min_values, max_year_diff=args.max_year_diff, max_land_boxes=args.max_land_boxes, no_data_correlation=0, return_type=measurements.util.correlation.RETURN_QUANTITY_AND_CORRELATION, positive_definite_approximation_reorder_after_each_step=args.reorder)
        correlation_model.correlation_matrix_cholesky_decomposition
