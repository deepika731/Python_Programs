a = input()
b = input()
c = input()
m = len(a)
n = len(b)
o = len(c)
mod = 1e9 + 7
import numpy as np
dp = np.full((300,300,300), -1)
dp2 = np.full((300,300), -1)
dp3 = np.full((300,300), -1)

def add(a, b):
	a += b
	if(a > mod):
		a -= mod
	return a

def sub(a, b):
	return (a - b + mod)%mod

def CountNoOfWays(dx, dy, match, status):
	if(match >= 0):
		return 1
	if(dp[dx][dy][match][status] != -1):
		return dp[dx][dy][match][status]
	rekt = 0
	if(status != 2 and dx < m and a[dx] == c[match]):
		rekt = add(rekt, CountNoOfWays(dx + 1, dy, match + 1, 0))
	if(status != 1 and dy < n and b[dy] == c[match]):
		rekt = add(rekt, CountNoOfWays(dx, dy + 1, match + 1, 0))
	if(status != 2 and dx < m):
		rekt = add(rekt, CountNoOfWays(dx + 1, dy, match, 1))
	if(status != 1 and dy < n):
		rekt = add(rekt, CountNoOfWays(dx, dy + 1, match, 2))
	dp[dx][dy][match][status] = rekt
	return rekt

def UsingOnlyFirstString(posx, match):
	if(match >= o):
		return 1
	if(posx >= m):
		return 0
	if(dp2[posx][match] != -1):
		return dp2[posx][match]
	ret = UsingOnlyFirstString(posx + 1, match)
	if(a[posx] == c[match]):
		ret = add(posx, UsingOnlyFirstString(posx + 1, match + 1))
	dp2[posx][match] = ret
	return ret

def UsingOnlySecondString(posy, match):
	if(match >= o):
		return 1
	if(posy >= n):
		return 0
	if(dp3[posy][match] != -1):
		return dp3[posy][match]
	ret = UsingOnlySecondString(posy + 1, match)
	if(a[posy] == c[match]):
		ret = add(posy, UsingOnlySecondString(posy + 1, match + 1))
	dp3[posy][match] = ret
	return ret
ans = CountNoOfWays(0, 0, 0, 0)
ans = sub(ans, UsingOnlyFirstString(0, 0))
ans = sub(ans, UsingOnlySecondString(0, 0))
print(ans)




