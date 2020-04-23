class ArrayAverage {
    public static void main(String[] args) {
        int[] values = { 1, 2, 3, 3, 9, 2, 3, 4, 10, 9 };
        int sum = 0;
        for (var v : values) {
            sum += v;
        }
        System.out.println((double) sum / values.length);
    }
}
