unit unitKnigaEdit;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  unitKniglist;

{
type
  Kniga = record
    Avtor : String[50];
    Nazvanie : String[50];
    GodIzdan : String[4];
  end;
}

type

  { TFormKnigaEdit }

  TFormKnigaEdit = class(TForm)
    Button1: TButton;
    Button2: TButton;
    ComboBox1: TComboBox;
    Edit2: TEdit;
    Edit3: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure ComboBox1Change(Sender: TObject);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  FormKnigaEdit: TFormKnigaEdit;
  kng : Kniga;

implementation

{$R *.lfm}

{ TFormKnigaEdit }

procedure TFormKnigaEdit.Button1Click(Sender: TObject);
begin
  Close;
end;

procedure TFormKnigaEdit.Button2Click(Sender: TObject);
var
  f : Text;
begin
  kng.Avtor := ComboBox1.Text;
  kng.Nazvanie := Edit2.Text;
  kng.GodIzdan := Edit3.Text;

  if ( FormKnigList.reg = 1) then begin
    FormKnigList.arrCount:=FormKnigList.arrCount+1;
    FormKnigList.arrKnig(FormKnigList.arrCount):=kng;
    FormKnigList.UpdateGrid(Sender);
    FormKnigList.WriteToFile('db/listknig.txt', kng);
 end;

  if ( FormKnigList.reg = 2) then begin
    FormKnigList.arrCount:=FormKnigList.arrCount+1;
    FormKnigList.arrKnig[FormKnigList.arrCount]:=kng;
    FormKnigList.UpdateGrid(Sender);
    FormKnigList.WriteArrToFile( 'db/listknig.txt', FormKnigList.arrCount, FormKnigList.arrKnig);
 end;

  Close;
end;

procedure TFormKnigaEdit.ComboBox1Change(Sender: TObject);
begin

end;

procedure TFormKnigaEdit.FormShow(Sender: TObject);
begin
  ComboBox1.Items.LoadFromFile('db/avtor.txt');
  ComboBox1.ItemIndex:= 0;

  if (FormKhigList.reg = 2) then
  begin
    x:= FormKhigList.StringGrid1.Row;

    ComboBox1.Text := FormKhigList.StringGrid1.Cells[0,x];
    Edit3.Text     := FormKhigList.StringGrid1.Cells[1,x];
    Edit2.Text     := FormKhigList.StringGrid1.Cells[2,x];

  end;

end;

end.

