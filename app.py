from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///education_system.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    classes = db.relationship('Class', backref='teacher', lazy=True)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    students = db.relationship('Student', backref='class', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    marks = db.relationship('Mark', backref='student', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    marks = db.relationship('Mark', backref='subject', lazy=True)

class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    max_score = db.Column(db.Float, default=100.0)
    exam_type = db.Column(db.String(20), nullable=False)  # quiz, test, exam
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    teachers = Teacher.query.all()
    classes = Class.query.all()
    students = Student.query.all()
    marks = Mark.query.all()
    
    # Get recent students (last 5)
    recent_students = Student.query.order_by(Student.id.desc()).limit(5).all()
    
    # Get recent marks (last 5)
    recent_marks = Mark.query.order_by(Mark.date.desc()).limit(5).all()
    
    return render_template('index.html', 
                         teachers=teachers, 
                         classes=classes, 
                         students=students, 
                         marks=marks,
                         recent_students=recent_students,
                         recent_marks=recent_marks)

@app.route('/teachers')
def teachers():
    teachers = Teacher.query.all()
    return render_template('teachers.html', teachers=teachers)

@app.route('/teachers/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        
        teacher = Teacher(name=name, email=email, subject=subject)
        db.session.add(teacher)
        db.session.commit()
        flash('Teacher added successfully!', 'success')
        return redirect(url_for('teachers'))
    
    return render_template('add_teacher.html')

@app.route('/classes')
def classes():
    classes = Class.query.all()
    return render_template('classes.html', classes=classes)

@app.route('/classes/add', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        teacher_id = request.form['teacher_id']
        
        class_obj = Class(name=name, grade=grade, teacher_id=teacher_id)
        db.session.add(class_obj)
        db.session.commit()
        flash('Class added successfully!', 'success')
        return redirect(url_for('classes'))
    
    teachers = Teacher.query.all()
    return render_template('add_class.html', teachers=teachers)

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        class_id = request.form['class_id']
        
        student = Student(name=name, student_id=student_id, class_id=class_id)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('students'))
    
    classes = Class.query.all()
    return render_template('add_student.html', classes=classes)

@app.route('/marks')
def marks():
    marks = Mark.query.all()
    return render_template('marks.html', marks=marks)

@app.route('/marks/add', methods=['GET', 'POST'])
def add_mark():
    if request.method == 'POST':
        student_id = request.form['student_id']
        subject_id = request.form['subject_id']
        score = float(request.form['score'])
        max_score = float(request.form['max_score'])
        exam_type = request.form['exam_type']
        
        mark = Mark(
            student_id=student_id,
            subject_id=subject_id,
            score=score,
            max_score=max_score,
            exam_type=exam_type
        )
        db.session.add(mark)
        db.session.commit()
        flash('Mark added successfully!', 'success')
        return redirect(url_for('marks'))
    
    students = Student.query.all()
    subjects = Subject.query.all()
    return render_template('add_mark.html', students=students, subjects=subjects)

@app.route('/reports')
def reports():
    classes = Class.query.all()
    return render_template('reports.html', classes=classes)

@app.route('/reports/<int:class_id>')
def class_report(class_id):
    class_obj = Class.query.get_or_404(class_id)
    students = Student.query.filter_by(class_id=class_id).all()
    
    # Calculate averages for each student
    student_data = []
    for student in students:
        marks = Mark.query.filter_by(student_id=student.id).all()
        if marks:
            total_score = sum(mark.score for mark in marks)
            total_max = sum(mark.max_score for mark in marks)
            average = (total_score / total_max) * 100
        else:
            average = 0
        
        student_data.append({
            'student': student,
            'average': round(average, 2),
            'marks_count': len(marks)
        })
    
    return render_template('class_report.html', class_obj=class_obj, student_data=student_data)

@app.route('/api/students/<int:class_id>')
def api_students(class_id):
    students = Student.query.filter_by(class_id=class_id).all()
    return jsonify([{'id': s.id, 'name': s.name, 'student_id': s.student_id} for s in students])

@app.route('/create-sample-data')
def create_sample_data():
    """Create sample data for demonstration purposes"""
    try:
        # Create sample teachers
        teacher1 = Teacher(name='John Smith', email='john.smith@school.com', subject='Mathematics')
        teacher2 = Teacher(name='Sarah Johnson', email='sarah.johnson@school.com', subject='Science')
        teacher3 = Teacher(name='Michael Brown', email='michael.brown@school.com', subject='English')
        
        db.session.add_all([teacher1, teacher2, teacher3])
        db.session.commit()
        
        # Create sample classes
        class1 = Class(name='Class 10A', grade='Grade 10', teacher_id=teacher1.id)
        class2 = Class(name='Class 9B', grade='Grade 9', teacher_id=teacher2.id)
        class3 = Class(name='Class 11C', grade='Grade 11', teacher_id=teacher3.id)
        
        db.session.add_all([class1, class2, class3])
        db.session.commit()
        
        # Create sample subjects
        subject1 = Subject(name='Mathematics', class_id=class1.id)
        subject2 = Subject(name='Physics', class_id=class1.id)
        subject3 = Subject(name='Chemistry', class_id=class2.id)
        subject4 = Subject(name='Biology', class_id=class2.id)
        subject5 = Subject(name='English Literature', class_id=class3.id)
        subject6 = Subject(name='Grammar', class_id=class3.id)
        
        db.session.add_all([subject1, subject2, subject3, subject4, subject5, subject6])
        db.session.commit()
        
        # Create sample students
        student1 = Student(name='Alice Johnson', student_id='ST001', class_id=class1.id)
        student2 = Student(name='Bob Wilson', student_id='ST002', class_id=class1.id)
        student3 = Student(name='Carol Davis', student_id='ST003', class_id=class2.id)
        student4 = Student(name='David Miller', student_id='ST004', class_id=class2.id)
        student5 = Student(name='Emma Taylor', student_id='ST005', class_id=class3.id)
        student6 = Student(name='Frank Anderson', student_id='ST006', class_id=class3.id)
        
        db.session.add_all([student1, student2, student3, student4, student5, student6])
        db.session.commit()
        
        # Create sample marks
        from random import randint
        
        # Marks for student1
        mark1 = Mark(student_id=student1.id, subject_id=subject1.id, score=85, max_score=100, exam_type='Test')
        mark2 = Mark(student_id=student1.id, subject_id=subject2.id, score=78, max_score=100, exam_type='Quiz')
        
        # Marks for student2
        mark3 = Mark(student_id=student2.id, subject_id=subject1.id, score=92, max_score=100, exam_type='Test')
        mark4 = Mark(student_id=student2.id, subject_id=subject2.id, score=88, max_score=100, exam_type='Quiz')
        
        # Marks for student3
        mark5 = Mark(student_id=student3.id, subject_id=subject3.id, score=75, max_score=100, exam_type='Exam')
        mark6 = Mark(student_id=student3.id, subject_id=subject4.id, score=82, max_score=100, exam_type='Assignment')
        
        # Marks for student4
        mark7 = Mark(student_id=student4.id, subject_id=subject3.id, score=95, max_score=100, exam_type='Exam')
        mark8 = Mark(student_id=student4.id, subject_id=subject4.id, score=89, max_score=100, exam_type='Assignment')
        
        # Marks for student5
        mark9 = Mark(student_id=student5.id, subject_id=subject5.id, score=87, max_score=100, exam_type='Midterm')
        mark10 = Mark(student_id=student5.id, subject_id=subject6.id, score=91, max_score=100, exam_type='Final')
        
        # Marks for student6
        mark11 = Mark(student_id=student6.id, subject_id=subject5.id, score=73, max_score=100, exam_type='Midterm')
        mark12 = Mark(student_id=student6.id, subject_id=subject6.id, score=79, max_score=100, exam_type='Final')
        
        db.session.add_all([mark1, mark2, mark3, mark4, mark5, mark6, mark7, mark8, mark9, mark10, mark11, mark12])
        db.session.commit()
        
        flash('Sample data created successfully! You can now explore the system.', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        flash(f'Error creating sample data: {str(e)}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 