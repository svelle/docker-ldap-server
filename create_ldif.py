import jsonlines
import re

org = "dc=planet,dc=express"
outfile = "bootstrap.ldif"
infile = "export.jsonl"
users = {}


def fetch_users():
    with jsonlines.open(infile) as file:
        for line in file:
            if line["type"] == "user":
                in_user = line['user']
                out_user = {'cn': in_user['username'], 'mail': in_user['email'], 'givenname': in_user['first_name'],
                            'sn': in_user['last_name'], 'password': re.escape(in_user['password']),
                            'displayname': f"{in_user['first_name']} {in_user['last_name']}"}
                if in_user['username'] not in users:
                    users[in_user['username']] = out_user


def create_user():
    i = 0
    f = open(outfile, "w")
    for _, user in users.items():
        out_user = f"dn: cn={user['cn']},{org}\n\
changetype: add\n\
objectclass: inetOrgPerson\n\
cn: {user['cn']}\n\
givenname: {user['givenname']}\n\
sn: {user['sn']}\n\
displayname: {user['displayname']}\n\
mail: {user['mail']}\n\
userpassword: {user['password']}\n\n"
        f.write(out_user)
        i += 1
    f.close()


def append_org():
    f = open(outfile, "a")
    appendage = f"dn: ou=Groups,{org}\n\
changetype: add\n\
objectclass: organizationalUnit\n\
ou: Groups\n\
\n\
dn: ou=Users,{org}\n\
changetype: add\n\
objectclass: organizationalUnit\n\
ou: Users\n\
\n\
dn: cn=Admins,ou=Groups,{org}\n\
changetype: add\n\
cn: Admins\n\
objectclass: groupOfUniqueNames\n\
uniqueMember: cn=adminuser,{org}\n"
    f.write(appendage)
    f.close()


fetch_users()
create_user()
append_org()
