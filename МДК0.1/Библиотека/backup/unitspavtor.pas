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

procedure TFormSpAvtor.BtnAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpAvtor.BtnDelClick(Sender: TObject);
begin
  //реализация кнопки удаления записи из списка
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpAvtor.BtnEditClick(Sender: TObject);
begin
  //реализация кнопки редактирования записи в списке при выделении ее
  if (ListBox1.ItemIndex >= 0 ) then
  ListBox1.Items[ListBox1.ItemIndex] := Edit1.Text;
end;

procedure TFormSpAvtor.BtnExitClick(Sender: TObject);
begin
  //реализация кнопки выхода из справочника
  Close;
end;

procedure TFormSpAvtor.BtnSaveClick(Sender: TObject);
begin
  //реализация кнопки сохранения записи в указанный файл
  ListBox1.Items.SaveToFile('db\avtor.db');
end;

procedure TFormSpAvtor.FormShow(Sender: TObject);
begin
   //при открытии формы загружаем файл, указанный ниже
  ListBox1.Items.LoadFromFile('db\avtor.db');
end;

procedure TFormSpAvtor.ListBox1Click(Sender: TObject);
begin
  //при нажатии на кнопку данные переносятся на ListBox1
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

