using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laba
{
    internal class Program
    {
        static void Main(string[] args)
        {
           double z=Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(Math.Abs(z));
            double x =Convert.ToDouble(Console.ReadLine());
            Console.WriteLine(Math.Max(x,z));
            Console.WriteLine(Math.Sqrt(z));
            Console.WriteLine(Math.Truncate(x));
        }
    }
}
