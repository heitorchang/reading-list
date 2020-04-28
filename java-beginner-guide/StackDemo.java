class StackDemo {
    public static void main(String[] args) {
        Stack s = new Stack(10);
        s.push('c');
        s.push('a');
        s.push('t');
        s.show();
        System.out.println(s.pop());
        s.show();

        s.push('r');
        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println(s.pop());
        s.show();
    }
}
