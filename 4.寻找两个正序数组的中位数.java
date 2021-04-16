/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class Solution_ {
    // public static void main(String[] args){
    //     int[] nums1=new int[]{1,2};
    //     int[] nums2=new int[]{3,4};
    //     findMedianSortedArrays(nums1, nums2);

    // }
    /***
     * 算法复杂度O(m+n), 空间复杂度O(m+n)
     * @param nums1
     * @param nums2
     * @return
     */
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m=nums1.length;
        int n=nums2.length;
        int[] temp=new int[m+n];
        int j=0;
        int k=0;
        int t=0;
        for(t=0;t<temp.length&&j<nums1.length&&k<nums2.length;t++){
            if(nums1[j]<=nums2[k]){
                temp[t]=nums1[j];
                j++;
            }
            else{
                temp[t]=nums2[k];
                k++;
            }
        }
        for(int i=k;i<nums2.length;i++)
        {
            temp[t]=nums2[i];
            t++;
        }
        for(int i=j;i<nums1.length;i++)
        {
            temp[t]=nums1[i];
            t++;
        }
        if(temp.length%2==0)
        {
            int mid1=temp.length/2;
            int mid2=mid1-1;
            
            return (double)(temp[mid1]+temp[mid2])/2;
        }
        else{
            int mid=temp.length/2;
            return temp[mid];
        }    
    }
    /***
     * 时间复杂度O(m+n),空间复杂度O(1)
     * @param A
     * @param B
     * @return
     */
    public static double findMedianSortedArrays1(int[] A, int[] B)
    {
        int m = A.length;
        int n = B.length;
        int len = m + n;
        int left = -1, right = -1;
        int aStart = 0, bStart = 0;
        for (int i = 0; i <= len / 2; i++) {
            left = right;
            if (aStart < m && (bStart >= n || A[aStart] < B[bStart])) {
                right = A[aStart++];
            } else {
                right = B[bStart++];
            }
        }
        if ((len & 1) == 0)
            return (left + right) / 2.0;
        else
            return right;
    }
}
// @lc code=end

