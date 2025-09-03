/// <summary>
/// This class provides an example of a C# class that can be exported as a DLL
/// and called from native code.
/// </summary>
public class DllExample
{
    /// <summary>
    /// Adds two integers and returns the result. This method is exported as "add".
    /// </summary>
    /// <param name="left">The first integer.</param>
    /// <param name="right">The second integer.</param>
    /// <returns>The sum of the two integers.</returns>
    [RGiesecke.DllExport.DllExport("add", CallingConvention = System.Runtime.InteropServices.CallingConvention.Cdecl)]
    public static int TestExport(int left, int right)
    {
        return left + right;
    }
}