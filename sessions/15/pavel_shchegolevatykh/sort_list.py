people = [
  {
    "firstName": "Hayden",
    "lastName": "Sims",
    "age": 39
  },
  {
    "firstName": "Hester",
    "lastName": "Downs",
    "age": 43
  },
  {
    "firstName": "Fisher",
    "lastName": "Rojas",
    "age": 54
  },
  {
    "firstName": "Maritza",
    "lastName": "York",
    "age": 37
  },
  {
    "firstName": "Bernice",
    "lastName": "Lester",
    "age": 31
  },
  {
    "firstName": "Sara",
    "lastName": "Livingston",
    "age": 59
  },
  {
    "firstName": "Whitney",
    "lastName": "Anthony",
    "age": 52
  },
  {
    "firstName": "Tonya",
    "lastName": "Grant",
    "age": 57
  },
  {
    "firstName": "Jacqueline",
    "lastName": "Cortez",
    "age": 37
  },
  {
    "firstName": "Wade",
    "lastName": "Brennan",
    "age": 58
  },
  {
    "firstName": "Freida",
    "lastName": "Glover",
    "age": 50
  },
  {
    "firstName": "Sheri",
    "lastName": "Mckenzie",
    "age": 18
  },
  {
    "firstName": "Chan",
    "lastName": "Hooper",
    "age": 19
  },
  {
    "firstName": "Skinner",
    "lastName": "Joyce",
    "age": 18
  },
  {
    "firstName": "Kendra",
    "lastName": "Porter",
    "age": 33
  },
  {
    "firstName": "Davidson",
    "lastName": "Crawford",
    "age": 39
  },
  {
    "firstName": "Schwartz",
    "lastName": "Avila",
    "age": 45
  },
  {
    "firstName": "Dixie",
    "lastName": "Bates",
    "age": 26
  },
  {
    "firstName": "Helga",
    "lastName": "Rios",
    "age": 52
  },
  {
    "firstName": "Ruiz",
    "lastName": "Simpson",
    "age": 37
  },
  {
    "firstName": "Lawrence",
    "lastName": "Maddox",
    "age": 31
  },
  {
    "firstName": "Cole",
    "lastName": "Tran",
    "age": 33
  },
  {
    "firstName": "Randall",
    "lastName": "French",
    "age": 39
  },
  {
    "firstName": "Cooke",
    "lastName": "Phelps",
    "age": 52
  },
  {
    "firstName": "Johanna",
    "lastName": "Orr",
    "age": 34
  },
  {
    "firstName": "Bartlett",
    "lastName": "Grimes",
    "age": 54
  },
  {
    "firstName": "Tanisha",
    "lastName": "Sampson",
    "age": 49
  },
  {
    "firstName": "Claudia",
    "lastName": "Haley",
    "age": 24
  },
  {
    "firstName": "Shelly",
    "lastName": "Higgins",
    "age": 31
  },
  {
    "firstName": "Hicks",
    "lastName": "Douglas",
    "age": 20
  },
  {
    "firstName": "Dejesus",
    "lastName": "Duffy",
    "age": 39
  },
  {
    "firstName": "Maxwell",
    "lastName": "Guzman",
    "age": 25
  },
  {
    "firstName": "Ellis",
    "lastName": "Donovan",
    "age": 27
  },
  {
    "firstName": "Davis",
    "lastName": "Zen",
    "age": 18
  },
  {
    "firstName": "Dorothea",
    "lastName": "Jones",
    "age": 46
  },
  {
    "firstName": "Tran",
    "lastName": "Hobbs",
    "age": 57
  },
  {
    "firstName": "Clarice",
    "lastName": "Lynch",
    "age": 47
  },
  {
    "firstName": "Rhodes",
    "lastName": "Rush",
    "age": 57
  },
  {
    "firstName": "Baker",
    "lastName": "Hayden",
    "age": 32
  },
  {
    "firstName": "Ashlee",
    "lastName": "Golden",
    "age": 52
  },
  {
    "firstName": "Carly",
    "lastName": "Conrad",
    "age": 32
  },
  {
    "firstName": "Davis",
    "lastName": "Ware",
    "age": 42
  },
  {
    "firstName": "Wolf",
    "lastName": "Woods",
    "age": 51
  },
  {
    "firstName": "Charmaine",
    "lastName": "Atkinson",
    "age": 39
  },
  {
    "firstName": "Katy",
    "lastName": "Larson",
    "age": 36
  },
  {
    "firstName": "Mullen",
    "lastName": "Glenn",
    "age": 56
  },
  {
    "firstName": "Aida",
    "lastName": "Hickman",
    "age": 60
  },
  {
    "firstName": "Mcgee",
    "lastName": "Summers",
    "age": 48
  },
  {
    "firstName": "Mcgee",
    "lastName": "Adams",
    "age": 33
  },
  {
    "firstName": "Jenna",
    "lastName": "Allison",
    "age": 53
  }
]

people.sort(key=lambda x: (x['firstName'], x['lastName']))

print(f'Sorted by first name then last name: {people}')

print(f'Sorted by age (new list): {sorted(people, key=lambda x: x["age"])}')

print(f'Original list remains untouched: {people}')
