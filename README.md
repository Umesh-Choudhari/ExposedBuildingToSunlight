# Building Exposure Calculator

## Overview

The Building Exposure Calculator is a Python script designed to calculate the length of exposed walls of buildings relative to a specified source point. It utilizes geometric calculations to determine the lengths of walls that are visible from the source point.

## Functionality

The script provides the following functionalities:

- Calculating the maximum point of a building.
- Determining whether a building is on the left or right side of a given source point.
- Calculating the length of exposed walls on the left and right sides of the source point.
- Handling cases where buildings intersect or coincide with the source point.
- Providing functions to calculate distances between points and find intersections between lines.

## Usage

To use the Building Exposure Calculator, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the provided Python script to your local environment.
3. Modify the `Buildings` variable to represent the buildings you want to analyze. Each building should be defined as a list of vertices, where each vertex is represented as `[x, y]` coordinates.
4. Set the `source` variable to represent the source point from which you want to calculate the exposure.
5. Run the script.

## Example

Here's an example of using the Building Exposure Calculator:

```python
Buildings = [[[4,0],[4,-5],[7,-5],[7,0]]]
source = [1,1]
sum = calculateLengthOfExposedWall(Buildings, source)
print("Length of exposed for %s is :- %s" % (Buildings, sum))
```

This example calculates the length of exposed walls for a single building relative to the source point `[1, 1]`.

## Dependencies

The script requires the `math` module for mathematical calculations.

## Contributors

- [Ramesh Choudhari] - [https://github.com/Umesh-Choudhari]

---

You can fill in the placeholders with your information and upload the README.md file to your project repository. Adjustments can be made based on your preferences and additional details you may want to include.
