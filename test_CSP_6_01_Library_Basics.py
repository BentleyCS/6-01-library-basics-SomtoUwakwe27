import CSP_6_01_Library_Basics as HW


def test_process_expenses():
    assert HW.process_expenses([100,200,300,400]) == [115,230,345,460]


def test_analyze_scores():
    assert HW.analyze_scores([100,25,50,75]) == ([100, 62.5])


def test_sanitize_usernames():
    assert HW.sanitize_usernames([["UP PER    ", "Lower    ", "smal l   ", "WhAt   "]]) == ([["up per", "lower", "smal l", "what"]])


def test_identify_outliers():
    assert HW.identify_outliers([4,50,110,200]) == ([[110,200]])


def test_search_and_report():
    assert HW.search_and_report([" Real ","Minds ", "Eye "], "eye") == (2)
