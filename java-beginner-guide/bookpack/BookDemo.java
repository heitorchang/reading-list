package bookpack;

class Book {
    private String title;
    private String author;
    private int pubDate;

    Book(String t, String a, int d) {
        title = t;
        author = a;
        pubDate = d;
    }

    void show() {
        System.out.println(title + "\t" + author + "\t" + pubDate);
    }
}

class BookDemo {
    public static void main(String[] args) {
        Book books[] = new Book[3];

        books[0] = new Book("A new beginning", "Carl Stein", 2019);
        books[1] = new Book("Java for noobs", "Mark Lipschitz", 2001);
        books[2] = new Book("Little classes", "Terry Powers", 2010);

        for (var book : books) {
            book.show();
        }
    }
}

// compile from java-beginner-guide/ directory:
// javac bookpack/BookDemo.java

// run:
// java bookpack.BookDemo
