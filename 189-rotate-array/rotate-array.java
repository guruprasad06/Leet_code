class Solution {


    void  reverse(int arr[],int start,int end){
int left,right,temp;
        left =start;
        right = end;
        while(left < right){
            temp = arr[left];
arr[left] = arr[right];
arr[right] = temp;

  left++;
        right--;
        }
      

        }




    public void rotate(int[] arr, int k) {
        int n=arr.length;
       if(n==0)return;
       k=k % n;

    reverse(arr, 0, n - 1);
    reverse(arr, 0, k - 1);
    reverse(arr, k, n - 1);

    
    
    }
}