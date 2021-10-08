from .models import Employee
import random


FIRST_NAME = ("Jay", "Jim", "Roy", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul",
			"Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren",
			"Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet",
			"Lydia", "Charles", "Pedro", "Bradley", "Aaron", "Abraham", "Adam", "Adrian", "Aidan",
			"Alan", "Albert", "Alejandro", "Alex", "Alexander", "Alfred", "Andrew", "Angel", "Anthony",
			"Antonio", "Ashton", "Austin", "Daniel", "David", "Dennis", "Devin", "Diego", "Dominic",
			"Donald", "Douglas", "Dylan", "Harold", "Harry", "Hayden", "Henry", "Herbert", "Horace",
			"Howard", "Hugh", "Hunter", "Malcolm", "Martin", "Mason", "Matthew", "Michael", "Miguel",
			"Miles", "Morgan")

LAST_NAME = ("Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers",
			"Warren", "Keller", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",
			"Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez",
			"Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez", "Harris",
			"Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young", "Allen", "Sanchez",
			"Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell",
			"Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins",
			"Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers",
			"Morgan", "Peterson", "Cooper", "Reed")

MOUNTS = list(map(str, range(1, 13)))

DAYS = list(map(str, range(1, 29)))


def seeder():
	for i in range(3):
		first_level_boss = Employee.objects.create(
													name 			= random.choice(FIRST_NAME) + ' ' + random.choice(LAST_NAME),
													position 		= 'level 1',
													employment_date = random.choice(['2015', '2016', '2017']) + '-' + random.choice(MOUNTS) + '-' + random.choice(DAYS),
													salary 			= random.choice([17000, 18000])
												  )
		for j in range(3):
			second_level_boss = Employee.objects.create(
														parent			= first_level_boss,
														name 			= random.choice(FIRST_NAME) + ' ' + random.choice(LAST_NAME),
														position 		= 'level 2',
														employment_date = random.choice(['2017', '2018', '2019']) + '-' + random.choice(MOUNTS) + '-' + random.choice(DAYS),
														salary 			= random.choice([14000, 15000])
													   )
			for k in range(3):
				third_level_boss = Employee.objects.create(
															parent			= second_level_boss,
															name 			= random.choice(FIRST_NAME) + ' ' + random.choice(LAST_NAME),
															position 		= 'level 3',
															employment_date = random.choice(['2019', '2020']) + '-' + random.choice(MOUNTS) + '-' + random.choice(DAYS),
															salary 			= random.choice([10000, 12000])
														  )
				for l in range(3):
					fourth_level_boss = Employee.objects.create(
																parent 			= third_level_boss,
																name 			= random.choice(FIRST_NAME) + ' ' + random.choice(LAST_NAME),
																position 		= 'level 4',
																employment_date = random.choice(['2020', '2021']) + '-' + random.choice(MOUNTS) + '-' + random.choice(DAYS),
																salary 			= random.choice([7000, 8000])
																)
					for m in range(3):
						Employee.objects.create(
												parent 			= fourth_level_boss,
												name 			= random.choice(FIRST_NAME) + ' ' + random.choice(LAST_NAME),
												position 		= 'level 5',
												employment_date = '2021-' + random.choice(MOUNTS) + '-' + random.choice(DAYS),
												salary 			= random.choice([5000, 6000])
												)

seeder()