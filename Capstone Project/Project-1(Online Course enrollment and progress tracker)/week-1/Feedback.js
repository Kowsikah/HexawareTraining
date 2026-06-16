db.students.insertMany([{"student_id":101,
"student_name":"Ravi",
"city":"Chennai"},
{
  "student_id":102,
   "student_name":"Vijaya",
   "city":"Hyderabad"
},
{
  "student_id":103,
  "student_name":"Arina",
  "city":"Bangalore"
}
]);

db.courses.insertMany([{
   "course_id":201,
   "course_name":"Data science with Python"
},
{
  "course_id":202,
  "course_name":"Web development"
}]);

db.feedback.insertMany([{
  "feedback_id":301,
  "student_id":101,
  "course_id":201,
  "Feedback":"course is more informative with interactive content"
},
{
  "feeback_id":302,
  "student_id":102,
  "course_id":201,
  "Feedback":"Good"
},
{
  "feedback_id":303,
  "student_id":101,
  "course_id":202,
  "Feedback":"More Practical"
}]);

db.feedback.createIndex({"student_id":1});
db.feedback.createIndex({"course_id":1});

db.feedback.find({"student_id":101});
db.feedback.find({"course_id":201});