#include <iostream>

namespace algorithms{
    void bubbleSort(int arr[], int tamanho){
        for (int i = 0; i < tamanho - 1; i++){
            for(int j = 0; j < tamanho - 1; j++){
                if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                }
            }
        }
        for(k = 0; k < tamanho; k++){
            cout << arr[k] << " ";
        }
    }


                void Merge(int arr[], int left, int mid, int right){
                    int i,j,k;
                    int n1 = mid - left + 1 
                    int n2 = right - mid;
                    int L[n1], R[n2];

                    for(i = 0; i < n1; i++){
                        L[i] = arr[left+1];
                    }
                    for(j=0;j< n2; j ++){
                        R[j]= arr[mid + 1 + j]
                    }

                    i = 0;
                j = 0;
                k = left;

                while (i < n1 && j < n2) {
                    if (L[i] <= R[j]) {
                        arr[k] = L[i];
                        ++i;
                    } else {
                        arr[k] = R[j];
                        ++j;
                    }
                    ++k;
                }
                
                while (i < n1) {
                    arr[k] = L[i];
                    ++i;
                    ++k;
                }

                while (j < n2) {
                    arr[k] = R[j];
                    ++j;
                    ++k;
                }
            }


    void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

    void insertionSort(int arr[], int size) {
    for (int i = 1; i < size; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        arr[j + 1] = key;
    }
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

    void linearSearch(int arr[], int goal){
        // Esse aqui foi eu que fiz "Ah, mas pq tá em ingles?" Para manter o padrão no código, com exceção dos comentários
        size = sizeof(arr)  - 1;
    for(int = 0; i < size; i ++){
        if arr[i] == goal{
            cout << "Goal found at index " << arr[i]; 
        }
    }
    }

    void binarySerach(int arr[], int low, int high, x){
        while (low <=  high){
            int mid = low + (high - low) / 2;
        if(arr[mid] == x){
            return mid;
        }
        if(arr[mid] < x){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }

        // Se o elemento não for encontrado
        return -1;
    }


}







