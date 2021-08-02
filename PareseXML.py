import xml.etree.ElementTree as ES

data = '''<person>
<name>Anmol</name>
<phone>8091782895</phone>
<email hide="yes"/>
</person>
'''

tree = ES.fromstring(data)
print('name :', tree.find('name').text)
print('atrr : ',tree.find('email').get('hide'))


input = '''
<stuff>
<users>
<user id = "2">
<name>AR</name>
<id>007</id>
</user>
<user x="3">
<name>BR</name>
<id>001</id>
</user>
</users>
</stuff>
'''

tree2 = ES.fromstring(input)
users = tree2.findall('users/user')
for user in users:
    print('name',user.find('name').text)
    print('id: ',user.find('id').text)
    print('att:',user.get("x"))
