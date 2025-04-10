#include <stdio.h>

#define MAX_SIZE 100

int count_elements_between_max(int nums[], int size) {
    int max_value = nums[0];
    int max_indices[MAX_SIZE];
    int count = 0;

    
    for (int i = 1; i < size; ++i) {
        if (nums[i] > max_value) {
            max_value = nums[i];
            count = 1;
            max_indices[0] = i;
        } else if (nums[i] == max_value) {
            max_indices[count++] = i;
        }
    }

   
    if (count == 1) {
        return 0;
    }

    return max_indices[count - 1] - max_indices[0] - 1;
}

int main() {
    int nums[MAX_SIZE];
    int size;

    printf("Введите количество элементов: ");
    scanf("%d", &size);

    printf("Введите элементы через пробел: ");
    for (int i = 0; i < size; ++i) {
        scanf("%d", &nums[i]);
    }

    int result = count_elements_between_max(nums, size);

    printf("Количество элементов между первым и последним максимальным элементом: %d\n", result);

    return 0;
}
