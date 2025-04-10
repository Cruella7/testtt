using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Text
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Ensure that text is currently selected in the text box.   
            if (richTextBox1.SelectedText != "")
                // Cut the selected text in the control and paste it into the Clipboard.
                richTextBox1.Cut();
        }

        private void buttonOpen_Click_1_Click(object sender, EventArgs e)
        {

            if (openFileDialog1.ShowDialog() == DialogResult.OK) //Проверяем был ли выбран файл
            {
                richTextBox1.Clear(); //Очищаем richTextBox
                openFileDialog1.Filter = "Text Files (*.txt)|*.txt"; //Указываем что нас интересуют
                                                                     //только текстовые файлы
                string fileName = openFileDialog1.FileName; //получаем наименование файл и путь к
                                                            //нему.
                richTextBox1.Text = File.ReadAllText(fileName, Encoding.GetEncoding(1251)); //Передаем
                                                                                            //содержимое файла в richTextBox
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {

            saveFileDialog1.Filter = "Text Files|*.txt";//Задаем доступные расширения
            saveFileDialog1.DefaultExt = ".txt"; //Задаем расширение по умолчанию
                                                 // 3
            if (saveFileDialog1.ShowDialog() == DialogResult.OK) //Проверяем подтверждение
                                                                 //сохранения информации.
            {
                var name = saveFileDialog1.FileName; //Задаем имя файлу
                File.WriteAllText(name, richTextBox1.Text, Encoding.GetEncoding(1251)); //Записываем
                                                                                        // в файл содержимое textBox с кодировкой 1251
            }
            richTextBox1.Clear();

        }


        private void поЦентруToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Select(); // выравнивание только выделенного текста
                                   //richTextBox1.SelectAll(); //выделение всего текста
            richTextBox1.SelectionAlignment = HorizontalAlignment.Center;
            //richTextBox1.DeselectAll(); //Отмена выделения


        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Ensure that text is selected in the text box.   
            //richTextBox1.SelectionLength > 0)
            if (richTextBox1.SelectionLength > 0)
                // Copy the selected text to the Clipboard.
                richTextBox1.Copy();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (Clipboard.GetDataObject().GetDataPresent(DataFormats.Text) == true)
            {
                // Determine if any text is selected in the text box.
                if (richTextBox1.SelectionLength > 0)
                {
                    // Ask user if they want to paste over currently selected text.
                    if (MessageBox.Show("Do you want to paste over current selection?", "Cut Example", MessageBoxButtons.YesNo) == DialogResult.No)
                        // Move selection to the point after the current selection and paste.
                        richTextBox1.SelectionStart = richTextBox1.SelectionStart + richTextBox1.SelectionLength;
                }
                // Paste current text in Clipboard into text box.
                richTextBox1.Paste();
            }
        }

        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            Font myFont = new Font("Tahoma", 12, FontStyle.Regular, GraphicsUnit.Pixel);
            string Hello = "Hello World!";
            e.Graphics.DrawString(Hello, myFont, Brushes.Black, 20, 20);
        }

        private void настройкаПринтераToolStripMenuItem_Click(object sender, EventArgs e)
        {
            pageSetupDialog1.ShowDialog();
        }

        private void предварительныйПросмотрToolStripMenuItem_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.ShowDialog();
        }

        private void печататьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (printDialog1.ShowDialog() == DialogResult.OK) printDocument1.Print();
        }

        private void оПрограммеToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            AboutBox1 from = new AboutBox1();
            from.Show();
            this.Hide();




        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Clear()
        {
            throw new NotImplementedException();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectionStart = 0;
            richTextBox1.SelectAll();
        }


        private void button6_Click(object sender, EventArgs e)
        {
            {
                ColorDialog MyDialog = new ColorDialog();
                // Keeps the user from selecting a custom color.
                MyDialog.AllowFullOpen = false;
                // Allows the user to get help. (The default is false.)
                MyDialog.ShowHelp = true;
                // Sets the initial color select to the current text color.
                MyDialog.Color = richTextBox1.ForeColor;

                // Update the text box color if the user clicks OK 
                if (MyDialog.ShowDialog() == DialogResult.OK)
                    richTextBox1.ForeColor = MyDialog.Color;

            }
        }

        private void копиоватьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Ensure that text is selected in the text box.   
            //richTextBox1.SelectionLength > 0)
            if (richTextBox1.SelectionLength > 0)
                // Copy the selected text to the Clipboard.
                richTextBox1.Copy();
        }

        private void вставитьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (Clipboard.GetDataObject().GetDataPresent(DataFormats.Text) == true)
            {
                // Determine if any text is selected in the text box.
                if (richTextBox1.SelectionLength > 0)
                {
                    // Ask user if they want to paste over currently selected text.
                    if (MessageBox.Show("Do you want to paste over current selection?", "Cut Example", MessageBoxButtons.YesNo) == DialogResult.No)
                        // Move selection to the point after the current selection and paste.
                        richTextBox1.SelectionStart = richTextBox1.SelectionStart + richTextBox1.SelectionLength;
                }
                // Paste current text in Clipboard into text box.
                richTextBox1.Paste();
            }
        }

        private void вырезатьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Ensure that text is currently selected in the text box.   
            if (richTextBox1.SelectedText != "")
                // Cut the selected text in the control and paste it into the Clipboard.
                richTextBox1.Cut();
        }

        private void очиститьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowColor = true;

            fontDialog1.Font = richTextBox1.Font;
            fontDialog1.Color = richTextBox1.ForeColor;

            if (fontDialog1.ShowDialog() != DialogResult.Cancel)
            {
                richTextBox1.Font = fontDialog1.Font;
                richTextBox1.ForeColor = fontDialog1.Color;
            }
        }


        private void поЛевойСторонеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Select();
            richTextBox1.SelectionAlignment = HorizontalAlignment.Left;
        }

            private void поПравойСторонеToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Select();
            richTextBox1.SelectionAlignment = HorizontalAlignment.Right;
        }

     
        private void вырезатьToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            // Ensure that text is currently selected in the text box.   
            if (richTextBox1.SelectedText != "")
                // Cut the selected text in the control and paste it into the Clipboard.
                richTextBox1.Cut();
        }

        private void копироватьToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Ensure that text is selected in the text box.   
            //richTextBox1.SelectionLength > 0)
            if (richTextBox1.SelectionLength > 0)
                // Copy the selected text to the Clipboard.
                richTextBox1.Copy();
        }

        private void вставитьToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            if (Clipboard.GetDataObject().GetDataPresent(DataFormats.Text) == true)
            {
                // Determine if any text is selected in the text box.
                if (richTextBox1.SelectionLength > 0)
                {
                    // Ask user if they want to paste over currently selected text.
                    if (MessageBox.Show("Do you want to paste over current selection?", "Cut Example", MessageBoxButtons.YesNo) == DialogResult.No)
                        // Move selection to the point after the current selection and paste.
                        richTextBox1.SelectionStart = richTextBox1.SelectionStart + richTextBox1.SelectionLength;
                }
                // Paste current text in Clipboard into text box.
                richTextBox1.Paste();
            }
        }

        private void очиститьToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void цветToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ColorDialog MyDialog = new ColorDialog();
            // Keeps the user from selecting a custom color.
            MyDialog.AllowFullOpen = false;
            // Allows the user to get help. (The default is false.)
            MyDialog.ShowHelp = true;
            // Sets the initial color select to the current text color.
            MyDialog.Color = richTextBox1.ForeColor;

            // Update the text box color if the user clicks OK 
            if (MyDialog.ShowDialog() == DialogResult.OK)
                richTextBox1.ForeColor = MyDialog.Color;
        }

        private void шрифтToolStripMenuItem_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowColor = true;

            fontDialog1.Font = richTextBox1.Font;
            fontDialog1.Color = richTextBox1.ForeColor;

            if (fontDialog1.ShowDialog() != DialogResult.Cancel)
            {
                richTextBox1.Font = fontDialog1.Font;
                richTextBox1.ForeColor = fontDialog1.Color;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void contextMenuStrip1_Opening(object sender, CancelEventArgs e)
        {

        }

        private void printPreviewDialog1_Load(object sender, EventArgs e)
        {

        }
    }
}

