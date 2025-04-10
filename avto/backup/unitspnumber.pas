unit unitSpNumber;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormSpNumber }

  TFormSpNumber = class(TForm)
    ButAdd: TButton;
    ButDel: TButton;
    ButEdit: TButton;
    ButExit: TButton;
    ButSave: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    ListBox1: TListBox;
    procedure ButAddClick(Sender: TObject);
    procedure ButDelClick(Sender: TObject);
    procedure ButEditClick(Sender: TObject);
    procedure ButExitClick(Sender: TObject);
    procedure ButSaveClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure ListBox1Click(Sender: TObject);
  private

  public

  end;

var
  FormSpNumber: TFormSpNumber;

implementation

{$R *.lfm}

{ TFormSpNumber }

procedure TFormSpNumber.ButExitClick(Sender: TObject);
begin
  Close;
end;

procedure TFormSpNumber.ButSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('txt\numder bus.txt');
end;

procedure TFormSpNumber.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile ('txt\numder bus.txt');
end;

procedure TFormSpNumber.ListBox1Click(Sender: TObject);
begin
   Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

procedure TFormSpNumber.ButAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpNumber.ButDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpNumber.ButEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0) then
  ListBox1.Items[ListBox1.ItemIndex]:= Edit1.Text;
end;

end.

