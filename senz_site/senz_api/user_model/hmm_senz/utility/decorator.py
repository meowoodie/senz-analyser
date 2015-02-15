__author__ = 'woodie'

import time
import senz_api.hmm_senz.utility.exception as exception
from functools import wraps


class SenzDecorator:

    @classmethod
    def funcLogger(cls, func):
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = func(*args, **kwargs)
            te = time.time()
            print "   ---- func logger ----"
            print "   * function  = {0}".format(func.__name__)
            print "   * arguments = {0} {1}".format(args, kwargs)
            print "   * return    = {0}".format(result)
            print "   * time      = %.6f sec" % (te - ts)
            return result
        return wrapper

    @classmethod
    def validHMM(cls, func):
        def wrapper(*args, **kwargs):
            print "Here check hmm's param validation."
            result = func(*args, **kwargs)
            return result

        return wrapper

