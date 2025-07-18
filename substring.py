s = "pwwkew"

max_length = 0
used_chars = set()
left = 0
for right in range(len(s)):
    while s[right] in used_chars:
        used_chars.remove(s[left])
        left = left + 1
    used_chars.add(s[right])
    max_length = max(max_length, right - left + 1)
print(max_length)
