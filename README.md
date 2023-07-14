# Data Loading Pipeline 
### Pipeline to load the own backup provided in csv files from s3 to mysql db.

<details>
  <summary>Python Setup</summary>
  <br>

* GIT tasks:
  * Clone repository data_load_pipeline.
  * Before running the project, make sure that your repository is updated and installed with latest code.
  * Clone the repository that you need to work on, for eg: "git clone URL".

* Virtual Environment setup:
  * Create a new python virtual environment to work on project.
  * Prefer conda environment. Install Anaconda on system.
  * In conda environment, install the necessary modules and libraries required to run the python scripts and to develop the codes.

* .env file description:
  * .env file will consist paths for the .csv and parameter files. These paths are actually used in the code.
  * Moreover, .env file also consist database details

</details>

<details>
  <summary>Data Pipeline job run commands</summary>
  <br>

* Run below commands after going into project path.
* Before running commands, start the virtual env, for eg: conda activate env_name

```commandline
python -m src.__main__ developer_details FULL
python -m src.__main__ devops_details FULL
python -m src.__main__ tester_details FULL

python -m src.__main__ developer_details INCREMENTAL
python -m src.__main__ devops_details INCREMENTAL
python -m src.__main__ tester_details INCREMENTAL
```

</details>

<p align="center">
  <i>All the best. Please let us know if any query.</i>
