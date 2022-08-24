from HarryPotterHouseGrade import traits
from HarryPotterHouseGrade import grade


def test_traits():
    assert traits('ambition') == 'slytherin'
    assert traits('courage') == 'gryffindor'


def test_grade():
    assert grade('2004') == 'grade:13'
    assert grade('2005') == 'grade:12'
    assert grade('2006') == 'grade:11'
    assert grade('2007') == 'grade:10'
    

def main():
    test_grade()
    test_traits()
    
if __name__ == '__main__':
    main()