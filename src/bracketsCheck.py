def bracketsCheck(strs):
    st = []

    def checkBrac(op, cl):
        if op == '[' and cl == ']':
            return True
        if op == '{' and cl == '}':
            return True
        if op == '(' and cl == ')':
            return True
        return False

    for ch in strs:

        if ch == '(' or ch == '[' or ch == '{':
            st.append(ch)
        elif ch == '}' or ch == ']' or ch == ')':
            if checkBrac(st[-1], ch):
                st.pop()
            else:
                return False

    return len(st)==0



if __name__ == '__main__':
    print(bracketsCheck("[{()[]}]{()}"))
