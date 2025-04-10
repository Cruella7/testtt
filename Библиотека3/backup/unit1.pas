unit unitRod;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TFormSpRod }

  TFormSpRod = class(TForm)
    BtnAdd: TBitBtn;
    BtnDel: TBitBtn;
    BtnEdit: TBitBtn;
    BtnExit: TBitBtn;
    BtnSave: TBitBtn;
    Edit1: TEdit;
    Label1: TLabel;
    ListBox1: TListBox;
    procedure BtnAddClick(Sender: TObject);
    procedure BtnDelClick(Sender: TObject);
    procedure BtnEditClick(Sender: TObject);
    procedure BtnExitClick(Sender: TObject);
    procedure BtnSaveClick(Sender: TObject);
    procedure Edit1Change(Sender: TObject);
    procedure Label1Click(Sender: TObject);
  private

  public

  end;

var
  FormSpRod: TFormSpRod;

implementation

{$R *.lfm}

{ TFormSpRod }

procedure TFormSpRod.Label1Click(Sender: TObject);
begin

end;
 // добавление новой записи
procedure TFormSpRod.BtnAddClick(Sender: TObject);
begin
    //при добавлении новой записи очищает Edit
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpRod.BtnDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpRod.BtnEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0 ) then
  ListBox1.Items[ListBox1.ItemIndex] := Edit1.Text;
end;

procedure TFormSpRod.BtnExitClick(Sender: TObject);
begin
  Close;
end;

procedure TFormSpRod.BtnSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('db\rod.db');
end;

procedure TFormSpRod.Edit1Change(Sender: TObject);
begin

end;

end.

