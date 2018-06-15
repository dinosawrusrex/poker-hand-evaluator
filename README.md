# Poker Hand Evaluator

## Intro
As part of a technical interview-ish day-in-the-office, I was asked to
build an evaluator that compares two poker hands. It was an interesting problem
to try solving. My first attempt involved quite a messy code with some bugs,
scenarios that were not accounted for, and intermingling definitions and
function calls.

As it is now, I have done some re-work to try mending the problems. I used
classes to try and handle the cards, hands, and game-running better.
Furthermore, the use of classes does seem to relate better to how we generally
understand and deal with card and hand informations. It also had an added
benefit of separating definitions and function calls. And of course, the
classes helped organise the methods (I'm not sure if the term 'encapsulation'
is the right term or if the way I called on the methods reflects this term).

I also dealt with a scenario that was previously unaccounted for, that is given
two hands are indentical and the highest matching cards are also identical. My
initial code would not handle this correctly. Now it does, but I have more work
to make it more readable. I certainly hope this would be the last scenario left
unaccounted for, but I would not be surprised if there were more.

## Files
### JSON
I decided to organise my cards in JSON format. I was familiar with it.
Currently, I have two different JSON files: `card_template` and `hands`.

`hands` was the first file I used and it still is used when
`evaluate_poker_hand.py` is called.

`card_template` was created when I recently worked on creating a random hands
generator. It is used when `random_hand_generator.py` is called, and note,
`random_hand_generator.py` will change the content of `card_template`.
`card_template` is also used in `main.py` but `main.py` will not update
`card_template`.

### Python
`main` is essentially a function call that draws from `random_hand_generator`
and `evaluate_poker_hand`. It gets a set of hands and then evaluates both of
them. So every instance `main` is run, different hands will be produced and
of course, different results will be produced through `evaluate_poker_hand`.

`random_hand_generator` generates a set of hands. It reads in the
`card_template.json` as a template to create a new JSON file/data for a new
instance of a game. Currently, it does not take into account whether a card has
been drawn or not. So imagine that this is running with an access to infinite
decks.

`evaluate_poker_hand` evaluates the hands given a JSON file/data.

`poker_hand_testing` is a set of tests using unittest. I created it on the
day-in-the-office to test whether my code was correctly attributing the right
poker hand given a set of hands. I am yet to update this test.

## To-Do
- Update and add tests to incorporate more scenarios.
- Refine the evaluator, especially how it stores the order of cards for when
  there are equal hands.
- Include in generator so that you cannot draw a card that has already been
  drawn.
