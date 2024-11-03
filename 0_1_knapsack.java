import java.util.*;
class KnapSack 
{
    static int knapDP(int W,int wt[],int val[],int n)
    {
        int dp[][]=new int[n+1][W+1];
        for(int i=0;i<=n;i++)
        {
            for(int w=0;w<=W;w++)
            {
                if(i==0||w==0)
                  dp[i][w]=0;
                else if(wt[i-1]<=w)
                   dp[i][w]=Math.max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w]);
                else
                   dp[i][w]=dp[i-1][w];
            }
        }
        int maxProfit= dp[n][W];
        
        List<Integer> selected=new ArrayList<>();
        int w=W;
        for(int i=n;i>0;i--)
        {
            if(dp[i][w]!=dp[i-1][w])
            {
                selected.add(i);
                w-=wt[i-1];
            }
        }
        System.out.print("selected items: ");
        for(int i=selected.size()-1;i>=0;i--)
        {
            System.out.print(selected.get(i)+" ");
        }
     return dp[n][W];    
    }

    public static void main(String[] args) {
        int val[]={2,3,4,1};
        int wt[]={3,4,5,6};
        int n = val.length;
        int W=8;
        System.out.println("Max profit (DP): " + knapDP(W, wt, val, n));
    }
}
