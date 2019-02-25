Commands
========

The Makefile contains the central entry points for common tasks related to this project.
This commands can be ran instead of using notebooks. 

Model scripts
^^^^^^^^^^^^^^^^^^

* `make data` will use src.data.make_dataset module to load raw data and create stratified splits. 
* `make train` will use src.models.train_model to train on processed data and save serialized model. 
* `make predict` will use src.models.train_model to train on processed data and save serialized model. 
* `make estimate` will use src.models.train_model to train on processed data and save serialized model. 
