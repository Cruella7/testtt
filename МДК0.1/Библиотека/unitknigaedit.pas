unit unitKnigaEdit;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  ExtCtrls, unitKnigList;



type
  { TFormKnigaEdit }

  TFormKnigaEdit = class(TForm)
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    ComboBox1: TComboBox;
    ComboBox2: TComboBox;
    Edit2: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label6: TLabel;
    procedure BitBtn1Click(Sender: TObject);
    procedure BitBtn2Click(Sender: TObject);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  FormKnigaEdit: TFormKnigaEdit;
  kng : Kniga;
    x : Integer;
implementation

{$R *.lfm}

{ TFormKnigaEdit }

procedure TFormKnigaEdit.BitBtn2Click(Sender: TObject);
begin
  // реализация кнопки закрытия формы
  Close;
end;

procedure TFormKnigaEdit.FormShow(Sender: TObject);
begin
  // при открытии формы загружаем данные из справочников в ComboBox
  // файл, где хранятся данные об авторах
  ComboBox1.Items.LoadFromFile('db/avtor.db');

  //автоматически будет виден один из элементов списка
  ComboBox1.ItemIndex:= 0;

  // файл, где хранятся данные о годе издания
  ComboBox2.Items.LoadFromFile('db/izdat.db');

  //автоматически будет виден один из элементов списка
  ComboBox2.ItemIndex:= 0;



  if ( FormKnigList.reg = 2 ) then
  begin
  // индекс выделенной строки
   x := FormKnigList.StringGrid1.Row;

   // считываем данные выделенной строки
   ComboBox1.Text :=  FormKnigList.StringGrid1.Cells[0, x];
   Edit2.Text     :=  FormKnigList.StringGrid1.Cells[1, x];
   ComboBox2.Text :=  FormKnigList.StringGrid1.Cells[1, x];

  end;

end;

procedure TFormKnigaEdit.BitBtn1Click(Sender: TObject);
var
  // подключение к файлу, куда будет производиться запись
  f : Text;
begin
  // считываем значение всех компонентов и записываем в структуру
  kng.Avtor := ComboBox1.Text;
  kng.Nazvanie := Edit2.Text;
  kng.GodIzdan := ComboBox2.Text;

  if ( FormKnigList.reg = 1 ) then begin
   // увеличиваем количество элементов  массива
    FormKnigList.arrCount:=FormKnigList.arrCount+1;

    // записываем новый элемент в массив
    FormKnigList.arrKnig[FormKnigList.arrCount] := kng;

    //обновляем данные
    FormKnigList.UpdateGrid(Sender);

    // сохранение данных
    FormKnigList.WriteToFile('db/listknig.db', kng);
  end;


  if ( FormKnigList.reg = 2 ) then begin
    // записываем данную структуру в текущий выделенный элемент
    FormKnigList.arrKnig[x] := kng;

    //обновляем данные
    FormKnigList.UpdateGrid(Sender);

    //// сохранение данных
    FormKnigList.WriteArrToFile('db/listknig.db', FormKnigList.arrCount, FormKnigList.arrKnig );
  end;
   // очищение полей при добавлении новой записи
   Edit2.Clear;
   ComboBox2.Text;


  Close;

end;

end.

