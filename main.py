from builtins import print

import pip_test
import library_install
import library_add

pip_test.pip_test()
library_install.library_install()

test_sentence = input("do you want add a library to this project ?")

if test_sentence == "yes":
    library_add.library_add()

print("the program is done")