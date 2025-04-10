unit unitSpIzdat;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TFormSpIzdat }

  TFormSpIzdat = class(TForm)
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
    //procedure Edit1Change(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure ListBox1Click(Sender: TObject);
  private

  public

  end;

var
  FormSpIzdat: TFormSpIzdat;

implementation

{$R *.lfm}

{ TFormSpIzdat }

//реализация кнопки добавления записи в список
procedure TFormSpIzdat.BtnAddClick(Sender: TObject);
begin
  //при добавлении новой записи очищает Edit
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

//реализация кнопки удаления записи из списка
procedure TFormSpIzdat.BtnDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

//реализация кнопки редактирования записи в списке при выделении ее
procedure TFormSpIzdat.BtnEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0 ) then
  ListBox1.Items[ListBox1.ItemIndex] := Edit1.Text;
end;

//реализация кнопки выхода из справочника
procedure TFormSpIzdat.BtnExitClick(Sender: TObject);
begin
  Close;
end;

//реализация кнопки сохранения записи в указанный файл
procedure TFormSpIzdat.BtnSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('db\izdat.db');
end;

//при открытии формы загружаем файл, указанный ниже
procedure TFormSpIzdat.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile('db\izdat.db');
end;

//при нажатии на кнопку данные переносятся на ListBox1
procedure TFormSpIzdat.ListBox1Click(Sender: TObject);
begin
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

