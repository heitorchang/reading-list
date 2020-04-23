class SortStrings {
    // Bubble sort
    // outer loop defines left boundary
    // inner loop goes from right to left, placing larger items to the right
    
    public static void main(String[] args) {
        String[] values = { "car", "door", "apple", "book", "elephant" };

        int size = values.length;
        
        for (int a = 1; a < size; a++) {
            for (int b = size-1; b >= a; b--) {
                if (values[b-1].compareTo(values[b]) > 0) {
                    String tmp = values[b];
                    values[b] = values[b-1];
                    values[b-1] = tmp;
                }
           }
        }

        for (var s : values) {
            System.out.println(s);
        }            
    }
}
