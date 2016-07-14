public class DllExample
{
    [RGiesecke.DllExport.DllExport("add", CallingConvention = System.Runtime.InteropServices.CallingConvention.Cdecl)]
    public static int TestExport(int left, int right)
    {
        return left + right;
    }
}