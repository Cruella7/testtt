/* В базе данных хранятся сведения о движении автобусов: номер автобуса, название станции прибытия, количество пассажиров
Структура входного файла in.txt (Номер Станция Количество пассажиров)
23А   Мытищи 37
157МН2 Ярославль 70
23А Мытищи 42
...
Определить общее количество пассажиров, перевезённое каждым автобусом, упорядочив по номеру автобуса
Структура выходного файла out.txt
Номер Количество пассажиров
157МН2 70
23А 79
Выполнила Арутюнян С.К. 32ИС-21 КМПО РАНХиГС
*/
#include <stdio.h>
#include <string.h>

#define MAX_BUSES 100
#define MAX_LEN 50

// Структура для хранения информации о движении автобусов
typedef struct {
    char number[MAX_LEN];   // Номер автобуса
    char station[MAX_LEN];  // Название станции
    int passengers;         // Количество пассажиров
} BusInfo;

/* Функция сортировки массива по номеру автобуса
void Sortnumber(BusInfo array[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int imin = i;
        for (int j = i + 1; j < n; j++) {
            if (strcmp(array[j].number, array[imin].number) < 0) {
                imin = j;
            }
        }
        if (imin != i) {
            BusInfo t = array[imin];
            array[imin] = array[i];
            array[i] = t;
        }
    }
} */

/* Функция сортировки массива по станции
void Sortstation(BusInfo arr[], int r) {
    for (int a = 0; a < r - 1; a++) {
        int indmin = a;
        for (int o = a + 1; o < r; o++) {
            if (strcmp(arr[o].station, arr[indmin].station) < 0) {
                indmin = o;
            }
        }
        if (indmin != a) {
            BusInfo q = arr[indmin];
            arr[indmin] = arr[a];
            arr[a] = q;
        }
    }
}*/

int main() {
    // Открытие файла для чтения
    FILE *in_file = fopen("in.txt", "r");
    if (in_file == NULL) {
        printf("Ошибка открытия файла in.txt\n");
        return 1;
    }

    // Создание массива структур BusInfo
    BusInfo buses[MAX_BUSES];
    int num_buses = 0;  // Количество автобусов

    // Чтение данных из файла и заполнение массива структур
    while (fscanf(in_file, "%s %s %d", buses[num_buses].number, buses[num_buses].station, &buses[num_buses].passengers) == 3) {
        num_buses++; // Увеличение счетчика автобусов
    }
    fclose(in_file); // Закрытие файла после чтения

    /*Вычисление общего количества пассажиров для каждого автобуса
    for (int i = 0; i < num_buses; i++) {
        if (buses[i].passengers == 0) continue; // Пропускаем уже обработанные автобусы
        for (int j = i + 1; j < num_buses; j++) {
            if (strcmp(buses[i].number, buses[j].number) == 0) {
                buses[i].passengers += buses[j].passengers;
                buses[j].passengers = 0; // Помечаем, что автобус j уже обработан
            }
        }
    }*/


    //Сортировка общего количества пассажиров для каждой станции
    for (int i = 0; i < num_buses; i++) {
        for (int j = i + 1; j < num_buses; j++) {
            if (strcmp(buses[i].station, buses[j].station) == 0) {
                buses[i].passengers += buses[j].passengers;
                buses[j].passengers = 0; // Помечаем, что станция  уже обработана
            }
        }
    }
    
    // Открытие файла для записи результатов
    FILE *out_file = fopen("out.txt", "w");
    if (out_file == NULL) {
        printf("Ошибка открытия файла out.txt\n");
        return 1;
    }

    // Вывод информации об автобусе в файл
    fprintf(out_file, "Номер автобуса | Количество пассажиров | Станция\n");
    for (int i = 0; i < num_buses; i++) {
        if (buses[i].passengers != 0) { // Проверяем, что количество пассажиров не равно 0
            fprintf(out_file, "%s %d %s \n", buses[i].number, buses[i].passengers, buses[i].station);
        }
    }
    fclose(out_file); // Закрытие файла после записи
    return 0;
}