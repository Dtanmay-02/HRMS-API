CREATE DATABASE if not exists HealthRecord;
CREATE TABLE if not exists Doctor(
    Doctor_Id varchar(20) PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Profession varchar(100) NOT NULL,
    Ratings varchar(20) NOT NULL,
    Contact_Information bigint(10) NOT NULL,
    Clinic_ID int(20),
    Hosp_ID int(20)
);
CREATE TABLE if not exists Hospital(
    Hosp_ID int(20) PRIMARY KEY,
    Hosp_name varchar(100) NOT NULL, 
    Specialisation varchar(100) NOT NULL,
    Hosp_address varchar(100) NOT NULL, 
    Contact bigint(10) unique NOT NULL,
    Availability time NOT NULL,
    Close_day varchar(20) NOT NULL,
    Patient_Id varchar(20),
    Doctor_Id varchar(20)
);

CREATE TABLE if not exists History(
    Hist_Id varchar(5) PRIMARY KEY,
    Recent_surgery_Name varchar(100) NOT NULL,
    Recent_surgery_date date NOT NULL,
    Recent_surgery_detail varchar(1000) NOT NULL,
    past_surgery_Name varchar (100) NOT NULL,
    past_surgery_date date NOT NULL,
    past_surgery_details varchar(1000) NOT NULL,
    On_going_treatment varchar(700)
);

CREATE TABLE if not exists Patient (
    Patient_Id varchar(20) PRIMARY KEY,
    Name varchar(100) NOT NULL,      
    Date_of_birth date NOT NULL,
    Gender varchar(20) NOT NULL,
    Contact_Information bigint(10) NOT NULL,
    Emergency_contact bigint(10) NOT NULL,
    Death_date date,
    Hist_ID varchar(5)
);

CREATE TABLE if not exists In_patient(
    In_patient_Id int(20) PRIMARY KEY AUTO_INCREMENT,
    Name varchar(100) NOT NULL,
    Patient_Id varchar(20) NOT NULL,
    Hist_Id varchar(5) NOT NULL,
    In_Date date NOT NULL
);

CREATE TABLE if not exists Out_patient(
    Out_patient_Id int(20) PRIMARY KEY AUTO_INCREMENT,
    Name varchar(100) NOT NULL,
    Patient_Id varchar(20) NOT NULL,
    Hist_Id varchar(5) NOT NULL,
    Out_Date date NOT NULL
);

CREATE TABLE if not exists Clinic(
    Clinic_ID int(20) PRIMARY KEY,
    Clinic_name varchar(100) NOT NULL, 
    Specialisation varchar(100) NOT NULL,
    Clinic_address varchar(100) NOT NULL, 
    Contact bigint(10) unique NOT NULL,
    Availability time NOT NULL,
    Close_day varchar(20) NOT NULL
);

Alter table Doctor add Foreign key (Hosp_ID) references Hospital(Hosp_ID);
Alter table Doctor add FOREIGN KEY (Clinic_ID) REFERENCES Clinic(Clinic_ID);
Alter table Hospital add FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_Id);
Alter table Hospital add FOREIGN KEY (Doctor_Id) REFERENCES Doctor(Doctor_Id);
Alter table Patient add FOREIGN KEY (Hist_ID) REFERENCES History(Hist_Id);
Alter table In_Patient add FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_Id);
Alter table In_Patient add FOREIGN KEY (Hist_Id) REFERENCES History(Hist_Id);
Alter table Out_Patient add FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_Id);
Alter table Out_Patient add  FOREIGN KEY (Hist_Id) REFERENCES History(Hist_Id);


