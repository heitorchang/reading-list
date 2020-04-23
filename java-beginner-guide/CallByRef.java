class CallByRef {
    public static void main(String[] args) {
        Double d = Double.valueOf(2.2);
        alter(d);

        System.out.println(d);        
    }

    static void alter(Double val) {
        val = 39.39;
        System.out.println(val);
    }
}
