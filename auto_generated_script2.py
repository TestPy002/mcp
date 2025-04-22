class Student {
    String name;
    int id;
    String major;

    public Student(String name, int id, String major) {
        this.name = name;
        this.id = id;
        this.major = major;
    }

    public void displayStudentInfo() {
        System.out.println("Name: " + name + ", ID: " + id + ", Major: " + major);
    }
    
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Student object destroyed: " + name);
        super.finalize();
    }
}

class Course {
    String courseName;
    String courseCode;
    int credits;

    public Course(String courseName, String courseCode, int credits) {
        this.courseName = courseName;
        this.courseCode = courseCode;
        this.credits = credits;
    }

    public void displayCourseInfo() {
        System.out.println("Course Name: " + courseName + ", Code: " + courseCode + ", Credits: " + credits);
    }
    
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Course object destroyed: " + courseName);
        super.finalize();
    }
}

public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("Alice", 123, "Computer Science");
        student1.displayStudentInfo();

        Course course1 = new Course("Introduction to Programming", "CS101", 3);
        course1.displayCourseInfo();

        //Destructors are called by garbage collector, not explicitly.  For demonstration purposes only.
        //System.gc(); //Request garbage collection (not guaranteed to happen immediately)

    }
}