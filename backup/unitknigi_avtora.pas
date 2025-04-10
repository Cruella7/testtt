unit unitKnigi_avtora;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ValEdit, Grids,
  ExtCtrls, EditBtn;

type

  { TFormKnigi_avtora }

  TFormKnigi_avtora = class(TForm)
    EditButton1: TEditButton;
    OpenDialog_Avtor: TOpenDialog;
    StringGrid1: TStringGrid;
  private

  public

  end;

var
  FormKnigi_avtora: TFormKnigi_avtora;

implementation

{$R *.lfm}

end.

