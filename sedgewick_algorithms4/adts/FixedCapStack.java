package adts;

public class FixedCapStack<T> {
    private T[] a;
    private int n;

    public FixedCapStack(int cap) {
        a = (T[]) new Object[cap];
    }

    public boolean isEmpty() {
        return n == 0;
    }

    public int size() {
        return n;
    }

    public void push(T item) {
        a[n++] = item;
    }

    public T pop() {
        return a[--n];
    }
}
