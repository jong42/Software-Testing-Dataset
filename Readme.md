
# Test Ranking

## Introduction

This is a prototype to use supervised learning for test prioritization.
In regression testing, running all tests can be very expensive, and so selecting relevant tests and running the tests first that are most likely to fail in the least amount of time is desirable to spot errors early.

The method that is implemented here is taken from Bertolino et al 2020 (). 

## Usage

## Method

The method that is implemented here is taken from Bertolino et al 2020 (). The goal is to select test cases that are affected by a given change and to rank them according to their probability of failure and their runtime, so that tests that are likely to fail can be run first, and of those, the tests than run fast can be run first.

At first a dependency graph of the codebase is created that can be queried for which files of the codebase are affected by a change in a given file. If a change is made, only the regression tests for those affected files have to be carried out, since all the other files are not affected by the change. For the affected tests, a SVM is then trained to predict wether a test will fail and how long the runtime ist. The tests are then ranked according to the SVM predictions. (What are the festures taht the SVM uses to predict?)

## Results

## Next steps

<<<<<<< HEAD
Necessary:
- Update dependency graph whenever a change is made
- How much better is this really than just using the metrics?
- Use more metrics as suggested by the authors of the paper
- Add test history to training data
=======
Update dependency graph whenever a change is made
>>>>>>> cd91a2daf507c678b6d92c9618cc8b398b335148

