#include <stdio.h>
#include <string.h>
/*1.	����������. 
�������� ���������� ����� �� ������� �� ����������. ������ ������� ������� �� ����� ������������� ���������� ����������
�������: ������� (��� �������, �������� �������), �������� (��� ��������, ����� ��������, ��������������� �����, �����������), ����� (��� �����, ��� �������, ��� ��������, ����� �����������).
����������:
- ������� ����������� ������ �� ������ �������?
- ������ ����� ���������� ����������?
*/
#define MAX_SIZE 10000

typedef struct {
    int codeS;
    char name[MAX_SIZE];
} Station;

typedef struct {
    int codeB;
    char mark [MAX_SIZE];
    int gosnum;
    int vmest;
} Bus;

typedef struct {
    int codeR;
    int codeS;
    int codeB;
    char time[MAX_SIZE];
} Reis;

