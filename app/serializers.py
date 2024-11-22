# convert complex data into native data type that can be easily rendered into JSON which can be used in react on client side 

from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        field = ['employee', 'department']
