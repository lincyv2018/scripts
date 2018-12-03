import pyodbc

driver_1 = '{SQL Server}'
driver_2 = '{SQL Server Native Client 11.0}'
driver_3 = '{ODBC Driver 13 for SQL Server}'
server = 'INSVRSQL03.alamy.com'
server_1 = '192.168.16.41'
db1 = '5nine_monitor'
tcon = 'yes'
uname = 'lincyv@alamy.com'
pword = 'welcome123$'
try:
    cnxn = pyodbc.connect(driver= driver_1, host=server_1, database=db1,
                      trusted_connection=tcon, user=uname, password=pword)
    print "Connected Sucessful"
except pyodbc.OperationalError, err:
    print err
    print "you have some issues with db connection"

#print cnxn

#cnxnstr = 'Driver={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2};HOST=192.168.16.41;PORT=1443;UID=lincyv@alamy.com'
#ODBC Driver 13 for SQL Server

# cnxnstr = (
#     r'Driver={SQL Server};'
#     r'SERVER=INSVRSQL03.alamy.com'
#     r'PORT=1443;'
#     r'DATABASE=5nine_monitor;'
#     r'Trusted_Connection=yes;' )
# #MyMSSQLServer


# cnxnstr = (
#     r'Driver={SQL Server};'
#     r'SERVER=192.168.16.41'
#     r'HOST=192.168.16.41;'
#     r'PORT=1443;'
#     r'DATABASE=5nine_monitor;'
#     r'UID=lincyv@alamy.com;'
#     r'PWD=welcome123$;'
#     r'OPTION=3;'
#     r'Trusted_Connection=yes;' )

#cnxnstr = 'Driver={MyMSSQLServer};HOST=192.168.16.41;PORT=1443;DATABASE=5nine_monitor;UID=lincyv@alamy.com;PWD=welcome123$;OPTION=3;'

#conn = pyodbc.connect('DNS=test;HOST=192.168.16.41;PORT=1443;DATABASE=5nine_monitor;UID=lincyv@alamy.com;PWD=welcome123$;OPTION=3;Trusted_Connection=yes')

#cnxn = pyodbc.connect(cnxnstr, autocommit=True)



# a = conn.cursor()
# print a

