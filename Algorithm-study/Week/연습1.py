import sys
sys.stdin = open('input.txt','r')

word = input()
word_dict = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}
stack = []
for i in word:
    if i == '(':
        stack.append(i)
    elif i == ')':
        check = 0

        while 1:
            target = stack.pop()
            if target == '(':
                break
            check += target
        stack.append(check)

    elif i in word_dict:
        stack.append(word_dict[i])
    else:
        stack[-1] *= int(i)
print(sum(stack))
