using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using RoomLibary;

namespace Rooms
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Room> lstRooms = new List<Room>(); //создание списка
        
        public MainWindow()
        {
            InitializeComponent();
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
        private void BAddRoom_Click(object sender, RoutedEventArgs e)
        {
            Room room = new Room();
            room.RoomLength = Convert.ToDouble(TBLengthR.Text);
            room.RoomWidth = Convert.ToDouble(TBWidthR.Text);
            lstRooms.Add(room); //добавление в список
        }

        private void BAddLivingRoom_Click(object sender, RoutedEventArgs e)
        {
            Livingroom livingroom = new Livingroom();
            livingroom.RoomLength = Convert.ToDouble(TBLengthL.Text);
            livingroom.RoomWidth = Convert.ToDouble(TBWidthL.Text);
            livingroom.NumWin = Convert.ToInt32(TBNumW.Text);
            lstRooms.Add(livingroom);
        }

        private void BAddOffice_Click(object sender, RoutedEventArgs e)
        {
            Office office = new Office();
            office.RoomLength = Convert.ToDouble(TBLengthO.Text);
            office.RoomWidth = Convert.ToDouble(TBWidthO.Text);
            office.NumSockets = Convert.ToInt32(TBNumS.Text);
            lstRooms.Add(office); //добавление в список
        }

        private void BGetList_Click(object sender, RoutedEventArgs e)
        {
            ListRooms.Content = " ";
            //вывод информации из списка
            foreach (Room r in lstRooms)
                ListRooms.Content += r.Info() + "\n";
        }
    }
    

}
