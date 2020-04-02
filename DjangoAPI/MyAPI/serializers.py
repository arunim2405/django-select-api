from rest_framework import serializers
from . models import loanmodel

class loanmodelSerializers(serializers.ModelSerializer):
	class Meta:
		model=loanmodel
		fields='__all__'