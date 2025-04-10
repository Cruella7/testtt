unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Menus, StdCtrls,
  ExtCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    ButOK: TButton;
    EditNumber: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    MainMenu1: TMainMenu;
    MenuNew: TMenuItem;
    MenuExit: TMenuItem;
    procedure ButOKClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure MenuExitClick(Sender: TObject);
    procedure MenuOptionsClick(Sender: TObject);
    procedure MenuNewClick(Sender: TObject);
    procedure NewGame;
  private

  public

  end;

var
  Form1: TForm1;
  i : Integer; //число попыток
  n : Integer; //вводимое число
  rn : Integer; // загаданное число

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.MenuNewClick(Sender: TObject);
begin
  //
  NewGame;
end;

procedure TForm1.NewGame;
begin
  //
  Randomize;
  rn := Random(9) + 1;
  i := 5;
  Label1.Caption := 'Количество попыток :' + IntToStr( i );
  EditNumber.Enabled := True;
  ButOK.Enabled := True;
  EditNumber.Clear;
  Label4.Caption:='';

end;

procedure TForm1.MenuOptionsClick(Sender: TObject);
begin
  //
end;

procedure TForm1.MenuExitClick(Sender: TObject);
begin
  Close;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  //
  NewGame;
end;

procedure TForm1.ButOKClick(Sender: TObject);
begin
  n := StrToInt( EditNumber.Text );
  //
  if ( rn = n) then begin
    Label4.Caption := 'Вы угадали число!';
    EditNumber.Enabled := False;
    ButOK.Enabled := False;
  end;

  if not( rn = n) then begin
    if (rn > n) then Label4.Caption:= 'Введеное число меньше загаданного.';
    if (rn < n) then Label4.Caption:= 'Введеное число больше загаданного.';
    i := i - 1;
    EditNumber.Clear;
  end;

  Label1.Caption := 'Количество попыток :' + IntToStr( i );

end;

end.

