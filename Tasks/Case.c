#include <stdio.h>

void number_name(int num) {
    if (!(100 <= num && num <= 999)) {
        printf("Не входит в диапозон\n");
        return;
    }

    char *ed_dict[] = {"", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"};
    char *desyatkiex_dict[] = {"", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"};
    char *desyatki_dict[] = {"", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"};
    char *sotnyi_dict[] = {"", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"};

    int sotnyi = num / 100;
    int remainder = num % 100;
    int desyatki = remainder / 10;
    int ed = remainder % 10;

    printf("%s %s %s\n", sotnyi_dict[sotnyi], desyatki_dict[desyatki], ed_dict[ed]);
}

int main() {
    int number;
    printf("Ввод: ");
    scanf("%d", &number);

    number_name(number);

    return 0;
}
