def process(operations):
    buffer = ""
    done = []

    for op in operations:
        if op[0] == '1': # append
            done.append(op)
            buffer += op[1]
            continue
        
        if op[0] == '2': # delete the last k characters
            k = int(op[1])
            done.append([op[0], buffer[len(buffer)-k:]])
            buffer = buffer[0:len(buffer) - k]
            continue

        if op[0] == '3': # print the kth character
            k = int(op[1])
            print(buffer[k-1])
            continue

        if op[0] == '4': # undo
            if len(done) > 0:
                op_to_undo = done.pop()
                if op_to_undo[0] == '1': # undo append
                    buffer = buffer[0:len(buffer) - len(op_to_undo[1])]
                if op_to_undo[0] == '2': # undo delete the last k characters
                    buffer += op_to_undo[1]
            continue

if __name__ == '__main__':
    q = int(input().strip())

    operations = []

    for _ in range(q):
        operations.append(input().rstrip().split())

    process(operations)