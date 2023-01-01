import ctypes
mainC = ctypes.cdll.LoadLibrary(r"layla\main.so")

def math(input):
    return mainC.eval("2+2")