unit unitKnigList;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ComCtrls, StdCtrls,
  Grids, Buttons, EditBtn;

// описание структуры
type
  Kniga = record
    Avtor : String[50];
    Nazvanie : String[50];
    GodIzdan : String[4];
    Rod : String[50];
  end;


type
  { TFormKnigList }

  TFormKnigList = class(TForm)
    BtnAdd: TBitBtn;
    BtnEdit: TBitBtn;
    BtnDel: TBitBtn;
    ComboBox1: TComboBox;
    EditButton1: TEditButton;
    StringGrid1: TStringGrid;
    ToolBar1: TToolBar;
    procedure BtnAddClick(Sender: TObject);
    procedure BtnDelClick(Sender: TObject);
    procedure BtnEditClick(Sender: TObject);
    //procedure ComboBox1Change(Sender: TObject);
    procedure EditButton1ButtonClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure UpdateGrid(Sender: TObject);
    procedure WriteToFile( namfile : string; kng : Kniga );
    procedure WriteArrToFile( namfile : string; count : integer;  kng : array of Kniga );
  private

  public
    //массив структур
   arrKnig : array[1..100] of Kniga;
   // переменная для хранения количества элементов массива
   arrCount : integer;
   // переменная - режим добавления и режим редактирования
   reg : integer;
  end;

var
  FormKnigList: TFormKnigList;

implementation
 uses unitKnigaEdit;
{$R *.lfm}

{ TFormKnigList }

//сохранение данных в файл
 procedure TFormKnigList.WriteToFile( namfile : string; kng : Kniga );
 var
   f : Text;
 begin
  AssignFile(f, namfile);
  Append(f);
  WriteLn(f, kng.Avtor);
  WriteLn(f, kng.Nazvanie);
  WriteLn(f, kng.GodIzdan);
  WriteLn(f, kng.Rod);
  WriteLn(f, '');
  CloseFile(f);
 end;

 // сохранение измененного массива в файл
 procedure TFormKnigList.WriteArrToFile( namfile : string; count : integer;  kng : array of Kniga );
 var
   f : Text;
   i : integer;
 begin
  AssignFile(f, namfile);
  Rewrite(f);
  for i:=1 to  count do begin
      WriteLn(f, kng[i].Avtor);
      WriteLn(f, kng[i].GodIzdan);
      WriteLn(f, kng[i].Rod);
      WriteLn(f, '');
   END;
  CloseFile(f);
 end;

procedure TFormKnigList.FormShow(Sender: TObject);
 var
  f : Text; //создание файловой переменной
  i : Integer; //локальная переменная для индексом массива
begin
  i := 1;
  //связываем переменную с файлом
  AssignFile(f, 'db/listknig.db');

  // открываем файл для чтения
  Reset(f);

  //построчное считывание до конца файла
  while not (EOF(f)) do begin
     ReadLn(f, arrKnig[i].Avtor);
     ReadLn(f, arrKnig[i].Nazvanie);
     ReadLn(f, arrKnig[i].GodIzdan);
     ReadLn(f, arrKnig[i].Rod);

  //считываем пустую строку, которая разделяет блоки между собой
     ReadLn(f);
     i := i + 1;
  end;

  // закрытие файла
    CloseFile(f);
 arrCount := i - 1 ;

 // обновление
 UpdateGrid(Sender);


end;
 // процедура для обновления данных
procedure TFormKnigList.UpdateGrid(Sender: TObject);
var
 i : Integer;
begin
 // считываем количество элементов
 StringGrid1.RowCount:= arrCount + 1;


 // запись элементов из массива в грид
 for i:=1 to arrCount do  begin
     StringGrid1.Cells[0, i] := arrKnig[i].Avtor;
     StringGrid1.Cells[1, i] := arrKnig[i].Nazvanie;

     // если поле "год издания" пустой - автоматически пишет "нет"
     if arrKnig[i].GodIzdan = '' then  StringGrid1.Cells[2, i] := 'Нет' else
        StringGrid1.Cells[2, i] := arrKnig[i].GodIzdan;

     // если поле "год издания" пустой - автоматически пишет "нет"
     if arrKnig[i].Rod = '' then  StringGrid1.Cells[2, i] := 'Нет' else
        StringGrid1.Cells[3, i] := arrKnig[i].Rod;
   end;

end;

// открытие формы в режиме добавления записи
procedure TFormKnigList.BtnAddClick(Sender: TObject);
begin
 // реализация кнопки добавить, после которой открывается форма для заполнения книг
 reg := 1;
 FormKnigaEdit.ShowModal;
end;

// выбор определенной строки и ее удаление
procedure TFormKnigList.BtnDelClick(Sender: TObject);
var
 i : Integer;
 x : Integer;
begin
  // индекс выделенной строки
  x := StringGrid1.Row;

  // удаление элемента из массива
  for i:= x to arrCount-1 do begin
    arrKnig[x] := arrKnig[x+1];
  end;
  // уменьшение количества элементов в массиве
  arrCount:=arrCount-1;

  // очищение грида
  for i:=1 to StringGrid1.RowCount-1 do
    StringGrid1.Rows[i].Clear;

  //обновление грида
  UpdateGrid(Sender);

  FormKnigList.WriteArrToFile('db/listknig.db', FormKnigList.arrCount, FormKnigList.arrKnig );

end;

// открытие формы в режиме редактирования записи
procedure TFormKnigList.BtnEditClick(Sender: TObject);
begin
 // открывается такая же форма, что и при добавлении, но уже с веденными данными
 reg := 2;
 FormKnigaEdit.ShowModal;
end;

// поиск
procedure TFormKnigList.EditButton1ButtonClick(Sender: TObject);
var
 i, k : Integer;
begin
  // очищаем грид
  for i:=1 to StringGrid1.RowCount-1 do
    StringGrid1.Rows[i].Clear;

  k:= 1;  // счетчик, чтобы текущее расположение строки не зависело от других сток


  // поиск по определенным атрибутам
  if ComboBox1.ItemIndex = 0 then

  // проходим по всему массиву
  for i:= 1 to arrCount do

    // ищем то значение, которое мы ввели в поиске
    if ( arrKnig[i].Avtor = EditButton1.Text) then begin

       // найденное значение выводим в массив
       StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
       StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
       StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
       StringGrid1.Cells[3, k] := arrKnig[i].Rod;
       k := k +1;

       // для уменьшения количества строк
       StringGrid1.RowCount:= k;
  end;


  if ComboBox1.ItemIndex = 1 then
  // проходим по всему массиву
  for i:= 1 to arrCount do

    // ищем то значение, которое мы ввели в поиске
    if ( arrKnig[i].Nazvanie = EditButton1.Text) then begin

       // найденное значение выводим в массив
       StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
       StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
       StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
       StringGrid1.Cells[3, k] := arrKnig[i].Rod;
       k := k +1;

       // для уменьшения количества строк
       StringGrid1.RowCount:= k;
  end;


      // ищем то значение, которое мы ввели в поиске
    if ( arrKnig[i].Rod = EditButton1.Text) then begin

       // найденное значение выводим в массив
       StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
       StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
       StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
       StringGrid1.Cells[3, k] := arrKnig[i].Rod;
       k := k +1;

       // для уменьшения количества строк
       StringGrid1.RowCount:= k;
  end;



  if ComboBox1.ItemIndex = 2 then

  // проходим по всему массиву
  for i:= 1 to arrCount do

    // ищем то значение, которое мы ввели в поиске
    if ( arrKnig[i].GodIzdan = EditButton1.Text) then begin

       // найденное значение выводим в массив
       StringGrid1.Cells[0, k] := arrKnig[i].Avtor;
       StringGrid1.Cells[1, k] := arrKnig[i].Nazvanie;
       StringGrid1.Cells[2, k] := arrKnig[i].GodIzdan;
       StringGrid1.Cells[3, k] := arrKnig[i].Rod;
       k := k +1;

       // для уменьшения количества строк
       StringGrid1.RowCount:= k;
  end;

  // при пустом поле отображается весь список
  if (EditButton1.Text = '' ) then  UpdateGrid(Sender);

end;

end.

