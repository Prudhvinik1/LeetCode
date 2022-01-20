# Recursion
```
def helper(self,s,wordDict,i):
#Base Condition
if(i == len(s)):
return True
#Decision
for j in wordDict:
if j == s[i:i+len(j)]:
return self.helper(s,wordDict,i+len(j))
return False
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
return self.helper(s,wordDict,0)
​
```