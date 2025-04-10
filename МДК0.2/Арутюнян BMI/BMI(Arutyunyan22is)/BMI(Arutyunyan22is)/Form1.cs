using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace BMI_Arutyunyan22is_
{
    public partial class Form1 : Form
    {
        float index;
        float wei;
        float hei;
        public Form1()
        {

            InitializeComponent();
        }
        private void tracBar1_Scroll(object sender, EventArgs e)
        {

        }

        private void Back_Click(object sender, EventArgs e)
        {
          Application.Exit();

        }

        private void Count_Click(object sender, EventArgs e)
        {
            hei = float.Parse(height.Text);
            wei = float.Parse(weight.Text);
            hei = hei / 100;
            index = wei / (hei * hei);
            Result.Text = index.ToString();
            if (
                index < 18.5)
            {
                index = 5;
                textBox3.Text = "Недостаточный";
            }
            else if (index >= 18.5 && index <= 24.9)
            {
                index = 15;
                textBox3.Text = "Здоровый";
            }
            else if (index >= 25 && index <= 29.9)
            {
                index = 25;
                textBox3.Text = "Избыточный";
            }
            else
            {
                index = 35;
                textBox3.Text = "Ожирение";
            }
            trackBar1.Value = Convert.ToInt32(index);
        }

        private void Cancel_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            pictureBox3.Image = Properties.Resources.female_icon;
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            pictureBox3.Image = Properties.Resources.male_icon;
        }

     
    }
}
