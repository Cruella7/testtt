unit unitSpAvtor;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TFormSpAvtor }

  TFormSpAvtor = class(TForm)
    BtnAdd: TBitBtn;
    BtnDel: TBitBtn;
    BtnEdit: TBitBtn;
    BtnExit: TBitBtn;
    BtnSave: TBitBtn;
    Edit1: TEdit;
    Label2: TLabel;
    ListBox1: TListBox;
    procedure BtnAddClick(Sender: TObject);
    procedure BtnDelClick(Sender: TObject);
    procedure BtnEditClick(Sender: TObject);
    procedure BtnExitClick(Sender: TObject);
    procedure BtnSaveClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure ListBox1Click(Sender: TObject);
  private

  public

  end;

var
  FormSpAvtor: TFormSpAvtor;

implementation

{$R *.lfm}

{ TFormSpAvtor }

 // добавление записи в справочник
procedure TFormSpAvtor.BtnAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

//реализация кнопки удаления записи из списка
procedure TFormSpAvtor.BtnDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

//реализация кнопки редактирования записи в списке при выделении ее
procedure TFormSpAvtor.BtnEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0 ) then
  ListBox1.Items[ListBox1.ItemIndex] := Edit1.Text;
end;

//реализация кнопки выхода из справочника
procedure TFormSpAvtor.BtnExitClick(Sender: TObject);
begin
  Close;
end;

//реализация кнопки сохранения записи в указанный файл
procedure TFormSpAvtor.BtnSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('db\avtor.db');
end;

//при открытии формы загружаем файл, указанный ниже
procedure TFormSpAvtor.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile('db\avtor.db');
end;

//при нажатии на кнопку данные переносятся на ListBox1
procedure TFormSpAvtor.ListBox1Click(Sender: TObject);
begin
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

