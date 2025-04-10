#include <stdio.h>
#include <string.h>

#define COLLEGE_SIZE 1000
#define EXAMS_COUNT 5000

typedef struct {
    int st_id;
    char gr[20];
    char fio[20];
    char fav_subject[20]; // Добавляем поле для любимой дисциплины
    double avg_mark; // Добавляем поле для среднего балла
} Student;

typedef struct {
    int st_id;
    char subject[20];
    double mark;
} Session;

int main(void) {
    Student v_students[COLLEGE_SIZE];
    Session v_session[EXAMS_COUNT];

    // Чтение информации о студентах из файла
    FILE *f_students = fopen("students.txt", "r");
    int n_students = 0;
    while (fscanf(f_students, "%d;%19[^;];%19[^;];%19s", &v_students[n_students].st_id,
                  v_students[n_students].gr, v_students[n_students].fio, v_students[n_students].fav_subject) == 4) {
        fgetc(f_students); // Считываем символ новой строки
        n_students++;
    }
    fclose(f_students);

    // Чтение информации об экзаменах из файла
    FILE *f_session = fopen("session.txt", "r");
    int n_session = 0;
    while (fscanf(f_session, "%d;%19[^;];%lf", &v_session[n_session].st_id,
                  v_session[n_session].subject, &v_session[n_session].mark) == 3) {
        fgetc(f_session); // Считываем символ новой строки
        n_session++;
    }
    fclose(f_session);

    // Расчет среднего балла для каждого студента
    for (int i = 0; i < n_students; i++) {
        double sum_marks = 0.0;
        int count_marks = 0;
        for (int j = 0; j < n_session; j++) {
            if (v_students[i].st_id == v_session[j].st_id &&
                strcmp(v_students[i].fav_subject, v_session[j].subject) == 0) {
                sum_marks += v_session[j].mark;
                count_marks++;
            }
        }
        if (count_marks > 0) {
            v_students[i].avg_mark = sum_marks / count_marks;
        } else {
            v_students[i].avg_mark = 0.0;
        }
    }

    // Сортировка студентов по группе и фамилии
    for (int i = 0; i < n_students - 1; i++) {
        for (int j = i + 1; j < n_students; j++) {
            if (strcmp(v_students[i].gr, v_students[j].gr) > 0 ||
                (strcmp(v_students[i].gr, v_students[j].gr) == 0 &&
                 strcmp(v_students[i].fio, v_students[j].fio) > 0)) {
                // Поменять местами
                Student temp = v_students[i];
                v_students[i] = v_students[j];
                v_students[j] = temp;
            }
        }
    }

    // Вывод информации о студентах в файл
    FILE *f_out = fopen("out.txt", "w");
    for (int i = 0; i < n_students; i++) {
        fprintf(f_out, "%s %s %s %.2f\n", v_students[i].gr, v_students[i].fio,
                v_students[i].fav_subject, v_students[i].avg_mark);
    }
    fclose(f_out);

    return 0;
}
