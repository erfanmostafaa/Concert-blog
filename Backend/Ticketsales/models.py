from django.db import models # type: ignore

class ConcertModel(models.Model):

    class Meta:
         verbose_name ="کنسرت"
         verbose_name_plural = "کنسرت"



    Name = models.CharField(max_length=200, verbose_name= "نام کنسرت")
    SingerName = models.CharField(max_length=150 ,verbose_name="نام خواننده")
    lenght = models.IntegerField(verbose_name=" مدت زمان")
    poster = models.ImageField(upload_to= "ConcertImage" , null= True,verbose_name = "پوستر")

    def __str__(self) :
        return self.SingerName
    


class LocationModel(models.Model):

    class Meta:
        verbose_name="محل برگزاری"
        verbose_name_plural="محل برگزاری"


    Name = models.CharField(max_length=100,verbose_name="مکان برگزاری")
    Address = models.CharField(max_length=500 , default= "برج میلاد",verbose_name="ادرس") 
    phone = models.CharField(max_length=11 , null= True ,verbose_name="شماره تماس")
    Capacity = models.IntegerField()

 
    def __str__(self):
        return self.Name
    

class TimeModel(models.Model):
   
    class Meta:
         verbose_name="زمان برگزاری"
         verbose_name_plural="زمان برگزاری"


    ConcertModel = models.ForeignKey("ConcertModel", on_delete= models.PROTECT,verbose_name="نام خواننده")
    LocationModel = models.ForeignKey( "LocationModel" , on_delete=models.PROTECT,verbose_name="مکان کنسرت")
    StartDatetime = models.DateTimeField(verbose_name = "تاریخ")
    Seats = models.IntegerField(verbose_name='تعداد صندلی')

    start =1
    End = 2
    Cancle = 3
    Sales = 4
    status_choises = (('start','فروش بلیط شروع شده است'),
                     ('end','فروش بلیط تمام شده است' ),
                     ("Cancle", "این سانس کنسل  شده است"),
                     ("Sales","در حال فروش بلیط"),
                     )



    Status = models.CharField(choices=status_choises , null=True , verbose_name="وضعیت" , max_length=50)


    def __str__(self) :
        return f"{self.StartDatetime} - {self.ConcertModel}"
    




class ProfileModel(models.Model):
        

        class Meta:
             verbose_name="شرکت کنندگان"
             verbose_name_plural="شرکت کنندگان"


        Name = models.CharField(max_length=100,verbose_name="نام")
        Family = models.CharField(max_length=100,verbose_name="نام خانوادگی")
        ProfileImage = models.ImageField(upload_to= "ProfileImage/" , null= True ,verbose_name = "عکس پروفایل")



        Man = 1
        Women = 2
        status_choises = (("Man", "مرد"), ("Women", "زن"))



        Gender = models.IntegerField(choices=status_choises ,verbose_name = "جنسیت")

        def __str__(self) :
            return "Full.Name:{} {} " .format( 'Name' ,'Family')
        


class TicketModel(models.Model):
        
        class Meta:
             verbose_name=" بلیط"
             verbose_name_plural=" بلیط"


        ProfileModel = models.ForeignKey("ProfileModel",on_delete=models.PROTECT,verbose_name="پروفایل")
        timeModel = models.ForeignKey("timeModel",on_delete=models.PROTECT,verbose_name="زمان")


        Name = models.CharField(max_length=100,verbose_name="نوع بلیط")
        price = models.IntegerField(verbose_name="قیمت")
        TicketImage = models.ImageField(upload_to= "TicketImages/", null= True,verbose_name="تصویر بلیط")




        def __str__(self) -> str:
            return "TicketInfo: Profile:{} ConcertInfo: {}".format( TimeModel.__str__())



































