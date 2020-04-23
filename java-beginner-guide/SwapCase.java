class SwapCase {
    public static void main(String[] args) throws java.io.IOException {
        System.out.println("Enter some words: ");
        char ch;
        do {
            ch = (char) System.in.read();
            if (ch >= 'a' && ch <= 'z') {
                System.out.print((char) (ch - 32));
            } else if (ch >= 'A' && ch <= 'Z') {
                System.out.print((char) (ch + 32));
            } else {
                System.out.print(ch);
            }
        } while (ch != '\n');
    }
}
