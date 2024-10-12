public class Main
{
    // Utility function to return the maximum of two integers
    static int max(int a, int b) 
    {
		return (a > b) ? a : b; // Return the larger of a or b
	}
    
    // Recursive function to solve the 0/1 Knapsack problem
	static int knapSack(int W, int wt[], int val[], int n) {
		if (n == 0 || W == 0) {
			// Base case: If no items are left (n == 0) or the knapsack is full (W == 0), return 0
			return 0; 
		}

		// If the weight of the nth item is greater than the remaining capacity W, exclude this item
		if (wt[n - 1] > W) {
			return knapSack(W, wt, val, n - 1);
		}

		// Otherwise, return the maximum of:
		// 1. Value obtained by including the nth item (val[n-1] + remaining knapsack capacity)
		// 2. Value obtained by excluding the nth item
		else {
			return max(
                val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),  // Include the item
                knapSack(W, wt, val, n - 1)                             // Exclude the item
            );
		}
	}

    // Main method to test the knapSack function
	public static void main(String[] args) 
	{
		// Example input: values and weights of the items
		int val[] = new int[] { 60, 100, 120 };  // Values of the items
		int wt[] = new int[] { 10, 20, 30 };    // Weights of the items
		int W = 50;                             // Capacity of the knapsack
		int n = val.length;                     // Number of items

		// Print the result of the knapSack function
		System.out.println(knapSack(W, wt, val, n));
	}
}
