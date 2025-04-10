unit unitMain;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, Menus, ExtCtrls,
  StdCtrls;

type

  { TFormMain }

  TFormMain = class(TForm)
    Image1: TImage;
    MainMenu1: TMainMenu;
    MenuItem1: TMenuItem;
    MenuItem2: TMenuItem;
    MenuItem3: TMenuItem;
    MenuItem4: TMenuItem;
    MenuItem7: TMenuItem;
    MenuItem8: TMenuItem;
    procedure FormCreate(Sender: TObject);
    procedure MenuItem1Click(Sender: TObject);
    procedure MenuItem3Click(Sender: TObject);
    procedure MenuItem4Click(Sender: TObject);
    procedure MenuItem7Click(Sender: TObject);
    procedure MenuItem8Click(Sender: TObject);
  private

  public

  end;

var
  FormMain: TFormMain;

implementation
// подключение форм
 uses unitSpIzdat, unitSpAvtor, unitKnigaEdit, unitKnigList, unitSpRod;
{$R *.lfm}

{ TFormMain }

//  в случае отсутствия файла, он должен создаваться
procedure MyFileCreate(name : string);
var
  i : Integer;
begin
  if not FileExists(name) then begin
   i := FileCreate(name);
   FileClose(i);
  end;
end;

// проверка наличия всех файлов в программе
procedure TFormMain.FormCreate(Sender: TObject);
begin
  MyFileCreate('db/avtor.db');
  MyFileCreate('db/izdat.db');
  MyFileCreate('db/listknig.db');
  MyFileCreate('db/rod.db');

end;

// закрытие формы
procedure TFormMain.MenuItem1Click(Sender: TObject);
begin
  Close;
end;

procedure TFormMain.MenuItem3Click(Sender: TObject);
begin
  //  реализация кнопки открытия формы справочника "Автор"
   FormSpAvtor.Show;
end;

procedure TFormMain.MenuItem4Click(Sender: TObject);
begin
  // реализация кнопки открытия формы "Год рождения"
   FormSpRod.Show;

end;

procedure TFormMain.MenuItem7Click(Sender: TObject);
begin
  //  реализация кнопки открытия формы справочника "Год издательства"
   FormSpIzdat.Show;
end;

procedure TFormMain.MenuItem8Click(Sender: TObject);
begin
  //  реализация кнопки открытия формы "Список книг"
  FormKnigList.Show;
end;

end.

