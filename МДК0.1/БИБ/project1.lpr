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
  Forms, unitMain, unitKnigList, unitKnigaEdit, unitSpavtor, unitSpName, 
unitSpiZ
  { you can add units after this };

{$R *.res}

begin
  RequireDerivedFormResource:=True;
  Application.Scaled:=True;
  Application.Initialize;
  Application.CreateForm(TFormMain, FormMain);
  Application.CreateForm(TFormKnigList, FormKnigList);
  Application.CreateForm(TFormKnigaEdit, FormKnigaEdit);
  Application.CreateForm(TFormSpavtor, FormSpavtor);
  Application.CreateForm(TFormSpName, FormSpName);
  Application.CreateForm(TFormSpiZ, FormSpiZ);
  Application.Run;
end.

