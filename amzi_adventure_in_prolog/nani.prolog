:- dynamic(here/1).

room(kitchen).
room(office).
room(hall).
room('dining room').
room(cellar).

door(office, hall).
door(kitchen, office).
door(hall, 'dining room').
door(kitchen, cellar).
door('dining room', kitchen).

location(desk, office).
location(apple, kitchen).
location(flashlight, desk).
location('washing machine', cellar).
location(nani, 'washing machine').
location(broccoli, kitchen).
location(crackers, kitchen).
location(computer, office).
location(bratwurst, cellar).

edible(apple).
edible(crackers).
edible(bratwurst).

tastes_yucky(broccoli).

here(kitchen).

% rules

where_food(X,Y) :-
    location(X,Y),
    edible(X).
where_food(X,Y) :-
    location(X,Y),
    tastes_yucky(X).

list_food_locs :-
    where_food(X,Y), write(X), write(' in '), write(Y), nl, fail.

connect(X,Y) :- door(X,Y).
connect(X,Y) :- door(Y,X).

list_things(Place):-
    location(X,Place), write(X), nl, fail.
list_things(AnyPlace).

list_connections(Place):-
    connect(Place,Y), write(Y), nl, fail.

look :-
    here(Place),
    write('You are in the '), write(Place), nl,
    write('You can see:'), nl,
    list_things(Place),
    nl,
    write('You can go to:'), nl,
    list_connections(Place).

goto(Place):-
    can_go(Place),
    move(Place),
    look.

can_go(Place):-
    here(X),
    connect(X, Place).
can_go(Place):-
    write('You can''t get there from here.'), nl,
    fail.

move(Place):-
    retract(here(X)),
    asserta(here(Place)).
    
