import adts.FixedCapStack;

class TestFixedCapStack {
    public static void main(String[] args) {
        FixedCapStack<Integer> s = new FixedCapStack<>(10);

        s.push(9);
        s.push(2);
        s.push(5);
        
        System.out.println(s.size());
        System.out.println(s.pop());
    }
}
