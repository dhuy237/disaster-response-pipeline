# Disaster Response Pipeline Project

This repository is the work for my second project from the Udacity Data Scientist Nanodegree Program. In this project, I applied data engineering skills to build an ETL pipeline to process the raw data then the data will go through an ML pipeline to classify data.

## :rocket: Table of contents

1. [Prerequisites](#prerequisites)
2. [Project Motivation](#structure)
3. [Instructions](#instructions)
4. [Acknowledgements](#acknowledgements)

### Prerequisites <a name="prerequisites"></a>

These are libraries that is used in this project:

- pandas
- numpy
- sklearn

### Project Structure <a name="structure"></a>

```bash
.
├── README.md
├── app
│   ├── run.py # Flask file that runs app
│   └── template
│       ├── go.html # Classification result page of web app
│       └── master.html # Main page of web app
├── data
│   ├── DisasterResponse.db # Database to save clean data
│   ├── disaster_categories.csv # Input data to process
│   ├── disaster_messages.csv # Input data to process
│   └── process_data.py # ETL pipeline
└── models
    └── train_classifier.py # ML pipeline
    └── classifier.pkl # Saved model. Please run the ML pipeline to create this file.
```

### Instructions <a name="instructions"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database

        ```bash
        python data/process_data.py \
            data/disaster_messages.csv \
            data/disaster_categories.csv \
            data/DisasterResponse.db
        ```

    - To run ML pipeline that trains classifier and saves the model as pickle file

        ```bash
        python models/train_classifier.py \
            data/DisasterResponse.db \
            models/classifier.pkl
        ```

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Go to `http://0.0.0.0:3000/` to access the website.

### Acknowledgements <a name="acknowledgements"></a>

This project use disaster data from [Appen](https://appen.com/) (formally Figure 8).

The code is inspired by Udacity Data Scientist Nanodegree Program.

## :hammer: Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/Feature`).
3. Commit your Changes (`git commit -m 'Add some feature'`).
4. Push to the Branch (`git push origin feature/Feature`).
5. Open a Pull Request.

## :mailbox: Contact

- Huy Tran ([dhuy237](https://github.com/dhuy237)) - d.huy723@gmail.com
