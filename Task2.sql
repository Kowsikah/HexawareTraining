CREATE TABLE patients
(
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
gender VARCHAR(10),
age INT,
city VARCHAR(50),
phone VARCHAR(15)
);
CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(100)
);
CREATE TABLE doctors
(
doctor_id INT PRIMARY KEY,
doctor_name VARCHAR(100),
specialization VARCHAR(100),
department_id INT references departments(department_id),
consultation_fee DECIMAL(10,2)
);
CREATE TABLE appointments
(
appointment_id INT PRIMARY KEY,
patient_id INT references patients(patient_id),
doctor_id INT references doctors(doctor_id),
appointment_date DATE,
appointment_status VARCHAR(30)
);
CREATE TABLE treatments
(
treatment_id INT PRIMARY KEY,
appointment_id INT references appointments(appointment_id),
treatment_name VARCHAR(100),
treatment_cost DECIMAL(10,2)
);
CREATE TABLE bills
(
bill_id INT PRIMARY KEY,
patient_id INT,
appointment_id INT references bills(appointment_id),
bill_date DATE,
total_amount DECIMAL(10,2),
bill_status varchar(30) 
);
CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
bill_id INT references bills(bill_id),
payment_mode VARCHAR(30),
paid_amount DECIMAL(10,2),
payment_status VARCHAR(30)
);

-- 1. DEPARTMENTS (5 Records)
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Cardiology'),
(2, 'Pediatrics'),
(3, 'Orthopedics'),
(4, 'Dermatology'),
(5, 'Neurology');

-- 2. DOCTORS (8 Records)
INSERT INTO doctors (doctor_id, doctor_name, specialization, department_id, consultation_fee) VALUES
(101, 'Dr. Arvind Sharma', 'Cardiologist', 1, 1500.00),
(102, 'Dr. Priya Nair', 'Pediatrician', 2, 1000.00),
(103, 'Dr. Rajesh Khanna', 'Orthopedic Surgeon', 3, 1200.00),
(104, 'Dr. Sneha Reddy', 'Dermatologist', 4, 800.00),
(105, 'Dr. Vikram Malhotra', 'Neurologist', 5, 2000.00),
(106, 'Dr. Anjali Desai', 'Cardiologist', 1, 1500.00),
(107, 'Dr. Manoj Joshi', 'Pediatrician', 2, 1000.00),
(108, 'Dr. Kiran Patel', 'Orthopedic Surgeon', 3, 1200.00);

-- 3. PATIENTS (12 Records)
INSERT INTO patients (patient_id, patient_name, gender, age, city, phone) VALUES
(1, 'Amit Kumar', 'Male', 45, 'Chennai', '9876543210'),
(2, 'Sunitha Rao', 'Female', 34, 'Bangalore', '9876543211'),
(3, 'Rahul Verma', 'Male', 12, 'Hyderabad', '9876543212'),
(4, 'Pooja Hegde', 'Female', 28, 'Mumbai', '9876543213'),
(5, 'Vijay Krishnan', 'Male', 60, 'Chennai', '9876543214'),
(6, 'Deepika Padukone', 'Female', 38, 'Bangalore', '9876543215'),
(7, 'Arjun Kapoor', 'Male', 8, 'Delhi', '9876543216'),
(8, 'Meera Jasmine', 'Female', 52, 'Kochi', '9876543217'),
(9, 'Siddharth Malhotra', 'Male', 31, 'Mumbai', '9876543218'),
(10, 'Kavitha Selvam', 'Female', 24, 'Chennai', '9876543219'),
(11, 'Rohan Das', 'Male', 67, 'Kolkata', '9876543220'),
(12, 'Aditi Rao', 'Female', 19, 'Hyderabad', '9876543221');

-- 4. APPOINTMENTS (20 Records)
INSERT INTO appointments (appointment_id, patient_id, doctor_id, appointment_date, appointment_status) VALUES
(501, 1, 101, '2026-05-01', 'Completed'),
(502, 2, 103, '2026-05-02', 'Completed'),
(503, 3, 102, '2026-05-02', 'Completed'),
(504, 4, 104, '2026-05-03', 'Completed'),
(505, 5, 105, '2026-05-04', 'Completed'),
(506, 6, 106, '2026-05-05', 'Completed'),
(507, 7, 107, '2026-05-05', 'Completed'),
(508, 8, 108, '2026-05-06', 'Completed'),
(509, 9, 101, '2026-05-07', 'Completed'),
(510, 10, 103, '2026-05-08', 'Completed'),
(511, 11, 105, '2026-05-09', 'Completed'),
(512, 12, 104, '2026-05-10', 'Completed'),
(513, 1, 106, '2026-05-11', 'Completed'),
(514, 2, 108, '2026-05-12', 'Completed'),
(515, 3, 107, '2026-05-12', 'Completed'),
(516, 4, 101, '2026-05-13', 'Scheduled'),
(517, 5, 103, '2026-05-14', 'Scheduled'),
(518, 6, 105, '2026-05-15', 'Cancelled'),
(519, 7, 102, '2026-05-16', 'Scheduled'),
(520, 8, 104, '2026-05-17', 'Scheduled');

-- 5. TREATMENTS (15 Records)
INSERT INTO treatments (treatment_id, appointment_id, treatment_name, treatment_cost) VALUES
(301, 501, 'ECG and Consultation', 1500.00),
(302, 502, 'Physiotherapy Session', 1200.00),
(303, 503, 'General Pediatrics Checkup', 1000.00),
(304, 504, 'Acne Laser Treatment', 3500.00),
(305, 505, 'EEG Test', 4000.00),
(306, 506, 'Echocardiogram', 5000.00),
(307, 507, 'Vaccination Drive', 1500.00),
(308, 508, 'Knee Joint Injection', 6000.00),
(309, 509, 'Cardiac Stress Test', 3000.00),
(310, 510, 'Fracture Plaster Application', 4500.00),
(311, 511, 'MRI Brain Scan', 8000.00),
(312, 512, 'Skin Allergy Patch Test', 2500.00),
(313, 513, 'Heart Rate Monitoring', 1500.00),
(314, 514, 'Spine Adjustment', 3500.00),
(315, 515, 'Nebulization Therapy', 1200.00);

-- 6. BILLS (15 Records)
INSERT INTO bills (bill_id, patient_id, appointment_id, bill_date, total_amount, bill_status) VALUES
(901, 1, 501, '2026-05-01', 1500.00, 'Paid'),
(902, 2, 502, '2026-05-02', 1200.00, 'Paid'),
(903, 3, 503, '2026-05-02', 1000.00, 'Paid'),
(904, 4, 504, '2026-05-03', 3500.00, 'Paid'),
(905, 5, 505, '2026-05-04', 4000.00, 'Paid'),
(906, 6, 506, '2026-05-05', 5000.00, 'Paid'),
(907, 7, 507, '2026-05-05', 1500.00, 'Paid'),
(908, 8, 508, '2026-05-06', 6000.00, 'Paid'),
(909, 9, 509, '2026-05-07', 3000.00, 'Paid'),
(910, 10, 510, '2026-05-08', 4500.00, 'Paid'),
(911, 11, 511, '2026-05-09', 8000.00, 'Paid'),
(912, 12, 512, '2026-05-10', 2500.00, 'Paid'),
(913, 1, 513, '2026-05-11', 1500.00, 'Paid'),
(914, 2, 514, '2026-05-12', 3500.00, 'Unpaid'),
(915, 3, 515, '2026-05-12', 1200.00, 'Unpaid');

-- 7. PAYMENTS (15 Records)
INSERT INTO payments (payment_id, bill_id, payment_mode, paid_amount, payment_status) VALUES
(701, 901, 'Cash', 1500.00, 'Success'),
(702, 902, 'UPI', 1200.00, 'Success'),
(703, 903, 'Credit Card', 1000.00, 'Success'),
(704, 904, 'Debit Card', 3500.00, 'Success'),
(705, 905, 'Net Banking', 4000.00, 'Success'),
(706, 906, 'UPI', 5000.00, 'Success'),
(707, 907, 'Cash', 1500.00, 'Success'),
(708, 908, 'Insurance Claim', 6000.00, 'Success'),
(709, 909, 'UPI', 3000.00, 'Success'),
(710, 910, 'Credit Card', 4500.00, 'Success'),
(711, 911, 'Insurance Claim', 8000.00, 'Success'),
(712, 912, 'Debit Card', 2500.00, 'Success'),
(713, 913, 'Cash', 1500.00, 'Success'),
(714, 914, 'UPI', 0.00, 'Failed'),
(715, 915, 'None', 0.00, 'Pending');

/*Display all patients records*/
select * from patients;
/*display all doctors records*/
select * from doctors;
/*patients from Hyderabad*/
select * from patients where city='Hyderabad';
/*doctor from Cardiology*/
select * from doctors d inner join departments d1 on d.department_id=d1.department_id where department_name='Cardiology';
/*Appointments after 2026-01-01*/
select * from appointments where appointment_date>'2026-01-01';
/*Cancelled*/
select * from appointments where appointment_status='Cancelled';
/*bills where total amount is greater than ₹5,000.*/
select * from bills where total_amount>5000;
/*Payments made through upi*/
select * from payments where payment_mode='UPI';
/*Age between 30 and 50*/
select * from patients where age between 30 and 50;
/*Constultation fee above 800*/
select * from doctors where consultation_fee>800;
/*count patients*/
select count(*) as TotalPatients from patients;
/*count doctors*/
select count(*) as TotalDoctors from doctors;
/*count appointments*/
select count(*) as TotalAppointment from appointments;
/*average consultation fee*/
select avg(consultation_fee) from doctors;
/*Highest treatment_cost*/
select max(treatment_cost) from treatments;
/*Total billing amount*/
select sum(total_amount) from bills;
/*Total paid amount*/
select sum(paid_amount) from payments;
/*count patients by city*/
select distinct city,count(patient_id) from patients group by city;
/*count doctors by specialization*/
select specialization,count(doctor_id) from doctors group by specialization;
/*count appointment by status*/
select appointment_status,count(appointment_id) from appointments group by appointment_status;
/*patient name with appointment date and status.*/
select p.patient_name,a.appointment_date,a.appointment_status from patients p inner join appointments a on p.patient_id=a.patient_id;
/*doctor name with department name.*/
select d.doctor_name,d1.department_name from doctors d inner join departments d1 on d.department_id=d1.department_id;
/*patient name, doctor name, and appointment date.*/
select p.patient_name,d.doctor_name,a.appointment_date from patients p inner join appointments a on p.patient_id=a.patient_id inner join doctors d on d.doctor_id=a.doctor_id;
/*appointment ID with treatment name and cost.*/
select appointment_id,treatment_name,treatment_cost from treatments;
/*bill ID with patient name and total amount.*/
select b.bill_id,p.patient_name,b.total_amount from bills b inner join patients p on p.patient_id=b.patient_id;
/*bill ID with payment mode, paid amount, and payment status.*/
select b.bill_id,p.payment_mode,p.paid_amount,p.payment_status from bills b inner join payments p on p.bill_id=b.bill_id;
/*Patient Name,Doctor Name,Department,Appointment Date,Appointment Status,Treatment Name,Treatment Cost,Bill Amount,Payment Status*/
select p.patient_name,d.doctor_name,d1.department_name,a.appointment_date,a.appointment_status,t.treatment_name,t.treatment_cost,b.total_amount,p1.payment_status from patients p inner join appointments a on p.patient_id=a.patient_id inner join doctors d on d.doctor_id=a.doctor_id inner join departments d1 on d1.department_id=d.department_id inner join treatments t on t.appointment_id=a.appointment_id inner join bills b on b.appointment_id=a.appointment_id inner join payments p1 on b.bill_id=p1.bill_id;
/*Count appointments by doctor.*/
select distinct d.doctor_id,count(a.doctor_id) from doctors d inner join appointments a on d.doctor_id=a.doctor_id group by a.doctor_id;
/*Count appointments by department.*/
select d1.department_name,count(a.appointment_id) from departments d1 inner join doctors d on d1.department_id=d.department_id inner join appointments a on d.doctor_id=a.doctor_id group by d1.department_id;
/*Total revenue by department.*/
SELECT d.department_name,SUM(b.total_amount) AS total_revenue FROM departments d
JOIN  doctors doc ON d.department_id = doc.department_id
JOIN  appointments a ON doc.doctor_id = a.doctor_id
JOIN  bills b ON a.appointment_id = b.appointment_id
WHERE b.bill_status = 'Paid' -- Optional: Include this if you only want realized/paid revenue
GROUP BY d.department_name
ORDER BY total_revenue DESC;
/*total billing by city*/
select p1.city,sum(b.total_amount) from bills b inner join patients p1 on b.patient_id=p1.patient_id group by p1.city;
/*Doctors having more than 2 appointments.*/
select d.doctor_name from doctors d inner join appointments a on d.doctor_id=a.doctor_id group by d.doctor_id having count(a.appointment_id)>2;
/*Departments generating revenue greater than ₹20,000.*/
SELECT d.department_name,SUM(b.total_amount) AS total_revenue FROM departments d
JOIN  doctors doc ON d.department_id = doc.department_id
JOIN  appointments a ON doc.doctor_id = a.doctor_id
JOIN  bills b ON a.appointment_id = b.appointment_id
WHERE b.bill_status = 'Paid' -- Optional: Include this if you only want realized/paid revenue
GROUP BY d.department_name
having total_revenue>20000;
/*cities more than 2 patients*/
select city from patients group by city having count(patient_id)>2;
/*Find patients who have appointments.*/
select patient_name from patients where patient_id in(select patient_id from appointments);
/*patients who never booked appointments.*/
select patient_name from patients where patient_id not in(select patient_id from appointments);
/*doctors who have no appointments.*/
select doctor_name from doctors where doctor_id not in(select doctor_id from appointments);
/*bills greater than average bill amount.*/
select * from bills where total_amount>(select avg(total_amount) from bills);
/*patient with highest bill amount.*/
select * from patients where patient_id in(select patient_id from bills where total_amount=(select max(total_amount) from bills));
/*doctors whose consultation fee is above average.*/
select * from doctors where consultation_fee>(select avg(consultation_fee) from doctors);
/*patients who visited Cardiology.*/
select * from patients where patient_id in(select patient_id from appointments where doctor_id in(select doctor_id from doctors where department_id in (select department_id from departments where department_name="Cardiology")));
/*Unpaid bills */
select * from bills where bill_status="Unpaid";
/*appointments that have treatments.*/
select * from appointments where appointment_id in (select appointment_id from treatments);
/*Find patients whose total bill is above average patient billing.*/
select * from patients where patient_id in(select patient_id from bills where total_amount>(select avg(total_amount) from bills));
/*appointments without treatments*/
select * from appointments where appointment_id not in (select appointment_id from treatments);
/*Find bills without payment.*/
select * from bills left join payments on bills.bill_id=payments.bill_id where payment_id is null;
/*payments with NULL or zero paid amount.*/
select * from payments where paid_amount is null or paid_amount=0;
/*cancelled appointments that still have bills.*/
select * from appointments right join bills on appointments.appointment_id=bills.appointment_id where appointments.appointment_status='Cancelled';
/*paid bills where payment amount is less than bill amount.*/
select * from bills b inner join payments p on p.bill_id=b.bill_id where b.total_amount>p.paid_amount;
/*Find doctors with invalid department ID.*/
select * from doctors where department_id not in(select department_id from departments);
/*Find appointments with invalid patient or doctor IDs.*/
select * from appointments where patient_id not in(select patient_id from patients) and doctor_id not in(select doctor_id from doctors);
/*Final Report*/
select p.patient_name,p.city,count(a.appointment_id),sum(b.total_amount),sum(p1.paid_amount),sum(b.total_amount)-sum(p1.paid_amount) as Pending_amount from patients p inner join appointments a on p.patient_id=a.patient_id inner join bills b on b.appointment_id=a.appointment_id inner join payments p1 on p1.bill_id=b.bill_id group by p.patient_id;