
#!/usr/bin/env python
import pydoop.mapreduce.api as api
import pydoop.mapreduce.pipes as pp

class Mapper(api.Mapper):
    def map(self, context):
        myfile = context.value.split(",")
        airport=myfile[16]
        if(myfile[15] > '0'):
            a="Delayed"
            context.emit(airport,a)
            
        elif(myfile[15] <= '0'):
            b="NotDelayed"
            context.emit(airport,b)
            
class Reducer(api.Reducer):
    def reduce(self, context):
        counte=0
        c=0
        for val in context.values:
            if(val =="Delayed"):
                c=c+1
                counte=counte+1
            elif(val=="NotDelayed"):
                counte=counte+1
        percentage_delay=(c*100./counte)
        context.emit(context.key,percentage_delay)
        


def __main__():
    pp.run_task(pp.Factory(Mapper, Reducer))

