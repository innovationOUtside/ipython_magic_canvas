"""Canvas magic"""
__version__ = '0.0.1'

from .canvas import CanvasMagic

def load_ipython_extension(ipython):
    ipython.register_magics(CanvasMagic)