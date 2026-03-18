class student:
	def __init__(self,name,year,roll_no):
		self.name = name
		self.year = year
		self.roll_no = roll_no

class internal_exam_marks(student):
	def __init__(self,name,year,roll_no,internal_1_marks,internal_2_marks,internal_3_marks):
		super().__init__(name,year,roll_no)
		self._internal_1_marks = internal_1_marks
		self._internal_2_marks = internal_2_marks
		self._internal_3_marks = internal_3_marks
	def best_of_two(self):
		best_of_two_list=[self._internal_1_marks,self._internal_2_marks,self._internal_3_marks]
		best_of_two_list.sort()
		best_of_two_list.pop(0)
		best_total=sum(best_of_two_list)
		return best_total


Student = internal_exam_marks("Bhavesh","first",1234,18,16,19)
print(Student.best_of_two())

