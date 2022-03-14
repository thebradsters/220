def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    class_acc = 0
    student_acc = 0
    for line in in_file.readlines():
        lines_split = line.split(':')
        names = lines_split[0]
        num_split = lines_split[1].split()
        w = num_split[0::2]
        v = num_split[1::2]
        acc = 0
        my_sum = 0
        for i in range(len(w)):
            equation = int(w[i]) * int(v[i])
            acc = acc + equation
            my_sum = my_sum + int(w[i])
        division = acc / 100

        if my_sum == 100:
            class_acc = class_acc + division
            student_acc = student_acc + 1
            print("{}'s average: {}".format(names, division), file=out_file)
        elif my_sum > 100:
            print("{}'s average: Error: The weights are more than 100".format(names), file=out_file)
        else:
            print("{}'s average: Error: The weights are less than 100".format(names), file=out_file)
    total = class_acc / student_acc
    print("Class average: {}".format(total), file=out_file)

    in_file.close()
    out_file.close()

if __name__ == '__main__':
    weighted_average('grades.txt', 'avg.txt')
