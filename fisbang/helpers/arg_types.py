import datetime

def datapoints(datas):
    try :
        return [{"timestamp": int(data['timestamp']), "value": float(data['value'])} for data in datas]
    except:
        raise ValueError("Malformed datapoints")