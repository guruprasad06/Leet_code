class Solution {

    public void dfs(char[][]grid,int i,int j){

        if(i<0 || i>=grid.length||j<0||j>=grid[0].length||grid[i][j]=='0')
        return;
        grid[i][j]='0';

        dfs(grid,i+1,j);
         dfs(grid,i-1,j);
          dfs(grid,i,j+1);
           dfs(grid,i,j-1);


    }
    public int numIslands(char[][] grid) {

        int count=0,i,j;
        for(i=0;i<grid.length;i++){

            for(j=0;j<grid[0].length;j++){

                if(grid[i][j]=='1'){dfs(grid,i,j);
                count++;
}
                
            }
        }   
        return count;    
    }
     
}