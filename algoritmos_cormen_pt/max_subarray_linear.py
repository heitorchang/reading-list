# p. 55 ex. 4.1-5

# Unsolved, gave up

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, -9999]

def max_subarray_linear(A):
    max_left = 0
    max_right = 0
    max_sum = 0
    running_sum = 0
    for i in range(len(A)):
        if max_right == i and A[i] > 0:  # max_subarray extends to end
            max_right = i
            max_sum += A[i]
        elif A[i] > max_sum:
            max_left = i
            max_right = i
            max_sum = A[i]
            running_sum = 0
        else:
            running_sum += A[i]
            print("unhandled case")

        # print("{}\t{}\t{}".format(A[i], running_sum, max_sum))
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(A[i], max_sum, max_left, max_right, max_sum, running_sum))

# http://www.math.rutgers.edu/~ajl213/CLRS/Ch4.pdf
def linear_time_max_subarray(A):
    M = float('-inf')
    low_M = high_M = None
    M_r = 0
    low_r = 0

    print("{}\t{}\t\t{}\t\t{}\t{}\t{}".format("A[i]", "M_r", "M", "low_M", "high_M", "low_r"))
    for i in range(len(A)):
        M_r += A[i]
        if M_r > M:
            low_M = low_r
            high_M = i
            M = M_r
        elif M_r < 0:
            M_r = 0
            low_r = i + 1
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(A[i], M_r, M, low_M, high_M, low_r))
    return (low_M, high_M, M)

def my_linear_time_max_subarray(A):
    max_sum = float('-inf')
    max_left = max_right = None
    running_sum = 0
    running_left = 0

    for i in range(len(A)):
        running_sum += A[i]
        if running_sum > max_sum:
            max_left = running_left
            max_right = i
            max_sum = running_sum
        elif running_sum < 0:
            running_sum = 0
            running_left = i + 1
    return (max_left, max_right, max_sum)

def my_max_subarray_2(A):
    max_sum = float('-inf')
    max_left = max_right = 0
    running_sum = 0
    running_left = 0

    table_header = "i A[i] max_s run_s max_L max_R".split()
    printrow(*table_header, w=9)
    for i in range(len(A)):
        running_sum += A[i]

        if running_sum > max_sum:
            max_left = running_left
            max_sum = running_sum
            max_right = i

        elif running_sum < 0:
            running_sum = 0
            running_left = i + 1
        printrow(i, A[i], max_sum, running_sum, max_left, max_right, w=9)

    return (max_left, max_right, max_sum)
