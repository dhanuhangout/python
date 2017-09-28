'''Create a data structure as follows:

variable = {
  'Date' = [],
  'VisitedPlaces' = [],
  'CreditcardUsed' = [],
  'TimeSpent' = []
}

Example usage:
The data structure holds the details of a person on "the date that the person
visited a place, used credit card in that place and the amount time the person
spent in that place.
Person1 = [
  ['Jan 01 2016', 'New York', 'Bank X', '6 hours'],
  ['Jan 30 2016', 'San Francisco', 'Bank Y', '3 hours'],
  ['Dec 01 2017', 'Tahoe', 'Bank Z', '12 hours']
]
Person2 = [
  ['Feb 10 2016', 'Delhi', 'Bank I', '6 hours'],
  ['Feb 20 2016', 'Agra', 'Bank J', '10 hours'],
]
'''

person_data = {
  'name' : '',
  'date' : [],
  'place' : [],
  'bank_name' : [],
  'time_spent' : []
}

class _PersonData:
  def __init__(self, name):
    # Initialize data.
    self.name = name
    self.date = []
    self.place = []
    self.bank_name = []
    self.time_spent = []


data_base = {
  'personA': _PersonData('personA'),
  'personB': _PersonData('personB'),
  'personC': _PersonData('personC'),
  'personD': _PersonData('personD'),
  'personE': _PersonData('personE'),
  'personF': _PersonData('personF'),
  'personG': _PersonData('personG'),
  'personH': _PersonData('personH'),
  'personI': _PersonData('personI'),
  'personJ': _PersonData('personJ'),
}


if __name__ == '__main__':
  # date = raw_input('Date you visited the place: ')
  data = [
    ['personA', 'Jan 01 2016', 'New York', 'Bank X', '6 hours'],
    ['personB', 'Jan 02 2016', 'New York', 'Bank X', '6 hours'],
    ['personA', 'Jan 03 2016', 'Texas', 'Bank Y', '6 hours'],
    ['personC', 'Jan 04 2016', 'New York', 'Bank X', '6 hours'],
    ['personD', 'Jan 05 2016', 'New York', 'Bank X', '6 hours'],
    ['personB', 'Jan 06 2016', 'Texas', 'Bank X', '6 hours'],
    ['personA', 'Jan 07 2016', 'New York', 'Bank Y', '6 hours'],
    ['personA', 'Jan 08 2016', 'SFO', 'Bank Z', '6 hours'],
    ['personE', 'Jan 09 2016', 'New York', 'Bank Z', '6 hours'],
    ['personF', 'Jan 01 2016', 'New York', 'Bank X', '6 hours'],
    ['personG', 'Jan 02 2016', 'New York', 'Bank X', '6 hours'],
    ['personH', 'Jan 03 2016', 'New York', 'Bank X', '6 hours'],
    ['personI', 'Jan 04 2016', 'New York', 'Bank X', '6 hours'],
    ['personJ', 'Jan 05 2016', 'New York', 'Bank X', '6 hours'],
    ['personI', 'Jan 06 2016', 'Texas', 'Bank Y', '6 hours'],
    ['personI', 'Jan 07 2016', 'SFO', 'Bank Z', '6 hours'],
  ]

  for i in range(len(data)):
    # print data[i][0]
    for value in data_base.keys():
      if data[i][0] == value:
        # print data_base[value].name
        data_base[value].date.append(data[i][1])
        data_base[value].place.append(data[i][2])
        data_base[value].bank_name.append(data[i][3])
        data_base[value].time_spent.append(data[i][4])
  print '\n\n\n\n\n'
  for value in data_base.keys():
    print '***** %s Details *****' % value
    print data_base[value].date
    print data_base[value].place
    print data_base[value].bank_name
    print data_base[value].time_spent
    print '**********************'
