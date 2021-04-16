

/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution_zui {
    public static void main(String[] args) {
        longestPalindrome("daomdukomcayjwgmmetypncdeixarhbectjcwftjjtwjrctixtrsehegwlfotpljeeqhntacfihecdjysgfmxxbjfeskvvfqdoedfxriujnoeteleftsjgdsagqvcgcdjbxgmguunhbjxyajutohgbdwqtjghdftpvidkbftqbpeahxbfyamonazvubzirhqseetaneptnpjbtrtitttxsyjckjvwtrmuwgidkofvobrwrffzrpnxbectsydbvswstfiqranjzhsebjnmprjoirqkgttahrivkcjtitdcpohwwerwgrdivqbltfnigavydxpmitttjjzyrmpaptkczzgnsovebvxezkkovgqegctxacvjfqwtiycnhartzczcgosiquhmdbljjzyrnmffcwnkyzytnsvyzayrieqyrfpxintbbiyrawxlguzaisedwabpzvevlejadztuclcpwvonehkhknicdksdcnjfaoeaqhcdkdtywilwewadcnaprcasccdcnvdgjdqirrsqwzhqqorlhbgpelpupdvuynzybcqkffnnpocidkkigimsa");
    }
    /**
     * 时间复杂度：O(n^2),超时
     */
    public static String longestPalindrome1(String s) {
        String str="";
        int current_len=0;
        if(s.length()==1)
        {
            return s;
        }
        
        for(int i=0;i<s.length();i++)
        {
            for(int j=i;j<s.length();j++)
            {
                char[] dst=new char[j-i+1];
                s.getChars(i, j+1, dst, 0);
                if(dst.length>current_len&&isReverseString(String.valueOf(dst)))
                {
                   
                    str=String.valueOf(dst);
                    current_len=dst.length;
                    
                }
            }
        }
        return str;
    }
    // 判断回文字符串
    public static boolean isReverseString(String s)
    {
        int i=0,j=s.length()-1;
        while(i<j)
        {
            if(s.charAt(i)!=s.charAt(j))
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    /**
     * 时间复杂度O(n^2), 动态规划条件：P(i+1,j-1) && S(i)==S(j)
     * @param s
     * @return
     */
    public static String longestPalindrome(String s)
    {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        String ans = "";
        for (int l = 0; l < n; ++l) {
            for (int i = 0; i + l < n; ++i) {
                int j = i + l;
                if (l == 0) {
                    dp[i][j] = true;
                } else if (l == 1) {
                    dp[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    dp[i][j] = (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]);
                }
                if (dp[i][j] && l + 1 > ans.length()) {
                    ans = s.substring(i, i + l + 1);
                }
            }
        }
        return ans;
    }
}
// @lc code=end

