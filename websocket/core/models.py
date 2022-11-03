from django.db import models

# Create your models here.


# import the standard Django Model
# from built-in library
from django.db import models
 
# declare a new model with a name "GeeksModel"
class TVS(models.Model):
        # fields of the model
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    machine_ID = models.CharField(max_length = 200)
    machine_IDC = models.CharField(max_length = 200)
    sensor = models.CharField(max_length = 200)
    sensorname = models.CharField(max_length = 200)
    phone=models.CharField(max_length = 200)
    
    
 
        # renames the instances of the model
        # with their title name
    # def __str__(self):
    #     return self.title















# class machines(models.Model):
# 	username = models.CharField(max_length=200, null=True)
# 	machine_name = models.CharField(max_length=200, null=True)
#     machine_name = models.CharField(max_length=200, null=True)
#     machine_name = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name

# class Product(models.Model):
# 	CATEGORY = (
# 			('Indoor', 'Indoor'),
# 			('Out Door', 'Out Door'),
# 			) 

# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField(null=True)
# 	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
# 	description = models.CharField(max_length=200, null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	tags = models.ManyToManyField(Tag)

# 	def __str__(self):
# 		return self.name

# class Order(models.Model):
# 	STATUS = (
# 			('Pending', 'Pending'),
# 			('Out for delivery', 'Out for delivery'),
# 			('Delivered', 'Delivered'),
# 			)

# 	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
# 	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	status = models.CharField(max_length=200, null=True, choices=STATUS)
# 	note = models.CharField(max_length=1000, null=True)

	# def __str__(self):
	# 	return self.product.name



	
