program project1;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  {$IFDEF HASAMIGA}
  athreads,
  {$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, Unit1, Unit2, Unit3, Unit4, Unit5, Unit6, Unit7, Unit8, Unit9, Unit10,
  unit1AddBus, unitSpMark, unitSpNumber, unitSpVmes
  { you can add units after this };

{$R *.res}

begin
  RequireDerivedFormResource:=True;
  Application.Scaled:=True;
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.CreateForm(TAbout, About);
  Application.CreateForm(TFormBus, FormBus);
  Application.CreateForm(TFormSt, FormSt);
  Application.CreateForm(TFormR, FormR);
  Application.CreateForm(TZapros1, Zapros1);
  Application.CreateForm(TZapros2, Zapros2);
  Application.CreateForm(TAddR, AddR);
  Application.CreateForm(TKodSt, KodSt);
  Application.CreateForm(TNameSt, NameSt);
  Application.CreateForm(TFormAddBus, FormAddBus);
  Application.CreateForm(TFormSpMark, FormSpMark);
  Application.CreateForm(TFormSpNumber, FormSpNumber);
  Application.CreateForm(TFormSpVmes, FormSpVmes);
  Application.Run;
end.

