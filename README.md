## End to End AI Project Pipeline

### Step 1: Create a new environment

```
conda create -p venv python==3.10

conda activate venv/
```
### Step 2: Create a .gitignore file
create the file by right click and include the venv in it


### Step 3: Create a requirements.txt file 
```
pip install -r requirements.txt
```

### Step 4: Create a setup.py file 
This is to install the entire project as a package. Additionally, write a function to read the packages from requirements.txt
```
python setup.py install
```
check if modules are imported if not then rerun step 3 and 4 and restart your IDE

### Step5: Create a folder `src` 
Include exception, logger, and utils python files. Make this folder as a package by including __init__.py file. The scr folder will include another folder with name components will be created. Include __init__.py also 

### Step 6 Create a folder `components`
Include data_ingestion, data_transformation, model trainer, and __init_.py. These components are to be interconnected in future. 

### Step 7 Create a folder called `pipeline`
Create two python files training_pipeline and prediction_pipeline with __init__.py folder


### Step 8: Import data from sql
Write a function to import sql data in utils.py

### Step 9: Complete your pipeline code
write all the nessesary code for the pipleine

### Step 10: runn app.py file and open browser to see the site
```
python app.py

http://127.0.0.1:5000/
```
### Step 11: Deploy in cloud
For vercel deployment make `vercel.json` and `package.json` file
For debugging open up log   