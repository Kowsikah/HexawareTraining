Database Design:
Database: OnlineCourseEnrollement
Entities/Tables:
   students
   courses
   enrollments
   modules
   progress

Relationship:
 Many-to-Many Relationship for student and courses(One students can pursue many courses and many students can do same courses)
 One-to-Many - One course can contain many modules

Attributes:
1)Students:
    student_id,student_name,blood_group,phone,student_status(indicates whether a student drop out or not)
2)Courses:
    course_id,course_name
3)Enrollments:
    enrollment_id,student_id,course_id
4)Modules:
   module_id,module_name,course_id,modules_videocontent,module_ppt,module_quiz
5)Progress:
  progress_id,enrollment_id,modules_id,video_completed,ppt_completed,quiz_completed


Report Analysis:
Popular course:
DataScience with Python
Completion_rate:
student_id 1: In Datascience completed 70%
              In web development 26%