unit Unit4;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Grids, StdCtrls, Unit10;

type

  { TFormSt }

  TFormSt = class(TForm)
    Button2: TButton;
    StringGrid1: TStringGrid;

    procedure Button2Click(Sender: TObject);
  private

  public

  end;
      //станции стринг грид
var
  FormSt: TFormSt;

implementation

{$R *.lfm}

{ TFormSt }


procedure TFormSt.Button2Click(Sender: TObject);
begin
    NameSt.Show;
end;

end.

