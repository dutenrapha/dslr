## Documentation for "Datascience X Logistic Regression: Harry Potter and a Data Scientist" (Updated)

### Project Overview

Set in the Harry Potter universe, this project tasks participants with creating a classifier to substitute the Sorting Hat using logistic regression. It's an exercise in data analysis, visualization, and logistic regression in a multi-classification setting.

### Implementation Details

- **Python with Libraries**: NumPy, Matplotlib, and Sklearn.
- **Class**: `logistic_regression` with methods for initialization, data splitting, standardization, model training (gradient descent or stochastic gradient descent), loss calculation, plotting loss, and model parameter handling.

### Makefile for Testing

- **Initialization**: The `init` command must be executed before running tests to set up necessary directories.
- **Test Scripts**: Include data description, histogram, pair plot, scatter plot, logistic regression training, and prediction.
- **Clean-up Command**: Removes all generated files and directories.

### Project Goals

- **Learning Focus**: Practical experience in machine learning, with an emphasis on logistic regression and data visualization.
- **Evaluation**: Classifier performance measured by accuracy, targeting at least 98% precision.

### Educational Value

This project uniquely combines theoretical and practical learning in an engaging context, fostering deep engagement with machine learning concepts. So no PR will be accepted.

### Usage Instructions

#### Setting Up the Environment

1. **Create a Virtual Environment**: To ensure a clean workspace with specific library versions, it is recommended to set up a Python virtual environment. This can be done using the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

#### Running the Project

2. **Initialization**: Before running any tests or scripts, it's crucial to execute the `make init` command. This sets up the necessary directories for the project.

   ```bash
   make init
   ```

3. **Executing Tests**: After initialization, use the provided test commands in the Makefile (e.g., ` make test-1`, `make test-2`, etc.) to run different parts of the project and validate its functionality.
