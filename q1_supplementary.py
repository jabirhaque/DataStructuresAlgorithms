#!/usr/bin/env python

#### WRITE YOUR SOLUTION BELOW####
#### COPY YOUR CODE FROM BELOW INTO A FILE q1.py FOR SUBMISSION ####
def compute_winner(moves_A, moves_B):
    """Computes the winner of a rock-paper-scissors game given the moves of players A and B.
    Returns "A" if player A wins, "B" if player B wins, and "D" if it is a draw.
    """
    a = 0
    b = 0
    for i in range(0,len(moves_A)):
        if moves_A[i] == 'R':
            if moves_B[i] == 'S':
                a+=1
            elif moves_B[i] == 'P':
                b+=1
        elif moves_A[i] == 'P':
            if moves_B[i] == 'R':
                a+=1
            elif moves_B[i] == 'S':
                b+=1
        else:
            if moves_B[i] == 'P':
                a += 1
            elif moves_B[i] == 'R':
                b += 1
    if a>b: return "A"
    if a<b: return "B"
    return "D"




def encode(moves):
    compressed = ""
    i=0
    while i<len(moves):
        j = i+1
        while j<len(moves) and moves[j] == moves[i]:
            j+=1
        compressed += moves[i]
        compressed += str(j-i)
        i = j
    return compressed


def decode(compressed_moves):
    decompressed = ""
    for i in range(0, len(compressed_moves), 2):
        for j in range(0, int(compressed_moves[i+1])):
            decompressed += compressed_moves[i]
    return decompressed

def compute_winner_compressed(compressed_moves_A, compressed_moves_B):

    def outcome(a, b):
        if a == b:
            return 0
        if (a, b) in [('R', 'S'), ('S', 'P'), ('P', 'R')]:
            return 1
        return -1

    i = j = 0
    remA = remB = 0

    scoreA = 0
    scoreB = 0

    while i < len(compressed_moves_A) and j < len(compressed_moves_B):
        if remA == 0:
            moveA = compressed_moves_A[i]
            remA = int(compressed_moves_A[i+1])
            i += 2
        if remB == 0:
            moveB = compressed_moves_B[j]
            remB = int(compressed_moves_B[j+1])
            j += 2
        k = min(remA, remB)
        result = outcome(moveA, moveB)
        if result == 1:
            scoreA += k
        elif result == -1:
            scoreB += k
        remA -= k
        remB -= k
    if scoreA > scoreB:
        return "A"
    elif scoreB > scoreA:
        return "B"
    return "D"


#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q1.py ####

moves_a = "RRSPPS"
moves_b = "RSPRSP"


def q1_simple_tests():
    assert(compute_winner(moves_a,moves_b)=="A")
    assert(encode(moves_a)=="R2S1P2S1")
    assert(encode(moves_b)=="R1S1P1R1S1P1")
    assert(decode("R2S3P1")=="RRSSSP")
    assert(compute_winner_compressed(encode(moves_a),encode(moves_b))=="A")
    
q1_simple_tests()