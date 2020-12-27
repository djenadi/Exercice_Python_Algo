<!-- ABOUT THE PROJECT -->
## About The Project

The largest square:
It's about finding the largest square possible on a board while avoiding obstacles.
- A board is transmitted to you in a file passed as an argument of the program.
- The first line of the board contains the information for reading the map:
- The number of lines on the board;
- The "empty" character;
- The "obstacle" character;
- The "full" character.

The board is made up of 'empty' character and 'obstacle' character lines.
◦ The purpose of the program is to replace the "empty" character "with" full "character to
represent the largest possible square.
◦ If there are several solutions, we will choose to represent the topmost square at
left

### Built With

* [Python3](https://docs.python.org/3/)
  * [Unittest](https://docs.python.org/fr/3/library/unittest.html)
  * [cProfile](https://docs.python.org/3/library/profile.html)
* [BASH](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)


<!-- GETTING STARTED -->
### Prerequisites

-Python 3

### Installation

Clone the repo over SSH :
  ```sh
   git clone git@github.com:djenadi/Exercice_Python_Algo.git
   ```
Or over HTTPS :
  ```sh
   https://github.com/djenadi/Exercice_Python_Algo.git
   ```
<!-- USAGE EXAMPLES -->
## Usage

To run the script : 
  $./find_square example_file

'examle_file' should contains a valid map file : 
  - All lines must be the same length.
  - There is at least one row of at least one box.
  - At the end of each line there is a new line.
  - The characters present in the card must be only those presented on the first line.
  - In the event of an invalid map, you will display the error output: map error followed by a return to the
  - line then it will move on to processing the next tray.

  #### options
 
  1. If you want to have some benchmarking, you can run the script with:
   ```
    $./find_square -p example_file
   ```
  2. If you want to execute unittest, you should execute: 
   ```
    $python -m unittest test_boardhelper.py  
   ```
   


<!-- CONTRIBUTING -->
## Contributing
Feel free to contribute, make sure that you .py file pass the flake8 linter.

<!-- CONTACT -->
## Contact

DJENADI AMIR REDOUANE, amirredouane@ymail.com




