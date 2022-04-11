from main.models import Customer, Worker, Document, VIPClient, Project
from datetime import date

aiganysh = Customer.objects.create(name="Aiganysh", birth_date=date(1989, 1, 1), address = "Bishkek", phone_number = 564738395)
dolat = Customer.objects.create(name="Dolatbek", birth_date=date(2004, 11, 5), address = "Bishkek", phone_number = 34757583)
kamila = Customer.objects.create(name="Kamila", birth_date=date(1999, 10, 11), address = "Biskek", phone_number = 8574638383)

samira = VIPClient.objects.create(name="Samira", birth_date=date(2004, 7, 16), address = "Bishkek", phone_number = 84847575, vip_status_start=date(2018, 1, 1), donation_amount=1000)


rassel = Worker.objects.create(name="Rassul", birth_date = date(2004, 11, 16), work_position="backend_developer", experience = date(2020, 9,1))
tahir = Worker.objects.create(name="Takhir", birth_date = date(2004, 7, 19), work_position="video editor", experience=date(2020, 1, 1))
salavat = Worker.objects.create(name="Salavat", birth_date = date(2001, 6, 15), position="developer", experience=date(2021, 10, 15))

p1 = Document.objects.create(employee=rassel, inn="M12736464", id_card="PA737474")
p2 = Document.objects.create(employee=tahir, inn="M83837373", id_card="PA733757")
p3 = Document.objects.create(employee=salavat, inn="M47563894", id_card="PA583958")

p3 = Document.objects.get(id=3)
p3.delete()

e3 = Worker.objects.get(id=3)
e3.delete()

lesson = Project.objects.create(project_name = "Codify")
lesson.members.set([rassel, tahir], through_defaults={'date_joined':date(2022, 4, 5)})

workers = Worker.objects.all()
print(workers)
workersid = workers.filter(Passport__inn__isnull = False, Passport__card_id__isnull = False )
print(workersid)
projects = Project.objects.all()
print(projects)
one_worker = Project.objects.get(Worker.fullname == "Rassul")
print(one_worker)