unit unit1AddBus;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  ExtCtrls;

type
  Bus = record
    mark : String [50];
    numder : String [50];
    vmes : String [50];
  end;

type

  { TFormAddBus }

  TFormAddBus = class(TForm)
    Button1: TButton;
    Button2: TButton;
    ComboBox1: TComboBox;
    ComboBox2: TComboBox;
    ComboBox3: TComboBox;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  FormAddBus: TFormAddBus;
  b : bus;

implementation

{$R *.lfm}

{ TFormAddBus }

procedure TFormAddBus.Button2Click(Sender: TObject);
begin
  Close;
end;

procedure TFormAddBus.FormShow(Sender: TObject);
begin
  ComboBox1.Items.LoadFromFile('txt\mark bus.txt');
  ComboBox1.ItemIndex:= 0;

  ComboBox2.Items.LoadFromFile('txt\numder bus.txt');
  ComboBox2.ItemIndex:= 0;

  ComboBox3.Items.LoadFromFile('txt\vmes bus.txt');
  ComboBox3.ItemIndex:= 0;
end;

procedure TFormAddBus.Button1Click(Sender: TObject);
var
  f : Text;
begin
  b.mark := ComboBox1.Text;
  b.numder := ComboBox2.Text;
  b.vmes := ComboBox3.Text;

  AssignFile(f, 'txt\addbus.txt');
  Append(f);
  Writeln(f, b.mark);
  Writeln(f, b.numder);
  Writeln(f, b.vmes);
  Writeln(f, '');
  CloseFile(f);


  Close;
end;

end.

