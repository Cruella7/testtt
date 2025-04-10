unit Unit5;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TFormR }

  TFormR = class(TForm)
    add: TButton;
    procedure addClick(Sender: TObject);
  private

  public

  end;

var
  FormR: TFormR;

implementation

{$R *.lfm}



{ TFormR }

procedure TFormR.addClick(Sender: TObject);
begin

end;

end.

