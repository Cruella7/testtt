// bus_data.h

#ifndef BUS_DATA_H
#define BUS_DATA_H

#define MAX_BUSES 100
#define MAX_LEN 50

// Структура для хранения информации о движении автобусов
typedef struct {
    char number[MAX_LEN];   // Номер автобуса
    char station[MAX_LEN];  // Название станции
    int passengers;         // Количество пассажиров
} BusInfo;

extern BusInfo buses[MAX_BUSES];
extern int num_buses;

// Прототипы функций
void loadFromFile();
void writeToOutFile();

#endif // BUS_DATA_H
