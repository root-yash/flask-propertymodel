class ctrans:
    def preprocess(data):
        try:
            data.price=np.log2(data.price)
            data.area=np.log2(data.area)
            data["new"]=data.latitude*data.longitude
            data["new2"]=data.Bedrooms*delhi.Bathrooms
            data=data.drop(columns='longitude')
        except:
            pass
        return data