!pip install openai==0.28

import openai

# Initialize OpenAI API key
openai.api_key = '123' #your API code goes here

class_data = [
    {
        "name": "Electricity & Electronics 1",
        "description": "This entry-level course is the study of Basic Electrical theory that also includes an introduction to electronics and residential wiring. The primary units of study include Ohm’s law and power in series, parallel and series-parallel circuits, magnetism and electromagnetism, measurement and testing instruments, circuit construction, testing and troubleshooting, and wiring and troubleshooting a variety of typical electrical circuits.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "None",
        "recommendation": "This entry-level course is recommended for students interested in careers related to electrical circuit design and repair, electrical engineering or residential and commercial electrician."
    },
    {
        "name": "Electricity 2",
        "description": "This course is the study of electrical systems and components. The primary units of study include hardware, troubleshooting, maintenance and repair, soldering and programming digital circuits. Students will demonstrate learning by repairing various electronic systems and devices. Eligible students may have the opportunity for a paid work experience through the YST program. The job will work around a student’s school schedule, it provides a sustaining wage, on-the-job training, and a quality resume builder for students interested in careers in the electrical or electronics industry.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Electricity & Electronics 1",
        "recommendation": "This course is recommended for students interested in careers related to electrical circuit design and repair, electrical engineering or residential and commercial electrician."
    },
    {
        "name": "Woods 1",
        "description": "This entry-level course gives students hands-on experiences in imagining, designing, and creating personalized projects while exploring all areas of STEM. Instead of purchasing on Etsy, learn how you can create it yourself for a fraction of the cost! Areas can include woodworking, electrical soldering, CAD, graphic design, 3D printing & laser engraving, and resin and metalworking. The primary units of study include graphic design to create projects for woodworking, 3D printing and laser engraving, vinyl cutter and large format printing. Students will demonstrate learning through exploratory, hands-on, project-based activities utilizing the machinery in our Innovation Center.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "None",
        "recommendation": "Students will develop hands-on skills and problem-solving skills in STEM areas of study. The course is offered at LSHS only. LNHS students provide their own transportation."
    },
    {
        "name": "Woods 2",
        "description": "This course is the study of the design and construction of medium-sized to larger size woodworking projects as well as product development. The primary units of study include the use of hand and machine tools incorporating methods used in industry, measurement, safety, joinery and assembly, preparation for finishes, and finishing. Students will demonstrate learning through the creation of wood projects through hands-on activities, sequence steps, and apply processes to complete projects and demonstrate safe equipment, tooling, and lab use.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Woods 1",
        "recommendation": "A fee will be assessed for any projects taken home. Students may purchase higher quality materials than offered as part of the course. LNHS students provide their own transportation."
    },
    {
        "name": "Woods 3",
        "description": "This course is the study of the design and construction of cabinet making and related furniture projects. The primary units of study include the artistic process and foundations, hand and machine tools incorporating methods used in industry, measurement, safety, joinery and assembly, preparation for finishes, and finishing. Students will demonstrate learning through the design of individual wood projects, sequence steps, apply processes to complete projects, and demonstrate safe equipment, tooling, and lab use.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Woods 2",
        "recommendation": "A fee will be assessed for any projects taken home. Students may purchase higher quality materials than offered as part of the course. LNHS students provide their own transportation. Colleges and universities may or may not accept this course as an Arts credit."
    },
    {
        "name": "Woods 4",
        "description": "This course is the study of the design and construction of cabinet making and related furniture projects. The primary units of study include the artistic process and foundations, hand and machine tools incorporating methods used in industry, measurement, safety, joinery and assembly, preparation for finishes, and finishing. Students will demonstrate learning through the design of individual wood projects, sequence steps, apply processes to complete projects, and demonstrate safe equipment, tooling, and lab use.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Woods 2",
        "recommendation": "A fee will be assessed for any projects taken home. Students may purchase higher quality materials than offered as part of the course. LNHS students provide their own transportation. Colleges and universities may or may not accept this course as an Arts credit."
    }
]


class_data += [
    {
        "name": "Engineering & Innovation 1",
        "description": "This course is the study of the fundamentals of engineering, manufacturing, and design technology. Students will experience problem-solving with engineering and design, product fabrication, and manufacturing processes. The primary units of study include the engineering design process, fabrication, 3-D printing, vinyl sticker and t-shirt design, CNC plasma cutting, CNC wood routing, laser engraving, and other technologies used in today's STEM careers. Students will demonstrate learning through assessments on safety and machine operation and will submit projects for grading.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students who wish to gain skills in STEM and Engineering careers. It is recommended for students who prefer hands-on, collaborative learning and want to learn about applying knowledge to real-world projects."
    },
    {
        "name": "Engineering & Innovation 2",
        "description": "This course is the advanced study of the fundamentals of manufacturing, engineering, and design technology. Students will experience problem-solving with engineering and design, product fabrication, and manufacturing processes. The primary units of study include the engineering design process, fabrication, 3-D printing, vinyl sticker, and t-shirt design, CNC plasma cutting, CNC wood routing, laser engraving, waterjet cutting, and other technologies used in today's manufacturing. Students will demonstrate learning through assessments on safety and machine operation and will submit projects for grading.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Engineering & Innovation 1",
        "recommendation": "This course is recommended for students who wish to gain an advanced understanding of manufacturing and engineering careers. It is also recommended for students who prefer hands-on, collaborative learning and want to learn more about applying knowledge to real-world projects."
    },
    {
        "name": "Engineering & Innovation 3",
        "description": "This course is the advanced study of applying previously learned skills in manufacturing, engineering, and design technology and creating one or more independent project(s). The primary units of study may include the engineering design process, fabrication, 3-D printing, vinyl sticker and t-shirt design, CNC plasma cutting, CNC wood routing, laser engraving, waterjet cutting, and other technologies used in today's manufacturing. Students will demonstrate learning through the evaluation of their independent projects.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Engineering & Innovation 2",
        "recommendation": "This course is recommended for students who are able to independently develop engineering and manufacturing projects. It is also recommended for students who prefer hands-on, collaborative learning and who want to learn more about applying their knowledge to real-world projects."
    },
    {
        "name": "Engineering & Innovation 4",
        "description": "This course is the advanced study of applying previously learned skills in manufacturing, engineering, and design technology and creating one or more independent project(s). The primary units of study may include the engineering design process, fabrication, 3-D printing, vinyl sticker and t-shirt design, CNC plasma cutting, CNC wood routing, laser engraving, waterjet cutting, and other technologies used in today's manufacturing. Students will demonstrate learning through the evaluation of their independent projects.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Engineering & Innovation 3",
        "recommendation": "This course is recommended for students who are able to independently develop engineering and manufacturing projects. It is also recommended for students who prefer hands-on, collaborative learning and who want to learn more about applying their knowledge to real-world projects."
    },
    {
        "name": "Computer-Aided Design & Engineering 1",
        "description": "This course is the study of engineering through problem solving related to design. Computer-Aided Design (CAD) software provides the foundation for modeling team projects and individual solutions to design briefs. The primary units of study include CAD commands and functions, applied geometry, international standards of representation, problem solving models, and the engineering design process. Students will demonstrate learning through the application of basic skills with Creo/Pro CAD software, reading and creating technical drawings and sketches, and applying design and problem-solving models while working individually and in teams to build functional models and mechanisms.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students interested in careers related to science, technology, and engineering."
    },
    {
        "name": "Computer-Aided Design & Engineering 2",
        "description": "This course is the continuous study of engineering through problem solving related to design. The primary units of study include CAD commands and functions, applied geometry, international standards of representation, problem solving models, the engineering design process, mechanisms, and kinematics. Students will demonstrate learning through projects with three-dimensional computer-aided design (CAD) software, perform kinematic analysis of CAD models, create animations and renderings of designs, and continue to apply design and problem-solving models while working individually and in teams to create structures and programmable remotely controlled mechanisms.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Computer-Aided Design & Engineering 1",
        "recommendation": "This course is recommended for students interested in careers related to science, technology, and engineering."
    },
    {
        "name": "Robotics",
        "description": "This course is the study of the use, programming, and applications of robotics in a problem-solving environment. The primary units of study include robot commands and functions, problem solving models, and the engineering design process. Students will demonstrate learning through designing, building, programming, and testing a robot. Students will work in teams to build a Tetrix robot specifically designed to meet a specific challenge. Problem-solving skills will need to be developed, projects will need to be tested and reengineered to meet the required outcomes.",
        "grades": ["10", "11", "12"],
        "location": ["North", "South"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students interested in careers related to robotics, STEM, and automation."
    },
    {
        "name": "Manufacturing, Metals & Welding 1",
        "description": "This course is the study of welding, manufacturing, engineering, and design processes along with their related technologies. The primary units of study include Problem Solving, Industrial Design, MIG, TIG, and Plastic welding as well as CNC Plasma & Waterjet cutting. Students will demonstrate learning through problem solving, safety, hands-on projects, custom designs, and fabrication with the Welding, Plasma, and Waterjet processes. Multiple projects designed by the students will be fabricated to take home.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students who love hands-on learning and wish to explore career fields in Manufacturing, Engineering, & Welding Technology."
    },
    {
        "name": "Manufacturing, Metals & Welding 2",
        "description": "This course is the advanced study of welding, manufacturing, engineering, and design processes along with their related technologies. The primary units of study include Problem Solving, Industrial Design, MIG, TIG, and Plastic welding as well as CNC Plasma & Waterjet cutting. Students will demonstrate learning through problem solving, safety, hands-on projects, custom designs, and fabrication with the Welding, Plasma, and Waterjet processes. Multiple projects designed by the students will be fabricated to take home.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Manufacturing, Metals & Welding 1",
        "recommendation": "This course is recommended for students who love hands-on learning and wish to explore career fields in Manufacturing, Engineering, & Welding Technology."
    }
]

class_data += [
    {
        "name": "Manufacturing, Metals & Welding 3",
        "description": "This course is the study of all available welding and manufacturing processes and their related technologies applied to create one or more independent project(s). The primary units of study include Mig, TIG, and Plastic welding as well as Plasma & Waterjet cutting. Students will demonstrate learning through the evaluation of their project(s) and course participation as well as the opportunity to work with local businesses.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Manufacturing, Metals & Welding 2",
        "recommendation": "This course is recommended for students who wish to explore career and post-secondary opportunities and eventually enter a career in the Manufacturing, Engineering & Welding industry."
    },
    {
        "name": "Manufacturing, Metals & Welding 4",
        "description": "This course is the study of all available welding and manufacturing processes and their related technologies applied to create one or more independent project(s). The primary units of study include Mig, TIG, and Plastic welding as well as Plasma & Waterjet cutting. Students will demonstrate learning through the evaluation of their project(s) and course participation as well as the opportunity to work with local businesses.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Manufacturing, Metals & Welding 3",
        "recommendation": "This course is recommended for students who wish to explore career and post-secondary opportunities and eventually enter a career in the Manufacturing, Engineering & Welding industry."
    },
    {
        "name": "Auto Technology 1",
        "description": "This course is the study of the various parts and general maintenance on small engines as well as working up to basic vehicle maintenance. Lakeville North does have a car lift and tire changer that will be available for some of the class activities. The primary units of study will be 2 and 4 cycle engines, Introduction to how cars work, Buying an automobile, Automotive expenses, Repair facilities, Safety around the automobile, Tools and equipment, Auto care and cleaning, Fluid level checks, Electrical systems, Lubrication systems, Fuel systems, Cooling and climate control, Ignition system, Suspension~steering and tires, Braking system, Drivetrain, Exhaust and emission systems, Alternative Fuels and designs, Automotive accessories, & Common problems and roadside Emergencies. The students will demonstrate learning through oral and written assignments as well as teardown and reassembly of a small engine. Students will have access to the shop car lift for general auto maintenance.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students who wish to learn more about basic small engine maintenance and repair as well as general automotive maintenance, light repair, auto ownership, and automobile mechanics. A car is not required to take the class but recommended."
    },
    {
        "name": "Auto Technology 2",
        "description": "This course will build upon the topics covered in level 1 and continue in Automotive Maintenance and repair topics and also include motorcycle topics. Lakeville North does have a car lift, multiple motorcycle lifts, and tire changer that will be available for some of the class activities. The Students will earn OHSA 10 Certification as well as have the opportunity to do the Youth Skills Training on-the-job program. This allows students to have a paid work experience with a local automotive company. The job will work around a student’s school schedule and allow them to make money and learn from industry experts while still getting credit for the class. This provides a sustaining wage, on-the-job training, and a quality resume builder for students interested in a career in the automotive or mechanics industry. The primary units of study will be Safety around the automobile, Tools and equipment, Auto care and cleaning, Fluid level checks, Electrical systems, Lubrication systems, Fuel systems, Cooling and climate control, Ignition system, Suspension~steering and tires, Braking system, Drivetrain, Exhaust and emission systems, Alternative Fuels and designs, Automotive accessories, & Common problems and roadside Emergencies. Basic repairs on student vehicles will be covered including exhaust and rust repair. Custom motorcycle class builds will be available for qualifying students. The students will demonstrate learning through oral and written assignments as well as hands-on class activities. Students will have access to the shop car lift for general auto maintenance and repairs approved by the instructor.",
        "grades": ["10", "11", "12"],
        "location": ["North"],
        "prerequisite": "Auto Technology 1",
        "recommendation": "This course is recommended for students who wish to learn more about general automotive maintenance, light repair, auto ownership, and motorcycle & automobile mechanics. A car is not required to take the class but recommended."
    },
    {
        "name": "Architecture 1",
        "description": "This course is the study of the basic concepts of residential design. Primary units of study include basic house designs, the artistic process and foundations, primary considerations, architectural drafting fundamentals, and room and space planning. Students will demonstrate learning through projects using basic skills with industry-standard AutoDesk computer-aided design software to create working drawings to include floor plans, elevation drawings, foundation plans, kitchen plans, and construction details and design.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North", "South"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students interested in careers related to architecture and building construction."
    },
    {
        "name": "Architecture 2",
        "description": "This course is a continuation of the study of architectural design focusing on multi-story and multi-unit residential structures. Primary units of study include CAD commands and functions, room and space planning, the artistic process and foundations, construction systems, presentation methods, specifications.",
        "grades": ["10", "11", "12"],
        "location": ["North", "South"],
        "prerequisite": "Architecture 1",
        "recommendation": ""
    },
    {
        "name": "Architecture 3",
        "description": "The course is a continuation of the study of architectural design with an introduction to commercial design. The primary units of study include CAD commands and functions, room and space planning, construction systems, presentation methods, specifications, and estimating as related to specific challenges. Students will demonstrate learning with AutoDesk Academy software, analyzing an architectural design brief and working in teams to design a solution to the challenge, completing a set of working drawings to include multiple levels, elevation drawings, site plans, foundation plans, and construction details and deliver a multimedia presentation to a panel of licensed architects for evaluation at the Minnesota STEM & MANUFACTURING.",
        "grades": ["10", "11", "12"],
        "location": ["North", "South"],
        "prerequisite": "Architecture 2",
        "recommendation": "This course is recommended for students interested in careers related to architecture and building construction."
    },
    {
        "name": "Crafting Solutions for Impact (CSI)",
        "description": "This course will explore a variety of STEM topics that highlight the social significance of engineering. Possible topics include smart cities and sustainability, sustainable fashion, Design Thinking, sustainable tourism practices, corporate social responsibility, clean water access and conservation, renewable energy, food waste reduction, ocean conservation, biofuels, environmental engineering, climate change awareness, role models in engineering, and biomedical applications.",
        "grades": ["9", "10", "11", "12"],
        "location": ["North"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students who are interested in understanding global issues and designing possible solutions to lessen the impact."
    },
    {
        "name": "Advanced Design & Manufacturing (Capstone 2)",
        "description": "This course is the study of the engineering design process. It engages students in a personalized learning experience where they can continue to build knowledge, skills, and abilities in their specialized area of interest. Students will perform research and apply the engineering design process to define a problem, design and build a solution while continuing to work closely with a community expert using the Agile philosophy and Scrum framework. The primary units of study will focus on computer programming, industrial technology, science, engineering, and manufacturing. The students will demonstrate their learning through an electronic portfolio, guided research, and the engineering process.",
        "grades": ["11", "12"],
        "location": ["South"],
        "prerequisite": "STEM Capstone or Teacher Approval",
        "recommendation": ""
    },
    {
        "name": "Engineering Your Future 1",
        "description": "This entry-level course expands on the study of all four STEM disciplines. It continues to challenge students with powerful real-world lessons, activities, and design problems. The primary units of study include engineering design and construction principles, engineering fundamentals of construction materials/methods, principles of technology in 3D printing, CAD design, computer-integrated manufacturing and robotics, exploration in woodworking, electronic technologies, digital electronics, and basic code writing, environmental engineering, career development and exploration, reading and understanding blueprints, the basic principle of circuits, and home wiring. The students will demonstrate learning through exploratory, hands-on, project-based activities, and engineering projects while working in teams.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "None",
        "recommendation": ""
    },
    {
        "name": "Engineering Your Future 2",
        "description": "This course expands on the study of all four STEM disciplines, picking up where Engineering Your Future 1 left off. It continues to challenge students with powerful real-world lessons, activities, and design problems. The primary units of study include engineering design and construction principles, engineering fundamentals of construction materials/methods, principles of technology in 3D printing, CAD design, computer integrated manufacturing and robotics, exploration in woodworking, electronic technologies, digital electronics, and basic code writing, environmental engineering, career development and exploration, reading and understanding blueprints, basic principle of circuits and home wiring. The students will demonstrate learning through exploratory, hands-on, project-based activities and engineering projects while working in teams.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Engineering Your Future 1",
        "recommendation": ""
    },
    {
        "name": "Engineering Your Future 3",
        "description": "This course expands on the study of all four STEM disciplines, picking up where Engineering Your Future 1 left off. It continues to challenge students with powerful real-world lessons, activities, and design problems. The primary units of study include engineering design and construction principles, engineering fundamentals of construction materials/methods, principles of technology in 3D printing, CAD design, computer-integrated manufacturing and robotics, exploration in woodworking, electronic technologies, digital electronics, basic code writing, environmental engineering, career development and exploration, reading and understanding blueprints, the basic principle of circuits, and home wiring. The students will demonstrate learning through exploratory, hands-on, project-based activities, and engineering projects while working in teams.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Engineering Your Future 2",
        "recommendation": ""
    },
    {
        "name": "Environmental & Biomedical Engineering",
        "description": "This course engages students in hands-on experiences through a project and mentor based course, in the environmental and biomedical engineering fields. This hands-on, real-world course actively engages students in their learning through the use of cutting-edge laboratory and engineering techniques such as using 3D printers, 3D scanners and AR/VR technologies. Students will perform research and apply the engineering design process to define a problem, design and build a solution while working closely with a community expert using the Agile philosophy and Scrum framework. There will also be opportunities to interact with professionals in the field. The primary units of study will focus on Environmental & Biological Engineering. The students will demonstrate their learning through an electronic portfolio, guided research, engineering process.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Engineering Your Future 2",
        "recommendation": ""
    },
    {
        "name": "Engine Technology 1",
        "description": "This entry-level course is the study of various power and energy systems which include small engines, hydraulics, and pneumatics. The primary units of study include 2 and 4 cycle engines, hydraulics, and pneumatics. Students will demonstrate learning through oral and written assessments as well as teardown and reassembly of small engines and construction of various hydraulic and pneumatic systems.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "None",
        "recommendation": "This course is recommended for students who wish to learn more about power and energy systems using a hands-on approach."
    },
    {
        "name": "Engine Technology 2",
        "description": "Students will earn OSHA 10 Certification and have the opportunity to work toward obtaining certifications that employers are seeking. These credentials and work experiences give students an edge when starting their careers. Students can gain paid work experience with a local automotive company, with job schedules that work around school hours, providing a sustaining wage, on-the-job training, and a quality resume builder for students interested in careers in the automotive or mechanics industry. The primary units of study include automotive-related systems.",
        "grades": ["10", "11", "12"],
        "location": ["North", "South"],
        "prerequisite": "Engine Technology 1, received Teacher Approval, and are 16 years old or older.",
        "recommendation": "This course is recommended for students who wish to learn more about power and energy systems using a hands-on approach."
    },
    {
        "name": "STEM Capstone",
        "description": "This course engages students in a personalized learning experience where students apply critical thinking skills and creativity while investigating a specialized area of interest. Students will perform research and apply the engineering design process to define a problem, design and build a solution while working closely with a community expert using the Agile philosophy and Scrum framework. Students will complete a group project. The primary units of study will focus on the area of expertise (Computer programming, Industrial Technology, Science, and Engineering). The students will demonstrate their learning through an electronic portfolio, guided research, engineering process, and a presentation to a committee of teachers and community members.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Engineering Your Future 1 and Engineering Your Future 2 and a Pathway Course",
        "recommendation": ""
    },
    {
        "name": "DIY Home Projects",
        "description": "This entry-level course gives students hands-on experiences in imagining, designing, and creating personalized projects while exploring all areas of STEM. Instead of purchasing on Etsy learn how you can create it yourself for a fraction of the cost! Areas can include woodworking, electrical soldering, CAD, graphic design, 3D printing & laser engraving, and resin and metalworking. The primary units of study include graphic design to create projects for woodworking, 3D printing and laser engraving, vinyl cutter and large format printing. The students will demonstrate learning through exploratory, hands-on, project-based activities utilizing the machinery in our Innovation Center.",
        "grades": ["9", "10", "11", "12"],
        "location": ["South"],
        "prerequisite": "None",
        "recommendation": ""
    },
    {
        "name": "Building Construction/Applied Architecture",
        "description": "This course is the study of residential construction and building trades. Primary units of study include blueprint reading, architectural scale modeling, and structural engineering concepts. Students will demonstrate learning through blueprint reading worksheets and hands-on activities building scale models and mock-ups. They will design simple structures with architectural CAD software, read and create scale design drawings and models, demonstrate familiarity with residential framing techniques and terminology, demonstrate safe lab and tool use, explore construction materials and technologies, and construct residential electrical circuits.",
        "grades": ["10", "11", "12"],
        "location": ["South"],
        "prerequisite": "Woods 1 & Architecture 1",
        "recommendation": "This course is recommended for students interested in careers related to architecture and building construction."
    }
]

def add_string_to_set(s, my_set):
    my_set.add(s)
    if s[-1].isdigit():
        i = len(s) - 1
        while i >= 0 and s[i].isdigit():
            i -= 1
        base, num = s[:i+1], s[i+1:]
        incremented_string1 = base + str(int(num) + 1)
        incremented_string2 = base + str(int(num) + 2)
        my_set.add(incremented_string1)
        my_set.add(incremented_string2)

def filter_classes(grade, location):
    qualified_classes = []
    for course in class_data:
        if grade in course["grades"] and location in course["location"]:
            qualified_classes.append(course)
    return qualified_classes

def check_prerequisites(qualified_classes):
    classes_taken = set()
    classes_not_taken = set()
    qualified_classes_after_prereq = []
    for course in qualified_classes:
      if(not course["prerequisite"] in classes_not_taken):
        if (course["prerequisite"] == "None" or course["prerequisite"] in classes_taken):
            qualified_classes_after_prereq.append(course)
        else:
            answer = input(f"Have you taken and passed {course['prerequisite']}? (yes/no): ").lower()
            if answer == "yes":
                qualified_classes_after_prereq.append(course)
                classes_taken.add(course["prerequisite"])
            else:
                 add_string_to_set(course["prerequisite"], classes_not_taken)
    for takenCourse in classes_taken:
        for candidateCourse in qualified_classes_after_prereq:
            if takenCourse == candidateCourse["name"]:
                qualified_classes_after_prereq.remove(candidateCourse)
    return qualified_classes_after_prereq

def get_grade_input():
    while True:
        grade = input("Enter the grade level you are selecting classes for (9-12): ")
        if grade.isdigit() and 9 <= int(grade) <= 12:
            return grade
        else:
            print("Invalid input. Please enter a valid grade level (9-12).")

def get_location_input():
    while True:
        location = input("Enter your location (North or South): ")
        if location in ["North", "South"]:
            return location
        else:
            print("Invalid input. Please enter a valid location (North or South).")

def main():
    grade = get_grade_input()
    location = get_location_input()
    if grade.isdigit() and 9 <= int(grade) <= 12 and location in ["North", "South"]:
        grade = str(grade)
        qualified_classes_stage1 = filter_classes(grade, location)


        if not int(grade) == 9:
            qualified_classes_stage2 = check_prerequisites(qualified_classes_stage1)
        else:
            qualified_classes_stage2 = qualified_classes_stage1

        if qualified_classes_stage2:
            # Prompt user for potential career paths and STEM interests
            prompt1 = input("Please enter your potential career paths: ")
            prompt2 = input("Please enter your STEM field interests (ex. 'woods', 'CAD design'): ")

            # Collect class names and descriptions
            class_names_descriptions = []
            for course in qualified_classes_stage2:
                class_names_descriptions.append(course["name"])
                class_names_descriptions.append(course["description"])

            # Generate recommendations from ChatGPT
            class_info = "\n".join([f"{course['name']}\nDescription: {course['description']}\n" for i, course in enumerate(qualified_classes_stage2, 1)])

            # Send data to ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"I am a high school student in grade {grade} located in {location}. My potential career paths are: {prompt1}, and my STEM interests are {prompt2}. Given this, which of the following classes would you recommend? Respond informatively, do not enumerate your answers in any way. Especially elaborate on how the classes relate to my STEM interests and may prepare me for my potential career field."},
                    {"role": "user", "content": class_info}
                ]
            )

            # Print recommendations
            print()
            print()
            for message in response["choices"]:
                print(message["message"]["content"])
        else:
            print("You have not taken and passed the prerequisites for any of the qualified classes.")

    else:
        print("Invalid input. Please enter a valid grade level (9-12) and location (North or South).")

if __name__ == "__main__":
    main()
