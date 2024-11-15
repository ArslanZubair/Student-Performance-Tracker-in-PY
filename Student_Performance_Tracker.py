class Student():
    def __init__(self,fullName,scores):
        self.fullName = fullName
        self.scores = scores

    def calculate_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self,passing_score = 40):
        return all(score >= passing_score for score in self.scores)
    
    
class PerformanceTracker():
    def __init__(self):
        self.students = {}


    def add_students(self,students):
        self.students[students.fullName] = students
        

    def calculate_class_average(self):
        if len(self.students) == 0:
            return 0    
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)


    def display_student_performance(self):
        if len(self.students) == 0:
            print("No Student Record found in the Trcaker !")
            return 
        
        for student in self.students.values():
            average = student.calculate_average()
            is_passing = student.is_passing()
            print( f"Student: {student.fullName} | Average: {average} | Passing: {'Yes ! Congragulations' if is_passing else 'No,Student Needs Improvement !'}")


def get_student_data():
    tracker = PerformanceTracker()

    while True:
        try:
            name = input("Enter the student's Name or type 'done' to finish: ")
            if name.lower() == 'done':
                break

            scores = []
            for i in range (1,4):
                score = float(input(f"Enter the score of subject {i}: "))
                if score < 0 or score > 100:
                    raise ValueError("Scores must betweeb 0 to 100")
                scores.append(score)

            student = Student(name,scores)
            tracker.add_students(student)    
        except ValueError as ve:
            print(f"Invalid input: {ve}")


    return tracker


def display_results(tracker):

    print("\n-----------------Student Performance-----------------:")
    tracker.display_student_performance()

    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_average}")
    


if __name__ == "__main__":
    tracker = get_student_data()
    display_results(tracker)

        
              


