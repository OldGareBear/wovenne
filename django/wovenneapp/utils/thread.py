from __future__ import absolute_import
import thread
import logging

def in_new_thread(inner):
    def outer(*args, **kwargs):
        try:
            thread.start_new_thread(inner, args, kwargs)
        except Exception, e:
            logging.warning(e)
    return outer