class RecursiveBackwards {
    static void iter(String remainder) {
        int len = remainder.length();
        if (len == 0) {
            return;
        }
        System.out.print(remainder.substring(len-1, len));
        iter(remainder.substring(0, len-1));
    }

    public static void main(String[] args) {
        iter(args[0]);
    }
}
                         
