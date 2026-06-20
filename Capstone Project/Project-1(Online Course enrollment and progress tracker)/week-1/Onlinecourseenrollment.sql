create table students(student_id int PRIMARY KEY,
                      student_name varchar(30),
                      blood_group varchar(10),
                      phone_no varchar(10),
                      city varchar(20),
                      student_status varchar(20)
                      );

          
 create table courses(course_id int PRIMARY KEY,
                      course_name varchar(30)
                    
                      );                    

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE NOT NULL,
    enrollment_status VARCHAR(20) DEFAULT 'Enrolled' 
        CHECK (enrollment_status IN ('Enrolled', 'Completed', 'Dropped')),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE modules (
    module_id INT PRIMARY KEY,
    course_id INT,
    module_name VARCHAR(50) NOT NULL,
    module_videos INT DEFAULT 0,
    module_ppts INT DEFAULT 0,
    module_quizzes INT DEFAULT 0,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) 
);

CREATE TABLE progress (
    progress_id INT PRIMARY KEY,
    enrollment_id INT,
    module_id INT,
    video_completed INT DEFAULT 0,
    ppt_completed INT DEFAULT 0,
    Quiz_completed INT DEFAULT 0,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id),
    FOREIGN KEY (module_id) REFERENCES modules(module_id)
);

insert into students values(1,"Anitha","O+ve","9876435267","Salem","Active"),
(2,"Vinay","9356701234","B+ve","Chennai","Active"),
(3,"Daniel","9768612345","O+ve","Coimbatore","InActive"),
(4,"Rithai","9876543210","A+ve","Coimbatore","Active"),
(5,"Vidhya","9102345678","AB-ve","Chennai","Active"),
(6,"cini","8765432109","B+ve","Chennai","InActive"),
(7,"Vinailakshmi","8765432108","O+ve","Salem","InActive");


INSERT INTO courses (course_id, course_name) VALUES 
(101, 'Data Science with Python'),
(102, 'Web Development Bootcamp'),
(103, 'Introduction to SQL Mastery');


INSERT INTO modules (module_id, course_id, module_name, module_videos, module_ppts, module_quizzes) VALUES
(501, 101, 'Module 1: Python Basics & NumPy', 15, 5, 10),  
(502, 101, 'Module 2: Pandas & Visualization', 10, 5, 10),
(601, 102, 'Module 1: HTML5 & CSS3 Essentials', 12, 4, 5),
(602, 102, 'Module 2: JavaScript & DOM Manipulation', 18, 6, 8),
(603, 102, 'Module 3: Backend Basics with Node.js', 15, 5, 5),
(701, 103, 'Module 1: Basic Queries & Filtering', 8, 3, 4),
(702, 103, 'Module 2: Joins, Aggregates & Subqueries', 12, 4, 6);



INSERT INTO enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
(1001, 1, 101, '2026-01-15'),
(1002, 2, 102, '2026-01-20'), 
(1003, 3, 101, '2026-02-01'), 
(1004, 4, 103, '2026-01-10'), 
(1005, 5, 102,'2026-01-10' ), 
(1006, 6, 101, '2026-02-15'), 
(1007, 7, 103, '2026-01-22');


INSERT INTO progress (progress_id, enrollment_id, module_id, video_completed, ppt_completed, Quiz_completed) VALUES
(2001, 1001, 501, 15, 5, 10), 
(2002, 1001, 502, 4, 2, 1),
(2003, 1002, 501, 5, 1, 2),
(2004, 1003, 501, 15, 5, 10),
(2005, 1003, 502, 3, 1, 2),
(2006, 1004, 601, 12, 4, 5),
(2007, 1005, 601, 0, 0, 0),
(2008, 1005, 602, 0, 0, 0),
(2009, 1005, 603, 0, 0, 0),
(2010, 1006, 701, 8, 3, 4),
(2011, 1007, 701, 5, 3, 3);

/*Displaying all tables*/
select * from students;
select * from courses;
select * from enrollments;

/*Displaying students and their course*/
select s.student_name,c.course_name from students s 
inner join enrollments e on s.student_id=e.student_id
inner join courses c on e.course_id=c.course_id;

/*Displaying courses and their modules*/
select c.course_name,m.module_name from
 courses c inner join modules m 
 on c.course_id=m.course_id;

/*Adding new enrollments*/
insert into enrollments values(1008,5,101,'2026-01-01','Dropped');
insert into progress values(2012,1008,501,10,2,0);


/*Updating progress data*/
update progress set video_completed=6 where progress_id=2002;
DELIMITER //

CREATE PROCEDURE completion_rate_per_module()
BEGIN
    SELECT 
        s.student_name,
        c.course_name,
        m.module_id,
        SUM(p.video_completed) / (SUM(m.module_videos)) * 100 AS videos_completion,
        SUM(p.ppt_completed) / (SUM(m.module_ppts)) * 100 AS ppt_completion,
        SUM(p.Quiz_Completed) / (SUM(m.module_quizzes)) * 100 AS quiz_rate 
    FROM students s 
    INNER JOIN enrollments e ON s.student_id = e.student_id
    INNER JOIN courses c ON c.course_id = e.course_id
    INNER JOIN modules m ON c.course_id = m.course_id
    INNER JOIN progress p ON p.enrollment_id = e.enrollment_id AND p.module_id = m.module_id
    GROUP BY s.student_name, c.course_name, m.module_id;
END //

DELIMITER ;

call completion_rate_per_module;

/*for all*/
DELIMITER //

CREATE PROCEDURE get_student_course_completion()
BEGIN
    SELECT 
        s.student_id,
        s.student_name,
        c.course_name,
        (SUM(p.video_completed) + SUM(p.ppt_completed) + SUM(p.Quiz_completed)) AS total_completed,
        (SUM(m.module_videos) + SUM(m.module_ppts) + SUM(m.module_quizzes)) AS total_required,
        ROUND(
            (SUM(p.video_completed) + SUM(p.ppt_completed) + SUM(p.Quiz_completed)) / 
            NULLIF(SUM(m.module_videos) + SUM(m.module_ppts) + SUM(m.module_quizzes), 0) * 100, 
            2
        ) AS course_completion_percentage

    FROM students s
    INNER JOIN enrollments e ON s.student_id = e.student_id
    INNER JOIN courses c ON c.course_id = e.course_id
    INNER JOIN modules m ON c.course_id = m.course_id
    LEFT JOIN progress p ON e.enrollment_id = p.enrollment_id AND m.module_id = p.module_id
    GROUP BY s.student_id, s.student_name, c.course_id, c.course_name;
END //

DELIMITER ;

call get_student_course_completion();
/* for paricular student*/
DELIMITER //

CREATE PROCEDURE get_student_course_completion_specific(IN input_student_id INT)
BEGIN
    SELECT 
        s.student_id,
        s.student_name,
        c.course_name,
        (SUM(p.video_completed) + SUM(p.ppt_completed) + SUM(p.Quiz_completed)) AS total_completed,
        (SUM(m.module_videos) + SUM(m.module_ppts) + SUM(m.module_quizzes)) AS total_required,
        ROUND(
            (SUM(p.video_completed) + SUM(p.ppt_completed) + SUM(p.Quiz_completed)) / 
            NULLIF(SUM(m.module_videos) + SUM(m.module_ppts) + SUM(m.module_quizzes), 0) * 100, 
            2
        ) AS course_completion_percentage

    FROM students s
    INNER JOIN enrollments e ON s.student_id = e.student_id
    INNER JOIN courses c ON c.course_id = e.course_id
    INNER JOIN modules m ON c.course_id = m.course_id
    LEFT JOIN progress p ON e.enrollment_id = p.enrollment_id AND m.module_id = p.module_id
    
    WHERE s.student_id = input_student_id
    GROUP BY s.student_id, s.student_name, c.course_id, c.course_name;
END //

DELIMITER ;

call get_student_course_completion_specific(1);

/*Popular courses*/
SELECT c.course_name 
FROM courses c
INNER JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
HAVING COUNT(e.enrollment_id) = (
    SELECT COUNT(enrollment_id) 
    FROM enrollments 
    GROUP BY course_id 
    ORDER BY COUNT(enrollment_id) DESC 
    LIMIT 1
);
