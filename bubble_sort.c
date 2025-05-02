/**
 * Implementation of the bubble sort algorithm
 * with potential memory safety concerns.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Performs bubble sort on an array of integers.
 * 
 * @param arr The array to sort
 * @param size The size of the array
 */
void bubble_sort(int* arr, int size) {
    if (arr == NULL || size <= 0) {
        return;
    }
    
    int i, j, temp;
    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap the elements
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

/**
 * Allocates memory for an array and initializes it with the given values.
 * Caller must free the returned pointer.
 * 
 * @param values Array of values to copy
 * @param size Size of the array
 * @return Pointer to the new array or NULL if allocation fails
 */
int* create_array(const int* values, int size) {
    if (values == NULL || size <= 0) {
        return NULL;
    }
    
    int* new_array = (int*)malloc(size * sizeof(int));
    if (new_array == NULL) {
        return NULL;
    }
    
    memcpy(new_array, values, size * sizeof(int));
    return new_array;
}

/**
 * Merges two sorted arrays into a single sorted array.
 * Caller must free the returned pointer.
 * 
 * @param arr1 First sorted array
 * @param size1 Size of first array
 * @param arr2 Second sorted array
 * @param size2 Size of second array
 * @return Pointer to the merged array or NULL if allocation fails
 */
int* merge_sorted_arrays(int* arr1, int size1, int* arr2, int size2) {
    if (arr1 == NULL || arr2 == NULL || size1 < 0 || size2 < 0) {
        return NULL;
    }
    
    int total_size = size1 + size2;
    int* result = (int*)malloc(total_size * sizeof(int));
    if (result == NULL) {
        return NULL;
    }
    
    int i = 0, j = 0, k = 0;
    
    // Merge the two arrays
    while (i < size1 && j < size2) {
        if (arr1[i] <= arr2[j]) {
            result[k++] = arr1[i++];
        } else {
            result[k++] = arr2[j++];
        }
    }
    
    // Copy remaining elements from first array, if any
    while (i < size1) {
        result[k++] = arr1[i++];
    }
    
    // Copy remaining elements from second array, if any
    while (j < size2) {
        result[k++] = arr2[j++];
    }
    
    return result;
}

/**
 * Filters an array to extract only values greater than the threshold.
 * Caller must free the returned pointer.
 * 
 * @param arr Input array
 * @param size Size of input array
 * @param threshold The threshold value
 * @param result_size Pointer to store the size of result array
 * @return Pointer to filtered array or NULL if allocation fails
 */
int* filter_array(int* arr, int size, int threshold, int* result_size) {
    if (arr == NULL || size <= 0 || result_size == NULL) {
        *result_size = 0;
        return NULL;
    }
    
    // Count elements that match the criteria
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > threshold) {
            count++;
        }
    }
    
    // Allocate memory for filtered array
    int* result = NULL;
    if (count > 0) {
        result = (int*)malloc(count * sizeof(int));
        if (result == NULL) {
            *result_size = 0;
            return NULL;
        }
        
        // Copy matching elements
        int j = 0;
        for (int i = 0; i < size; i++) {
            if (arr[i] > threshold) {
                result[j++] = arr[i];
            }
        }
    }
    
    *result_size = count;
    return result; // Could be NULL if count is 0
}

/**
 * Finds the median value in an array.
 * Note: This function modifies the original array by sorting it.
 * 
 * @param arr Input array
 * @param size Size of the array
 * @return The median value of the array
 */
double find_median(int* arr, int size) {
    if (arr == NULL || size <= 0) {
        return 0.0;
    }
    
    // Sort the array
    bubble_sort(arr, size);
    
    // Calculate median
    if (size % 2 == 0) {
        // Even number of elements - average of two middle elements
        return (arr[size / 2 - 1] + arr[size / 2]) / 2.0;
    } else {
        // Odd number of elements - middle element
        return arr[size / 2];
    }
}

/**
 * Main function that demonstrates the usage of the above functions.
 */
int main() {
    const int test_array[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(test_array) / sizeof(test_array[0]);
    
    // Create a copy of the array
    int* array_copy = create_array(test_array, size);
    if (array_copy == NULL) {
        printf("Failed to allocate memory for array copy\n");
        return 1;
    }
    
    // Sort the array
    bubble_sort(array_copy, size);
    
    // Print the sorted array
    printf("Sorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array_copy[i]);
    }
    printf("\n");
    
    // Find median
    double median = find_median(array_copy, size);
    printf("Median value: %.1f\n", median);
    
    // Filter array
    int filtered_size;
    int* filtered_array = filter_array(array_copy, size, 20, &filtered_size);
    if (filtered_array != NULL) {
        printf("Elements greater than 20: ");
        for (int i = 0; i < filtered_size; i++) {
            printf("%d ", filtered_array[i]);
        }
        printf("\n");
        free(filtered_array);
    }
    
    // Create another array for merging
    const int test_array2[] = {10, 20, 30, 40, 50};
    int size2 = sizeof(test_array2) / sizeof(test_array2[0]);
    int* array_copy2 = create_array(test_array2, size2);
    
    if (array_copy2 != NULL) {
        // Merge the two sorted arrays
        int* merged_array = merge_sorted_arrays(array_copy, size, array_copy2, size2);
        if (merged_array != NULL) {
            printf("Merged array: ");
            for (int i = 0; i < size + size2; i++) {
                printf("%d ", merged_array[i]);
            }
            printf("\n");
            free(merged_array);
        }
        free(array_copy2);
    }
    
    // Cleanup
    free(array_copy);
    
    return 0;
}