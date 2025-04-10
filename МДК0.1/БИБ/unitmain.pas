unit unitMain;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Menus, ExtCtrls,
  StdCtrls;

type

  { TFormMain }

  TFormMain = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    MainMenu1: TMainMenu;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
  private

  public

  end;

var
  FormMain: TFormMain;

implementation
uses unitSpavtor, unitSpName, unitSpiZ, unitKnigaEdit, unitKnigList;

{$R *.lfm}

{ TFormMain }

procedure TFormMain.Button1Click(Sender: TObject);
begin
  FormSpavtor.Show;

end;

procedure TFormMain.Button2Click(Sender: TObject);
begin
  FormSpName.Show;

end;
procedure TFormMain.Button3Click(Sender: TObject);
begin
  FormSpiZ.Show;

end;

procedure TFormMain.Button4Click(Sender: TObject);
begin
  FormKnigaEdit.Show;
end;

procedure TFormMain.Button5Click(Sender: TObject);
begin
  FormKnigList.Show;
end;


end.

