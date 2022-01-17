# Recall the “Building Block” strategy discussed in previous classes. Using this strategy:
# a. Implement “merge” algorithm as a building block (as a function).
# b. Implement “mergeSort” algorithm using recursion. Use “merge” as the building 
# block in the implementation of mergeSort.
# c. Test your program on a randomly generated list of 100 integers and display the 
# output.

def merge(LeftHalf_List,RightHalf_List):
    Sorted_List = []
    LeftHalf_Index = 0
    RightHalf_Index = 0
    LeftHalf_Length = len(LeftHalf_List)
    RightHalf_Length = len(RightHalf_List)
    for i in range(LeftHalf_Length + RightHalf_Length):
        if  LeftHalf_Index < LeftHalf_Length and RightHalf_Index < RightHalf_Length:
            if LeftHalf_List[LeftHalf_Index] <= RightHalf_List[RightHalf_Index]:
                Sorted_List.append(LeftHalf_List[LeftHalf_Index])
                LeftHalf_Index = LeftHalf_Index + 1
            else:
                Sorted_List.append(RightHalf_List[RightHalf_Index])
                RightHalf_Index = RightHalf_Index + 1
        elif LeftHalf_Index == LeftHalf_Length:
            Sorted_List.append(RightHalf_List[RightHalf_Index])
            RightHalf_Index = RightHalf_Index + 1
        elif RightHalf_Index == RightHalf_Length:
            Sorted_List.append(LeftHalf_List[LeftHalf_Index])
            LeftHalf_Index = LeftHalf_Index + 1
    return Sorted_List
def merge_Sort(Unsorted_List):
    if len(Unsorted_List) <= 1:
        return Unsorted_List
    Half = len(Unsorted_List)//2
    LeftHalf_List = (Unsorted_List[:Half])
    print("Left HAlf Merged List = ", LeftHalf_List)
    RightHalf_List = (Unsorted_List[Half:])
    print("Right HAlf Merged List = ", RightHalf_List)
    LeftHalf_List = merge_Sort(Unsorted_List[:Half])
    RightHalf_List = merge_Sort(Unsorted_List[Half:])
    return merge(LeftHalf_List,RightHalf_List)
import random
print("Enter the number from where you satrt to generate List: ")
Start = int(input(" "))
print("Enter the Limit where you want to end the List: ")
End = int(input(" "))
print("How many numbers you want to generate in a unsorted List: ")
Limit = int(input(" "))
Unsorted_List = random.sample(range(Start, End), Limit)
print("Here is Given Below random generated List By the User: ")
print(Unsorted_List)
Unsorted_List = merge_Sort(Unsorted_List)
print("Here is the User Given Sorted List")
print(Unsorted_List)
