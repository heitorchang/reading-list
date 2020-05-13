class GenDemo {
    public static void main(String[] args) {
        Gen<Integer> iOb = new Gen<>(99);
        Gen<String> sOb = new Gen<>("Hello");

        iOb.showType();
        sOb.showType();

        int v = iOb.getob();
        System.out.println(v);
        System.out.println(sOb.getob());
    }
}

