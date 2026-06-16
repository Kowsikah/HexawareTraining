db.audit_log.insertMany([
  {
    "log_id":9001,
     "product_id":10,
     "warehouse_id":1001,
     "log_details":{
        "reason":"product damage in packing due to water leakage",
        "monitored by":"Inventory Supervisor"
     },
     "quantity-affected":5,
     "date":'2026-06-01'
  },
    {
    "log_id":9002,
     "product_id":30,
     "warehouse_id":1003,
     "log_details":{
        "reason":"damage piece unchecked",
        "monitored by":"Inventory Supervisor"
     },
     "quantity-affected":3,
     "date":'2026-06-10'
  },
     {
    "log_id":9003,
     "product_id":30,
     "warehouse_id":1003,
     "log_details":{
        "reason":"Count mismatch from system count ",
        "monitored by":"Inventory Manager"
     },
     "quantity-affected":1,
     "date":'2026-06-10'
  },
  
]
  );

db.audit_log.createIndex({"product_id":1});
db.audit_log.createIndex({"warehouse_id":1});

db.audit_log.find({"product_id":30});