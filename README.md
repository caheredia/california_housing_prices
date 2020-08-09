California Housing Prices README
==============================
# TODO add section to run notebook
- https://docs.anaconda.com/anaconda/user-guide/tasks/docker/
This projects predicts median house values in Californian districts. The median house prices are derived from the 1990 census.

See report and documentation [here](https://caheredia.github.io/california_housing_prices/build/html/index.html)




Data Publishers
------------
- http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

# Data-Oriented Design

### Proposed Data Pipeline 
compress csv -> csv -> numpy arrays -> ML models -> serialized model  

## On object oriented design
> When a class owns some data, it gives that data a context which can sometimes limit the ability to reuse the data or understand the impact of operations upon it. Adding functions to a context can bring in further data, which quickly leads to classes containing many different pieces of data that are unrelated in themselves, but need to be in the same class because an operation required a context and the context required more data for other reasons such as for other related operations. This sounds awfully familiar, and Joe Armstrong is quoted to have said "I think the lack of reusability comes in object-oriented languages, not functional languages. Because the problem with object-oriented languages is they've got all this implicit environment that they carry around with them. You wanted a banana but what you got was a gorilla holding the banana and the entire jungle." which certainly seems to resonate with the issue of contextual referencing that seems to be plaguing the object-oriented languages. 

## Regarding numpy (raw data) over DataFrames
> Putting data structures inside your object designs might make sense from what they are, but they often make little sense from the perspective of data manipulation.

> We only care about what transforms we do, and where the data ends up. In practice, when you discard meanings from data, you also reduce the chance of tangling the facts with their contexts, and thus you also reduce the likelihood of mixing unrelated data just for the sake of an operation or two. 


# References
[conda env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment)
[Data-oriented Design](https://www.dataorienteddesign.com/dodbook/node2.html#SECTION00220000000000000000)
[ddo in games](http://gamesfromwithin.com/data-oriented-design)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── .ipynb             <- Jupyter notebooks. 
    │                         
    │                         
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.yml   <- The requirements file for reproducing the analysis environment
    │                         
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   ├── train_model.py
        │   ├── cost_estimator.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------
