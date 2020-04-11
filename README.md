# HowTo Develop

## To run unit and blackbox tests

Prerequisites: 
 - python3 and 
 - tox, 
 
For running unittests and blackbox tests, run the command `tox`, sample output below:

    $ tox
    unittest run-test-pre: PYTHONHASHSEED='3621537090'
    unittest run-test: commands[0] | python -m unittest discover -s tests
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    blackbox installed: robotframework==3.1.2
    blackbox run-test-pre: PYTHONHASHSEED='3621537090'
    blackbox run-test: commands[0] | robot blackbox.robot
    ==============================================================================
    Blackbox                                                                      
    ==============================================================================
    Hello World                                                           | PASS |
    ------------------------------------------------------------------------------
    Blackbox                                                              | PASS |
    1 critical test, 1 passed, 0 failed
    1 test total, 1 passed, 0 failed
    ==============================================================================
    Output:  /Users/prezi/pet/pythontrial/output.xml
    Log:     /Users/prezi/pet/pythontrial/log.html
    Report:  /Users/prezi/pet/pythontrial/report.html
    _____________________________________ summary ______________________________________
      unittest: commands succeeded
      blackbox: commands succeeded
      congratulations :)

## To experiment in jupyter

To play around and prototype just run the jupyter environment, with the command `tox -e jupyter`

    $ tox -e jupyter

This will install jupyter labs and start it, open the web editor in your default browser.