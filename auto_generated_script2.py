class Student {
    String name;
    int id;
    String major;

    Student(String name, int id, String major) {
        this.name = name;
        this.id = id;
        this.major = major;
    }

    void displayStudentInfo() {
        System.out.println("Name: " + name + ", ID: " + id + ", Major: " + major);
    }
}

class Course {
    String courseName;
    String courseCode;
    int credits;

    Course(String courseName, String courseCode, int credits) {
        this.courseName = courseName;
        this.courseCode = courseCode;
        this.credits = credits;
    }

    void displayCourseInfo() {
        System.out.println("Course Name: " + courseName + ", Course Code: " + courseCode + ", Credits: " + credits);
    }
}

public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("Alice", 123, "Computer Science");
        Course course1 = new Course("Introduction to Programming", "CS101", 3);

        student1.displayStudentInfo();
        course1.displayCourseInfo();
    }
}