class TestResizingStackArray {
    public static void main(String[] args) {
        ResizingArrayStack<Integer> ras = new ResizingArrayStack<>();

        int[] reversed = new int[3];
            
        ras.push(10);
        ras.push(20);
        ras.push(30);

        int index = 0;
        for (var i : ras) {
            System.out.println(i);
            reversed[index] = i;
            index++;
        }

        System.out.println("Iterate again");
        for (var i : ras) {
            System.out.println(i);
        }

        System.out.print("Reversed array: ");
        for (int i = 0; i < 3; i++) {
            System.out.print(reversed[i] + " ");
        }
        
    }
}
