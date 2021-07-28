import unittest
import utils.calculate as cal


class TestCalcullate(unittest.TestCase):
    def test_distance(self):
        lat_center = 55.755826
        long_center = 37.6173

        lat_target = 55.771646
        long_target = 37.593875

        distance = cal.haversine(lat_center, long_center, lat_target, long_target)
        self.assertEqual(distance, 2.2895359215574236)

    def test_outarea(self):
        lat_center = 55.755826
        long_center = 37.6173
        area = 17.4519

        dst = cal.haversine(lat_center, long_center, 55.825492, 49.080974)
        if dst >= area:
            result = True
        else:
            result = False

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
