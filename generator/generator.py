import os
import random
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        # full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(18,100),
        salary=random.randint(1000,100000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_ru.address(),  # different address. current_address != permanent_address
        mobile=faker_en.basic_phone_number()
    )


def generate_text_file(extension):
    """Generate file with different file extension."""
    path = generate_file_name(extension)
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close()
    return file.name, path


def generate_file_name(extension):
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(path, 'filetest') + f'{random.randint(0, 999)}' + '.' + extension


def select_one_random_photo_of_a_cat():
    images_directory = os.path.abspath(".."+os.sep+"images")
    file = random.choice(os.listdir(images_directory))
    return os.path.join(images_directory, file)


def generate_subjects(): # TODO
    pass


    #     value: 1,
    #     label: "Hindi"
    # }, {
    #     value: 2,
    #     label: "English"
    # }, {
    #     value: 3,
    #     label: "Maths"
    # }, {
    #     value: 4,
    #     label: "Physics"
    # }, {
    #     value: 5,
    #     label: "Chemistry"
    # }, {
    #     value: 6,
    #     label: "Biology"
    # }, {
    #     value: 7,
    #     label: "Computer Science"
    # }, {
    #     value: 8,
    #     label: "Commerce"
    # }, {
    #     value: 9,
    #     label: "Accounting"
    # }, {
    #     value: 10,
    #     label: "Economics"
    # }, {
    #     value: 11,
    #     label: "Arts"
    # }, {
    #     value: 12,
    #     label: "Social Studies"
    # }, {
    #     value: 13,
    #     label: "History"
    # }, {
    #     value: 14,
    #     label: "Civics"
    # }]

def convert_phone_number_live_only_numbers(phone_number):
    return "".join(c for c in phone_number if c.isdecimal())
