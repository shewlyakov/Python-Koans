#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        self.assertTrue(True)

    def test_assert_with_message(self):
        self.assertTrue(True)

    def test_fill_in_values(self):
        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        assert True

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        self.assertEqual(str, "navel".__class__)
