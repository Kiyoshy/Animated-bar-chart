# Animated bar chart data visualization

The code in this repository allows you to visualize data in an animated bar chart, using the sjvisualizer python library.

sjvisualizer is a data visualization and animation library for Python.
Library: https://github.com/SjoerdTilmans/sjvisualizer

Author of the library https://github.com/SjoerdTilmans

## Technical details

* The library only works with .png images.

* The images of the flags are added to the "assets" folder, so that the library can use them automatically.

* With the file "colors.json" you can define the colors used for each country in the graph, in case the file does not exist, the library will assign them.

* Image positions and coordinates should be adapted to the size of the screen.


### Prerequisites

This is the basic information to be able to execute the code.

You first need to have Python 3 and Pip 3 installed in your computer. Check here for the proper instructions and code:
```
https://www.python.org/downloads/

$ sudo apt install python3
$ sudo apt install python3-pip
```

Working on Windows:

* Installing the python library sjvisualizer.
```
pip install sjvisualizer
```

Working on Ubuntu:

* Installing the python library sjvisualizer.
```
$ sudo pip install sjvisualizer
```

* Installing Tkinter.
```
$ sudo apt install python3-tk
```

* Installing ImageTk.
```
$ sudo apt-get install python3-pil python3-pil.imagetk
```

### Files

The code in this repository was written and tested in Python 3.

Files contained:

* The `assets` folder is used by the library to store the images of the country flags.

* The file `avocado.xlsx` inside the `data` folder contains all the data used for the graph.

* The `Avocado.py` file contains the Python code with the comments that will help you modify the graph.

* In the `colors.json` file, you can find the rgb values of the colors used to represent each country.


## Graph

![](Avocado.gif)


## License

sjvisualizer is released under the MIT License - see the [LICENSE](LICENSE) file for details.