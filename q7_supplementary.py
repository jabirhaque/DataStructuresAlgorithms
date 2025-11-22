def merge(A,B):
    """Return the sorted lists A and B merged into
    a single list L
    """
    L=[]
    while A and B:
        if A[0] <= B[0]:
            L.append(A.pop(0))
        else:
            L.append(B.pop(0))
    L.extend(A)
    L.extend(B)
    return L

def check_list(L):
    """Return a pair (A,B) of lists (or None values)

    Check if L is sorted, or can be partitioned
    into sorted subsequences A and B, or neither,
    and return (L,None) or (A,B) or (None,None)
    accordingly
    """

def best_pivot(L,p1,p2,p3):
    """Return the pivot candidate among p1, p2, p3 that
    splits L in the most balanced way

    """

def extra_check_quicksort(L):
    """Return a sorted version of L

    Use check_list to check if L is sorted or can be partitioned
    into two sorted sublists. Otherwise, pick the elements at
    the start, middle and end of L as candidate pivots and
    use best_pivot to select the best of them. Then partition
    the list using that pivot, make recursive calls, and
    combine the results to get a sorted version of L.
    """

assert check_list([1,5,8]) == ([1,5,8],None)

(A,B) = check_list([4,1,2,5,8,9,3])
assert ( A == [4,5,8,9] and B == [1,2,3] ) or ( A == [1,2,3] and B == [4,5,8,9] )

assert check_list([4,8,12,7,14,6]) == (None,None)

assert best_pivot([5,2,3,1,4],5,3,4) == 3

L=[ 20,13,15,12,17,19,25 ]
assert extra_check_quicksort(L) == [12,13,15,17,19,20,25]

