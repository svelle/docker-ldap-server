FROM osixia/openldap

LABEL maintainer="sven.svelle@gmail.com"

ENV LDAP_ORGANISATION="Planet Express" \     
    LDAP_DOMAIN="planet.express"

COPY bootstrap.ldif /container/service/slapd/assets/config/bootstrap/ldif/50-bootstrap.ldif
