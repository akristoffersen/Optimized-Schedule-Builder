import berkeleytimescraper as scrape

class Course:
    def __init__(self, name, number):
        self.name = name #string
        self.number = number #takes a number or string

        infos = scrape.getinfo(self.name, self.number)
        self.classes = [Class(info) for info in infos]
        self.finaltime = self.classes[0][8]


class Class:
    #base object, representing one time slot for a course
    def __init__(self, info):
        #type of class (ex. 'Discussion' or 'Lecture')
        self.type = info[1]
        #class number
        self.num = info[2]
        #times of that class [[day, start, end], [day, start, end]... ]
        self.times = info[3]
        #Location [building, room]
        self.location = info[4]
        #amount enrolled
        self.enrolled = info[5]
        #waitlisted
        self.waitlist = info[6]

class Schedule:
    courseload = []

    def __init__(self, *courses):
        for course in courses:
            self.courseload.append(course)
    
    def addcourse(self, course):
        assert isinstance(course, Course), "Must be a Course instance."
        self.courseload.append(course)
    
    def removecourse(self, ind):
        return self.courseload.pop(ind)
