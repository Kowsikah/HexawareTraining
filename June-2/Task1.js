db.customers.insertMany([
{
customer_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
membership: "Gold",
phone: "9876543210"
},
{
customer_id: 2,
name: "Priya Reddy",
city: "Bangalore",
membership: "Silver",
phone: "9876543211"
},
{
customer_id: 3,
name: "Amit Kumar",
city: "Mumbai",
membership: "Gold",
phone: null
},
{
customer_id: 4,
name: "Sneha Patel",
city: "Chennai",
membership: "Bronze",
phone: "9876543213"
},
{
customer_id: 5,
name: "Arjun Verma",
city: "Delhi",
membership: "Silver",
phone: "9876543214"

}
])
db.restaurants.insertMany([
{
restaurant_id: 101,
name: "Spice Hub",
city: "Hyderabad",
cuisine: "Indian",
rating: 4.5
},
{
restaurant_id: 102,
name: "Pizza Corner",
city: "Bangalore",
cuisine: "Italian",
rating: 4.2
},
{
restaurant_id: 103,
name: "Green Bowl",
city: "Chennai",
cuisine: "Healthy",
rating: 4.7
},
{
restaurant_id: 104,
name: "Burger Street",
city: "Mumbai",
cuisine: "Fast Food",
rating: 3.9
},
{
restaurant_id: 105,
name: "Royal Tandoor",
city: "Delhi",
cuisine: "Indian",
rating: 4.8

}
])
db.delivery_partners.insertMany([
{
partner_id: 201,
partner_name: "FastMove Logistics",
city: "Hyderabad",
rating: 4.4
},
{
partner_id: 202,
partner_name: "QuickShip",
city: "Bangalore",
rating: 4.1
},
{
partner_id: 203,
partner_name: "SpeedKart",
city: "Mumbai",
rating: 4.6
},
{
partner_id: 204,
partner_name: "DoorDash India",
city: "Delhi",
rating: 4.0
}
])
db.orders.insertMany([
{
order_id: 1001,

customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Biryani", quantity: 2, price: 250 },
{ item_name: "Kebab", quantity: 1, price: 180 }
],
order_amount: 680,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 35,
order_rating: 5
},
{
order_id: 1002,
customer_id: 2,
restaurant_id: 102,
partner_id: 202,
items: [
{ item_name: "Pizza", quantity: 1, price: 500 },
{ item_name: "Garlic Bread", quantity: 1, price: 150 }
],
order_amount: 650,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 42,
order_rating: 4
},
{
order_id: 1003,
customer_id: 3,
restaurant_id: 104,
partner_id: 203,
items: [
{ item_name: "Burger", quantity: 2, price: 180 },
{ item_name: "Fries", quantity: 1, price: 120 }
],
order_amount: 480,

payment: {
mode: "Cash",
status: "Pending"
},
order_status: "Pending",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1004,
customer_id: 4,
restaurant_id: 103,
partner_id: null,
items: [
{ item_name: "Salad Bowl", quantity: 1, price: 350 }
],
order_amount: 350,
payment: {
mode: "UPI",
status: "Failed"
},
order_status: "Cancelled",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1005,
customer_id: 5,
restaurant_id: 105,
partner_id: 204,
items: [
{ item_name: "Tandoori Chicken", quantity: 1, price: 600 },
{ item_name: "Naan", quantity: 2, price: 60 }
],
order_amount: 720,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 50,
order_rating: 5
},
{

order_id: 1006,
customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Paneer Curry", quantity: 1, price: 300 },
{ item_name: "Roti", quantity: 4, price: 25 }
],
order_amount: 400,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 30,
order_rating: 4
}
])
//displaying all customers
db.customers.find()
//displaying all restaurants
db.restaurants.find()
//customer name, city and membership.
db.customers.find({},{name:1,city:1,membership:1,_id:0})
//customers from Hyderabad.
db.customers.find({city:'Hyderabad'})
//Gold members.
db.customers.find({membership:'Gold'})
//restaurants with rating greater than 4.5.
db.restaurants.find({rating:{$gt:4.5}})
//orders with amount greater than ₹500.
db.orders.find({order_amount:{$gt:500}})
//Find delivered orders.
db.orders.find({order_status:'Delivered'})
//9. Find cancelled orders.
db.orders.find({order_status:'Cancelled'})
//customers where phone is null.
db.customers.find({"phone":null})
//orders where amount is between ₹400 and ₹700.
db.orders.find({
  order_amount:{$gte:400, $lte:700}
  
})
//customers from Hyderabad, Delhi or Mumbai.
db.customers.find({city:{$in:['Hyderabad','Delhi','Mumbai']}})
//restaurants whose cuisine is Indian or Fast Food.
db.restaurants.find({cuisine:{$in:['Indian','Fast Food']}})
//orders where payment status is not Success.
db.orders.find({"payment.status":{$ne:'Success'}})
//orders where delivery time is null.
db.orders.find({delivery_time_minutes:null})
//orders where rating is greater than or equal to 4.
db.orders.find({order_rating:{$gte:4}})
//restaurants not located in Bangalore or Chennai.
db.restaurants.find({ city: { $nin: ['Bangalore', 'Chennai'] } })
//orders containing item Biryani
db.orders.find({"items.item_name":'Biryani'})
//orders containing item Pizza
db.orders.find({"items.item_name":'Pizza'})
//orders where any item quantity is greater than 1.
db.orders.find({"items.quantity":{$gt:1}})
//
db.orders.find({ "items.price": { $gt: 300 } })
//Display only order ID and items.
db.orders.find({},{order_id:1,items:1,_id:0})
//Sort restaurants by rating descending.
db.restaurants.find().sort({rating:-1})
//Display top 3 highest rated restaurants.
db.restaurants.find().sort({rating:-1}).limit(3)
//Sort orders by order amount descending.
db.orders.find().sort({order_amount:-1})
//Display top 2 highest value orders.
db.orders.find().sort({order_amount:-1}).limit(2)
//27. Sort delivery partners by rating descending.
db.delivery_partners.find().sort({rating:-1})
//Update customer 1 membership to Platinum
db.customers.updateOne({customer_id:1},{$set:{membership:'Platinum'}})
//Update restaurant 104 rating to 4.1
db.restaurants.updateOne({restaurant_id:104},{$set:{rating:4.1}})
//Update order 1003 status to Delivered
db.orders.updateOne({order_id:1003},{$set:{"payment.status":'Delivered'}})
//Set delivery time of order 1003 to 45 .
db.orders.updateOne({order_id:1003},{$set:{delivery_time_minutes:45}})
//Add field active: true to all customers.
db.customers.updateMany({},{$set:{active:true}})
//Remove field active
db.customers.updateMany({},{$unset:{active:""}})
//Add a new item to order 1006:
db.orders.updateOne({order_id:1006},{$push:{items:{item_name: "Curd Rice", quantity: 1, price: 120 }}})
//Delete cancelled orders.
db.orders.deleteMany({order_status:'Cancelled'})
//Delete restaurants with rating less than 4.0.
db.restaurants.deleteMany({rating:{$lt:4.0}})
//Count total customers.
db.customers.countDocuments()
//count total order
db.orders.countDocuments()
//Count delivered orders.
db.orders.countDocuments({order_status:'Delivered'})
//Count failed payments.
db.orders.countDocuments({"payment.status":'Failed'})
//Display distinct customer cities.
db.customers.distinct("city")
//Display distinct restaurant cuisines.
db.restaurants.distinct("cuisine")
//Display distinct payment modes.
db.orders.distinct("payment.mode")
//Revenue by Payment Mode
db.orders.aggregate([{
  $group:{
    _id:"$payment.mode",
    totalRevenue:{$sum:"$order_amount"}
  }
}])
//Revenue by Order Status Order Status,Total Revenue
db.orders.aggregate([{
  $group:{
    _id:"$order_status",
    totalRevenue:{$sum:"$order_amount"}
  }
  
}])
//Calculate average delivery time for delivered orders.
db.orders.aggregate([
  { 
    $match: { order_status: 'Delivered' } 
  },
  {
    $group: {
      _id: null,
      averageTime: { $avg: "$delivery_time_minutes" }
    }
  }
])
//Customer ID,Total Orders,Total Amount
db.orders.aggregate([{
  $group:{
    _id:"$customer_id",
    totalorders:{$sum:1},
    totalamount:{$sum:"$order_amount"}
  }
  }])
  //Orders by Restaurant Restaurant ID,Total Orders,Total Revenue
  db.orders.aggregate([{
    $group:{
      _id:"$restaurant_id",
      totalorders:{$sum:1},
      totalamount:{$sum:"$order_amount"}
    }
  }])
  //Average Rating by Restaurant,Restaurant ID,Average Order Rating
  db.orders.aggregate([{
    $group:{
       _id:"$restaurant_id",
       Average_order_rating:{$avg:"$order_rating"}
    }
  }])
//Find customers whose total spending is greater than ₹700.
  db.orders.aggregate([
  {
    $group: {
      _id: "$customer_id", // or "$customer_name" depending on your schema
      totalSpending: { $sum: "$order_amount" }
    }
  },
  {
    $match: {
      totalSpending: { $gt: 700 }
    }
  }
  
])
//51. Orders with Customer Details Display:Order ID,Customer Name,City,Order Amount,Order Status
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",          
      localField: "customer_id",   
      foreignField: "customer_id",         
      as: "customerDetails"       
    }
  },
  {
    $unwind: "$customerDetails"
  },
  {
    $project: {
      _id: 0,                              // Hides the MongoDB Object ID
      "Order ID": "$_id",
      "Customer Name": "$customerDetails.name",
      "City": "$customerDetails.city",
      "Order Amount": "$order_amount",
      "Order Status": "$order_status"
    }
  }
])

/*52. Orders with Restaurant Details*/
db.orders.aggregate([
  {
    $lookup: {
      from: "restaurants",
      localField: "restaurant_id",
      foreignField: "restaurant_id",
      as: "resDetails"
    }
  },
  {
    $unwind: "$resDetails"
  },
  {
    $project: {
      _id: 0,
      "Order ID": "$order_id",
      "Restaurant Name": "$resDetails.name",
      "Cuisine": "$resDetails.cuisine",
      "Order Amount": "$order_amount"
    }
  }
])
db.orders.aggregate([
  {
    $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "partnerDetails"
    }
  },
  {
    
    $unwind: {
      path: "$partnerDetails",
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $project: {
      _id: 0,
      "Order ID": "$order_id",
      "Partner Name": { $ifNull: ["$partnerDetails.partner_name", "Not Assigned"] },
      "Delivery Time": { $ifNull: ["$delivery_time_minutes", "N/A"] },
      "Order Status": "$order_status"
    }
  }
])
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $lookup: {
      from: "restaurants",
      localField: "restaurant_id",
      foreignField: "restaurant_id",
      as: "res"
    }
  },
  { $unwind: "$res" },
  {
    $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "partner"
    }
  },
  {
    $unwind: {
      path: "$partner",
      preserveNullAndEmptyArrays: true
    }
  },
  {
    $project: {
      _id: 0,
      "Order ID": "$order_id",
      "Customer Name": "$cust.name",
      "Restaurant Name": "$res.name",
      "Cuisine": "$res.cuisine",
      "Partner Name": { $ifNull: ["$partner.partner_name", "N/A"] },
      "Order Amount": "$order_amount",
      "Payment Mode": "$payment.mode",
      "Payment Status": "$payment.status",
      "Order Status": "$order_status",
      "Delivery Time": { $ifNull: ["$delivery_time_minutes", "N/A"] },
      "Rating": { $ifNull: ["$order_rating", "No Rating"] }
    }
  }
])