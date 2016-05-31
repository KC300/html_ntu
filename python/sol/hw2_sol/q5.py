s = input()
s = s.lower()
inv_s = s[: : -1]
rem_head_s = s[1: ]
inv_rem_head_s = rem_head_s[: : -1]
rem_tail_s = s[: len(s) - 1]
inv_rem_tail_s = rem_tail_s[: : -1]
if (s == inv_s):
	print ("yes")
elif (rem_head_s == inv_rem_head_s):
	print ("yes")
elif (rem_tail_s == inv_rem_tail_s):
	print ("yes")
else:
	print ("no")