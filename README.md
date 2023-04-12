# Health Record Management System -API
This API is built using the Python programming language and FastAPI framework. It provides a simple and easy-to-use interface for managing patient data, including information about patients, doctors, hospitals, and medical histories. The API allows any frontend user to connect easily and retrieve, create, update, or delete patient data using standard HTTP methods.

# Flow for the API -  
- entities in the database, and what endpoints i will need to expose for each of them?

1) Doctor
2) Hospital
3) History
4) Patient
5) In_patient
6) Out_patient
7) Clinic

Q) To expose these entities through a REST API, we  would need to define endpoints for each Entity.

# Doctor

GET /doctors - Returns a list of all doctors
GET /doctors/{doctor_id} - Returns the details of a specific doctor
POST /doctors - Creates a new doctor
PUT /doctors/{doctor_id} - Updates the details of a specific doctor
DELETE /doctors/{doctor_id} - Deletes a specific doctor

# Hospital

GET /hospitals - Returns a list of all hospitals
GET /hospitals/{hosp_id} - Returns the details of a specific hospital
POST /hospitals - Creates a new hospital
PUT /hospitals/{hosp_id} - Updates the details of a specific hospital
DELETE /hospitals/{hosp_id} - Deletes a specific hospital

# History

GET /histories - Returns a list of all medical histories
GET /histories/{hist_id} - Returns the details of a specific medical history
POST /histories - Creates a new medical history
PUT /histories/{hist_id} - Updates the details of a specific medical history
DELETE /histories/{hist_id} - Deletes a specific medical history

# Patient

GET /patients - Returns a list of all patients
GET /patients/{patient_id} - Returns the details of a specific patient
POST /patients - Creates a new patient
PUT /patients/{patient_id} - Updates the details of a specific patient
DELETE /patients/{patient_id} - Deletes a specific patient

# In_patient

GET /in_patients - Returns a list of all in-patients
GET /in_patients/{in_patient_id} - Returns the details of a specific in-patient
POST /in_patients - Creates a new in-patient record
PUT /in_patients/{in_patient_id} - Updates the details of a specific in-patient
DELETE /in_patients/{in_patient_id} - Deletes a specific in-patient

# Out_patient

GET /out_patients - Returns a list of all out-patients
GET /out_patients/{out_patient_id} - Returns the details of a specific out-patient
POST /out_patients - Creates a new out-patient record
PUT /out_patients/{out_patient_id} - Updates the details of a specific out-patient
DELETE /out_patients/{out_patient_id} - Deletes a specific out-patient

# Clinic

GET /clinics - Returns a list of all clinics
GET /clinics/{clinic_id} - Returns the details of a specific clinic
POST /clinics - Creates a new clinic
PUT /clinics/{clinic_id} - Updates the details of a specific clinic
DELETE /clinics/{clinic_id} - Deletes a specific clinic

Q2) HTTP methods will I need to use for each endpoint (GET, POST, PUT, DELETE)?

1) /doctors
GET: Retrieve a list of all doctors
POST: Create a new doctor

2) /doctors/{id}
GET: Retrieve a single doctor by ID
PUT: Update an existing doctor by ID
DELETE: Delete a doctor by ID

3) /hospitals
GET: Retrieve a list of all hospitals
POST: Create a new hospital

4) /hospitals/{id}
GET: Retrieve a single hospital by ID
PUT: Update an existing hospital by ID
DELETE: Delete a hospital by ID

5) /patients
GET: Retrieve a list of all patients
POST: Create a new patient

6) /patients/{id}
GET: Retrieve a single patient by ID
PUT: Update an existing patient by ID
DELETE: Delete a patient by ID

7) /inpatients
GET: Retrieve a list of all inpatients
POST: Create a new inpatient

8) /inpatients/{id}
GET: Retrieve a single inpatient by ID
PUT: Update an existing inpatient by ID
DELETE: Delete an inpatient by ID

9) /outpatients
GET: Retrieve a list of all outpatients
POST: Create a new outpatient

10) /outpatients/{id}
GET: Retrieve a single outpatient by ID
PUT: Update an existing outpatient by ID
DELETE: Delete an outpatient by ID

11) /clinics
GET: Retrieve a list of all clinics
POST: Create a new clinic

12) /clinics/{id}
GET: Retrieve a single clinic by ID
PUT: Update an existing clinic by ID
DELETE: Delete a clinic by ID

13) /histories
GET: Retrieve a list of all histories
POST: Create a new history

14) /histories/{id}
GET: Retrieve a single history by ID
PUT: Update an existing history by ID
DELETE: Delete a history by ID

3Q) How will I handle authentication and authorization to ensure that only authorized clients can access the data?
To handle authentication and authorization in your REST API, you can implement an authentication and authorization mechanism such as OAuth 2.0, JWT, or basic authentication.

4Q) what error codes and messages will you return to the client ?

HTTP status codes that you can return to the client for different types of errors:

200 OK: The request was successful.
201 Created: The resource was successfully created.
204 No Content: The request was successful, but there is no response body.
400 Bad Request: The client sent an invalid request.
401 Unauthorized: The client is not authenticated and needs to provide valid credentials.
403 Forbidden: The client is authenticated, but does not have the necessary permissions to access the resource.
404 Not Found: The requested resource was not found.
500 Internal Server Error: An error occurred on the server that prevented the request from being fulfilled.

When an error occurs, you can include a descriptive error message in the response body to provide more information to the client. For example, if the client sends an invalid request, you can include an error message like "Invalid request parameters" or "Missing required parameter". If a server error occurs, you can include an error message like "Internal server error occurred" or "Unexpected error occurred".

#(Steps For Installation) 

1) Here are the steps to use the FastAPI-based REST API code in Visual Studio Code:

2) Open Visual Studio Code and create a new folder for your project.

3) Open the terminal in Visual Studio Code by selecting "Terminal" from the main menu and then clicking "New Terminal".

4) In the terminal, navigate to the project folder using the cd command.

5) Create a new virtual environment for the project by running the following command:

    python -m venv venv

6) Activate the virtual environment by running the following command:
         
    .\venv\Scripts\activate

7) Install the necessary dependencies by running the following command:

   pip install fastapi uvicorn[standard] pydantic

8) Create a new Python file named main.py in the project folder.

9) Copy the FastAPI-based REST API code into the main.py file.

10) Save the main.py file.

11) In the terminal, start the server by running the following command:
    
     uvicorn main:app --reload

12) You can now test the API by opening a web browser and navigating to 
     http://localhost:8000/docs to view the Swagger documentation, 
  or http://localhost:8000/redoc to view the ReDoc documentation.



// Now For Connecting Own Data base //  


- To connect your own database to the API you have created, you will need to modify the database settings in your main.py file.

- First, import the database client you will be using. For example, if you are using SQLAlchemy with SQLite:

  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker

- Define the database URL, which is a string that specifies the location of your database. The format of the URL will depend on the database you are using. For example, if you are using SQLite:

 DATABASE_URL = "sqlite:///./my_database.db"
- This URL assumes that your database file is located in the same directory as your main.py file.

- Create the database engine using the create_engine function, passing in the DATABASE_URL :

  engine = create_engine(DATABASE_URL)

- Create a sessionmaker, which is a factory function that creates new database sessions. You will use this sessionmaker to create a new session each time you need to interact with the database:

 SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

- Update your API endpoints to use the database session. For example, if you have an endpoint that retrieves all patients, you would use the session to query the database:

  from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(models.Patient).all()
    return patients


* In this example, the get_db function is a dependency that creates a new database session and closes it when the endpoint is finished. The db parameter is the session, which is passed to the get_patients endpoint using the Depends function.* 

- Note that you will also need to create your database schema in your database. You can do this using the create_all method of the Base class in your models.py file:

from .database import Base, engine
Base.metadata.create_all(bind=engine)
