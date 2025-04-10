unit Unit2;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TAbout }

  TAbout = class(TForm)
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    procedure Label1Click(Sender: TObject);
  private

  public

  end;

var
  About: TAbout;

implementation

{$R *.lfm}

{ TAbout }

procedure TAbout.Label1Click(Sender: TObject);
begin

end;


end.

