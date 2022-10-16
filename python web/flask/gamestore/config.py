SECRET_KEY = 'Parangaricotirimirruaro'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='Marcel1987',
        servidor='127.0.0.1',
        database='jogoteca'
    )
