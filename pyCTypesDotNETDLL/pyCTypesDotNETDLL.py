"""
This module provides an example of how to call a C# DLL from Python.
It uses the ctypes library to load the DLL and call a function.
"""
import ctypes
import time

def main():
    """
    This script demonstrates calling a C# DLL from Python using ctypes.
    It calls an 'add' function in the DLL and times the execution.
    """
    try:
        lib = ctypes.cdll.LoadLibrary('../DllExample/bin/x86/Debug/DllExample.dll')
    except OSError as e:
        print(f"Error loading DLL: {e}")
        print("Please ensure that the DllExample.dll has been built and is in the correct path.")
        return

    # Time the call to the add function in the C# DLL
    start = time.perf_counter()
    result_from_dll = lib.add(3, 5)
    end = time.perf_counter()
    print(f"lib.add(3, 5) = {result_from_dll}")
    print(f"Time taken for DLL call: {end - start:.6f}s")

    # Time the native Python addition
    start = time.perf_counter()
    result_from_python = 3 + 5
    end = time.perf_counter()
    print(f"3 + 5 = {result_from_python}")
    print(f"Time taken for native Python addition: {end - start:.6f}s")

if __name__ == "__main__":
    main()