unit Unit8;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TAddR }

  TAddR = class(TForm)
    Save: TButton;
    ComboBox1: TComboBox;
    ComboBox2: TComboBox;
    Edit1: TEdit;
    Edit4: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    procedure FormCreate(Sender: TObject);
    procedure SaveClick(Sender: TObject);
  private

  public

  end;

var
  AddR: TAddR;
  //KodR: integer;

implementation

{$R *.lfm}

{ TAddR }


procedure TAddR.SaveClick(Sender: TObject);
begin

end;

procedure TAddR.FormCreate(Sender: TObject);
begin

end;


  //KodR:= StrToInt(Edit1.Caption);

end.

