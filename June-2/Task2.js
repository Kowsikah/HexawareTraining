db.learners.insertMany([
{
learner_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
experience_years: 2,
goal: "Data Engineer",
phone: "9876543210"
},
{
learner_id: 2,
name: "Priya Reddy",
city: "Bangalore",
experience_years: 4,
goal: "AI Engineer",
phone: "9876543211"
},
{
learner_id: 3,
name: "Amit Kumar",
city: "Mumbai",
experience_years: 1,
goal: "Data Analyst",
phone: null
},
{
learner_id: 4,
name: "Sneha Patel",
city: "Chennai",
experience_years: 6,
goal: "ML Engineer",
phone: "9876543213"
},
{
learner_id: 5,
name: "Farhan Ali",

city: "Delhi",
experience_years: 3,
goal: "Cloud Engineer",
phone: "9876543214"
},
{
learner_id: 6,
name: "Meera Nair",
city: "Pune",
experience_years: 0,
goal: "AI Engineer",
phone: null
}
])


db.instructors.insertMany([
{
instructor_id: 101,
instructor_name: "Abdullah Khan",
expertise: ["AI", "Data Engineering", "Cloud"],
rating: 4.9
},
{
instructor_id: 102,
instructor_name: "Neha Singh",
expertise: ["Power BI", "SQL", "Analytics"],
rating: 4.6
},
{
instructor_id: 103,
instructor_name: "Ravi Kumar",
expertise: ["Python", "Machine Learning"],
rating: 4.7
}
])


db.courses.insertMany([
{
course_id: 201,
course_name: "Data Engineering with Azure",
category: "Data Engineering",
instructor_id: 101,
price: 15000,
level: "Intermediate",
tools: ["SQL", "Python", "Azure Data Factory", "Databricks"]
},
{
course_id: 202,
course_name: "AI Engineer Roadmap",
category: "Artificial Intelligence",
instructor_id: 101,
price: 20000,
level: "Beginner",
tools: ["Python", "OpenAI", "Vector DB", "LangChain"]
},
{
course_id: 203,
course_name: "Power BI for Business",
category: "Analytics",
instructor_id: 102,
price: 8000,
level: "Beginner",
tools: ["Power BI", "Excel", "SQL"]
},
{
course_id: 204,
course_name: "Machine Learning Practical",
category: "Machine Learning",
instructor_id: 103,
price: 12000,
level: "Intermediate",
tools: ["Python", "Scikit-learn", "Pandas"]
},
{
course_id: 205,
course_name: "Cloud AI Engineer",

category: "Cloud",
instructor_id: 101,
price: 18000,
level: "Advanced",
tools: ["Azure", "AWS", "GCP", "AI Services"]
}
])
db.enrollments.insertMany([
{
enrollment_id: 1001,
learner_id: 1,
course_id: 201,
enrollment_date: ISODate("2026-01-10"),
payment: {
amount: 15000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 8,
total_modules: 10,
completion_percent: 80
},
quiz_scores: [75, 82, 88],
status: "Active"
},
{
enrollment_id: 1002,
learner_id: 2,
course_id: 202,
enrollment_date: ISODate("2026-01-15"),
payment: {
amount: 20000,
mode: "Card",
status: "Success"
},
progress: {
completed_modules: 10,

total_modules: 10,
completion_percent: 100
},
quiz_scores: [90, 92, 95],
status: "Completed"
},
{
enrollment_id: 1003,
learner_id: 3,
course_id: 203,
enrollment_date: ISODate("2026-02-01"),
payment: {
amount: 8000,
mode: "Cash",
status: "Pending"
},
progress: {
completed_modules: 3,
total_modules: 8,
completion_percent: 37.5
},
quiz_scores: [60, 65],
status: "Active"
},
{
enrollment_id: 1004,
learner_id: 4,
course_id: 204,
enrollment_date: ISODate("2026-02-10"),
payment: {
amount: 12000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 6,
total_modules: 12,
completion_percent: 50
},
quiz_scores: [78, 80, 85],
status: "Active"
},
{
enrollment_id: 1005,

learner_id: 5,
course_id: 205,
enrollment_date: ISODate("2026-03-05"),
payment: {
amount: 18000,
mode: "Card",
status: "Failed"
},
progress: {
completed_modules: 0,
total_modules: 12,
completion_percent: 0
},
quiz_scores: [],
status: "Payment Failed"
},
{
enrollment_id: 1006,
learner_id: 6,
course_id: 202,
enrollment_date: ISODate("2026-03-12"),
payment: {
amount: 20000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 2,
total_modules: 10,
completion_percent: 20
},
quiz_scores: [55],
status: "Active"
}
])


 
//Display alllearners
db.learners.find()
//Display all courses.
db.courses.find()
//Display learner name, city, and goal only.
db.learners.find({},{name:1,city:1,goal:1,_id:0})
//Find learners from Hyderabad.
db.learners.find({city:'Hyderabad'})
//Find learners whose goal is AI Engineer .
db.learners.find({goal:'AI Engineer'})
//Find courses in the Data Engineering category.
db.courses.find({category:'Data Engineer'})
//Find courses priced above ₹10,000.
db.courses.find({price:{$gt:10000}})
//Find beginner-level courses.
db.courses.find({level:'Beginner'})
//Find enrollments with successful payments.
db.enrollments.find({"payment.status":'Success'})
//Find learners where phone is null.
db.learners.find({phone:null})
//Find learners having experience greater than 2 years.
db.learners.find({experience_years:{$gt:2}})
//Find courses priced between ₹8,000 and ₹18,000.
db.courses.find({price:{$gt:8000,$lt:18000}})
// Find courses where level is either Beginner or Intermediate .
db.courses.find({level:{$in:['Beginner','Intermediate']}})
//Find enrollments where completion percent is greater than or equal to 80.
db.enrollments.find({"progress.completion_percent":{$gte:80}})
//Find enrollments where payment status is not Success .
db.enrollments.find({"payment.status":{$ne:'Success'}})
// Find learners from Hyderabad, Bangalore, or Pune.
db.learners.find({city:{$in:['Hyderabad','Bangalore','Pune']}})
//Find courses not in the Cloud category.
db.courses.find({category:{$ne:'Cloud'}})
//Find instructors having expertise in AI .
db.instructors.find({expertise:'AI'})
// Find instructors having expertise in SQL .
db.instructors.find({expertise:'SQL'})
//Find courses using tool Python .
db.courses.find({tools:'Python'})
//Find courses using tool Databricks .
db.courses.find({tools:'Databricks'})
//Find enrollments where quiz score contains 95 .
db.enrollments.find({quiz_scores:95})
//Find enrollments where any quiz score is greater than 85.
db.enrollements.find({quiz_scores:{$gt:85}})
//Sort courses by price descending.
db.courses.find().sort({price:-1})
// Display top 3 most expensive courses.
db.courses.find().sort({price:-1}).limit(3)
//Sort learners by experience years descending.
db.learners.find().sort({experience_years:-1})
//Display top 2 most experienced learners.
db.learners.find().sort({experience_years:-1}).limit(2)
//Sort instructors by rating descending.
db.instructors.find().sort({rating:-1})
//Update learner 1 city to Secunderabad .
db.learners.updateOne({learner_id:1},{$set:{city:'Secunderabad'}})
//Update course 203 price to 9000 .
db.courses.updateOne({course_id:203},{$set:{price:9000}})
//Update enrollment 1006 completion percent to 30 .
db.enrollements.updateOne({enrollment_id:1006},{$set:{completion_percent:30}})
//Change enrollment 1005 status to Inactive .
db.enrollments.updateOne({enrollment_id:1005},{$set:{status:'Inactive'}})
//Add field active: true to all learners.
db.learners.updateMany({},{$set:{active:true}});
//Remove field active from all learners.
db.learners.updateMany({},{$unset:{active:true}})
//Add tool MongoDB to course 201.
db.courses.updateOne({course_id:201},{$addToSet:{tools:'MongoDB'}})
//Delete enrollments where payment status is Failed .
db.enrollements.deleteOne({"payment.status":'Failed'})
//Delete learners whose experience years is 0.
db.learners.deleteMany({experience_years:0})
//Count total learners.
db.learners.countDocuments()
// Count total courses.
db.courses.countDocuments()
// successful enrollments.
db.enrollments.countDocuments({status:'Success'})
//Display distinct learner cities.
db.learners.distinct("city")
//Display distinct course categories.
db.courses.distinct("category")
//Display distinct payment modes.
db.enrollments.distinct("payment.mode")
//Revenue by payment mode.
db.enrollments.aggregate([
  {
    $group: {
      _id: "$payment.mode",
      totalRevenue: { $sum: "$payment.amount" }
    }
  }
]);
//Revenue by course.
db.enrollments.aggregate([
  {
    $group:{
      _id:'$course_id',
      totalRevenue: {$sum: "$payment.amount"}
    }
  }
]);
// Count learners by goal.
db.learners.aggregate([
  {
    $group:{
      _id:'$goal',
      totallearners: {$sum:1}
    }
  }
])
//Average course price by category.
db.courses.aggregate([
  {
    $group:{
      _id:'$category',
       Averageprice:{$avg:"$price"}
    }
  }
])
//Average completion percentage by course.
db.enrollments.aggregate([
  {
    $group:{
      _id:'$course_id',
      Averagecompletion:{$avg:"$progress.completion_percent"}
    }
  }
  ])
//Count enrollments by status.
db.enrollments.aggregate([
  {
    $group:{
      _id:'$status',
      CountEnrollments:{$sum:1}
    }
  }
])
//Courses having revenue greater than ₹15,000.
db.enrollments.aggregate([
  {
    $group:{
      _id:'$course_id',
      totalRevenue:{$sum:"$payment.amount"}
    }
  },
  {
    $match:{
      totalRevenue:{$gt:15000}
    }
  }
  ]);
//Enrollments with Learner Details
db.enrollments.aggregate([
  {
    $lookup: {
      from: "learners",
      localField: "learner_id",
      foreignField: "learner_id",
      as: "learner_info"
    }
  },
  { $unwind: "$learner_info" },
  {
    $project: {
      _id: 0,
      "Enrollment ID": "$enrollment_id",
      "Learner Name": "$learner_info.name",
      "City": "$learner_info.city",
      "Course ID": "$course_id",
      "Status": "$status"
    }
  }
]);
//52. Enrollments with Course Details
db.enrollments.aggregate([
  {
    $lookup: {
      from: "courses",
      localField: "course_id",
      foreignField: "course_id",
      as: "course_info"
    }
  },
  { $unwind: "$course_info" },
  {
    $project: {
      _id: 0,
      "Enrollment ID": "$enrollment_id",
      "Course Name": "$course_info.name",
      "Category": "$course_info.category",
      "Amount": "$payment.amount",
      "Payment Status": "$payment.status"
    }
  }
]);
//Courses with Instructor Details
db.courses.aggregate([
  {
    $lookup: {
      from: "instructors",
      localField: "instructor_id",
      foreignField: "instructor_id",
      as: "instructor_info"
    }
  },
  { $unwind: "$instructor_info" },
  {
    $project: {
      _id: 0,
      "Course Name": "$name",
      "Category": "$category",
      "Instructor Name": "$instructor_info.name",
      "Instructor Rating": "$instructor_info.rating"
    }
  }
]);
//Full Report
db.enrollments.aggregate([
  {
    $lookup: {
      from: "learners",
      localField: "learner_id",
      foreignField: "learner_id",
      as: "learner_info"
    }
  },
  { $unwind: "$learner_info" },
  {
    $lookup: {
      from: "courses",
      localField: "course_id",
      foreignField: "course_id",
      as: "course_info"
    }
  },
  { $unwind: "$course_info" },
  {
    $lookup: {
      from: "instructors",
      localField: "course_info.instructor_id",
      foreignField: "instructor_id",
      as: "instructor_info"
    }
  },
  { $unwind: "$instructor_info" },
  {
    $project: {
      _id: 0,
      "Enrollment ID": "$enrollment_id",
      "Learner Name": "$learner_info.name",
      "City": "$learner_info.city",
      "Goal": "$learner_info.goal",
      "Course Name": "$course_info.name",
      "Category": "$course_info.category",
      "Instructor Name": "$instructor_info.name",
      "Payment Amount": "$payment.amount",
      "Payment Status": "$payment.status",
      "Completion %": "$progress.completion_percent",
      "Enrollment Status": "$status"
    }
  }
]);