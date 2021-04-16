public class MergeSort {
    public static void main(String[] args){
        int[] nums=new int[]{3,2,1,5,6,4};
        mergeSort(nums, 0, nums.length-1);
        System.out.print(nums.toString());
    }

    /**
     * 合并排序，分治和回归
     */
    public static void mergeSort(int[] nums, int left, int right){
        //int left=0,right=nums.length;
        int mid=(left+right)/2;
        if(left<right){
            //分治，按照左边部分和右边部分
            mergeSort(nums, left, mid);
            mergeSort(nums, mid+1, right);
            merge(nums, left, mid, right);
        }
    }
    /***
     * 数组的合并
     * @param nums
     * @param left
     * @param mid
     * @param right
     */
    public static void merge(int[] nums, int left,int mid ,int right){
        int i=left;
        int j=mid+1;
        int t=0;
        int[] temp=new int[right-left+1];
        while(i<=mid&&j<=right){
            if(nums[i]<nums[j]){
                temp[t++]=nums[j++];
            }
            else{
                temp[t++]=nums[i++];
            }
        }
        //合并前半段未合并的序列
        while(i<=mid){
           temp[t++]=nums[i++]; 
        }
        //合并后半段中出现的
        while(j<=right){
            temp[t++]=nums[j++];
        }
        for(int z=0;z<temp.length;z++){
            nums[left++]=temp[z];
        }
    }
}
