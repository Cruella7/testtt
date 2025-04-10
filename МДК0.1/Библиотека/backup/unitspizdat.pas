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

procedure TFormSpIzdat.BtnAddClick(Sender: TObject);
begin
   //реализация кнопки добавления записи в список
  //при добавлении новой записи очищает Edit
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpIzdat.BtnDelClick(Sender: TObject);
begin
  //реализация кнопки удаления записи из списка
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpIzdat.BtnEditClick(Sender: TObject);
begin
  //реализация кнопки редактирования записи в списке при выделении ее
  if (ListBox1.ItemIndex >= 0 ) then
  ListBox1.Items[ListBox1.ItemIndex] := Edit1.Text;
end;

procedure TFormSpIzdat.BtnExitClick(Sender: TObject);
begin
  //реализация кнопки выхода из справочника
  Close;
end;

procedure TFormSpIzdat.BtnSaveClick(Sender: TObject);
begin
  //реализация кнопки сохранения записи в указанный файл
  ListBox1.Items.SaveToFile('db\izdat.db');
end;

procedure TFormSpIzdat.FormShow(Sender: TObject);
begin
  //при открытии формы загружаем файл, указанный ниже
  ListBox1.Items.LoadFromFile('db\izdat.db');
end;

procedure TFormSpIzdat.ListBox1Click(Sender: TObject);
begin
  //при нажатии на кнопку данные переносятся на ListBox1
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

