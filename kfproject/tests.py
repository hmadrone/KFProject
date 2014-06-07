import unittest
import transaction

from pyramid import testing

from .models import DBSession


class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_home(self):
        from .views import KFViews
        request = testing.DummyRequest()
        inst = KFViews(request)
        info = inst.home()
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'KFProject')
        self.assertEqual(info['view'], 'home')

    def test_style(self):
        from .views import KFViews
        request = testing.DummyRequest()
        inst = KFViews(request)
        info = inst.style()
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'KFProject')
        self.assertEqual(info['view'], 'style')

    def test_size(self):
        from .views import KFViews
        request = testing.DummyRequest()
        inst = KFViews(request)
        info = inst.size()
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'KFProject')
        self.assertEqual(info['view'], 'size')

    def test_yarn(self):
        from .views import KFViews
        request = testing.DummyRequest()
        inst = KFViews(request)
        info = inst.yarn()
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'KFProject')
        self.assertEqual(info['view'], 'yarn')

    def test_sweater_type(self):
        from .garment import SweaterType
        inst = SweaterType()
        self.assertEqual(inst.pattern_name, 'My KnitFitter Sweater')
        self.assertEqual(inst.yoke, 'raglan')
        self.assertEqual(inst.sleeves, 'tapered')
        self.assertEqual(inst.style, 'pullover')
        self.assertEqual(inst.collar, 'none')
        self.assertEqual(inst.neck, 'crew')
        self.assertEqual(inst.neck_depth, 6)
        inst.pattern_name = 'Your Special KnitFitter Sweater'
        inst.yoke = 'standard'
        inst.sleeves = 'bell'
        inst.style = 'cardigan'
        inst.collar = 'peter pan'
        inst.neck = 'vee'
        inst.neck_depth = 8
        self.assertEqual(inst.pattern_name, 'Your Special KnitFitter Sweater')
        self.assertEqual(inst.yoke, 'standard')
        self.assertEqual(inst.sleeves, 'bell')
        self.assertEqual(inst.style, 'cardigan')
        self.assertEqual(inst.collar, 'peter pan')
        self.assertEqual(inst.neck, 'vee')
        self.assertEqual(inst.neck_depth, 8)

    def test_size(self):
        from .sizing import SweaterSize
        inst = SweaterSize('standard', "Child's", '2')
        self.assertEqual(inst.category, "Child's")
        self.assertEqual(inst.size, '2')
        self.assertEqual(inst.back_neck, 4.5)
        self.assertEqual(inst.underarm_depth, 4.5)
        self.assertEqual(inst.underarm, 0.5)
        self.assertEqual(inst.chest, 23)
        self.assertEqual(inst.body_len, 12)
        self.assertEqual(inst.sleeve_len, 7.5)
        self.assertEqual(inst.upper_arm, 8.5)
        self.assertEqual(inst.wrist, 6.5)
        if inst.category == 'standard':
            self.assertEqual(inst.upper_chest, 9)
            self.assertEqual(inst.shoulder, 2.5)
            self.assertEqual(inst.sleeve_cap, 2.1)
        inst.category = "Men's"
        inst.size = "custom"
        inst.back_neck = 9
        inst.underarm_depth = 13
        inst.underarm = 4
        inst.chest = 42
        inst.body_len = 25
        inst.sleeve_len = 19
        inst.upper_arm = 16
        inst.wrist = 9
        inst.upper_chest = 17
        inst.shoulder = 7
        inst.sleeve_cap = 4
        self.assertEqual(inst.category, "Men's")
        self.assertEqual(inst.size, "custom")
        self.assertEqual(inst.back_neck, 9)
        self.assertEqual(inst.underarm_depth, 13)
        self.assertEqual(inst.underarm, 4)
        self.assertEqual(inst.chest, 42)
        self.assertEqual(inst.body_len, 25)
        self.assertEqual(inst.sleeve_len, 19)
        self.assertEqual(inst.upper_arm, 16)
        self.assertEqual(inst.wrist, 9)
        self.assertEqual(inst.upper_chest, 17)
        self.assertEqual(inst.shoulder, 7)
        self.assertEqual(inst.sleeve_cap, 4)


class TestMyViewFailureCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_failing_home(self):
        from .views import KFViews
        request = testing.DummyRequest()
        inst = KFViews(request)
        info = inst.home()
        self.assertEqual(info.status_int, 500)

    def test_failing_sweater_type(self):
        from .garment import SweaterType
        inst = SweaterType()
        with self.assertRaises(AttributeError):
            inst.yoke = 'religious'
        with self.assertRaises(AttributeError):
            inst.sleeves = 'carillon'
        with self.assertRaises(AttributeError):
            inst.style = 'dress'
        with self.assertRaises(AttributeError):
            inst.collar = 'dog'
        with self.assertRaises(AttributeError):
            inst.neck = 'lace'
        with self.assertRaises(AttributeError):
            inst.neck_depth = 42

    def test_failing_sweater_size(self):
        from .sizing import SweaterSize
        inst = SweaterSize()
        with self.assertRaises(AttributeError):
            inst.category = "Dolphin's"
        with self.assertRaises(AttributeError):
            inst.back_neck = -9
        with self.assertRaises(AttributeError):
            inst.underarm_depth = 130
        with self.assertRaises(AttributeError):
            inst.underarm = 54
        with self.assertRaises(AttributeError):
            inst.chest = -42
        with self.assertRaises(AttributeError):
            inst.body_len = 325
        with self.assertRaises(AttributeError):
            inst.sleeve_len = 219
        with self.assertRaises(AttributeError):
            inst.upper_arm = 1016
        with self.assertRaises(AttributeError):
            inst.wrist = 89
        with self.assertRaises(AttributeError):
            inst.upper_chest = -17
        with self.assertRaises(AttributeError):
            inst.shoulder = -7
        with self.assertRaises(AttributeError):
            inst.sleeve_cap = 144
