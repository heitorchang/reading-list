class ForDeclaration {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
        System.out.println(i); // outside for, the symbol is not found
    }
}
