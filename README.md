
# PyCharm for Data Science Tasks

A demo project for working on Data Science tasks inside PyCharm IDE

---

### Start

* Configure Python Interpreter
* Install libraries from `requierements.txt`
* Indexing

### Navigation

* Search Everywhere (Double `Shift`)
* Find Action (`Ctrl + Shift + A`)

### Smart Code editing

`s01_code_insight/galaxies.py`

* Errors highlighting
* Code insight: code completion, type inferring, libraries information
* Works for Data Science libraries
* Files saving and Local History

### Code Execution

`s02_run_debug/planets.py`

* Right click -> Run 
* Run configurations
* Right click -> Debug
* Debug widow: Variables, Frames, Watches
* Add breakpoint, Resume, Step Into, Step Over
* Debug Console, Evaluate Expression


## Data Science features

### Data Viewer

`s02_run_debug/galaxies_dataview.py`

* But breakpoint on the line `train_model(features, targets)`
* Run Debugger
* Click "View as DataFrame" or "View as Array" in Variables
* The same in Python Console: 
Right click -> Run File in Python Console

### Scientific Mode

`s03_sci_mode/plotting.py`

Enable Scientific Mode: Find Action (`Ctrl + Shift + A`), type: Scientific Mode

* Editor / Interactive Console / Documentation / SciView
* Execute cells inside Interactive Console
* Inspect scientific arrays (numpy arrays, pandas DataFrames, pandas Series) in Data Viewer
* Inspect plots under 'Plots' tab

### Jupyter Notebooks

`s04_notebooks/notebook_demo.ipynb`

* PyCharm smart code editing inside Jupyter Notebook
* Jupyter execution features inside PyCharm
* Cell execution and local Jupyter Server
* Use Variables View
* Data Viewer for Jupyter variables
* Debug cells

