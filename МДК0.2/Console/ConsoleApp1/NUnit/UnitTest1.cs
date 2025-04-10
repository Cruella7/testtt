using NUnit.Framework;
using System.IO;
using System;

namespace HelloWorld.Tests
{
    public class Tests
    {
        private const string Expected = "Hello World!";
        [SetUp]
        public void SetUp()
        {

        }
        [Test]
        public void Test1()
        {
            //Assert.Pass();
            using (var sw = new StringWriter())
            {
                Console.SetOut(sw);
                ConsoleApp1.Program.Main();

                var result = sw.ToString().Trim();
                Assert.AreEqual(Expected, result);
            }
        }
    }
}
