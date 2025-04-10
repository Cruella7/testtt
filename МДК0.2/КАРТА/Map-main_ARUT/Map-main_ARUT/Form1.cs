using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace Map_main_ARUT
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }

        private void clear()
        {
            pictureBoxDrinks.Visible = false; labelDrinks.Visible = false;
            pictureBoxEnergy.Visible = false; labelEnergy.Visible = false;
            pictureBoxTuilets.Visible = false; labelToilets.Visible = false;
            pictureBoxInformation.Visible = false; labelInformation.Visible = false;
            pictureBoxMedical.Visible = false; labelMedical.Visible = false;
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox13_Click(object sender, EventArgs e)
        {
            nameLabel.Text = "ФИНИШ!";
            pictureBoxDrinks.Visible = false; labelDrinks.Visible = false;
            pictureBoxEnergy.Visible = false; labelEnergy.Visible = false;
            pictureBoxTuilets.Visible = false; labelToilets.Visible = false;
            pictureBoxInformation.Visible = false; labelInformation.Visible = false;
            pictureBoxMedical.Visible = false; labelMedical.Visible = false;
        }

        private void pictureBox17_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Старт гонки 1";
            marafonLabel.Text = "Самбо полный марафон";
           
        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Старт гонки 3";
            marafonLabel.Text = "Капоэйра веселый забег на 5км";
          
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Старт гонки 2";
            marafonLabel.Text = "Джонго полумарафон";
            
        }

        private void nameLabel_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox15_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "МЦК Лужники"; marafonLabel.Text=null;
            pictureBoxEnergy.Visible = true; labelDrinks.Visible = true;
            pictureBoxDrinks.Visible = true; labelEnergy.Visible = true;
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Новодевичей монастырь"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
            pictureBoxInformation.Visible = true; labelInformation.Visible = true;
            pictureBoxMedical.Visible = true; labelMedical.Visible = true;
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Метро Киевская";
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "МИД"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
            pictureBoxMedical.Visible = true; labelMedical.Visible = true;
            pictureBoxMedical.Location = new Point(550, 350); labelMedical.Location = new Point(612, 350);
        }

        private void pictureBox9_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Парк Горького"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
            pictureBoxInformation.Visible = true; labelInformation.Visible = true;
        }

        private void pictureBox10_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Здание РАН"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
        }

        private void pictureBox11_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Метро Воробьевы горы"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
            pictureBoxInformation.Visible = true; labelInformation.Visible = true;
            pictureBoxMedical.Visible = true; labelMedical.Visible = true;
            pictureBoxMedical.Location = new Point(550, 415); labelMedical.Location = new Point(612, 425);
        }

        private void pictureBox12_Click(object sender, EventArgs e)
        {
            clear();
            nameLabel.Text = "Стадион Лужники"; marafonLabel.Text = null;
            pictureBoxDrinks.Visible = true; labelDrinks.Visible = true;
            pictureBoxEnergy.Visible = true; labelEnergy.Visible = true;
            pictureBoxTuilets.Visible = true; labelToilets.Visible = true;
            pictureBoxInformation.Visible = true; labelInformation.Visible = true;
            pictureBoxMedical.Visible = true; labelMedical.Visible = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void labelInformation_Click(object sender, EventArgs e)
        {

        }
    }
}
