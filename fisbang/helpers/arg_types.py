import datetime

def date_type(data):
    try:
        import datetime
        return datetime.datetime.fromtimestamp(int(data))
    except:
        raise ValueError("Malformed timestamp")

def datapoints(datas):
    try :
        import datetime
        return [{"time": datetime.datetime.fromtimestamp(int(data['time'])), "value": data['value']} for data in datas]
    except:
        raise ValueError("Malformed datapoints")