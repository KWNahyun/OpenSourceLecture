# Selection sorting (최솟값 중심 정리)

def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

list = [64, 35, 12, 22, 11]
print("Original list =", list)

selectionSort(list)

print("Sorted list by selection method ")
print(list)