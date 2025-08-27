use std::rc::Rc;
use std::sync::{Arc, Mutex};

fn main() {
    let a = 10;
    let b = Box::new(20); // heap
    let c = Rc::new(Box::new(30)); // wrapped in a reference counter
    let d = Arc::new(Mutex::new(40));
    println!("a: {:?}, b: {:?}, c: {:?}, d: {:?}", a, b, c, d);
}
