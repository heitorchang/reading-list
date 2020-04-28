class Unreachable {
    // unreachable code is an error

    public static void main(String[] args) {
        if (1 == 2) {
            System.out.println("one is two");
        }
        try {
            System.out.println("in try block");
        } catch (Exception e) {
            System.out.println("catch any exception");
// exception already caught            
//        } catch (ArrayIndexOutOfBoundsException ai) { 
//            System.out.println("array index error");
        }
    }
}
