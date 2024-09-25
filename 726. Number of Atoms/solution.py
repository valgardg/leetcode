import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []

        ss = '' #substring
        nn = '' #number
        passes = 0

        for i in range(len(formula)):
            if passes > 0:
                passes -= 1
            else:
                char = formula[i]
                if char == ')':
                    while stack and stack[-1] != '(':
                        ss += stack.pop()
                    stack.pop()
                    di = i + 1 # digit index
                    while di < len(formula) and formula[di].isdigit():
                        nn += formula[di]
                        di += 1

                    # print(ss)
                    # print(nn)
                    # print(f'multiple: {int(nn[::-1])}, substring: {ss[::-1]}')
                    if nn != '':
                        # for char in (int(nn) * ss[::-1]):
                        stack.extend(list((int(nn) * ss[::-1])))
                        passes += len(nn)
                        ss = ''
                        nn = ''
                    else:
                        for char in ss[::-1]:
                            stack.append(char)
                        ss = ''
                        nn = ''
                else:
                    stack.append(char)
            # print(f'{stack}, i: {i}')

        # print(stack)
        # print(len(stack))

        hm = {}
        atom = ''
        spasses = 0

        for i in range(len(stack)):
            if spasses > 0:
                spasses -= 1
            char = stack[i]
            if not char.isdigit():
                atom += char
            # case where next value is a new atom
            if i < len(stack)-1 and stack[i+1].isupper():
                if atom != '':
                    if atom in hm:
                        if atom == 'F':
                            # print(f'added to atom X: ({atom})')
                            print(f'i: {i}')
                        hm[atom] += 1
                    else:
                        # print(f'new atom X: ({atom})')
                        hm[atom] = 1
                    atom = ''
                    spasses += 1
            # case where next value is a number
            if i < len(stack)-1 and stack[i+1].isdigit() and stack[i+1]:
                nv = '' # number value
                ni = i+1 # number index
                
                while ni < len(stack) and stack[ni].isdigit() and stack[ni]:
                    nv += stack[ni]
                    ni += 1

                finalValue = int(nv)

                if atom != '':
                    if atom in hm:
                        hm[atom] += finalValue
                        # print(f'added to atom X: ({atom})')
                    else:
                        hm[atom] = finalValue
                        # print(f'new atom Y: ({atom})')
                    atom = ''
                    spasses += len(nv)
                    nv = ''
        if atom != '':
            if atom in hm:
                # print(f'adding to atom {atom}')
                hm[atom] += 1
            else:
                hm[atom] = 1
        
        # print(hm)

        orderedhm = collections.OrderedDict(sorted(hm.items()))

        # print(orderedhm)

        finalString = ''

        for key, value in orderedhm.items():
            # print(key, value)
            finalString += key
            if value > 1:
                finalString += str(value)

        return finalString

# print(Solution().countOfAtoms("G(H2O)2"))
# print(Solution().countOfAtoms("Mg(OH)2"))
# print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
# print(Solution().countOfAtoms("Be32"))
# print(Solution().countOfAtoms("H50"))
# print(Solution().countOfAtoms("(B2O39He17BeBe49)39"))
print(Solution().countOfAtoms("Mg(H2O)N"))
# print(Solution().countOfAtoms("Mg((H2O)2Na)4(F)(H2SO4)N"))
print(Solution().countOfAtoms("Mg(OH)234"))