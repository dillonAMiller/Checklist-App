from django.db import models

# Create your models here.

class item(models.Model):

    ''' description of item '''
    item_desc = models.CharField(max_length=30)

    ''' I don't remember what this does'''
    objects = models.Manager()

    '''tuple (?) of choices for itemDisplayed attribute'''
    item_is_displayed_choices = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    '''property of item object which indicates whether or not it is displayed'''
    itemDisplayed = models.CharField(max_length=3, choices=item_is_displayed_choices, default='No')

    '''calls the item description when item is displayed'''
    def __str__(self):
        return self.item_desc
    
class sets(models.Model):
    set_name = models.CharField(max_length=30)
    objects = models.Manager()
    def __str__(self):
        return self.set_name

    itemsInSet = models.ManyToManyField(item)