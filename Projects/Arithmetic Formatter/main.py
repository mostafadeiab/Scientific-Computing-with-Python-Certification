def arithmetic_arranger(problems, show_answers=False):
    
    if (len(problems) > 5):  return "Error: Too many problems."

    op1 = []
    op2 = []
    ops = []
    res = []
    arr = []

    for prob in problems:
        part = prob.split()

        if not (part[0].isdigit() and part[2].isdigit()): return "Error: Numbers must only contain digits."
        if len(part[0]) > 4 or len(part[2]) > 4: return "Error: Numbers cannot be more than four digits."
        if part[1] not in ['+', '-']: return "Error: Operator must be '+' or '-'."

        op1.append(part[0])
        ops.append(part[1])
        op2.append(part[2])

        if part[1] == '+': res.append(str(int(part[0]) + int(part[2])))
        else: res.append(str(int(part[0]) - int(part[2])))

    line1 = ""
    line2 = ""
    dash = ""
    ans = ""

    for i in range(len(problems)):

        width = max(len(op1[i]),len(op2[i])) + 2

        line1 += op1[i].rjust(width)
        line2 += ops[i] + op2[i].rjust(width - 1)
        dash += '-' * width
        ans += res[i].rjust(width)

        if i < len(problems) - 1: 
            line1 += "    "
            line2 += "    "
            dash += "    "
            ans += "    "

    if show_answers: return line1 + "\n" + line2 + "\n" + dash + "\n" + ans
    else: return line1 + "\n" + line2 + "\n" + dash

result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])

print(result)