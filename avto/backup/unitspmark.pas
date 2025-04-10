unit unitSpMark;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormSpMark }

  TFormSpMark = class(TForm)
    ButAdd: TButton;
    ButEdit: TButton;
    ButDel: TButton;
    ButSave: TButton;
    ButExit: TButton;
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
  FormSpMark: TFormSpMark;

implementation

{$R *.lfm}

{ TFormSpMark }

procedure TFormSpMark.ButExitClick(Sender: TObject);
begin
  Close;
end;

procedure TFormSpMark.ButAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpMark.ButDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpMark.ButEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0) then
  ListBox1.Items[ListBox1.ItemIndex]:= Edit1.Text;
end;

procedure TFormSpMark.ButSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('txt\mark bus.txt');
end;

procedure TFormSpMark.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile ('txt\mark bus.txt');
end;

procedure TFormSpMark.ListBox1Click(Sender: TObject);
begin
   Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

end.

