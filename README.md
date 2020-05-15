# BOKEH
# Date: 14-05-2020
# Author: Harsh Goel
Bokeh is a Python Interactive Visualisation library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js and to extend this capability with high performance interactivity over very large or streaming datsets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, anddata applications.
The bokeh library was so named because it allows the users the flexibility to focus on the most important data without losing track of the rich context that allows it to be understood.

There are 3 ways to look at all the data:
-> Perceptual approaches
-> Automated approaches
-> Data transformation pipeline

Bokeh has two primary means of use: on a server and in the browser

Client-based visualizations
Bokeh also creates standalone visualizations viewable in browsers with no use of the Bokeh server. These plots have many interactive tools and features, such as panning, brushing, hover etc.

Server-based apps
The Bokeh server provides an environment where data can be updated and manipulated such that it can then update the visualization and where the user interface and selection process can trigger visual updates.

How does Bokeh work?
Bokeh is designed such that high-level objects that go into your model (like glyphs, axes, plots, etc) are created in Python and then converted to JSON format. BokehJS uses this to create the visualizations which are rendered in Javascript for display by the browser.

Limitations: the display of large quantities of data is limited by the browser and its ability to handle large amounts of data.

#WORKFLOW

1. Import libraries
2. Generate a figure
3. Create a load data and enrichments
4. Generate glyphs
5. Add attributes, annotations, interactions
6. Create outputs

##Note:
Single ? directs you to the Documentation of particular object or function
double ?? gives you the source code

The ColumnDataSource is basically a simpler version of that. It is a collection of arrays of data (columns) that can be referred to by names. The actual internal structure is just that: a dictionary that maps strings to lists/arrays. It is the primary way that data is moved from python, to the BokehJS browser library.

Widget boxes
Widgets are HTML objects like buttons, and dropdown menus. They behave slightly differently to plots and and putting them in a widgetbox is necessary so that they can all work together. In fact, if you try and put a Widget in Row or Column it will be automatically put into a WidgetBox. As a result, it’s a good idea to wrap your own widgets in a WidgetBox using widgetbox() as then you can be sure about how your widgets are getting arranged.

if we plot 2 different plots one after another then last plot overwrites the previous plot.

Bokeh Server attempts to get past that and enable the browser and the data to be synced more effectively:

Event response: respond to User Interface (UI) and tool events generated in the browser with computations or queries using the full power of Python
Server-side updates: automatically push server-side updates to the UI (i.e. widgets or plots in a browser)
Streaming updates use periodic, timeout, and asynchronous callbacks to drive streaming updates
Bokeh Server can be used in several modes:

--local / individual use
--deployable application

####Server Based App
Run the following commands in command line for windows users
1. pip install tornado
2. https://github.com/bokeh/bokeh  clone or download from here
3. cd bokeh-master/examples/app/stocks/
python download_sample_data.py
4. cd ..

bokeh serve--show .  run this command 

