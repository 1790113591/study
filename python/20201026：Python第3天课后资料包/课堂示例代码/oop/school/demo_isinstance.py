from oop.school.person import Person
from oop.school.student import Student
from oop.school.teacher import Teacher

zzr = Student("周芷若", 25, "女", "S1013", "全程5期")

print("isinstance(zzr, Student) :", isinstance(zzr, Student))
print("isinstance(zzr, Teacher) :", isinstance(zzr, Teacher))
print("isinstance(zzr, Person) :", isinstance(zzr, Person))
print("isinstance(1.83, float) :", isinstance(1.83, float))
