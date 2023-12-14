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
    )


def generate_file(format_file):
    path = generate_file_name(format_file)
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close()
    return file.name, path


def generate_file_name(format_file):
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(path, 'filetest') + f'{random.randint(0, 999)}' + '.' + format_file
