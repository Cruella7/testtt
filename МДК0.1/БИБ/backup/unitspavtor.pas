unit unitSpavtor;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormSpavtor }

  TFormSpavtor = class(TForm)
    BtnAdd: TButton;
    BtnEdit: TButton;
    BtnDel: TButton;
    BtnExit: TButton;
    BtnSave: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    ListBox1: TListBox;
    procedure BtnDelClick(Sender: TObject);
    procedure BtnExitClick(Sender: TObject);
    procedure BtnSaveClick(Sender: TObject);
    procedure BtnEditClick(Sender: TObject);
    procedure BtnAddClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure ListBox1Click(Sender: TObject);
  private

  public

  end;

var
  FormSpavtor: TFormSpavtor;

implementation

{$R *.lfm}

{ TFormSpavtor }

procedure TFormSpavtor.BtnExitClick(Sender: TObject);
begin
  Close;


end;

procedure TFormSpavtor.BtnDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpavtor.BtnSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('db\avtor.txt');
end;

procedure TFormSpavtor.BtnEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0 )then
  ListBox1.Items[ListBox1.ItemIndex]:= Edit1.Text;
end;

procedure TFormSpavtor.BtnAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;

end;

procedure TFormSpavtor.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile('db\avtor.txt');
end;

procedure TFormSpavtor.ListBox1Click(Sender: TObject);
begin
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

