unit unitSpiZ;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormSpiZ }

  TFormSpiZ = class(TForm)
    BtnAdd: TButton;
    BtnDel: TButton;
    BtnEdit: TButton;
    BtnExit: TButton;
    BtnSave: TButton;
    Edit1: TEdit;
    Label1: TLabel;
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
  FormSpiZ: TFormSpiZ;

implementation

{$R *.lfm}

{ TFormSpiZ }

procedure TFormSpiZ.BtnAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpiZ.BtnDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpiZ.BtnEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0 )then
  ListBox1.Items[ListBox1.ItemIndex]:= Edit1.Text;
end;

procedure TFormSpiZ.BtnExitClick(Sender: TObject);
begin
  Close;
end;

procedure TFormSpiZ.BtnSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('db\izdat.txt');
end;


procedure TFormSpiZ.FormShow(Sender: TObject);
begin
   ListBox1.Items.LoadFromFile('db\izdat.txt');
end;

procedure TFormSpiZ.ListBox1Click(Sender: TObject);
begin
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

