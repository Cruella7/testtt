unit unitSpVmes;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormSpVmes }

  TFormSpVmes = class(TForm)
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
  FormSpVmes: TFormSpVmes;

implementation

{$R *.lfm}

{ TFormSpVmes }

procedure TFormSpVmes.ListBox1Click(Sender: TObject);
begin
  Edit1.Text:=ListBox1.Items[ListBox1.ItemIndex];
end;

procedure TFormSpVmes.ButExitClick(Sender: TObject);
begin
  Close;
end;

procedure TFormSpVmes.ButSaveClick(Sender: TObject);
begin
  ListBox1.Items.SaveToFile('txt\vmes bus.txt');
end;

procedure TFormSpVmes.FormShow(Sender: TObject);
begin
  ListBox1.Items.LoadFromFile ('txt\vmes bus.txt');
end;

procedure TFormSpVmes.ButAddClick(Sender: TObject);
begin
  ListBox1.Items.AddText(Edit1.Text);
  Edit1.Clear;
end;

procedure TFormSpVmes.ButDelClick(Sender: TObject);
begin
  ListBox1.Items.Delete(ListBox1.ItemIndex);
end;

procedure TFormSpVmes.ButEditClick(Sender: TObject);
begin
  if (ListBox1.ItemIndex >= 0) then
  ListBox1.Items[ListBox1.ItemIndex]:= Edit1.Text;
end;

end.

