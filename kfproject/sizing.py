__author__ = 'heather'
import collections


class Error(Exception):
    pass


SizingClasses = ["Men's", "Women's", "Child's"]

# One of the challenges in knitting is getting the shaping to work with the stitch
# patterns. How to specify and express the harmonies needed to make a sweater a
# coherent whole?

# Women's raglan, poncho, or round yoke sizing
RaglanSize = collections.namedtuple("RaglanSize",
                                    "category size back_neck underarm_depth underarm "
                                    "chest body_len sleeve_len upper_arm wrist")
RaglanSizes = [RaglanSize("Women's", "30", 4.5, 9, 1, 32, 24, 16.5, 13, 8),
               RaglanSize("Women's", "32", 5, 9, 1, 34, 24.5, 16.75, 13.5, 8.25),
               RaglanSize("Women's", "34", 5, 9.5, 1, 36, 25, 17.5, 14.5, 8.5),
               RaglanSize("Women's", "36", 5.5, 9.5, 1, 38, 25, 17.5, 15, 9),
               RaglanSize("Women's", "38", 6, 10, 1, 40, 26, 17.5, 15, 9.5),
               RaglanSize("Women's", "40", 6, 10.5, 1.5, 42, 27, 18, 16, 9.5),
               RaglanSize("Women's", "42", 6.5, 11, 1.5, 44, 27.5, 18, 16.5, 10),
               RaglanSize("Women's", "44", 6.5, 11, 1.5, 46, 27.5, 18.5, 17.5, 10.5),
               RaglanSize("Women's", "46", 7.5, 11.5, 1.5, 48, 28, 18.5, 17.5, 11),
               RaglanSize("Women's", "48", 8, 12, 1.5, 50, 28, 19, 18, 11.5),
               RaglanSize("Women's", "50", 8, 12.5, 1.5, 52, 29, 19.5, 19, 12),
               RaglanSize("Child's", "6 months", 4, 4.5, 0.5, 21, 10.5, 6.5, 7.5, 6),
               RaglanSize("Child's", "1", 4, 5, 0.5, 22, 12.5, 7, 8, 6.25),
               RaglanSize("Child's", "2", 4, 5.5, 0.5, 23, 13.5, 7.5, 8.5, 6.5),
               RaglanSize("Child's", "3", 4, 5.5, 0.5, 24, 14.5, 8, 9, 6.75),
               RaglanSize("Child's", "4", 4, 6, 0.75, 25, 15, 8.5, 10, 7),
               RaglanSize("Child's", "5", 4, 6.25, 0.75, 26, 15.75, 9, 10.5, 7.25),
               RaglanSize("Child's", "6", 4, 6.5, 1, 27, 16.5, 9, 11, 7.5),
               RaglanSize("Child's", "8", 4.5, 7, 1, 29, 18.5, 10.5, 11.5, 8),
               RaglanSize("Child's", "10", 4.5, 7.5, 1, 30.5, 20.5, 12, 12.25, 8.25),
               RaglanSize("Child's", "12", 5, 8, 1, 32, 21.5, 13, 12.5, 8.5),
               RaglanSize("Men's", "34", 5, 10, 0.5, 36, 25, 18, 14.5, 9),
               RaglanSize("Men's", "36", 5.5, 10, 0.75, 38, 26, 18, 15, 9.5),
               RaglanSize("Men's", "38", 6, 10.5, 1, 40, 26.5, 18.5, 15.5, 9.5),
               RaglanSize("Men's", "40", 6, 11, 1, 42, 27, 19, 16.5, 10),
               RaglanSize("Men's", "42", 6.5, 11.5, 1, 44, 28.5, 19.5, 17, 10.5),
               RaglanSize("Men's", "44", 7, 12, 1, 46, 28.5, 20, 17.5, 11),
               RaglanSize("Men's", "46", 7, 12.5, 1.5, 48, 29.5, 20.5, 18.5, 11.5),
               RaglanSize("Men's", "48", 7, 13, 1.5, 50, 31, 20.5, 19.5, 12),
               RaglanSize("Men's", "50", 7.5, 13, 1.5, 52, 31, 21, 20, 12.5)]

StandardSize = collections.namedtuple("StandardSize",
                                      "category size back_neck underarm_depth underarm "
                                      "upper_chest chest body_len sleeve_len upper_arm wrist shoulder sleeve_cap")
StandardSizes = [StandardSize("Women's", "30", 6, 8, 1, 13, 32, 22, 16.5, 14, 8, 3.5, 3.5),
                 StandardSize("Women's", "32", 6.25, 8, 1, 13.25, 34, 22.5, 16.75, 14.5, 8.25, 3.5, 3.6),
                 StandardSize("Women's", "34", 6.5, 8.5, 1, 13.5, 36, 23, 17.5, 14.5, 8.5, 3.5, 3.6),
                 StandardSize("Women's", "36", 6.5, 8.5, 1, 14, 38, 23.5, 17.5, 15, 9, 3.75, 3.75),
                 StandardSize("Women's", "38", 7, 9, 1, 14.5, 40, 24, 17.5, 15, 9.5, 3.75, 3.75),
                 StandardSize("Women's", "40", 7, 9, 1.5, 15, 42, 24.5, 18, 15.5, 9.5, 4, 3.9),
                 StandardSize("Women's", "42", 7.5, 9.5, 1.5, 15.5, 44, 25, 18, 16, 10, 4, 4),
                 StandardSize("Women's", "44", 7.5, 9.5, 1.5, 16, 46, 25.5, 18.5, 16.5, 10.5, 4.25, 4.1),
                 StandardSize("Women's", "46", 8, 10, 1.5, 16.5, 48, 26, 18.5, 17, 11, 4.25, 4.25),
                 StandardSize("Women's", "48", 8, 10.5, 1.5, 17, 50, 26.5, 19, 17.5, 11.5, 4.5, 4.4),
                 StandardSize("Women's", "50", 8.25, 11, 1.5, 17.25, 52, 27, 19.5, 18, 12, 4.5, 4.5),
                 StandardSize("Child's", "6 months", 4, 3.75, 0.5, 7.8, 21, 9.75, 6.5, 7.5, 6, 1.9, 2),
                 StandardSize("Child's", "1", 4.5, 4, 0.5, 8, 22, 11, 7, 8, 6.25, 1.75, 2),
                 StandardSize("Child's", "2", 4.5, 4.5, 0.5, 9, 23, 12, 7.5, 8.5, 6.5, 2.25, 2.1),
                 StandardSize("Child's", "3", 5, 4.5, 0.5, 9.2, 24, 12.5, 8.5, 9.5, 6.75, 2.1, 2.4),
                 StandardSize("Child's", "4", 5.5, 5, 0.75, 9.5, 25, 13.5, 10, 10.5, 7, 2, 2.6),
                 StandardSize("Child's", "5", 5.5, 5.25, 0.75, 9.7, 26, 14.25, 10.5, 11, 7.25, 2.1, 2.75),
                 StandardSize("Child's", "6", 5.5, 5.5, 1, 10.3, 27, 14.5, 11, 11.5, 7.5, 2.4, 2.9),
                 StandardSize("Child's", "8", 6, 6, 1, 11, 29, 16.5, 12.5, 12, 8, 2.5, 3),
                 StandardSize("Child's", "10", 6, 6.5, 1, 11.5, 30.5, 18.5, 14, 12.5, 8.25, 2.75, 3.1),
                 StandardSize("Child's", "12", 6, 7, 1, 12, 32, 20, 15.5, 13, 8.5, 3, 3.25),
                 StandardSize("Men's", "34", 6.5, 9, 0.5, 15.5, 36, 23.5, 18, 15, 9, 4.5, 3.75),
                 StandardSize("Men's", "36", 7, 9, 0.75, 16, 38, 24, 18, 15.5, 9.5, 4.5, 3.9),
                 StandardSize("Men's", "38", 7.5, 9.5, 1, 16.5, 40, 24.5, 18.5, 16, 9.5, 4.5, 4),
                 StandardSize("Men's", "40", 7.5, 9.5, 1, 17, 42, 25, 19, 16.5, 10, 4.75, 4.1),
                 StandardSize("Men's", "42", 8, 10, 1, 17.5, 44, 26, 19.5, 17, 10.5, 4.75, 4.25),
                 StandardSize("Men's", "44", 8, 10.5, 1, 18, 46, 26.5, 20, 17.5, 11, 5, 4.4),
                 StandardSize("Men's", "46", 8.5, 11, 1.5, 18.5, 48, 27.5, 20.5, 18.5, 11.5, 5, 4.6),
                 StandardSize("Men's", "48", 8.5, 11.5, 1.5, 19, 50, 28.5, 20.5, 19.5, 12, 5.25, 4.9),
                 StandardSize("Men's", "50", 9, 11.5, 1.5, 19.5, 52, 28.5, 21, 20.5, 12.5, 5.25, 5.1)]


def get_size_categories():
    return SizingClasses


def get_size_choices(yoke='raglan', category="Women's"):
    sizes = RaglanSizes
    if yoke == 'standard':
        sizes = StandardSizes
    choices = []
    for size in sizes:
        if size.category == category:
            choices.append(size.size)
    return choices


def get_size_info(yoke='raglan', category="Women's", desired_size='34'):
    sizes = RaglanSizes
    if yoke == 'standard':
        sizes = StandardSizes
    for size in sizes:
        if size.category == category and size.size == desired_size:
            return size
    raise (IndexError, "Desired size not found in size table")


class SweaterSize:
    def __init__(self, yoke='raglan', category="Women's", desired_size='34'):
        """Returns size table instance for customization
        :param yoke:
        :param category:
        :param desired_size:
        """

        try:
            size_inst = get_size_info(yoke, category, desired_size)
        except IndexError:
            raise
        else:
            self.__category = category
            self.__size = desired_size
            self.__back_neck = size_inst.back_neck
            self.__underarm_depth = size_inst.underarm_depth
            self.__underarm = size_inst.underarm
            self.__chest = size_inst.chest
            self.__body_len = size_inst.body_len
            self.__sleeve_len = size_inst.sleeve_len
            self.__upper_arm = size_inst.upper_arm
            self.__wrist = size_inst.wrist
            if category == 'standard':
                self.__upper_chest = size_inst.upper_chest
                self.__shoulder = size_inst.shoulder
                self.__sleeve_cap = size_inst.sleeve_cap
            else:
                self.__upper_chest = self.__chest
                self.__shoulder = 14
                self.__sleeve_cap = 4

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in SizingClasses:
            raise AttributeError("Sweater category ", value, " unknown. Supported sweater categories are",
                                 SizingClasses)
        self.__category = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def back_neck(self):
        return self.__back_neck

    @back_neck.setter
    def back_neck(self, value):
        if value < 0 or value > 20:
            raise AttributeError("Back neck ", value, " out of range 0-20.")
        self.__back_neck = value

    @property
    def underarm_depth(self):
        return self.__underarm_depth

    @underarm_depth.setter
    def underarm_depth(self, value):
        if value < 0 or value > 30:
            raise AttributeError("Underarm depth ", value, " out of range 0-30.")
        self.__underarm_depth = value

    @property
    def underarm(self):
        return self.__underarm

    @underarm.setter
    def underarm(self, value):
        if value < 0 or value > 20:
            raise AttributeError("Underarm ", value, " out of range 0-20.")
        self.__underarm = value

    @property
    def chest(self):
        return self.__chest

    @chest.setter
    def chest(self, value):
        if value < 0 or value > 100:
            raise AttributeError("Chest ", value, " out of range 0-100.")
        self.__chest = value

    @property
    def body_len(self):
        return self.__body_len

    @body_len.setter
    def body_len(self, value):
        if value < 0 or value > 60:
            raise AttributeError("Body length ", value, " out of range 0-60.")
        self.__body_len = value

    @property
    def sleeve_len(self):
        return self.__sleeve_len

    @sleeve_len.setter
    def sleeve_len(self, value):
        if value < 0 or value > 40:
            raise AttributeError("Sleeve length ", value, " out of range 0-40.")
        self.__sleeve_len = value

    @property
    def upper_arm(self):
        return self.__upper_arm

    @upper_arm.setter
    def upper_arm(self, value):
        if value < 0 or value > 40:
            raise AttributeError("Upper arm ", value, " out of range 0-40.")
        self.__upper_arm = value

    @property
    def wrist(self):
        return self.__wrist

    @wrist.setter
    def wrist(self, value):
        if value < 0 or value > 30:
            raise AttributeError("Wrist ", value, " out of range 0-30.")
        self.__wrist = value

    @property
    def upper_chest(self):
        return self.__upper_chest

    @upper_chest.setter
    def upper_chest(self, value):
        if value < 0 or value > 100:
            raise AttributeError("Upper chest ", value, " out of range 0-100.")
        self.__upper_chest = value

    @property
    def shoulder(self):
        return self.__shoulder

    @shoulder.setter
    def shoulder(self, value):
        if value < 0 or value > 30:
            raise AttributeError("Shoulder ", value, " out of range 0-30.")
        self.__shoulder = value

    @property
    def sleeve_cap(self):
        return self.__sleeve_cap

    @sleeve_cap.setter
    def sleeve_cap(self, value):
        if value < 0 or value > 30:
            raise AttributeError("Sleeve cap ", value, " out of range 0-30.")
        self.__sleeve_cap = value
