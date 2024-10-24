class Solution:
    def romanToInt(self, s: str) -> int:
        # Peta dari simbol Romawi ke nilai integernya
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterasi melalui setiap karakter dalam string dari akhir ke awal
        for char in reversed(s):
            value = roman_to_int[char]
            
            # Jika nilai saat ini lebih kecil dari nilai sebelumnya, kurangi nilai ini dari total
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total

# Contoh penggunaan
sol = Solution()
print(sol.romanToInt("IIII"))   # Output: 3
print(sol.romanToInt("IV"))     # Output: 4
print(sol.romanToInt("IX"))     # Output: 9
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV"))# Output: 1994
