# Next-Word-Prediction

This repository contains scripts to create an n-gram model and a Streamlit application to showcase the model's word completion capabilities.

## Files:

- `n-gram.py`: This script is responsible for creating and saving the n-gram model.
- `app.py`: This script runs a Streamlit application where users can test the n-gram model.

## Instructions:

### 1. Creating the N-Gram Model:
- Ensure you have the necessary libraries installed (`nltk`, `sklearn`,etc).
- Adjust the data path in `n-gram.py` to point to your dataset and the output directory.
- Run the `n-gram.py` script to create the n-gram model chunks.
  ```
  python n-gram.py
  ```

### 2. Running the Streamlit App:
- Ensure you have Streamlit installed.
- Adjust the path in `app.py` where the pickled n-gram model is saved.
- Run the Streamlit application using:
  ```
  streamlit run app.py
  ```

**Note**: Ensure that the data paths in both scripts are adjusted to your local setup.
