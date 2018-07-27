FROM ubuntu:18.04

# Install postgresql
#RUN apt-get update && apt-get install -y sudo postgresql-10

#RUN /etc/init.d/postgresql stop

#RUN mkdir 0777 /config/

#RUN chown postgres /usr/lib/postgresql

#USER postgres

#COPY ./config/pw.txt    /config/

#RUN rm -rf /var/lib/postgresql/10/main

#RUN ["/usr/lib/postgresql/10/bin/initdb", "-D", "/var/lib/postgresql/10/main", "-U", "admin", "--pwfile=/config/pw.txt"]

#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10/main/pg_hba.conf

#RUN echo "listen_addresses='*'" >> /etc/postgresql/10/main/postgresql.conf

#RUN mkdir /var/run/postgresql/10-main.pg_stat_tmp/

#RUN touch /var/run/postgresql/10-main.pg_stat_tmp/global.tmp

#CMD ["/usr/lib/postgresql/10/bin/pg_ctl", "-D", "/var/lib/postgresql/10/main", "-l", "var/log/postgresql/logfile", "start"]

#CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]

#EXPOSE 5432

