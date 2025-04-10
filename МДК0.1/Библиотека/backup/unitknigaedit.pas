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
  // при открытии формы подгружаем данные из справочников в ComboBox
  ComboBox1.Items.LoadFromFile('db/avtor.db'); // файл, где хранятся данные об авторах
  ComboBox1.ItemIndex:= 0; //автоматически будет виден один из элементов списка

  ComboBox2.Items.LoadFromFile('db/izdat.db'); // файл, где хранятся данные о годе издания
  ComboBox2.ItemIndex:= 0; //автоматически будет виден один из элементов списка


  if ( FormKnigList.reg = 2 ) then
  begin
   x := FormKnigList.StringGrid1.Row;

   ComboBox1.Text :=  FormKnigList.StringGrid1.Cells[0, x];
   Edit2.Text     :=  FormKnigList.StringGrid1.Cells[1, x];
   ComboBox2.Text :=  FormKnigList.StringGrid1.Cells[1, x];

  end;

end;

procedure TFormKnigaEdit.BitBtn1Click(Sender: TObject);
var
  f : Text; // подключение к файлу, куда будет производиться запись
begin
  kng.Avtor := ComboBox1.Text; // заносим данные из формы в  созданную переменную
  kng.Nazvanie := Edit2.Text;  // заносим данные из формы в  созданную переменную
  kng.GodIzdan := ComboBox2.Text; // заносим данные из формы в  созданную переменную


  if ( FormKnigList.reg = 1 ) then begin
    FormKnigList.arrCount:=FormKnigList.arrCount+1;
    FormKnigList.arrKnig[FormKnigList.arrCount] := kng;
    FormKnigList.UpdateGrid(Sender);
    FormKnigList.WriteToFile('db/listknig.db', kng);
  end;

  if ( FormKnigList.reg = 2 ) then begin
    FormKnigList.arrKnig[x] := kng;
    FormKnigList.UpdateGrid(Sender);
    FormKnigList.WriteArrToFile('db/listknig.db', FormKnigList.arrCount, FormKnigList.arrKnig );
  end;

   Edit2.Clear;
   ComboBox2.Text;


  Close;

end;

end.

