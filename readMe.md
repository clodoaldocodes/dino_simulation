# Python Implementation of the Browser Dinosaur Game

This project was developed exclusively for the purpose of exploring the application of the pygame library in creating simulations and implementing models based on reinforcement learning.

The implementation adopts a learning approach based on genetic evolution, and the configuration files meticulously describe each of the architectures employed. While the source files are provided for reference, it's essential to note that minimal alterations were made, primarily adjusting the number of outputs and hidden layers to shape the dinosaurs' behavior.

To run this implementation, you'll need the neat and pygame libraries, both of which contribute to a lightweight and comprehensible codebase. Key features, such as the dinosaurs' hitboxes and distances, are conveniently displayed in the corner of the screen to facilitate a comprehensive understanding of the simulation.

These codes draw inspiration from a series of instructional videos on YouTube, culminating in the final video showcasing some of my specific enhancements. It's worth mentioning that the code in these videos is presented with simplifications for clarity.

# Potential Future Enhancements:

* Expand the neural network's complexity by increasing the number of layers used.
* Consider adopting a more sophisticated cost function, as the current implementation relies on a straightforward distance-based metric.
* Visualize the neural network's behavior using the pygame library. This visual representation could serve as a valuable educational tool, offering insights into how artificial intelligence layers are activated.
* By pursuing these suggestions, we aim to deepen the educational value and performance capabilities of this browser dinosaur game implementation.

# Code to install the libraries 
```
python3 -m pip install -U pygame --user
python3 -m pip install -U neat-python==0.92 --user
```

# References to read if you would like

[^1] [Evolving Neural Networks through
Augmenting Topologies - Paper](https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)


[^2] [NEAT-Python’s documentation](https://neat-python.readthedocs.io/en/latest/)