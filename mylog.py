""" Robert Gonzalez logging decorator """
from __future__ import print_function
import time
import sys
from functools import wraps
import datetime


def log(*log_file):
    def log2(func):
        @wraps(func)
        def log_wrap(*fp):
            if log_file:
                if str(type(log_file[0]).__name__) == 'str':
                    sys.stdout = open(log_file[0], 'a')
            print("***********************************************************")
            print("Calling function \'" + str(func.__name__) + "\' at " + str(datetime.datetime.now()) + ".")
            print("Arguments: ")
            for arg in fp:
                fp_type = type(arg)
                print("    " + str(arg) + " of type " + str(fp_type.__name__))
            #print("Output: ")
            #print("    ", end='')
            start = time.time()
            ret = func(*fp)
            end = time.time()
            time_func = end - start
            print("Execution time: %.5f s." % time_func)
            if ret is None:
                print("No return value.")
            else:
                ret_type = type(ret)
                #print("Return value: " + str(ret) + " of type " + str(ret_type.__name__) + ".")
                print("Return value of type " + str(ret_type.__name__) + ".")
            print("***********************************************************")
            return ret
        return log_wrap
    return log2

