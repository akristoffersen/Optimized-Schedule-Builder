from Utils import combine

class TimeSlot(object):
    """A TimeSlot is the basic building block behind a course's components"""

    days = ['Monday, Tuesday, Wednesday, Thursday, Friday']

    def __init__(self, day, start, end, location=''):
        assert day in days, 'Day of slot not valid'
        self.day = day
        self.start = start
        self.end = end
        self.location = location

class Section(object):
    """A section is a group of time slots associated with a course."""

    types = ['Lecture', 'Discussion', 'Lab']

    def __init__(self, dept, dept_num, long_num, type, tslots, instructor=None):
        self.dept = upper(dept)
        self.dept_num = upper(dept_num)
        self.name = self.dept + ' ' + self.dept_num
        self.long_num = long_num
        self.type = type
        self.tslots = tslots
        self.locations = [t.location for t in tslots]
        self.instructor = instructor

class Course(object):
    """A course is a group of sections with the same characteristics"""

    def __init__(self, sections, units):
        first = sections[0]
        for s in sections:
            assert first.name == s.name and first.long_num == s.long_num, 'Sections do not all belong to same course.'
        self.sections = sections
        sorted = self.sort_sections_by_type()
        self.lectures = sorted[0]
        self.discussions = sorted[1]
        self.labs = sorted[2]
        self.department = first.dept
        self.name = first.name
        self.long_num = first.long_num
        self.units = units
        self.permutations =

    def sort_sections_by_type(self):
        """Sorts sections by first listing all lectures, then all discussions, then all labs."""
        lectures, discussions, labs = [], [], []
        for s in self.sections:
            if s.type == 'Lecture':
                lectures += [s]
            elif s.type == 'Discussion':
                discussions += [s]
            elif s.type == 'Lab':
                labs += [s]
        self.sections = lectures + discussions + labs
        return [lectures, discussions, labs]

    def permute(self):
        step_one = [[lec] for lec in self.lectures]
        step_two = []
        for dis in self.discussions:
            step_two += combine(step_one, dis)
        step_three = []
        for lab in self.labs:
            step_three += combine(step_three, dis)
        return step_three

class CourseList(object):
    """A course list is a collection of courses."""

    def __init__(self, courses):
        self.courses = courses

    def add_course(self, course):
        assert isinstance(course, Course), 'Not a course'
        self.courses.append(course)
        return 'Successfully added course ' + str(course)

    def remove_course(self, course):
        assert isinstance(course, Course), 'Not a course'
        current_pos = 0
        for c in self.courses:
            if c.name == course.name and c.units == course.units:
                self.courses = self.courses[:current_pos] + self.course[current_pos+1:]
                return 'Successfully removed course ' + str(course)
            current_pos += 1
        assert True, 'Could not find and remove course ' + str(course)

    def generate_course_list(self):
        str = 'Courses:\n'
        for c in self.courses:
            str += 'Name: {0} Units: {1} \n'.format(c.name, c.units)
        return str

class Schedule(CourseList):
    """A schedule is a collection of courses assigned to a student. The Schedule class also records the amount of units."""

    def __init__(self, courses, filters = []):
        CourseList.__init__(self, courses)
        self.student = student
        self.total_units = 0
        for course in courses:
            self.total_units += course.units
        self.filters = filters

    def add_course(self, course):
        ret_val = CourseList.add_course(self, course)
        self.total_units += course.units
        return ret_val + ' to bring unit total up to ' + self.total_units

    def remove_course(self, course):
        ret_val = CourseList.remove_course(self, course)
        self.total_units -= course.units
        return ret_val + ' to bring unit total down to ' + self.total_units

    def __str__(self):
        student_str = 'Student Name: {0}\nStudent Major: {1}\n\n'.format(self.student.name, self.student.major)
        course_list_str = CourseList.generate_course_list(self)
        return str + course_list_str + '\nTotal units: ' + self.total_units + '\n'

class CourseDatabase(CourseList):
    """The CourseDatabase class manages all the possible courses in the course catalog."""

    def __init__(self, courses, departments):
        CourseList.__init__(courses)
        self.departments = departments

    def add_course(self, course):
        #TBD

    def remove_course(self, course):
        #TBD

    def get_department_courses(self, department):
        #TBD

    def filter_by(self, filter):
        #TBD

    def find_course(self, course):
        #TBD

class TimeSchedule(Schedule):
    """A timed schedule is a collection of courses and their
       corresponding order and time slots assigned to a student."""

    def __init__(self, student, courses, start_time, end_time, filters=[]):
        Schedule.__init__(self, student, courses, filters)
        self.start_time = start_time
        self.end_time = end_time
        self.slots = []
        self.slots = self.clear_slots()

    def create_empty_slots(day, start, end):
        slots = []
        while start + 0.5 <= end:
            slots += [TimeSlot(day, start, end)]
            start += 0.5
        return slots

    def clear_slots(self):
        slots = []
        for day in TimeSlot.days:
            slots += self.create_empty_slots(day, self.start_time, self.end_time)
        self.slots = slots

    def fill_slots(self):
        #TBD

    def add_course(self, course):
        #TBD

    def remove_course(self, course):
        #TBD

    def get_day_schedule(self, day):
        #TBD

    def clip_by_time(self):
        #TBD
