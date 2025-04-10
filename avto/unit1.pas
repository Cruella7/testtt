unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Menus, ExtCtrls,
  StdCtrls, Unit2, Unit3, Unit4, Unit5, Unit6, Unit7, unitSpMark,unitSpNumber,unitSpVmes, unit1AddBus;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    Image1: TImage;
    Image2: TImage;
    Image3: TImage;
    MainMenu1: TMainMenu;
    MenuItem1: TMenuItem;
    MenuItem2: TMenuItem;
    MenuItem3: TMenuItem;
    MenuItem4: TMenuItem;
    MenuItem5: TMenuItem;
    MenuItem6: TMenuItem;
    MenuItem7: TMenuItem;
    MenuItem8: TMenuItem;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
    procedure Image2Click(Sender: TObject);
    procedure MenuItem3Click(Sender: TObject);
    procedure MenuItem4Click(Sender: TObject);
    procedure MenuItem5Click(Sender: TObject);
    procedure MenuItem6Click(Sender: TObject);
    procedure MenuItem7Click(Sender: TObject);
    procedure MenuItem8Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation
//uses unitSpMark;
//uses unitSpNumber;
//uses unitSpVmes;

{$R *.lfm}

{ TForm1 }




procedure TForm1.Button1Click(Sender: TObject);
begin
  FormSpMark.Show;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
   FormSpNumber.Show;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  FormSpVmes.Show;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  FormAddBus.Show;
end;

procedure TForm1.Button5Click(Sender: TObject);
begin
  FormBus.Show;
end;

procedure TForm1.Image2Click(Sender: TObject);
begin

end;


procedure TForm1.MenuItem3Click(Sender: TObject);
begin
   About.Show;
end;

procedure TForm1.MenuItem4Click(Sender: TObject);
begin
   FormBus.Show;
end;

procedure TForm1.MenuItem5Click(Sender: TObject);
begin
   FormSt.Show;
end;

procedure TForm1.MenuItem6Click(Sender: TObject);
begin
   FormR.Show;
end;

procedure TForm1.MenuItem7Click(Sender: TObject);
begin
     Zapros1.Show;
end;

procedure TForm1.MenuItem8Click(Sender: TObject);
begin
  Zapros2.Show;
end;

end.

