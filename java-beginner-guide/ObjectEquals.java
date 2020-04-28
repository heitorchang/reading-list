class Dummy {
    int i;

    Dummy(int init) {
        i = init;
    }
}

class ObjectEquals {
    public static void main(String[] args) {
        Dummy d = new Dummy(2);
        Dummy d2 = new Dummy(2);

        System.out.println(d.equals(d2));
    }
}
