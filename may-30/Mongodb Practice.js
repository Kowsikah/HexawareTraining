//insert one document
db.customers.insertOne({
  customer_id: 1,
  name: "Rahul Sharma",
  city: "Hyderabad",
  phone: "9876543210",
  membership:"Gold"
})

//insert Many documents
db.customers.insertMany([
  {
    customer_id:2,
    name: "Priya Reddy",
    city: "Bangalore",
    phone: "9876543211",
    membership: "Silver"
  },
  {
    customer_id: 3,
    name: "Amit Kumar",
    city: "Mumbai",
    phone:null,
    membership:"Gold"
  },
  {
    customer_id: 4,
    name:"Sneha Patel",
    city: "Chennai",
    phone:"9876543213",
    membership: "Bronze"
  }])
  
//to display the all documents in collection
db.customers.find()
//to display the customers in Hyderabad city
db.customers.find({city:"Hyderabad"})
//Todisplay customer > id 2
db.customers.find({customer_id:{$gt:2}})
//lte-less than equal
db.customers.find({customer_id:{$lte:3}})
//if city has Hyderabad,Bangalore
db.customers.find({city:{$in:["Hyderabad","Bangalore"]}})
//And logicalopertaion
db.customers.find({city:"Hyderabad",membership:"Gold"})
//OR logical operation
db.customers.find({$or:[{city:"Hyderabad"},{membership:"Silver"}]})
//to display specific fields
db.customers.find({},{name:1,city:1,_id:0})
//to sort in ascend
db.customers.find().sort({customer_id:1})
//to sort in desc
db.customers.find().sort({customer_id:-1})
//to display 3 documents
db.customers.find().limit(3)