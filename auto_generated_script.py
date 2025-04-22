class Student {
    private String name;
    private int studentID;
    private String major;

    public Student(String name, int studentID, String major) {
        this.name = name;
        this.studentID = studentID;
        this.major = major;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }


    public int getStudentID() {
        return studentID;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println("Student object " + studentID + " is being garbage collected.");
        super.finalize();
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", studentID=" + studentID +
                ", major='" + major + '\'' +
                '}';
    }
}

class Course {
    private String courseName;
    private String courseID;
    private int credits;
    private Student[] enrolledStudents;
    private int numEnrolled;
    private final int MAX_STUDENTS = 100;


    public Course(String courseName, String courseID, int credits) {
        this.courseName = courseName;
        this.courseID = courseID;
        this.credits = credits;
        this.enrolledStudents = new Student[MAX_STUDENTS];
        this.numEnrolled = 0;
    }

    public void enrollStudent(Student student) {
        if (numEnrolled < MAX_STUDENTS) {
            enrolledStudents[numEnrolled++] = student;
        } else {
            System.out.println("Course is full. Cannot enroll " + student.getName());
        }
    }

    public String getCourseName() {
        return courseName;
    }

    public String getCourseID() {
        return courseID;
    }

    public int getCredits() {
        return credits;
    }

    public Student[] getEnrolledStudents() {
        return enrolledStudents;
    }

    public int getNumEnrolled() {
        return numEnrolled;
    }


    @Override
    protected void finalize() throws Throwable {
        System.out.println("Course object " + courseID + " is being garbage collected.");
        super.finalize();
    }

    @Override
    public String toString() {
        return "Course{" +
                "courseName='" + courseName + '\'' +
                ", courseID='" + courseID + '\'' +
                ", credits=" + credits +
                '}';
    }
}