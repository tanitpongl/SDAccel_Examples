import ctypes
from ctypes import cdll,c_float

lib = cdll.LoadLibrary('./nearest')

lib.Init.argtypes = []
lib.Init.restype = ctypes.c_void_p

lib.Run.argtypes = [ctypes.c_void_p,c_float,c_float,c_float]

obj = lib.Init(5)
lib.Run(obj,89.221,4.2,41.5)
