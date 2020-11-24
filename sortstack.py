def sortstack(stack):
    aux = []
    while len(stack) > 0:
        if len(aux) == 0 or stack[-1] <= aux[-1]:
            aux.append(stack.pop())
        elif stack[-1] > aux[-1]:
            store = stack.pop()
            while len(aux)>0 and store > aux[-1]:
                stack.append(aux.pop())
            aux.append(store)
    return aux
