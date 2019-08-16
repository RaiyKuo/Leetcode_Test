# ---------Solution--------------
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1, s2 = len(str1), len(str2)
        D = [['']*s2, [str2[j:] for j in range(s2)]]  # memory reuse，所以只需要兩列的DP；不然會Memory Limit Exceeded
        def dp(i, j, ii):                             # dp查找用函數
            if j >= s2:                               # 若超過邊界，則傳回另一個string剩下部分
                return str1[i:]
            return D[ii % 2][j]                       # 若沒超過則從DP查找 (注意ii % 2為memory re-use)
        ii = 1
        for i in range(s1-1, -1, -1):
            ii = (ii + 1) % 2              # memory re-use:  實際上DP查找只有本列(i)和下一列(i+1)；但因為i有些是string操作
            for j in range(s2-1, -1, -1):  # 故另外弄一個ii。當 (ii+1)%2會循環回來，故可重複使用
                if str1[i] == str2[j]:     # 若此字元相等，則將此字元加入答案，且兩string都往下移
                    D[ii][j] = str1[i] + dp(i+1, j+1, ii+1)
                else:                      # 若字元不相等，看是要哪個string往下移；取結果較短者
                    D[ii][j] = min(str1[i] + dp(i+1, j, ii+1), str2[j] + dp(i, j+1, ii), key=len)
        return D[ii][0]                    # !!!!千萬記得這裡要用ii，因為最後是填入[ii][0]而不一定是[0][0]。這裡debug超久

#----Input---------
#I = ["bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb","dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa"]
#I = ['ab', 'cd']
#I = ["abac", "cab"]# "cabac"
#I = ['aaaaaaaa', 'aaaaaaaaaaaaaaa']
I = ["bbbaaaba", "bbababbb"]  #"bbabaaababb" or "bbababbaaba"
# -----------Testing(Output)--------------
S = Solution()
print(S.shortestCommonSupersequence(I[0], I[1]))