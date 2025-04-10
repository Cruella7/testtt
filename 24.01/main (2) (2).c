#include <stdio.h>
#include <string.h>
/*1.	јвтовокзал. 
јвтобусы производ€т рейсы до станций по расписанию.  аждый автобус вмещает не более определенного количества пассажиров
“аблицы: станции (код станции, название станции), автобусы (код автобуса, марка автобуса, государственный номер, вместимость), рейсы (код рейса, код станции, код автобуса, врем€ отправлени€).
ќпределить:
- сколько выполн€етс€ рейсов до каждой станции?
- каково общее количество пассажиров?
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

