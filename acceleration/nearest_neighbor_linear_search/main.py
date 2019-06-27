import ctypes
from ctypes import cdll

lib = cdll.LoadLibrary('./nearest')

lib.Init.argtypes = []
lib.Init.restype = ctypes.c_void_p

lib.Run.argtypes = [ctypes.c_void_p]

obj = lib.Init(5)
lib.Run(obj)
