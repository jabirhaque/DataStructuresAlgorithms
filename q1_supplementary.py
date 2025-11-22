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
    def points(compressed_moves_A, compressed_moves_B):
        if compressed_moves_A == compressed_moves_B: return 0,0
        a = 0
        b = 0
        if compressed_moves_A[0] == 'R':
            if compressed_moves_B[0] == 'S':
                a += 1
            elif compressed_moves_B[0] == 'P':
                b += 1
        elif compressed_moves_A[0] == 'P':
            if compressed_moves_B[0] == 'R':
                a += 1
            elif compressed_moves_B[0] == 'S':
                b += 1
        else:
            if compressed_moves_B[0] == 'P':
                a += 1
            elif compressed_moves_B[0] == 'R':
                b += 1

        if compressed_moves_A[1] == '1':
            compressed_moves_A = compressed_moves_A[2:]
        else:
            compressed_moves_A = compressed_moves_A[0] + str(int(compressed_moves_A[1])-1) + compressed_moves_A[2:]
        if compressed_moves_B[1] == '1':
            compressed_moves_B = compressed_moves_B[2:]
        else:
            compressed_moves_B = compressed_moves_B[0] + str(int(compressed_moves_B[1])-1) + compressed_moves_B[2:]

        i, j = points(compressed_moves_A, compressed_moves_B)
        return a+i, b+j

    a, b = points(compressed_moves_A, compressed_moves_B)
    if a > b: return "A"
    if a < b: return "B"
    return "D"


#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q1.py ####

def q1_simple_tests():
    # --- Given example ---
    moves_a = "RRSPPS"
    moves_b = "RSPRSP"
    assert(compute_winner(moves_a, moves_b) == "A")
    assert(encode(moves_a) == "R2S1P2S1")
    assert(encode(moves_b) == "R1S1P1R1S1P1")
    assert(decode("R2S3P1") == "RRSSSP")
    assert(compute_winner_compressed(encode(moves_a), encode(moves_b)) == "A")

    # --- Basic single-move cases ---
    assert(compute_winner("R", "S") == "A")
    assert(compute_winner("S", "R") == "B")
    assert(compute_winner("P", "P") == "D")

    # --- Equal repeated moves ---
    assert(encode("RRR") == "R3")
    assert(encode("SSS") == "S3")
    assert(encode("PPP") == "P3")
    assert(decode("R3") == "RRR")

    # --- Alternating sequences ---
    assert(encode("RPRPRP") == "R1P1R1P1R1P1")
    assert(decode("R1P1R1P1R1P1") == "RPRPRP")

    # --- Edge: long mixed + decode + encode inversion ---
    m = "RRRSSPPSSPRR"
    assert(decode(encode(m)) == m)

    # --- Winner consistency between compressed and normal ---
    a = "RRRRSSPPPS"
    b = "SSSSRPRPRS"
    assert(compute_winner(a, b) == compute_winner_compressed(encode(a), encode(b)))

    # --- Draw cases ---
    assert(compute_winner("RPS", "RPS") == "D")
    assert (compute_winner("RPS", "RSP") == "D")
    # Check compressed version too
    assert(compute_winner_compressed("R1P1S1", "R1P1S1") == "D")

    # --- All pairwise matchups for length 3 ---
    for A in ["R", "P", "S"]:
        for B in ["R", "P", "S"]:
            # build length-3 repeats
            sA = A*3
            sB = B*3
            winner = compute_winner(sA, sB)
            winner_c = compute_winner_compressed(encode(sA), encode(sB))
            assert(winner == winner_c)

    # --- Alternating long tests ---
    a = "RPS"*5
    b = "SPR"*5
    assert(compute_winner(a, b) == compute_winner_compressed(encode(a), encode(b)))

    # --- Random-like (deterministic) patterns ---
    patterns = [
        "RRSPSPRSPR",
        "SPPRRSSRSP",
        "PRSRSPRSPR",
        "RRRRRPSSSS",
        "PSPSPSPSPS",
        "RSSPRSPRSP",
    ]
    for x in patterns:
        for y in patterns:
            assert(decode(encode(x)) == x)
            assert(compute_winner(x, y) == compute_winner_compressed(encode(x), encode(y)))

    print("All tests passed!")

q1_simple_tests()