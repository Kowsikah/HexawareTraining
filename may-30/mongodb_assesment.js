
db.restaurants.insertMany([
{
restaurant_id: 1, name: "Spice Hub", city: "Hyderabad", cuisine: "Indian", rating: 4.5,
avg_order_value: 450,
delivery_available: true,
tags: ["biryani", "north indian", "family"], contact: {
phone: "9876543210",
email: "spicehub@mail.com"
}
},
{
restaurant_id: 2,
name: "Pizza Corner", city: "Bangalore",
 
cuisine: "Italian", rating: 4.2,
avg_order_value: 600,
delivery_available: true,
tags: ["pizza", "fast food", "cheese"], contact: {
phone: "9876543211",
email: "pizza@mail.com"
}
},
{
restaurant_id: 3,
name: "Green Bowl", city: "Chennai",
cuisine: "Healthy", rating: 4.7,
avg_order_value: 350,
delivery_available: false,
tags: ["salad", "vegan", "healthy"], contact: {
phone: null,
email: "greenbowl@mail.com"
}
},
{
restaurant_id: 4,
name: "Burger Street", city: "Hyderabad",
cuisine: "Fast Food", rating: 3.9,
avg_order_value: 300,
delivery_available: true,
tags: ["burger", "fries", "fast food"], contact: {
phone: "9876543213",
email: null
}
},
{
restaurant_id: 5,
name: "Royal Tandoor", city: "Delhi",
cuisine: "Indian", rating: 4.8,
 
avg_order_value: 800,
delivery_available: true,
tags: ["tandoor", "north indian", "premium"], contact: {
phone: "9876543214",
email: "royal@mail.com"
}
},
{
restaurant_id: 6, name: "Tea Tales", city: "Pune",
cuisine: "Cafe", rating: 4.1,
avg_order_value: 200,
delivery_available: false,
tags: ["tea", "snacks", "cafe"], contact: {
phone: "9876543215",
email: "tea@mail.com"
}
},
{
restaurant_id: 7,
name: "Ocean Grill", city: "Mumbai",
cuisine: "Seafood", rating: 4.6,
avg_order_value: 900,
delivery_available: true,
tags: ["fish", "grill", "premium"], contact: {
phone: "9876543216",
email: "ocean@mail.com"
}
},
{
restaurant_id: 8,
name: "Dosa Point", city: "Chennai",
cuisine: "South Indian", rating: 4.3,
avg_order_value: 250,
delivery_available: true,
 
tags: ["dosa", "idli", "breakfast"], contact: {
phone: null, email: null
}
}
])

/*Exercise 1-Display all menu*/
db.restaurants.find()

/*Exercise 2-Display name,city,cuisine*/
db.restaurants.find({},{name:1,city:1,cuisine:1,_id:0})

/*Exercise 3- restaurants in Hyderabad*/
db.restaurants.find({city:'Hyderabad'})

/*Exercise 4- Restarunt with indian cuisine*/
db.restaurants.find({cuisine:'Indian'})
/*Exercise 5-delivery is available*/
db.restaurants.find({delivery_available:true})
/*Exercise 6- rating greater than 4.5*/
db.restaurants.find({rating:{$gt:4.5}})
/*Exercise 7-average order value is less than ₹400*/
db.restaurants.find({avg_order_value:{$lt:400}})
/*Exercise 8-rating is between 4.0 and 4.7*/
db.restaurants.find({rating:{$gt:4.0,$lt:4.7}})
/*Exercise 9- average order value is greater than or equal to ₹600*/
db.restaurants.find({avg_order_value:{gte:400}})
/*Exercise 10-restaurants from Hyderabad with delivery available.*/
db.restaurants.find({$or:[{city:'Hyderabad'},{delivery_available:true}]})
/*Exercise 11- restaurants that are either from Chennai or cuisine is Indian*/
db.restaurants.find({$or:[{city:'Chennai'},{cuisine:'Indian'}]})
/*Exercuse 12- restaurants where delivery is not available*/
db.restaurants.find({delivery_available:{ne:true}})
/*Exercise 13- restaurant from Hyderabad,Mumbai,Delhi*/
db.restaurants.find({ city: { $in: ['Hyderabad', 'Mumbai', 'Delhi'] } })
/*Exercise 14-restaurant with cuisine Indian,Italian,cafe*/
db.restaurants.find({$or:[{cuisine:'Indian'},{cuisine:'Italian'},{cuisine:'Cafe'}]})
/*Exercise 15-restaturant not in Bangalore and Hyderabad*/
db.restaurants.find({city:{$not:{$in:['Hyderabad','Bangalore']}}})
/*Exercise 16-Restaruants start with P*/
db.restaurants.find({name:{$regex: /^P/i}})
/*Exercise 17-Restaurants contain Point*/
db.restaurants.find({name:{$regex: /Point/i}})
/*Exercise 18- Restaurant containg Food*/
db.restaurants.find({cuisine:{$regex: /Food/i}})
/*Exercise 19- Restaturant with contact -phone null*/
db.restaurants.find({"contact.phone": null})
/*Exercise 20-Email null restaurants*/
db.restaurants.find({"contact.email": null})
/*Exercise 21-Either phone or email null*/
db.restaurants.find({$or:[{"contact.phone":null},{"contact.email":null}]})
/*Exercise 22-Tag with both Premium ,FastFood*/
db.restaurants.find({tag:{$all:["Premium","Fast Food"]}})
/*Exercise 23-Tag premium*/
db.restaurants.find({ tags: "premium" })
/*Exercise 24-Tag fast food"
db.restaurants.find({ tags: "fast food" })
/*Exercise 25- Tags that having north indian or premium
db.restaurants.find({ tags: { $in: ["north indian", "premium"] } })
/*Exercise 26- Sort rating desc*/
db.restaurants.find().sort({rating:-1})
/*Exercise 27-Top3*/
db.restaurants.find().limit(3)
/*Exercise 28-sort by avg_order_value*/
db.restaurants.find().sort({avg_order_value:1})
/*Exercise 29-sort by avg_order_value top 2
db.restaurants.find().sort({avg_order_value:-1}).limit(2)
/*Exercise 30- Update Burger Street*/
db.restaurants.updateOne({name:"Burger Street"},{$set:{rating:4.0}})
/*Exercise 31- Update delivery availability*/
db.restaurants.updateOne({name:"Tea Tales"},{$set:{delivery_availabilty:true}})
/*Exercise 32-Add new field active*/
db.restaurants.updateMany({}, { $set: { active: true } })
/*Exercise 33- add to array tags*/
db.restaurants.updateOne( { restaurant_id: 1 }, { $addToSet: { tags: "popular" } })
/*Exercise 34 - delete a fielt in all */
db.restaurants.updateMany({}, { $unset: { active: "" } })
/*Exercise 35 - delete a document 6*/
db.restaurants.deleteOne({restaurant_id:6})
/*Exercise 36- delete document with rating<4.0*/
db.restaurants.deleteMany({ rating: { $lt: 4.0 } })
/*Exercise 37- Total documents*/
db.restaurants.countDocuments()
/*Exercise 38- count with delivery*/
db.restaurants.countDocuments({delivery_available:true})
/*Exercise 39- distinct city*/
db.restaurants.distinct("city")
/*Exercise 40- distinct cuisine*/
db.restaurants.distinct("cuisine")
/*Exercise 41 - Count restaurnts by cuisine*/
db.restaurants.aggregate([{ $group: {_id: "$cuisine",totalrestaurants: { $sum: 1 }}}])
/*Exercise 42- Average rating for each cuisine*/
db.restaurants.aggregate([{ $group: { _id: "$cuisine", averagerating: { $avg: "$rating" } }}])
/* Exercise 43*/
db.restaurants.aggregate([{$group: { _id: "$city", avg_order_value: { $avg: "$avg_order_value" } } }])
/*Exercise 44*/
db.restaurants.aggregate([{ $group: { _id: "$cuisine",highest_avg_order_value: { $max: "$avg_order_value" }}  }])
/*Exercise 45*/
db.restaurants.aggregate([{ $group: {  _id: "$cuisine", total_restaurants: { $sum: 1 }}},{ $match: {  total_restaurants: { $gt: 1 }}  }])