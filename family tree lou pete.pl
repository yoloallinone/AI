man(lou).
man(pete).
man(ian).
man(peter).
woman(pauline).
woman(cathy).
woman(lucy).
parent(ian, lucy).
parent(ian, peter).
parent(cathy, ian).
parent(pete, ian).
parent(lou, pete).
parent(lou, pauline).
mother(X,Y) :- woman(X), parent(X,Y).
father(X,Y) :- man(X), parent(X,Y).
sibling(X,Y) :- parent(Z,X), parent(Z,Y).
brother(X,Y) :- man(X), sibling(X,Y).
sister(X,Y) :- woman(X), sibling(X,Y).
grandfather(X,Y) :- father(X,Z), parent(Z,Y).
grandmother(X,Y) :- mother(X,Z), parent(Z,Y).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
