unit unitKnigList;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Grids, ComCtrls,
  StdCtrls, EditBtn;

type
  Kniga = record
    Avtor : String[50];
    Nazvanie : String[50];
    GodIzdan : String[4];
  end;



type

  { TFormKnigList }

  procedure TFormKnigList.WriteToFile( namfile : string, kng : Kniga);
  var
    f: Text;
  begin
  AssignFile(f, 'db/listknig.txt');
  Append(f);
  WriteLn(f, kng.Avtor);
  WriteLn(f, kng.Nazvanie);
  WriteLn(f, kng.GodIzdan);
  WriteLn(f, '');
  CloseFile(f);
  end;


  TFormKnigList = class(TForm)
    BtnAdd: TButton;
    BtnEdit: TButton;
    BtnDel: TButton;
    ComboBox1: TComboBox;
    EditButton1: TEditButton;
    StringGrid1: TStringGrid;
    ToolBar1: TToolBar;
    procedure BtnAddClick(Sender: TObject);
    procedure BtnEditClick(Sender: TObject);
    procedure BtnDelClick(Sender: TObject);
    procedure EditButton1ButtonClick(Sender: TObject);
    procedure EditButton1Change(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure StringGrid1Click(Sender: TObject);
    procedure UpDateGrid(Sender: TObject);
    procedure WriteToFile(namfile : string, kng : Kniga);
    procedure WriteArrToFile( namfile : string, count : integer, kng  : array of Kniga);
  private

  public
   arrKnig : array[1..100] of Kniga;
   arrCount : integer;
   reg : integer;

 end;

var
  FormKnigList: TFormKnigList;


implementation
uses unitKnigaEdit;


{$R *.lfm}

{ TFormKnigList }

procedure TFormKnigList.FormShow(Sender: TObject);
var
  f : Text;
  i : Integer;
begin
  i := 1;
  AssignFile(f, 'db/listknig.txt');
  Reset(f);
  while not (EOF(f)) do begin
     ReadLn (f, arrKnig[i].Avtor);
     ReadLn (f, arrKnig[i].Nazvanie);
     ReadLn (f, arrKnig[i].GodIzdan);
     ReadLn (f);
     i := i + 1;
  end;
      CloseFile(f);
   arrCount := i - 1;

   UpDateGrid(Sender);

end;

procedure TFormKnigList.StringGrid1Click(Sender: TObject);
begin

end;

procedure TFormKnigList.UpDateGrid(Sender: TObject);
var
  i : Integer;
begin

  for i:=1 to arrCount do
    if ( arrKnig[i].Avtor = EditButton1.Text) then begin
    StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
    StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
    StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
end;

end;

procedure TFormKnigList.BtnAddClick(Sender: TObject);
begin
  //Add
  reg :=1;
  FormKnigaEdit.ShowModal;
end;



procedure TFormKnigList.BtnEditClick(Sender: TObject);
begin
  //Edit
  reg:= 2;
  FormKnigaEdit.ShowModal;

end;

procedure TFormKnigList.BtnDelClick(Sender: TObject);
begin

end;

procedure TFormKnigList.EditButton1ButtonClick(Sender: TObject);
var
    i, k : Integer;
begin
   for i:=1 to StringGrid1.RowCount-1 do
    StringGrid1.Rows[i].Clear;
   k:=1;

   if ComboBox1.ItemIndex = 0 then
   for i:=1 to arrCount do
    if ( arrKnig[i].Avtor = EditButton1.Text) then begin
     StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
     StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
     StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
    k:= k+1;
    StringGrid1.RowCount:=k+1;
    end;

procedure BtnDelClick(Sender: TObject);
var
  i, j : integer;
  x : Integer;
begin

  x:=StringGrid1.Row;

  for i := x to arrCount-1 do begin
     arrKnig[x] := arrKnig[x+1];
  end;
  arrCount:=arrCount-1;

  for i:=1 to StringGrid1.RowCount-1 do
    StringGrid1.Rows[i].Clear;

  UpdateGrid(Sender);

  FormKnigList.WriteArrToFile( 'db/listknig.txt', FormKnigList.arrCount, FormKnigList.arrKnig);

end;


end.
