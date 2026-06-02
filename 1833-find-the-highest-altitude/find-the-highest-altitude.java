class Solution {
    public int largestAltitude(int[] gain) {
        int max=0;
        int currentSum=0;
        for(int i=0;i<gain.length;i++){

            currentSum+=gain[i];
            max=Math.max(max,currentSum);
        }
        return max;
    }
}