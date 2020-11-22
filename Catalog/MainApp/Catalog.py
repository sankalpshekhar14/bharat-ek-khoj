import pymongo

class Catalog(object):
    Recomclient = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0.cjuxp.mongodb.net/RecommendationsDB?retryWrites=true&w=majority')
    db=None
    userid=None

    def __init__(self,uid):
        self.db=self.Recomclient.RecommendationsDB
        self.userid=uid

    def getRecomBooks(self):
        recom_table=self.db.Recommendations
        print("Retrieveing recommendations from the recommender USERID:",self.userid)
        recom_books=list(recom_table.find({"UserID":self.userid}))
        print("Recommendations extracted, Length:",len(recom_books))
        return recom_books

    def UpdateCatalog(self,recom_books):
        cat_table=self.db.UserCatalog;
        print("Updating catalog")
        _=cat_table.insert_many(recom_books)
        print("Catalog Updated")

def makeCatalog(data):
    catalog = Catalog(data["userID"])
    recomBooks=catalog.getRecomBooks()
    catalog.UpdateCatalog(recomBooks)
