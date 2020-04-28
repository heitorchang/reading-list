import java.util.Arrays;
import java.util.Scanner;

class MyBinarySearch {
    static int indexOf(int[] arr, int x) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (x < arr[mid])
                high = mid - 1;
            else if (x > arr[mid])
                low = mid + 1;
            else
                return mid;
        }
        return -1;
    }

    
    public static void main(String[] args) {
        int n = args.length;
        int[] vals = new int[n];
        for (int i = 0; i < n; i++) {
            vals[i] = Integer.parseInt(args[i]);
        }
        Arrays.sort(vals);

        System.out.print("Enter a number to search: ");
        Scanner in = new Scanner(System.in);
        int lookFor = in.nextInt();

        System.out.print("The array is: ");

        for (int elem : vals) {
            System.out.print(elem + " ");
        }
        System.out.println();
        System.out.println("Item at index: " + indexOf(vals, lookFor));
    }
}
