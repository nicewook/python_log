# python_log
example of python logging


## example_main / sub

- three handler with different level
- one stdout, two file save handler
- loggin variables
- logging from another file

## no_propa_main / sub

- sub do not have handler. so just propagate it to root logger

## propa_main / sub

### commentted propagate = False

- default, It's true
- so sub handler works, and then it propagate event to the root logger
- finally, root logger handler works

### uncommentted propagate = False

- set propagate = Flase
- so, only sub logger handler works, and no propagation to the root logger
