# Python ctypes with .NET DLL Example

This project is a simple example of how to call a function in a .NET DLL from Python using the `ctypes` library.

The project consists of two parts:
1.  A C# DLL (`DllExample`) that exports a simple `add` function.
2.  A Python script (`pyCTypesDotNETDLL`) that loads the DLL and calls the `add` function.

## Building the DLL

To build the C# DLL, you will need to have a .NET development environment set up. This typically means having Visual Studio installed on Windows.

1.  Open the `pyCTypesDotNETDLL.sln` file in Visual Studio.
2.  Select the `Debug` and `x86` configuration.
3.  Build the solution (F6 or Build > Build Solution).

This will create the `DllExample.dll` file in the `DllExample/bin/x86/Debug/` directory.

**Note:** An attempt to build the DLL in an automated environment without the necessary .NET build tools failed. Ensure you have a proper .NET development environment to build the DLL.

## Running the Python Script

Once the DLL has been built, you can run the Python script:

```bash
python pyCTypesDotNETDLL/pyCTypesDotNETDLL.py
```

The script will load the DLL, call the `add` function, and print the result and the time it took to execute.

## Dependencies

### C#
- The C# project uses the `UnmanagedExports` NuGet package to export the `add` function in a way that can be called from native code.

### Python
- The Python script uses the built-in `ctypes` library. No external packages are needed.
