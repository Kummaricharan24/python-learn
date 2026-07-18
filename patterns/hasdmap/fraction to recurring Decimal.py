class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Add sign
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        n = abs(numerator)
        m = abs(denominator)

        # Integer part
        result.append(str(n // m))
        remainder = n % m

        # No decimal part
        if remainder == 0:
            return "".join(result)

        result.append(".")
        seen = {}  # remainder -> position in result

        while remainder != 0:
            if remainder in seen:
                index = seen[remainder]
                result.insert(index, "(")
                result.append(")")
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // m))
            remainder %= m

        return "".join(result)