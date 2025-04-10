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

namespace ToursApp
{
    /// <summary>
    /// Логика взаимодействия для HotelsPage.xaml
    /// </summary>
    public partial class HotelsPage : Page
    {
        public HotelsPage()
        {
            InitializeComponent();
            //DGridHotels.ItemsSource = TourBaseEntities.GetContext().Hotels.ToList();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
        }


        

        private void BtnEdit_Click(object sender, RoutedEventArgs e)
        {

            Manger.MainFrame.Navigate(new AddEditPage((sender as Button).DataContext as Hotel ));
        }

        private void BtnDelete_Click(object sender, RoutedEventArgs e)
        {
            var hotelsForRemoving = DGridHotels.SelectedItems.Cast<Hotel>().ToList();

            if (MessageBox.Show($"Вы точно хотите удалить следующие {hotelsForRemoving.Count()} элементов?", "Внимание!", 
                MessageBoxButton.YesNo, MessageBoxImage.Question) == MessageBoxResult.Yes)

         {
                try
                {
                    TourBaseEntities.GetContext().Hotels.RemoveRange(hotelsForRemoving);
                    TourBaseEntities.GetContext().SaveChanges();
                    MessageBox.Show("Данные удалины!");

                    DGridHotels.ItemsSource = TourBaseEntities.GetContext().Hotels.ToList();
                }       
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message.ToString());
                }
         }   

        }

        private void BtnAdd_Click(object sender, RoutedEventArgs e)
        {
            Manger.MainFrame.Navigate(new AddEditPage(null));
        }

        private void Page_IsVisibleChanged(object sender, DependencyPropertyChangedEventArgs e)
        {
            if (Visibility == Visibility.Visible)
            {
                TourBaseEntities.GetContext().ChangeTracker.Entries().ToList().ForEach(p => p.Reload());
                DGridHotels.ItemsSource = TourBaseEntities.GetContext().Hotels.ToList();

            }
        }
    }
}