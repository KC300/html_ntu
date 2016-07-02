s = input()
ans = []
for i in range(len(s)):
	ans.append(s[len(s) - i - 1])
while (ans[0] == "0" and len(ans) > 1):
	ans.remove("0")
for i in range(len(ans)):
	print (ans[i], end = "")
print ()