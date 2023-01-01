from ctypes import c_float
import ctypes
mainC = ctypes.cdll.LoadLibrary(r"layla\Ccode\main.so")
mainC.eval.restype = c_float

def math(input):
    x = input.encode('utf-8')
    return mainC.eval(x)