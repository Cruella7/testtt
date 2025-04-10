unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Image1: TImage;
    Image2: TImage;
    Image3: TImage;
    Image4: TImage;
    Image5: TImage;
    Image6: TImage;
    Image7: TImage;
    Image8: TImage;
    Image9: TImage;
    Label1: TLabel;
    Panel1: TPanel;
    Panel2: TPanel;
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure StartGame (Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  player : integer;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.StartGame (Sender: TObject);
var
  i : Integer;
begin
   player := 1;
   Label1.Caption:= inttostr(player);

   for i := 1 to 9 do begin
     TImage( FindComponent('Image'+inttostr(i))).Picture.LoadFromFile('img\i.png');
   end;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  StartGame (Sender);
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
   StartGame (Sender);
end;

end.

