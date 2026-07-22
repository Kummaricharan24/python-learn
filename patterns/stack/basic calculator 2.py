class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        s = s + "+"  # sentinel to flush the last number

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == " ":
                continue
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # truncate toward zero

                sign = ch
                num = 0

        return sum(stack)