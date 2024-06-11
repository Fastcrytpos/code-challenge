class Band:

    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name
    @property
    def hometown(self):
        return self._hometown
    @hometown.setter
    def hometown(self,newhometown):
        if type(newhometown)==str and len(newhometown)>0:
           return self._hometown
    @name.setter
    def name(self,newname):
        if type(newname)==str and len(newname)>0:
            self._name = newname


    def concerts(self):
        concerts_for_band = [concert for concert in Concert.all if concert.band == self]
        result =concerts_for_band if concerts_for_band else None
        return result

    def venues(self):
        self.concerts() if self.concerts else None
        if self.concerts():
            result=list(set(concert.venue for concert in self.concerts() if isinstance(concert.venue,Venue)))
            return result if result else None   
        else:
            return None
        
        

    def play_in_venue(self, venue, date):
        concert=Concert(date,self,venue)
        return concert
        pass

    def all_introductions(self):
        result = []
        if self.concerts :
            for concert in self.concerts():
                
                result.append(f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}")
            return result if result else None
        else:
            return None
        


class Concert:
    all=[]
    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue
        self.all.append(self)
    @property
    def date(self):
        return self._date
    @property
    def band(self):
        return self._band
    @property
    def venue(self):
        return self._venue
    @date.setter
    def date(self,newdate):
        if type(newdate)==str and len(newdate)>0:
            self._date = newdate
    @band.setter
    def band(self,newband):
        if isinstance(newband,Band):
            self._band = newband
    @venue.setter
    def venue(self,newvenue):
        if isinstance(newvenue,Venue):
            self._venue = newvenue

    def hometown_show(self):
        return (self.band.hometown==self.venue.city)
        pass

    def introduction(self):
        return(f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}")
        pass


class Venue:
    all=[]
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self.all.append(self)
    @property
    def city(self):
        return self._city
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,newname):
        if type(newname)==str and len(newname)>0:
            self._name = newname
    @city.setter
    def city(self,newcity):
        if type(newcity)==str and len(newcity)>0:
            self._city = newcity

    def concerts(self):
        return[concerts for concerts in Concert.all if concerts.venue==self]
        pass

    def bands(self):
        return list(set(concert.band for concert in self.concerts() if isinstance(concert.band,Band)))

        pass
