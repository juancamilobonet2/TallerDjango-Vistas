from variables.models import Variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    if new_var.get("variable"):
        measurement.variable = Variable.objects.get(pk=int(new_var.get("variable")))
    if new_var.get("value"):
        measurement.value = new_var.get("value")
    if new_var.get("unit"):
        measurement.unit = new_var.get("unit")
    if new_var.get("place"):
        measurement.place = new_var.get("place")
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=Variable.objects.get(pk=int(var["variable"])), value=var["value"], unit=var["unit"], place=var["place"])
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return measurement