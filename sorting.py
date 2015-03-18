# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:51:40 2014

@author: Wang Yacong
"""

# sorting algorithm
# buble sort
# special focus function with on return value
def bubble_sort(a_list):    
    for pass_num in range(len(a_list) - 1, 0, -1):
        #print a_list
        for i in range(pass_num):            
            if a_list[i] > a_list[i + 1]:                
                # swap two values
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp    
#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#bubble_sort(a_list)
#print(a_list)

# when listed already sorted ,stop the loop and continue the next loop
def short_bubble_sort(a_list):    
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:                
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_num = pass_num - 1    
#a_list=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
#short_bubble_sort(a_list)
#print a_list

def selection_sort(li):
    for i in range(len(li)-1):  #外循环控制趟数，n个数选n-1趟
        pos_of_min = i          #假设当前趟的第一个数为最小值,记在pos_of_min中
        for j in range(i + 1, len(li)):  #从下一个数到最后一个数之间找最值
            if li[j] < li[pos_of_min]:  #若其后有比最值更小的
                pos_of_min = j          #则将其下标记在index中
        if pos_of_min != i:             #若pos_of_min不为最初的i值，说明在其后找到比其更小的数
            temp = li[pos_of_min]       #交换两数
            li[pos_of_min] = li[i]
            li[i] = temp

#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#selection_sort(a_list)
#print(a_list)

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#insertion_sort(a_list)
#print(a_list)

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value
#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#shell_sort(a_list)
#print(a_list)   

# an divide and couquer algorithm
def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list)//2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print ("Merging", a_list)
#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#merge_sort(a_list)
#print(a_list)

# quick sort
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)           
def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
b_list = a_list[:] # make an copy of original list
# quick_sort(b_list)
# print(a_list)
# print(b_list)









