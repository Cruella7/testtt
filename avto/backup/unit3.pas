unit Unit3;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Grids, StdCtrls,
  EditBtn, unit1AddBus;


type
  Bus = record
    mark : String [50];
    numder : String [50];
    vmes : String [50];
  end;

type

  { TFormBus }

  TFormBus = class(TForm)
    ButAdd: TButton;
    ButEdit: TButton;                   //автобусы грид
    ButDel: TButton;
    ComboBox1: TComboBox;
    EditButton1: TEditButton;
    StringGrid1: TStringGrid;
    procedure ButAddClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure ButEditClick(Sender: TObject);
    procedure ButDelClick(Sender: TObject);
    procedure UpdateGrid(Sender: TObject);
  private

  public

  end;

var
  FormBus: TFormBus;
  arrBus : array[1..100] of Bus;
  arrCount : integer;


implementation

{$R *.lfm}



{ TFormBus }

procedure TFormBus.ButAddClick(Sender: TObject);
begin
  FormAddBus.ShowModal;
end;
procedure TFormBus.ButEditClick(Sender: TObject);
begin
  FormAddBus.ShowModal;
end;

procedure TFormBus.UpdateGrid(Sender: TObject);
var
  i : integer;
begin
  for i:=1 to arrCount do
    StringGrid1.Cells[0,i] := arrBus[i] .mark;
    StringGrid1.Cells[1,i] := arrBus[i] .numder;
    StringGrid1.Cells[2,i] := arrBus[i] .vmes;


end;

procedure TFormBus.ButDelClick(Sender: TObject);
begin
  Caption := IntToStr(StringGrid1.Row);
end;

procedure TFormBus.FormCreate(Sender: TObject);
begin

end;

procedure TFormBus.FormShow(Sender: TObject);
var
  f : Text;
  i : integer;
begin
  i := 0;
  AssignFile(f, 'txt\addbus.txt');
  Reset(f);
  while not (EOF(f)) do begin
    Readln(f, arrBus[i].mark);
    Readln(f, arrBus[i].numder);
    Readln(f, arrBus[i].vmes);
    Readln(f);
    i := i + 1;
  end;
  arrCount:= i;

  UpdateGrid(Sender);
end;

end.

