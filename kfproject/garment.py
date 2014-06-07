__author__ = 'heather'


class Error(Exception):
    pass

# Sweater can be raglan, poncho, round yoke, saddle shoulder, or standard
# Standard measurements vary depending on type of sweater construction and
# age and sex of wearer.
YokeTypes = ["raglan", "poncho", "round yoke", "saddle shoulder", "standard"]
RaglanYokes = ["raglan", "poncho", "round yoke"]
StandardYokes = ["standard", "saddle shoulder"]

# standard sweaters can have sleeves or no sleeves (vests, tanks, shells)
# Sleeves in sweaters can be any length.
# There are really only a few sleeve styles that make sense for knitted garments:
# tapered, rectangular, bell, and puff.
# The more interesting thing in sleeve styles is patterned knitting or colorwork
# different from the body pattern.
SleeveTypes = ["none", "tapered", "rectangular", "bell", "puffed"]

# Neck type can be one of crew, scoop, vee, shawl, U, or square vee
# Front fills in over time with center increases until front is as wide as back
NeckTypes = ["crew", "scoop", "vee", "shawl"]

# Sweaters can have collars or none
CollarTypes = ["none", "shirt", "mandarin", "peter pan", "ruffled", "full hood", "fitted hood"]

# Sweater can be cardigan or puilover
Styles = ["cardigan", "pullover"]


class SweaterType:
    def __init__(self):
        """ Class for Sweater Style Choices
        """
        self.__pattern_name = 'My KnitFitter Sweater'
        self.__yoke = 'raglan'
        self.__sleeves = 'tapered'
        self.__style = 'pullover'
        self.__collar = 'none'
        self.__neck = 'crew'
        self.__neck_depth = 6

    @property
    def pattern_name(self):
        return self.__pattern_name

    @pattern_name.setter
    def pattern_name(self, value):
        self.__pattern_name = value

    @property
    def yoke(self):
        return self.__yoke

    @yoke.setter
    def yoke(self, value):
        if value not in YokeTypes:
            raise AttributeError("Sweater yoke type ", value, " unknown. Supported sweater yoke types are ", YokeTypes)
        self.__yoke = value

    @property
    def sleeves(self):
        return self.__sleeves

    @sleeves.setter
    def sleeves(self, value):
        if value not in SleeveTypes:
            raise AttributeError("Sweater sleeve type ", value, " unknown. Supported sweater sleeve types are ", SleeveTypes)
        self.__sleeves = value

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, value):
        if value not in Styles:
            raise AttributeError("Sweater style ", value, " unknown. Supported sweater styles types are ", Styles)
        self.__style = value

    @property
    def collar(self):
        return self.__collar

    @collar.setter
    def collar(self, value):
        if value not in CollarTypes:
            raise AttributeError("Sweater collar type ", value, " unknown. Supported sweater collar types are ", CollarTypes)
        self.__collar = value

    @property
    def neck(self):
        return self.__neck

    @neck.setter
    def neck(self, value):
        if value not in NeckTypes:
            raise AttributeError("Sweater neck type ", value, " unknown. Supported sweater neck types are ", NeckTypes)
        self.__neck = value

    @property
    def neck_depth(self):
        return self.__neck_depth

    @neck_depth.setter
    def neck_depth(self, value):
        if value < 0 or value > 20:
            raise AttributeError("Sweater neck depth ", value, " out of range 0-20 ")
        self.__neck_depth = value


# SweaterType
