﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RoomLibrary
{
    public class Room
    {
        double roomLength; //длина комнаты
        double roomWidth; // ширина комнаты

        public double RoomLength
        { 
            get { return roomLength; } 
            set { roomLength = value; } 
        }
        public double RoomWidth
        { 
            get { return roomWidth; } 
            set { roomWidth = value; }
        }
        /// <summary>
        /// Метод вычисляет периметр комнаты
        /// </summary>
        /// <returns> Возвращает значение периметра </returns>
        public double RoomPerimeter()
        {
            return 2 * (roomLength + roomWidth);
        }
        /// <summary>
        /// Метод вычисляет площадь комнаты
        /// </summary>
        /// <returns> Возвращает значение площади </returns>
        public double RoomArea()
        {
            return roomLength * roomWidth;
        }
        /// <summary>
        /// Метод вычисляет число квадратных метров на одного человека
        /// </summary>
        /// <param name="np"> Число человек</param>
        /// <returns>Возвращает число квадратных метров</returns>
        public double PersonArea(int np)
        {
            return RoomArea() / np;
        }
        

    }
}
