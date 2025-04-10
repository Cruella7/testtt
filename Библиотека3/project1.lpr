program project1;

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}{$IFDEF UseCThreads}
  cthreads,
  {$ENDIF}{$ENDIF}
  Interfaces, // this includes the LCL widgetset
  Forms, unitMain, unitKnigList, unitKnigaEdit,
  unitSpIzdat, unitSpAvtor, unitSpRod
  { you can add units after this };

{$R *.res}

begin
  RequireDerivedFormResource:=True;
  Application.Scaled:=True;
  Application.Initialize;
  Application.CreateForm(TFormMain, FormMain);
  Application.CreateForm(TFormKnigList, FormKnigList);
  Application.CreateForm(TFormKnigaEdit, FormKnigaEdit);
  Application.CreateForm(TFormSpIzdat, FormSpIzdat);
  Application.CreateForm(TFormSpAvtor, FormSpAvtor);
  Application.CreateForm(TFormSpRod, FormSpRod);
  Application.Run;
end.

