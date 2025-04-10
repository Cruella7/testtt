using Microsoft.VisualStudio.TestTools.UnitTesting;
using ClassLibraryPassword;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibraryPassword.Tests
{
    [TestClass()]
    public class PasswordCheckerTests
    {
        [TestMethod()]
        public void Check_8Symbols_ReturnsTrue()
        {
            //Arrange.
            string password = "ASqw123a$$";
            bool expected = true;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);
            
            //Assert.
            Assert.AreEqual(expected, actual);
        }

        [TestMethod()]
        public void Check_4Symbols_ReturnsFalse()
        {
            //Arrange.
            string password = "Aq1$";

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.IsFalse(actual);
        }


        [TestMethod()]
        public void Check_30Symbols_ReturnsFalse()
        {
            //Arrange.
            string password = "ASDqwe123$ASDqwe123$ASDqwe123$";
            bool expected = false;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithDigts_ReturnsTrue()
        {
            //Arrange.
            string password = "ASDqwe1$";
            bool expected = true;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithoutDigts_ReturnsFalse()
        {
            //Arrange.
            string password = "ASDqweASD$";
            bool expected = false;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }

        [TestMethod()]
        public void Check_PasswordWithSpecSymbols_ReturnsTrue()
        {
            //Arrange.
            string password = "Aqwe123$";
            bool expected = true;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithoutSpecSymbols_ReturnsFalse()
        {
            //Arrange.
            string password = "ASDqwe123";
            bool expected = false;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithCapSymbols_ReturnsTrue()
        {
            //Arrange.
            string password = "Aqwe123$";
            bool expected = true;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithoutCapsSymbols_ReturnsFalse()
        {
            //Arrange.
            string password = "asdqwe123$";
            bool expected = false;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithLowerSymbols_ReturnsTrue()
        {
            //Arrange.
            string password = "ASDq123$";
            bool expected = true;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }


        [TestMethod()]
        public void Check_PasswordWithoutLowerSymbols_ReturnsFalse()
        {
            //Arrange.
            string password = "ASDQWE123$";
            bool expected = false;

            //Act.
            bool actual = PasswordChecker.ValidatePassword(password);

            //Assert.
            Assert.AreEqual(expected, actual);
        }
    }
}