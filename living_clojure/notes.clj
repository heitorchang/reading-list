Clojure types

integer         2
decimal/float   1.5
ratio           1/3
string          "abc"
char            \t, \tab
keyword         :jam
boolean         true, false
nil             nil Note: (= nil '()) is false

Collections

immutable: the value of the collection does not change. Altering one creates
  a new version of the structure
  
persistent: a collection will do smart creations of a new version of itself
  by using structural sharing

commas in collections are optional. They should only be used in maps

lists           '(1 2 "jam" :marmalade)  like a linked list
  first rest (cons elem my-list) count
  last is not recommended because the whole list needs to be traversed

vectors         [:jar 1 2 3 :pot]  collects data by index
  first rest last (nth my-vector index) count
  
maps            {:jam1 "strawberry" :jam2 "blackberry"}
  (get map key [default value]) (:key map) keys vals
  (assoc map :key value) (dissoc map :key) (merge map1 map2 map3 ...)
  
sets            #{:red :blue :pink}
  clojure.set/ union difference intersection
  (set another-collection)
  get contains?
  (:key set)
  conj disj
  

(conj coll x) adds x in the collection's most natural way (for lists, it's the beginning, and for vectors, the end)

(def symbol value) creates a global var

let binds symbols to values only inside a let

(let [developer "Alice"
      rabbit "white"]
  (str developer " met the " rabbit " rabbit"))

To create a function, use defn. It creates a var for functions

(defn fn-name [param1 param2 ...] body)
(fn [param1 param2 ...] body) creates an anonymous function

#(...) is a shorthand for an anonymous function. If there is only one parameter, use %. For more, use %1, %2, etc.

(#(+ %1 %2) 1 20)  ; => 21

(ns namespace) creates a namespace and switches to it

(ns alice.favfoods)  ; evaluate in REPL

alice.favfoods/fav-food is the fully qualified name of the var

(require 'lib-namespace) enables access to vars in that namespace via the fully qualified namespace

(require [alice.favfoods :as af]) creates an alias

ns and require can be combined
(ns wonderland
  (:require [alice.favfoods :as af]))

Adding :refer :all to require loads all the symbols into the current namespace. Using aliases is more common

(class x) tells you the class (type) of x

(true? x) (false? x) (nil? x) (not x)

nil and false are the only logically false values

(complement fn) returns a function that gives the opposite truth value

(= a b c ...) checks if values are equal (like Java's equals method)
(identical? a b) checks object identity

(= '(1 2) [1 2]) ; => true, a special case

(not= a b c ...)

(empty? coll)

(seq coll) turns coll into a sequence (a walkable list abstraction)

use (seq coll) to check if coll is not empty

(every? predicate coll) a predicate is a test that returns true or false
(not-any? predicate coll)

(some predicate coll) will return the first logiacl true value or nil otherwise

(#{1 2 3 4 5} 3) ; => 3
(some #{4 5} [1 2 3 4 5]) ; => 4

(some #{nil} [nil nil]) ; => nil
(some #{false} [false false]) ; => nil

Conditional control structures

(if predicate if-true if-false)
(if-let [need-to-grow-small (> 5 1)]
  (str "drink bottle: " need-to-grow-small)
  "don't drink it") ; => "drink bottle: true"

(when predicate eval-something)  ; returns nil if predicate is false
(when-let [need-to-grow-small true]
  "drink bottle")

(cond pairs-of-expressions)

(let [bottle "drinkme"]
  (cond
    (= bottle "poison") "do not drink"
    (= bottle "drinkme") "grow smaller"
    (= bottle "empty") "all gone")) ; => "grow smaller"

Once a condition matches, the others are not tested

:else may be the last condition, otherwise nil is returned

(case bottle
  "poison" "do not drink"
  "drinkme" "grow smaller"
  ...)

is a shortcut when there is only one test value that can be compared with =

an optional last expression is the default case. otherwise an exception is thrown

(let [fruit "b"]
  (case fruit
    "a" "apple"
    "b" "banana"
    "c" "cherry"
    "no fruit found")) ; => banana

(partial fn arg) is a way of currying (generating a new function with an argument partially applied)

(comp fn1 fn2 ...) composes the functions going from right to left

destructuring is assigning named bindings to elements in things such as collections

(let [[color size] ["blue" "small"]]
  (str "the " color " window is " size))

(let [[color [size]] ["blue" ["very small"]]]
  (str "the " color " window is " size))

:as ORIGINAL at the end allows us to keep the whole initial data structure as ORIGINAL

(let [[color [size] :as original] ["blue" ["small"]]] ...)

(let [{flower1 :flower1 flower2 :flower2}
      {:flower1 "red" :flower2 "blue"}]
  (str "The first flower was " flower1 " and the other one " flower2))

{flower2 :flower2 :or {flower2 "missing"}}

(let [{:keys [flower1 flower2]}
      {:flower1 "red" :flower2 "blue"}]
  ...)

(defn flower-colors [{:keys [flower1 flower2]}]
  (str "the flowers are " flower1 " and " flower2))

(flower-colors {:flower1 "rose" :flower2 "tulip"})

Laziness allows you to deal with infinite lists

(take 5 (range)) ; => (0 1 2 3 4)

(repeat 3 "ha")

(repeatedly 12 #(rand-int 10))  ; random ints from 0 to 9 inclusive, repeatedly will re-evaluate the rand-int function

(take 9 (cycle ["a" "b" "c" "d" "e"]))

A recursive function might also be written with loop

(def alice-adjs ["normal" "too small" "too big" "swimming"])

(defn alice-is-recursive [in out]
  (if (empty? in)
    out
    (alice-is-recursive
     (rest in)
     (conj out (str "Alice is " (first in))))))

(alice-is-recursive alice-adjs [])

(defn alice-is-loop [input]
  (loop [in input
         out []]
    (if (empty? in)
      out
      (recur (rest in)
             (conj out (str "Alice is " (first in)))))))

(alice-is-loop alice-adjs)

loop and recur does not consume the call stack

recur may appear alone in a function

(defn countdown [n]
  (if (= n 0)
    n
    (recur (- n 1))))

(countdown 100)

(def animals ["cat" "dog" "mouse"])
(map fn coll) returns a lazy sequence

(doall (map #(println %) animals)) will force evaluation

(map) may take a function of several arguments and the same number of collections. it stops when the shortest collection ends

(reduce + [1 2 3]) ; => 6

(reduce (fn [r x] (if (nil? x) r (conj r x)))
        []
        [:mouse nil :duck nil nil :cat]) ; => [:mouse :duck :cat]

You cannot reduce an infinite sequence

(filter predicate-to-keep coll)

(remove predicate coll)

