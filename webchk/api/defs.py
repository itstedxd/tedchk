
async def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    

async def get_random_info(session):
    try:
        import random
        async def get_state_abbreviation(state_name):
            state_dict = {
            "Alabama": "AL",
            "Alaska": "AK",
            "Arizona": "AZ",
            "Arkansas": "AR",
            "California": "CA",
            "Colorado": "CO",
            "Connecticut": "CT",
            "Delaware": "DE",
            "Florida": "FL",
            "Georgia": "GA",
            "Hawaii": "HI",
            "Idaho": "ID",
            "Illinois": "IL",
            "Indiana": "IN",
            "Iowa": "IA",
            "Kansas": "KS",
            "Kentucky": "KY",
            "Louisiana": "LA",
            "Maine": "ME",
            "Maryland": "MD",
            "Massachusetts": "MA",
            "Michigan": "MI",
            "Minnesota": "MN",
            "Mississippi": "MS",
            "Missouri": "MO",
            "Montana": "MT",
            "Nebraska": "NE",
            "Nevada": "NV",
            "New Hampshire": "NH",
            "New Jersey": "NJ",
            "New Mexico": "NM",
            "New York": "NY",
            "North Carolina": "NC",
            "North Dakota": "ND",
            "Ohio": "OH",
            "Oklahoma": "OK",
            "Oregon": "OR",
            "Pennsylvania": "PA",
            "Rhode Island": "RI",
            "South Carolina": "SC",
            "South Dakota": "SD",
            "Tennessee": "TN",
            "Texas": "TX",
            "Utah": "UT",
            "Vermont": "VT",
            "Virginia": "VA",
            "Washington": "WA",
            "West Virginia": "WV",
            "Wisconsin": "WI",
            "Wyoming": "WY"
        }
            state_name = state_name.title()
            if state_name in state_dict:
                return state_dict[state_name]
            else:
                return "NY"
        result = await session.get("https://randomuser.me/api/?nat=us")
        data = result.json()
        first_name = data['results'][0]['name']['first']
        last_name = data['results'][0]['name']['last']
        email = first_name + last_name + str(random.randint(1, 100000)) + "@gmail.com"
        phone = (str(random.randint(220, 820)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999)))
        add1 = str(data['results'][0]['location']['street']['number']) + ' ' + data['results'][0]['location']['street']['name']
        city = data['results'][0]['location']['city']
        state = data['results'][0]['location']['state']
        state_short = await get_state_abbreviation(state)
        zip_code = data['results'][0]['location']['postcode']
    except:
        first_name = "Alex"
        last_name = "Smith"
        email = "alexsmith" + str(random.randint(1, 100000)) + "@gmail.com"
        phone = (str(random.randint(220, 820)) + str(random.randint(100, 999)) + str(random.randint(1000, 9999)))
        add1 = "17 East 73rd Street"
        city = "New York"
        state = "NY"
        state_short = "NY"
        zip_code = "10021"
    json = {
        "fname": first_name,
        "lname": last_name,
        "email": email,
        "phone": phone,
        "add1": add1,
        "city": city,
        "state": state,
        "state_short": state_short,
        "zip": zip_code
    }
    return json
