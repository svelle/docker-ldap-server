#!/bin/python3

org="dc=planet,dc=express"
filename="bootstrap.ldif"

def create_user():
    i = 0
    f = open(filename, "w")
    while i < 10000:
        user = f"dn: cn=developer,{org}\n\
changetype: add\n\
objectclass: inetOrgPerson\n\
cn: maintainer\n\
givenname: givenname{i}\n\
sn: surname{i}\n\
displayname: User{i} Name{i}\n\
mail: user{i}r@example.com\n\
userpassword: UserPass{i}234\!\n\n"
        f.write(user)
        i += 1
    f.close()

def append_org():
    f = open(filename, "a")
    appendage = "dn: ou=Groups,{org}\n\
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
uniqueMember: cn=admin,{org}\n\
\n\
dn: cn=Maintaners,ou=Groups,{org}\n\
changetype: add\n\
cn: Maintaners\n\
objectclass: groupOfUniqueNames\n\
uniqueMember: cn=maintainer,{org}\n\
uniqueMember: cn=developer,{org}\n"
    f.write(appendage)
    f.close()

create_user()
append_org()