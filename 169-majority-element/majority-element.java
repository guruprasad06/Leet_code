class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();//hash map create

        int n=nums.length;

        for(int i=0;i<n;i++){              // add the key value pair accordingly

            if(map.containsKey(nums[i])){    // TRUE
                map.put(nums[i],map.get(nums[i])+1); 
 
            }else{                    // FALSE
                map.put(nums[i],1);
            }

        }

        for(int key:map.keySet()){

            if(map.get(key)>n/2){
                return key;
            }
        }
       return -1;
    }
}