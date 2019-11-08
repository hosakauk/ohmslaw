import math

class ohmslaw():
    def __init__(self, volts,resistance,amps,watts):
        self.v = volts
        self.r = resistance
        self.i = amps
        self.p = watts

    def get_watts(self):
        if self.p is not None:
            return self.p
        elif self.v and self.i is not None:
            self.p = self.v*self.i
            return self.p
        elif self.r and self.i is not None:
            self.p = self.r*(math.pow(self.i,2))
            return self.p
        elif self.v and self.r is not None:
            self.p = (math.pow(self.v,2))/self.r
            return self.p
        else:
            pass

    def get_amps(self):
        if self.i is not None:
            return self.i
        elif self.p and self.r is not None:
            self.i = math.sqrt((self.p/self.r))
            return self.i
        elif self.p and self.v is not None:
            self.i = self.p/self.v
            return self.i
        elif self.v and self.r is not None:
            self.i = self.v/self.r
            return self.i
        else:
            pass

    def get_resistance(self):
        if self.r is not None:
            return self.r
        elif self.p and self.i is not None:
            self.r = self.p/(math.pow(self.i,2))
            return self.r
        elif self.v and self.p is not None:
            self.r = (math.pow(self.v,2))/p
            return self.r
        elif self.v and self.i is not None:
            self.r = self.v/self.i
            return self.r
        else:
            pass

    def get_volts(self):
        if self.v is not None:
            return self.v
        elif self.p and self.r is not None:
            self.v = math.sqrt(self.p*self.r)
            return self.v
        elif self.p and self.i is not None:
            self.v = self.i/self.i
            return self.v
        elif self.r and self.i is not None:
            self.v = self.r*self.i
            return self.v
