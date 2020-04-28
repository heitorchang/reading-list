class Test {
    int a;
    Test(int i) {
        a = i;
    }
}


class SwapObjData {
    public static void main(String[] args) {
        Test t1 = new Test(1);
        Test t2 = new Test(2);
        int tmp = t1.a;
        t1.a = t2.a;
        t2.a = tmp;

        System.out.println("Test1: " + t1.a);
        System.out.println("Test2: " + t2.a);
    }
}
